---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/getting-started-with-aws-solutions-constructs.html
---

# Getting Started with AWS Solutions Constructs
<a name="getting-started-with-aws-solutions-constructs"></a>

This topic describes how to install and configure AWS Cloud Development Kit (AWS CDK), AWS Solutions Constructs, and create your first AWS CDK app using AWS Solutions Constructs patterns.

**Tip**
Want to dig deeper? Try the [CDK Workshop](https://cdkworkshop.com/) for a more in-depth tour of a real-world project.

**Tip**
For more information about getting started with the AWS Cloud Development Kit (AWS CDK), refer to the [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html).

## Prerequisites
<a name="prerequisites"></a>

AWS Solutions Constructs is built upon the AWS CDK, so you need to install Node.js (>= 10.3.0), even those working in languages other than TypeScript or JavaScript. This is because the [AWS CDK](https://github.com/aws/aws-cdk) and AWS Solutions Constructs are developed in TypeScript and run on Node.js. The bindings for other supported languages use this backend and toolset.

You must provide your credentials and an AWS Region to use the AWS CDK CLI, as described in Specifying Your Credentials and Region.

Other prerequisites depend on your development language, as follows.

| Language | Prerequisites |
| --- | --- |
|  ![Python](https://docs.aws.amazon.com/solutions/latest/constructs/images/python.png)Python | Python >= 3.6 |
|  ![TypeScript](https://docs.aws.amazon.com/solutions/latest/constructs/images/typescript.png)TypeScript | TypeScript >= 2.7 |
|  ![Java](https://docs.aws.amazon.com/solutions/latest/constructs/images/java.png)Java | Java >= 1.8 |

## Installing the AWS CDK
<a name="installing-the-aws-cdk"></a>

To install and configure the AWS CDK, please refer to the AWS CDK Developer Guide - [Installing the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install).

## Working with AWS Solutions Constructs
<a name="working-with-the-aws-solutions-constructs-library"></a>

The typical workflow for creating a new app when working with AWS Solutions Constructs follows the same approach as the AWS CDK.

1. Create the app directory.

1. Initialize the app.

1. Add the AWS Solutions Constructs pattern dependencies.

1. Add additional code to the app.

1. Compile the app, if necessary.

1. Deploy the resources defined in the app.

1. Test the app.

If there are any issues, loop through modify, compile (if necessary), deploy, and test again.
