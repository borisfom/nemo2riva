# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT

import os
import subprocess
from distutils import cmd as distutils_cmd
from distutils import log as distutils_log
from pathlib import Path

from setuptools import Extension, setup

install_requirements = [
    "isort<5.0",
    "nemo_toolkit>=1.0.0",
    "nvidia-eff>=0.5.3,<=0.6.2",
    "onnxruntime>=1.9",
    "onnx_graphsurgeon",
    "packaging",
]

packages = ["nemo2riva", "nemo2riva.cli", "nemo2riva.patches"]

setup_py_dir = Path(__file__).parent.absolute()


def get_version():
    version_file = setup_py_dir / "VERSION"
    versions = open(version_file, "r").readlines()
    version = "devel"
    for v in versions:
        if v.startswith("RIVA_VERSION: "):
            version = v[len("RIVA_VERSION: ") :].strip()
    return version


setup(
    description="NeMo Model => Riva Deployment Converter",
    author="NVIDIA",
    author_email="nvidia.com",
    version=get_version(),
    setup_requires="nvidia-pyindex",
    install_requires=install_requirements,
    packages=packages,
    name="nemo2riva",
    python_requires=">=3.7.0",
    include_package_data=True,
    package_dir={"nemo2riva": "nemo2riva"},
    package_data={"nemo2riva": ["validation_schemas/*.yaml"]},
    entry_points={"console_scripts": ["nemo2riva = nemo2riva.cli:nemo2riva",]},
)