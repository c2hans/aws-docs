---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

## Build environment specifications
<a name="build-environment-specifications"></a>

To build and deploy this guidance:
+ We recommend using Ubuntu with minimum 4 cores CPU and16GB RAM. MacOS (Intel) or other Linux distributions are also supported.
+ The computer used to build the guidance must be able to access the internet.

## AWS account
<a name="aws-account"></a>

 **A CDK bootstrapped AWS account**: You must Bootstrap your AWS CDK environment in the target Region you want to deploy, using the AWS CDK toolkit’s `cdk bootstrap` command. From the command line, authenticate into your AWS account, and run `cdk bootstrap aws://<YOUR ACCOUNT NUMBER>/<REGION>`. For more information, refer to the [AWS CDK’s Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) page.

## Tools
<a name="tools"></a>
+ The latest version of the [AWS CLI](https://aws.amazon.com/cli/), installed and configured.
+ The latest version of the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html).
+  [Nodejs](https://docs.npmjs.com/getting-started) version 20 or newer.
+  [Git](https://git-scm.com/) command line.
+ Java Runtime
+ The guidance requires a Java 17 Runtime. We recommend using [Amazon Corretto 17](https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html). Alternatively, you can also use other OpenJDKs such as [Eclipse Temurin](https://adoptium.net/en-GB/temurin/releases/?version=8).
+ Maven (>=3.5.2)
+ https://maven.apache.org/install.html. We recommend configuring Maven to use an OpenJDK17 compatible JAVA version, such as Amazon Corretto 17.
+ Docker Desktop (>= v20.10): https://www.docker.com/get-started/
+ Curl: https://curl.se/
