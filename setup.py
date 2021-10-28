import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lodging",
    version="0.0.1",
    author="Austin Poor",
    author_email="a-poor@users.noreply.github.com",
    description="A JSON logging library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/lodging",
    project_urls={
        "Bug Tracker": "https://github.com/a-poor/lodging/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)