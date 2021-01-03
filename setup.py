import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tauno-serial-plotter", # Replace with your own username
    version="1.1",
    author="Tauno Erik",
    author_email="sedumacre@gmail.com",
    description="Tauno-Serial-Plotter is simple serial plotter for Arduino and others.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taunoe/tauno-serial-plotter",
    packages=["tauno-serial-plotter"],
    #packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)