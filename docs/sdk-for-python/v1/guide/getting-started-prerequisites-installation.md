---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/getting-started-prerequisites-installation.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Prerequisites and installation
<a name="getting-started-prerequisites-installation"></a>

To start building with the AWS SDK for Python, you need an AWS account, a supported Python version, and the SDK's service client packages. The following steps help you verify your environment, create an isolated workspace, and install only the packages that your application requires.

Before you begin:
+ Create an AWS account if you don't have one. For instructions, see [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management User Guide*.
+ Install Python 3.12 or later. The installation commands in this guide use **pip**, the package installer included with most Python installations. To install Python, see [Download Python](https://www.python.org/downloads/).

Confirm that Python and **pip** are available:

```
python --version
python -m pip --version
```

Create a virtual environment to keep this project's packages separate from other Python projects:

```
python -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```
source .venv/bin/activate
```

On Windows, activate it with the following command instead:

```
.venv\Scripts\activate
```

Then update **pip**:

```
python -m pip install --upgrade pip
```

The preceding steps are the standard setup for most SDK projects. The packages that you install next are specific to the examples in this chapter.

The SDK publishes a separate package for each AWS service client. Install the Amazon DynamoDB and Amazon Transcribe client packages:

```
python -m pip install aws-sdk-dynamodb aws-sdk-transcribe-streaming
```

This command installs both clients as individual packages.

Alternatively, install the same clients as optional dependencies of the `aws-sdk-python` meta-package:

```
python -m pip install "aws-sdk-python[dynamodb,transcribe_streaming]"
```

The meta-package installs only the service clients that you select as extras; without extras, it installs no clients. It coordinates client versions through its MAJOR.MINOR version, so it installs compatible client versions together.

Use the meta-package when your application depends on several clients. Install individual client packages when your application uses only one or two services and you want the smallest dependency set.

The preceding commands install the latest package versions. To control which version is installed, add a version specifier to the package name. Version specifiers work for both individual client packages and the meta-package:

```
# Install version 0.11.0 specifically
python -m pip install "aws-sdk-dynamodb==0.11.0" "aws-sdk-transcribe-streaming==0.11.0"  # individual client packages
python -m pip install "aws-sdk-python[dynamodb,transcribe_streaming]==0.11.0"            # meta-package

# Install the latest version that is at least 0.11.0
python -m pip install "aws-sdk-dynamodb>=0.11.0" "aws-sdk-transcribe-streaming>=0.11.0"  # individual client packages
python -m pip install "aws-sdk-python[dynamodb,transcribe_streaming]>=0.11.0"            # meta-package

# Install the latest version that is at most 0.11.0
python -m pip install "aws-sdk-dynamodb<=0.11.0" "aws-sdk-transcribe-streaming<=0.11.0"  # individual client packages
python -m pip install "aws-sdk-python[dynamodb,transcribe_streaming]<=0.11.0"            # meta-package

# Install the latest version that is compatible with 0.11.0 (>=0.11.0, <0.12.0)
python -m pip install "aws-sdk-dynamodb~=0.11.0" "aws-sdk-transcribe-streaming~=0.11.0"  # individual client packages
python -m pip install "aws-sdk-python[dynamodb,transcribe_streaming]~=0.11.0"            # meta-package
```
