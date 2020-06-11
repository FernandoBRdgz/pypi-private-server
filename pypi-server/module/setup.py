from setuptools import setup

with open("README.md", "r") as f:
  long_description = f.read()

with open("requirements.txt", "r") as f:
  requirements = f.read()

setup(
  name = 'helloworld',
  version = '0.0.1',
  description = 'Say hello!',
  py_modules = ['helloworld'],
  package_dir = {'': 'src'},
  classifiers = [
      "Operating System :: Unix",
      "Development Status :: 3 - Alpha",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "License :: OSI Approved :: MIT License",
  ],
  long_description = long_description,
  long_description_content_type = "type/markdown",
  install_requires = requirements,
  extras_require = {
      "dev":[
          "twine>=3.1", 
      ],
  },
  url = "https://github.com/FernandoBRdgz/pypi-private-server",
  author = "Fernando Barranco",
  author_email = "fernando.barranco.r@gmail.com",
)