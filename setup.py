import os
import pathlib
#import subprocess
#import sys
import setuptools

#def install(package):
#    subprocess.check_call([sys.excutable,"-m","pip","install",package])

# GH_TOKEN = os.getenv("GH_TOKEN")
# if GH_TOKEN is None:
#     required = 'python-dotenv==1.0.0'
#     install(required)
#     from dotenv import load_dotenv
#
#     load_dotenv()
#     GH_TOKEN = os.getenv("GH_USERNAME")+ ":" +os.getenv("GH_TOKEN")
#     print(f"##### GH_TOKEN is :::: {GH_TOKEN}")

GH_USERNAME = os.getenv("GH_USERNAME")
GH_TOKEN = os.getenv("GH_TOKEN")
#GH_USER_WITH_TOKEN = GH_USERNAME +" : "+GH_USERNAME


PACKAGE_REQUIREMENTS = [
    "PyYAML==6.0",
    "pysftp==0.2.9",
    "boto3==1.34.51",
    "wheel",
    f"python_generic_func_library @ git+https://{GH_USER_WITH_TOKEN}@github.com/skr-python-org/python_generic_func_library.git@v1.0.0"

]

DEV_REQUIREMENTS = [
    "pytest == 7.1.3",
    "pandas == 1.5.0",
    "numpy == 1.23.1",
    "pytest-cov == 3.0.0",
    "python-dotenv == 1.0.0"
]



current_dir = pathlib.Path(__file__).parent.resolve()
#long_description = (current_dir / 'README.md').read_txt(encoding="utf-8")
long_description = "test project "


setuptools.setup(
    name="2_python_prj_with_setupfile",
    version="1.0.0",
    author="ABC Team",
    author_email = "sekher.talupula@gmail.com,sekhar.jagadeesh9@gmail.com",
    description = "contains detailed setup.py file and read env files functions",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(exclude=["test_*","**/test/*"]),
    python_requires = ">=3.9",
    setup_requires = ["setuptools" , "wheel"],
    install_requires = PACKAGE_REQUIREMENTS,
    extras_require = { "dev" : DEV_REQUIREMENTS },
    classifiers= [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_data = {
        'me.personal': ['*.csv' , '*.json']
    }


)