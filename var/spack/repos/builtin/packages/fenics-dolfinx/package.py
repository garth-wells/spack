# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FenicsDolfinx(CMakePackage):
    """Next generation FEniCS problem solving environment"""

    homepage = "https://github.com/FEniCS/dolfinx"
    git = "https://github.com/FEniCS/dolfinx.git@garth/test-spack"
    maintainers = ["js947", "chrisrichardson"]

    version("master", branch="master")

    variant("kahip", default=False, description="kahip support")
    variant("parmetis", default=False, description="parmetis support")
    variant("slepc", default=False, description="slepc support")

    depends_on("cmake@3.9:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("mpi", type=("build", "run"))
    depends_on("hdf5+hl")
    depends_on("boost")
    depends_on("eigen@3.3.7:")
    depends_on("petsc+mpi+shared+hypre")
    depends_on("scotch+mpi")

    depends_on("kahip", when="+kahip")
    depends_on("parmetis", when="+parmetis")
    depends_on("slepc", when="+slepc")

    depends_on("py-fenics-ffcx", type=("build", "run"))

    conflicts('%gcc@:6', msg='C++17 support required')

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        args = [
            "-DDOLFINX_SKIP_BUILD_TESTS=True",
            "-DDOLFINX_ENABLE_KAHIP={0}".format('ON' if "+kahip" in self.spec else 'OFF'),
            "-DDOLFINX_ENABLE_PARMETIS={0}".format('ON' if "+parmetis" in self.spec else 'OFF'),
            "-DDOLFINX_ENABLE_SLEPC={0}".format('ON' if "+slepc" in self.spec else 'OFF'),
            "-DBOOST_ROOT={0}".format(self.spec['boost'].prefix),
            "-DPython3_ROOT_DIR={0}".format(self.spec['python'].home),
            "-DPython3_FIND_STRATEGY=LOCATION",
        ]
        return args
