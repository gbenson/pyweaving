import os.path
from distutils.errors import DistutilsInternalError
from setuptools import Command


class build_lambda(Command):

    description = "build container images for AWS Lambda"

    user_options = [
        ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def call_command(self, command):
        """Run another command and return the files it generated."""
        self.run_command(command)
        return (filename
                for build_command, pyversion, filename
                    in self.distribution.dist_files
                if build_command == command)

    def run(self):
        wheels = tuple(self.call_command("bdist_wheel"))
        if len(wheels) != 1:
            raise DistutilsInternalError(
                f"bdist_wheel built {len(wheels)} files")
        [wheel] = wheels

        name = self.distribution.get_name()
        self.spawn((
            "docker", "build",
            "--tag", name,
            "--build-arg", f"{name.upper()}_WHEEL={os.path.basename(wheel)}",
            "."
        ))
