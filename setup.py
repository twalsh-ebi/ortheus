#!/usr/bin/env python3

#Copyright (C) 2008-2011 by Benedict Paten (benedictpaten@gmail.com)
#
#Released under the MIT license, see LICENSE.txt

from pathlib import Path
from stat import S_IXUSR, S_IXGRP, S_IXOTH
import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.install_lib import install_lib


class BuildWithMake(build_py):
    """Make package executables before building Python package."""
    def run(self):
        subprocess.run(["make"], check=True)
        build_py.run(self)


class InstallWithExecutables(install_lib):
    """Install Python package while ensuring its executables have appropriate permissions."""
    def run(self):
        install_lib.run(self)

        install_dir_path = Path(self.install_dir).resolve()
        for package_name, rel_exe_file_paths in package_exe_files.items():
            for rel_exe_file_path in rel_exe_file_paths:
                exe_file_path = install_dir_path / package_name / rel_exe_file_path
                old_exe_file_mode = exe_file_path.stat().st_mode
                new_exe_file_mode = old_exe_file_mode | S_IXUSR | S_IXGRP | S_IXOTH
                exe_file_path.chmod(new_exe_file_mode)


package_exe_files = {
    "ortheus": ["bin/ortheus_core"],
}


setup(
    cmdclass={
        "build_py": BuildWithMake,
        "install_lib": InstallWithExecutables,
    },
    package_data=package_exe_files,
    zip_safe=False,
)