---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/python.html
---

# Amazon S3 Encryption Client for Python
<a name="python"></a>

This topic explains how to install and use the Amazon S3 Encryption Client for Python. For details about programming with the Amazon S3 Encryption Client for Python, see the [amazon-s3-encryption-client-python](https://github.com/aws/amazon-s3-encryption-client-python) repository on GitHub.

**Topics**
+ [Prerequisites](#python-prerequisites)
+ [Installation](#python-installation)
+ [Amazon S3 Encryption Client for Python examples](python-examples.md)

## Prerequisites
<a name="python-prerequisites"></a>

Before you install the Amazon S3 Encryption Client for Python, be sure you have the following prerequisites.

**A Python development environment**
The Amazon S3 Encryption Client for Python requires Python 3.10 or later, but we recommend that you use the latest version.
You can view your current version of Python by running the following command.

```
python3 --version
```

**Boto3**
The Amazon S3 Encryption Client for Python requires the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) AWS SDK for Python (Boto). The Amazon S3 Encryption Client for Python uses the Boto3 Amazon S3 and AWS KMS service clients. For more information, see [Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) in the *Boto3 documentation*.

## Installation
<a name="python-installation"></a>

To install the Amazon S3 Encryption Client for Python and its dependencies, run the following pip command.

```
pip install amazon-s3-encryption-client-python
```
