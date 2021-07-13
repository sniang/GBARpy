import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GBARpy", # Replace with your own username
    version="1.1.0",
    author="Samuel Niang",
    author_email="samuel.niang@cern.ch",
    description="Libraries and software to analyse data (the MCP's picture and CsI signals) in the framework of the GBAR experiment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sniang/GBARpy",
    project_urls={
        "Bug Tracker": "https://github.com/sniang/GBARpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy",
    "matplotlib",
    "scipy",
    "scikit-image",
    "dill"],
    include_package_data=True,
)


