# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class HsakmtRoct(CMakePackage):
    """This is a thunk python recipe to build and install Thunk Interface.
       Thunk Interface is a user-mode API interfaces used to interact
       with the ROCk driver."""

    homepage = "https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface"
    url      = "https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/archive/rocm-3.5.0.tar.gz"

    maintainers = ['srekolam', 'arjun-raj-kuppala']

    version('3.7.0', sha256='b357fe7f425996c49f41748923ded1a140933de7564a70a828ed6ded6d896458')
    version('3.5.0', sha256='d9f458c16cb62c3c611328fd2f2ba3615da81e45f3b526e45ff43ab4a67ee4aa')

    variant('build_type', default='Release', values=("Release", "Debug"), description='CMake build type')

    depends_on('cmake@3:', type='build')
    depends_on('numactl')

    @property
    def install_targets(self):
        if self.version == Version('3.5.0'):
            return ['install', 'install-dev']
        else:
            return ['install']

    def cmake_args(self):
        args = [
            '-DBUILD_SHARED_LIBS="on"',
        ]
        return args
