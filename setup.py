import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AlekeMath", 
    version="0.0.1",
    author="Almaz Kydyrmin",
    author_email="kydyrmin.almaz@gmail.com",
    description="This project is experimental",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlekefromKz/Delivery-Food",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
