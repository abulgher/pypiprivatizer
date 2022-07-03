# -*- coding: utf-8 -*-
"""
The pyprivatizer module

This module allows to download from PyPI a list of packages satisfying a
requirement file and to copy them to a local directory with a struture that
resemble the one of a private python index.

"""

import argparse
import re
import shutil
import subprocess
from pathlib import Path


def main():
    """Execute the module.

    The module takes two input parameters, the requirements file and the
    output directory where the index structure will be created.

    Raises
    ------
    OSError
        An OSError will be raised if the input parameters are not found on
        the filesystem.

    Returns
    -------
    None.

    """
    # command line arguments. only for logging level at the moment.
    parser = argparse.ArgumentParser(description='''
                                     Tool for downloading packages from PyPI and
                                     made them available for a local private index
                                     ''')
    parser.add_argument('-r', type=Path, dest='requirements_file',
                        default=(Path.cwd() / Path('requirements.txt')),
                        help='A requirements file with the packages to be downloaded.')
    parser.add_argument('-d', '--output-dir', type=Path, dest='output_dir',
                        default=(Path.cwd()), help='The directory where the private index is stored.')
    args = parser.parse_args()

    # check that the give parameters are valid.
    if not args.requirements_file.exists():
        raise OSError(
            f'Requirement file {str(args.requirements_file)} doesn\'t exist')
    if not args.requirements_file.is_file():
        raise OSError(
            f'Requirement file {str(args.requirements_file)} isn\'t a file')
    if not args.output_dir.is_dir() and args.output_dir.exists():
        raise OSError(f'Output dir {str(args.output_dir)} isn\'t a directory')

    if not args.output_dir.exists():
        args.output_dir.mkdir(parents=True)

    # be sure to be using the latest version of pip
    command = 'python -m pip install --upgrade pip'
    print(command)
    cmd_output = subprocess.run(command.split(), capture_output=True)
    if cmd_output.returncode:
        print(cmd_output.stdout.decode('utf-8'))
        print(cmd_output.stderr.decode('utf-8'))
        raise OSError('Error upgrading pip')
    else:
        print(cmd_output.stdout.decode('utf-8'))

    tmp_dir = Path().cwd() / Path('temp')
    tmp_dir.mkdir(exist_ok=True)
    command = f'python -m pip download -r {str(args.requirements_file)} -d {str(tmp_dir)}'
    print(command)
    cmd_output = subprocess.run(command.split(), capture_output=True)
    if cmd_output.returncode:
        print(cmd_output.stdout.decode('utf-8'))
        print(cmd_output.stderr.decode('utf-8'))
        raise OSError('Error upgrading pip')
    else:
        print(cmd_output.stdout.decode('utf-8'))

    for file in tmp_dir.glob('*'):
        if file.is_file():
            dir_name = file.name.split('-')[0]
            norm_name = re.sub(r"[-_.]+", "-", str(dir_name)).lower()
            (args.output_dir / Path(norm_name)).mkdir(exist_ok=True, parents=True)
            package_name = file.name
            shutil.copy(file, (args.output_dir
                        / Path(norm_name) / package_name))

    shutil.rmtree(tmp_dir)

    print('Packages downloaded and trasfered to destination directory')


if __name__ == '__main__':
    main()
