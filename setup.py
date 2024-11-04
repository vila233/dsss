from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    packages=find_packages(),
    description='A simple math quiz game',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    install_requires=[
        # Add your dependencies here, e.g., 'numpy', 'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)