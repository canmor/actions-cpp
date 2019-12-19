from conans import ConanFile, CMake, tools


class ActionsConan(ConanFile):
    name = "actions"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Actions here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/canmor/actions-cpp.git")

    def build(self):
        if self.settings.compiler == "gcc":
            self.run("conan install actions-cpp -s compiler.libcxx=libstdc++11 arch=%s" %self.settings.arch)
        elif self.settings.compiler == "apple-clang":
            self.run("conan install actions-cpp")
        cmake = CMake(self)
        cmake.configure(defs={"CMAKE_TOOLCHAIN_FILE": "conan_paths.cmake"}, source_folder="actions-cpp")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="actions-cpp/include")
        self.copy("*action.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["action"]

