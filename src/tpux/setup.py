import setuptools

setuptools.setup(
    name="tpux",
    version="0.1",
    author="nikolageorgiev2000",
    author_email="nikola.georgiev2000@gmail.com",
    description="A set of Python scripts that makes your experience on TPU better",
    url="https://github.com/nikolageorgiev2000/tpux",
    packages=setuptools.find_packages(),
    install_requires=[
        "psutil",
        "fabric"
    ],
)