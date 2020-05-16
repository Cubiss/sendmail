from setuptools import setup

packages = []

setup(name='sendmail',
      version='1.0',
      description='Simple email sending via already working SMTP server without authentication.',
      url='https://github.com/Cubiss/sendmail',
      author='Cubiss',
      author_email='cubiss.dev@gmail.com',
      license='WTFPL',
      packages=['sendmail'],
      zip_safe=True,
      install_requires=packages)
