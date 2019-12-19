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
        cmake = CMake(self)
        cmake.configure(source_folder="actions-cpp")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="actions-cpp")
        self.copy("*action.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["action"]

