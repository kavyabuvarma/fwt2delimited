import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fwt",
    version="1.0.0",
    author="Kavya Varma",
    author_email="kavyabu@gmail.com",
    description="A library to convert fixed width text file to delimited file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kavyabuvarma/fwt2delimited",
    packages=setuptools.find_packages(),
    keywords="fwt fwt delimited fixedwidthtext",
    project_urls={
        'Source': "https://github.com/kavyabuvarma/fwt2delimited"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    package_data={'': ['config/*']},
)
