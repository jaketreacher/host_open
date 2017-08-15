from setuptools import setup

setup(name='HostOpen',
	  version='0.1.1',
	  description='Open \'remote\' vagrant files locally',
	  author='Jake Treacher',
      author_email='git@jaketreacher.com',
      url='https://github.com/jaketreacher/host_open',
      packages=['host_open', ],
      entry_points={
        'console_scripts': [
            'hostopen = host_open.client:main',
            'hostopen-server = host_open.server:main'
        ],
      },
      )
