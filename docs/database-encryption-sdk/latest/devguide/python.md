---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/python.html
---

# DynamoDB Encryption Client for Python
<a name="python"></a>

**Note**
Our client-side encryption library was [renamed to AWS Database Encryption SDK](DDBEC-rename.md). The following topic provides information on versions 1.*x*—2.*x* of the DynamoDB Encryption Client for Java and versions 1.*x*—3.*x* of the DynamoDB Encryption Client for Python. For more information, see [AWS Database Encryption SDK for DynamoDB version support](legacy-dynamodb-encryption-client.md#legacy-support).

This topic explains how to install and use the DynamoDB Encryption Client for Python. You can find the code in the [aws-dynamodb-encryption-python](https://github.com/aws/aws-dynamodb-encryption-python/) repository on GitHub, including complete and tested [sample code](https://github.com/aws/aws-dynamodb-encryption-python/tree/master/examples) to help you get started.

**Note**
Versions 1.*x*.*x* and 2.*x*.*x* of the DynamoDB Encryption Client for Python are in [end-of-support phase](what-is-database-encryption-sdk.md#support) effective July 2022. Upgrade to a newer version as soon as possible.

**Topics**
+ [Prerequisites](#python-prerequisites)
+ [Installation](#python-installation)
+ [Using the DynamoDB Encryption Client for Python](python-using.md)
+ [Python examples](python-examples.md)

## Prerequisites
<a name="python-prerequisites"></a>

Before you install the Amazon DynamoDB Encryption Client for Python, be sure you have the following prerequisites.

**A supported version of Python**
Python 3.8 or later is required by the Amazon DynamoDB Encryption Client for Python versions 3.3.0 and later. To download Python, see [Python downloads](https://www.python.org/downloads/).
Earlier versions of the Amazon DynamoDB Encryption Client for Python support Python 2.7 and Python 3.4 and later, but we recommend that you use the latest version of the DynamoDB Encryption Client.

**The pip installation tool for Python**
Python 3.6 and later include **pip**, although you might want to upgrade it. For more information about upgrading or installing pip, see [Installation](https://pip.pypa.io/en/latest/installation/) in the **pip** documentation.

## Installation
<a name="python-installation"></a>

Use **pip** to install the Amazon DynamoDB Encryption Client for Python, as shown in the following examples.

**To install the latest version**

```
pip install dynamodb-encryption-sdk
```

For more details about using **pip** to install and upgrade packages, see [Installing Packages](https://packaging.python.org/tutorials/installing-packages/).

The DynamoDB Encryption Client requires the [cryptography library](https://cryptography.io/en/latest/) on all platforms. All versions of **pip** install and build the **cryptography** library on Windows. **pip** 8.1 and later installs and builds **cryptography** on Linux. If you are using an earlier version of **pip** and your Linux environment doesn't have the tools needed to build the **cryptography** library, you need to install them. For more information, see [Building cryptography on Linux](https://cryptography.io/en/latest/installation/#building-cryptography-on-linux).

You can get the latest development version of the DynamoDB Encryption Client from the [aws-dynamodb-encryption-python](https://github.com/aws/aws-dynamodb-encryption-python/) repository on GitHub.

After you install the DynamoDB Encryption Client, get started by looking at the example Python code in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
