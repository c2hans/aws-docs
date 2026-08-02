---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/prerequisites.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# AWS CDK prerequisites
<a name="prerequisites"></a>

Complete all prerequisites before getting started with the AWS Cloud Development Kit (AWS CDK).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the * AWS Account Management Reference Guide*.

## Install and configure the AWS CLI
<a name="prerequisites-cli"></a>

When you develop AWS CDK applications on your local machine, you will use the AWS Cloud Development Kit (AWS CDK) Command Line Interface (CLI) to interact with AWS, such as deploying applications to provision your AWS resources. To interact with AWS outside of the AWS Management Console, you must configure security credentials on your local machine. To do this, we recommend that you install and use the AWS Command Line Interface (AWS CLI).

For instructions on installing the AWS CLI, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the * AWS Command Line Interface User Guide*.

How you configure security credentials will depend on how you or your organization manages users. For instructions, see [Authentication and access credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html) in the * AWS Command Line Interface User Guide*.

After installing and configuring the AWS CLI, you should have the following:
+ The AWS CLI installed on your local machine.
+ Credentials configured in a `config` on your local machine using the AWS CLI.

## Install Node.js and programming language prerequisites
<a name="prerequisites-node"></a>

All AWS CDK developers, regardless of the supported programming language that you will use, require [Node.js](https://nodejs.org/en/download/) 22.x or later. All supported programming languages use the same backend, which runs on Node.js. We recommend a version in [active long-term support](https://nodejs.org/en/about/releases/).

For more information on supported Node.js versions, see [Supported Node versions](node-versions.md).

Other programming language prerequisites depend on the language that you will use to develop AWS CDK applications:

**Example**
+ TypeScript 3.8 or later (`npm -g install typescript`)
+ No additional requirements
+ Python 3.9 or later including `pip` and `virtualenv`
+ Java Development Kit (JDK) 8 (a.k.a. 1.8) or later
+ Apache Maven 3.5 or later

  Java IDE recommended (we use Eclipse` in some examples in this guide). IDE must be able to import Maven projects. Check to make sure that your project is set to use Java 1.8. Set the JAVA\_HOME environment variable to the path where you have installed the JDK.
.NET 8.0 or later.
Visual Studio 2019 (any edition) or Visual Studio Code recommended.
Go 1.23 or later.

**Third-party language deprecation**
Each language version is only supported until it is EOL (End Of Life) and is subject to change with prior notice.

## Next steps
<a name="prerequisites-next"></a>

To get started with the AWS CDK, see [Getting started with the AWS CDK](getting-started.md).
