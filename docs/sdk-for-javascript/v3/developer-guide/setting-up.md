---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-up.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Set up the SDK for JavaScript
<a name="setting-up"></a>

The topics in this section explain how to install and load the SDK for JavaScript so you can access the web services supported by the SDK.

**Topics**
+ [Prerequisites](#jssdk-prerequisites)
+ [Install the SDK for JavaScript](#installing-jssdk)
+ [Load the SDK for JavaScript](#loading-the-jssdk)

## Prerequisites
<a name="jssdk-prerequisites"></a>

[Install Node.js](https://nodejs.org/en/download). AWS recommends using the Active LTS version of Node.js for development.

**Topics**
+ [Set up an AWS Node.js environment](#setting-up-node)
+ [Supported web browsers](#browsers-supported)

### Set up an AWS Node.js environment
<a name="setting-up-node"></a>

To set up an AWS Node.js environment in which you can run your application, use any of the following methods:
+ Choose an Amazon Machine Image (AMI) with Node.js preinstalled. Then create an Amazon EC2 instance using that AMI. When creating your Amazon EC2 instance, choose your AMI from the AWS Marketplace. Search the AWS Marketplace for Node.js and choose an AMI option that includes a preinstalled version of Node.js (32-bit or 64-bit).
+ Create an Amazon EC2 instance and install Node.js on it. For more information about how to install Node.js on an Amazon Linux instance, see [Setting up Node.js on an Amazon EC2 instance](setting-up-node-on-ec2-instance.md).
+ Create a serverless environment using AWS Lambda to run Node.js as a Lambda function. For more information about using Node.js within a Lambda function, see [Programming model (Node.js)](https://docs.aws.amazon.com/lambda/latest/dg/programming-model.html) in the *AWS Lambda Developer Guide*.
+ Deploy your Node.js application to AWS Elastic Beanstalk. For more information about using Node.js with Elastic Beanstalk, see [Deploying Node.js applications to AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.html) in the *AWS Elastic Beanstalk Developer Guide*.

### Supported web browsers
<a name="browsers-supported"></a>

The AWS SDK for JavaScript supports all modern web browsers.

In version 3.567.0 or later, the SDK for JavaScript emits ES2021 artifacts, which supports the following minimum versions.

****

| Browser | Version |
| --- | --- |
| Google Chrome | 85.0\+ |
| Mozilla Firefox | 80.0\+ |
| Opera | 71.0\+ |
| Microsoft Edge | 85.0\+ |
| Apple Safari | 14.1\+ |
| Samsung Internet | 14.0\+ |

In version 3.183.0 through 3.566.0, the SDK for JavaScript uses ES2020 artifacts, which supports the following minimum versions.

****

| Browser | Version |
| --- | --- |
| Google Chrome | 80.0\+ |
| Mozilla Firefox | 80.0\+ |
| Opera | 63.0\+ |
| Microsoft Edge | 80.0\+ |
| Apple Safari | 14.1\+ |
| Samsung Internet | 12.0\+ |

In version 3.182.0 or earlier, the SDK for JavaScript uses ES5 artifacts, which supports the following minimum versions.

****

| Browser | Version |
| --- | --- |
| Google Chrome | 49.0\+ |
| Mozilla Firefox | 45.0\+ |
| Opera | 36.0\+ |
| Microsoft Edge | 12.0\+ |
| Windows Internet Explorer | N/A |
| Apple Safari | 9.0\+ |
| Android Browser | 76.0\+ |
| UC Browser | 12.12\+ |
| Samsung Internet | 5.0\+ |

**Note**
Frameworks such as AWS Amplify might not offer the same browser support as the SDK for JavaScript. See the [AWS Amplify Documentation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) for details.

## Install the SDK for JavaScript
<a name="installing-jssdk"></a>

Not all services are immediately available in the SDK or in all AWS Regions.

To install a service from the AWS SDK for JavaScript using [npm, the Node.js package manager](https://www.npmjs.com/), enter the following command at the command prompt, where {{SERVICE}} is the name of a service, such as `s3`.

```
npm install @aws-sdk/client-{{SERVICE}}
```

For a full list of the AWS SDK for JavaScript service client packages, see the [AWS SDK for JavaScript API Reference guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/).

## Load the SDK for JavaScript
<a name="loading-the-jssdk"></a>

After you install the SDK, you can load a client package in your node application using `import`. For example, to load the Amazon S3 client and the Amazon S3 [ListBuckets](https://docs.aws.amazon.com//AmazonS3/latest/API/API_ListBuckets.html) command, use the following.

```
import { S3Client, ListBucketsCommand } from "@aws-sdk/client-s3";
```
