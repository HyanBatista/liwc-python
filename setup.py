import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fr:
    requirements = [l for l in fr.readlines()]

setuptools.setup(
    name="mec-liwc",
    version="0.0.1",
    author="aiboxlab",
    author_email="aiboxlab@gmail.com",
    description="Portuguese Version of LIWC.",
    long_description=long_description,
    url="https://github.com/mec-correcaotextual/mec-liwc",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
