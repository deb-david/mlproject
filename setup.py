from setuptools import setup, find_packages


def get_requirements(file_path):
    """
    This function will return the list of requirements
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    description='An example project for Machine Learning',
    author='Deb David',
    author_email='deborrahdavid777@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}, # Define root directory for packages
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)

