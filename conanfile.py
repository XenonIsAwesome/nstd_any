from conan import ConanFile
from conan.tools.files import copy
import os

class NstdConan(ConanFile):
    name = "nstd"
    version = "1.0.0"
    license = "MIT"
    author = "mkmagic"
    url = "https://github.com/mkmagic/nstd_any"
    description = (
        "nstd::any is a robust, single-header C++17 implementation of a type-safe "
        "container for single values of any type."
    )
    topics = ("header-only", "cpp")
    package_type = "header-library"

    def export_sources(self):
        copy(self, "*.hpp", src=os.path.join(self.recipe_folder, "include"),
             dst=os.path.join(self.export_sources_folder, "include"))

    def package(self):
        copy(self, "*.hpp",
             src=os.path.join(self.export_sources_folder, "include"),
             dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
