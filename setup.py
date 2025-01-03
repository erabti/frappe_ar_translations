from setuptools import setup, find_packages

setup(
    name="custom_ar_translations",
    version="1.0.0",
    description="Custom Translations for ERPNext",
    author="Erabti",
    author_email="admin@lavandania.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)