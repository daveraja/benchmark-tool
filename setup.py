from setuptools import setup

setup(
    name='Potassco Benchmark Tool',
    version='0.0.1',
    url='https://github.com/daveraja/potassco/benchmark-tool',
    author='Roland Kaminski',
#    author_email='info@potassco.com',
    description='Potassco Benchmark Tool',
    license='MIT',
    package_dir={'': 'src'},
    packages=['benchmarktool', 'benchmarktool.result',
              'benchmarktool.resultparser','benchmarktool.runscript'],
    install_requires=['lxml >= 4.6.0'
                      # 'clingo >= 5.3.0', - not a pip installed package
                      # 'clorm >= 1.1.0'   - not a pip installed package
                      ],
    python_requires='>=3.0',
    entry_points={
        'console_scripts': [
            'bconv = benchmarktool.main.bconv:main',
            'beval = benchmarktool.main.beval:main',
            'bstat = benchmarktool.main.bstat:main',
            'bfeat = benchmarktool.main.bfeat:main',
            'bgen = benchmarktool.main.bgen:main',
        ]
    }
)
