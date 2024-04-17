import setuptools

setuptools.setup (
    name = "libs_zip",
    packages = ["libs"],
    version = "0.0.3",
    download_url = "",
    classifiers=[
        "Programming Language :: Python :: 3"],
    install_requires=[
        # web
        'selenium',
        'beautifulsoup4',
        'requests',
        # image
        'pillow',
        'pyautogui',
        # data
        'pandas',
        'Matplotlib',
        'numpy',
    ],
)
