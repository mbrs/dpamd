import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dpamd",
    version="0.5dev",
	author='MBS',
	author_email='broes.michael@gmail.com',
    description="dpam data package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mbrs/dpamd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


