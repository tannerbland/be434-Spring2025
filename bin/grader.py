#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-01-31
Purpose: Report test results
"""

import argparse
import os
import sys
import stat
import numpy as np
from subprocess import getoutput
from xml.etree.ElementTree import ElementTree
from random import shuffle


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Report test results',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-d',
                        '--test_dir',
                        help='The directory to grade',
                        metavar='str',
                        type=str,
                        nargs='+',
                        default='01_salutations')

    parser.add_argument('-r',
                        '--repo_dir',
                        help='"biosys-analytics code" directory',
                        metavar='str',
                        type=str,
                        default=os.path.join(os.getenv('HOME'), 'work',
                                             'be434',
                                             'code'))

    parser.add_argument('-s',
                        '--students_dir',
                        help='location of students repos',
                        metavar='str',
                        type=str,
                        default=os.path.join(os.getenv('HOME'), 'work',
                                             'be434',
                                             'students'))

    parser.add_argument('-t',
                        '--assignment_type',
                        choices=['assignments', 'extra', 'project'],
                        help='Assignment type',
                        metavar='str',
                        type=str,
                        default="assignments")

    parser.add_argument('-p',
                        '--private',
                        help='Do not show student IDs',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    repo_dir = args.repo_dir
    students_dir = args.students_dir
    assignment_type = args.assignment_type
    test_dir_names = args.test_dir

    # Check for "hurwitzlab:biosys-analytics" dir
    if not os.path.isdir(repo_dir):
        die('Bad --repo_dir "{}"'.format(repo_dir))

    # Check for "../repos" dir
    if not students_dir:
        students_dir = os.path.abspath(
            os.path.join(os.path.dirname(sys.argv[0]), '..', 'repos'))

    if not os.path.isdir(students_dir):
        die('Cannot find --students_dir "{}"'.format(students_dir))

    # Get a list of valid test dirs
    assign_dir = os.path.join(repo_dir, assignment_type)
    if not os.path.isdir(assign_dir):
        die(f'Cannot find {assignment_type} dir "{assign_dir}"')

    valid_test_dirs = os.listdir(assign_dir)

    # List possible test dirs if none given
    invalid = set(test_dir_names).difference(
        set(valid_test_dirs)) if test_dir_names else []

    if not test_dir_names or invalid:
        msg = 'Bad -d/--test_dir ({}), choose from:\n{}'.format(
            ', '.join(invalid) if invalid else 'Missing',
            '\n'.join(map(lambda s: ' - ' + s, sorted(valid_test_dirs))))
        die(msg)

    # Gather student dirs
    student_dirs = list(
        map(lambda d: os.path.join(students_dir, d), os.listdir(students_dir)))

    if len(student_dirs) == 0:
        die("There are no student directories?!")

    if args.private:
        print('>>>>>>> Shuffling <<<<<<<')
        shuffle(student_dirs)  # in-place
    else:
        # Schwartzian Transform in Python!
        student_dirs = map(
            lambda y: y[1],
            sorted(map(lambda x: (os.path.split(x)[-1], x), student_dirs)))

    def wanted(filename):
        return filename.endswith(
            '.py') and filename != 'test.py' and filename != 'solution.py'

    scores = []
    for i, student_dir in enumerate(student_dirs):
        student_id = os.path.basename(student_dir)

        results = []
        for test_dir_name in test_dir_names:
            test_dir = os.path.join(student_dir, assignment_type,
                                    test_dir_name)
            xml_out = os.path.join(test_dir, 'result.xml')
            result = 0
            reason = ''

            if os.path.isfile(xml_out):
                os.remove(xml_out)

            if not os.path.isdir(test_dir):
                reason = 'Missing test_dir'
            else:
                cmd = 'python3 -m pytest --junit-xml={} test.py'.format(
                    xml_out)
                os.chdir(test_dir)

                try:
                    for py in filter(wanted, os.listdir(test_dir)):
                        py_path = os.path.join(test_dir, py)
                        st = os.stat(py_path)
                        os.chmod(py_path, st.st_mode | stat.S_IEXEC)
                        _ = getoutput(f'dos2unix {py_path}')

                    _ = getoutput(cmd)
                except Exception:
                    reason = 'Test failed completely'

                if not os.path.isfile(xml_out):
                    reason = 'Missing XML out "{}"'.format(xml_out)
                else:
                    tree = ElementTree()
                    root = tree.parse(xml_out)
                    testsuite = list(root.findall('testsuite'))

                    if not testsuite:
                        reason = f'No "testsuite" in "{xml_out}"'
                    else:
                        test_out = testsuite[0].attrib
                        errors = test_out.get('errors')

                        if errors and errors.isdigit() and int(errors) > 0:
                            reason = 'Test errors!'
                        else:
                            num_tests = test_out.get('tests')
                            failures = test_out.get('failures')

                            if num_tests and num_tests.isdigit(
                            ) and failures and failures.isdigit():
                                num_tests = int(num_tests)
                                if num_tests:
                                    failures = int(failures)
                                    num_passed = num_tests - failures
                                    result = int((num_passed / num_tests) * 100)
                                else:
                                    reason = 'No tests'
                            else:
                                reason = 'Parse error'

            results.append(result)

        score = np.mean(results)
        scores.append(score)
        print('{:7}% {:20} {}'.format(score,
                                      'XXX' if args.private else student_id,
                                      reason))

    print('Done, graded {}, average {:.2f}%.'.format(len(scores),
                                                     np.mean(scores)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
