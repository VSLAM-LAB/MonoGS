from setuptools import setup, find_packages

setup(
    name="monogs",
    version="1.0.0",
    description="MonoGS Visual SLAM system",
    author="Your Name",
    license="MIT",
    packages=find_packages(),
    py_modules=["slam"], 
    install_requires=[
        "numpy",
        "torch",
    ],
    entry_points={
        "console_scripts": [
            "monogs = slam:main",
        ],
    },
    include_package_data=True,
)
