try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Barry Wainstock',
        'url': 'None',
        'author_email': 'barrywainstock@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)
