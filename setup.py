from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.0.1",
    author="Devashish",
    author_email="doraplex123@gmail.com",
    description="A machine learning project package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas",
        "numpy",
        "seaborn",
        "scikit-learn",
    ],
    python_requires=">=3.8",
    include_package_data=True,
)
