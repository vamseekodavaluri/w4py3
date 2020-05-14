import setuptools

with open('webware/Properties.py') as f:
    properties = {}
    exec(f.read(), properties)
    version = properties['version']
    version = '.'.join(map(str, version[:3])) + '.'.join(version[3:])
    description = properties['synopsis']

with open('README.md') as fh:
    long_description = fh.read()

requireDev = [
    'Pygments>=2.6,<3', 'WebTest>=2.0,<3',
    'waitress>=1.4.3,<2', 'hupper>=1.10,<2',
]
requireDocs = [
    'Sphinx>=2.4,<3', 'sphinx_rtd_theme>=0.4'
]
requireExamples = [
    'Pygments>=2.6,<3', 'Pillow>=7,<8', 'dominate>=2.5,<3', 'yattag>=1.13,<2'
]
requireTests = [
    'psutil>=5.7,<6', 'flake8>=3.8,<4', 'pylint>=2.5,<3', 'tox>=3.15,<4',
    'pywin32>=227,<300;sys_platform=="win32"'
] + requireDev + requireDocs + requireExamples


setuptools.setup(
    name='Webware-for-Python',
    version=version,
    author='Christoph Zwerschke et al.',
    author_email='cito@online.de',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='web framework servlets',
    url='https://webwareforpython.github.io/w4py3/',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
    extras_require={
        'dev': requireDev,
        'docs': requireDocs,
        'examples': requireExamples,
        'tests': requireTests,
    },
    entry_points={
        'console_scripts': [
            'webware = webware.Scripts.WebwareCLI:main'
        ],
        'webware.plugins': [
            'MiscUtils = webware.MiscUtils',
            'PSP = webware.PSP',
            'TaskKit = webware.TaskKit',
            'UserKit = webware.UserKit',
            'WebUtils = webware.WebUtils'
        ]
    }
)
