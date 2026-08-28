---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_polly.html
---

# aws-lambda-polly
<a name="aws_lambda_polly"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_lambda_polly`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-lambda-polly`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.lambdapolly`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Lambda function connected to Amazon Polly text-to-speech service. For asynchronous speech synthesis tasks, the construct can optionally create an S3 bucket for audio output and an SNS topic for completion notifications, with appropriate IAM permissions for the Lambda function to interact with Amazon Polly service.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { LambdaToPolly } from '@aws-solutions-constructs/aws-lambda-polly';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new LambdaToPolly(this, 'LambdaToPollyPattern', {
    lambdaFunctionProps: {
        runtime: lambda.Runtime.NODEJS_22_X,
        handler: 'index.handler',
        code: lambda.Code.fromAsset(`lambda`)
    }
});
```

```
from aws_solutions_constructs.aws_lambda_polly import LambdaToPolly
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

LambdaToPolly(self, 'LambdaToPollyPattern',
        lambda_function_props=_lambda.FunctionProps(
            code=_lambda.Code.from_asset('lambda'),
            runtime=_lambda.Runtime.PYTHON_3_14,
            handler='index.handler'
        )
        )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.lambdapolly.*;

new LambdaToPolly(this, "LambdaToPollyPattern", new LambdaToPollyProps.Builder()
        .lambdaFunctionProps(new FunctionProps.Builder()
                .runtime(Runtime.NODEJS_22_X)
                .code(Code.fromAsset("lambda"))
                .handler("index.handler")
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - instance of an existing Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. Function will have these Polly permissions: ['polly:SynthesizeSpeech']. When asyncJobs is true, function will also have ['polly:StartSpeechSynthesisTask', 'polly:GetSpeechSynthesisTask', 'polly:ListSpeechSynthesisTasks']. |
| asyncJobs? |  `boolean`  | Whether to enable asynchronous speech synthesis tasks. When true, an S3 bucket for audio output and an SNS topic for completion notifications will be created, and the Lambda function will be granted permissions to start and monitor asynchronous synthesis tasks. Default: false |
| existingBucketObj? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Existing instance of S3 Bucket object for audio output, providing both this and `bucketProps` will cause an error. Only valid when asyncJobs is true. |
| bucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Bucket. Only valid when asyncJobs is true. |
| bucketEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the name of the output bucket. Only valid when asyncJobs is true. Default: OUTPUT\_BUCKET\_NAME |
| logS3AccessLogs? |  `boolean`  | Whether to turn on Access Logs for the S3 bucket with the associated storage costs. Enabling Access Logging is a best practice. Only valid when asyncJobs is true. Default: true |
| loggingBucketProps? |  [`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the S3 Logging Bucket. Only valid when asyncJobs is true. |
| existingTopicObj? |  [`sns.Topic`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)  | Optional - existing instance of SNS topic object, providing both this and `topicProps` will cause an error. Only valid when asyncJobs is true. |
| topicProps? |  [`sns.TopicProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.TopicProps.html)  | Optional - user provided properties to override the default properties for the SNS topic. Providing both this and `existingTopicObj` causes an error. Only valid when asyncJobs is true. |
| topicEnvironmentVariableName? |  `string`  | Optional Name for the Lambda function environment variable set to the ARN of the SNS topic used for asynchronous task completion notifications. Only valid when asyncJobs is true. Default: SNS\_TOPIC\_ARN |
| existingTopicEncryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | If an existing topic is provided in the `existingTopicObj` property, and that topic is encrypted with a customer managed KMS key, this property must specify that key. Only valid when asyncJobs is true. |
| topicEncryptionKey? |  [`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)  | An optional, imported encryption key to encrypt the SNS Topic with. Only valid when asyncJobs is true. |
| topicEncryptionKeyProps? |  [`kms.KeyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)  | Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with. Only valid when asyncJobs is true. |
| enableTopicEncryptionWithCustomerManagedKey? |  `boolean`  | If no key is provided, this flag determines whether the SNS Topic is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: topicProps.masterKey, topicEncryptionKey or topicEncryptionKeyProps. Only valid when asyncJobs is true. |
| existingVpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An existing VPC for the construct to use (construct will NOT create a new VPC in this case) |
| vpcProps? |  [`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Properties to override default properties if deployVpc is true |
| deployVpc? |  `boolean`  | Whether to deploy a new VPC. Default: false |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| lambdaFunction |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |
| destinationBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of the S3 bucket if it is created by the pattern. |
| loggingBucket? |  [`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)  | Returns an instance of s3.Bucket created by the construct as the logging bucket for the destination bucket. |
| destinationBucketInterface? |  [`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)  | Returns an interface of s3.IBucket used by the construct for the destination bucket whether created by the pattern or supplied from the client. |
| snsNotificationTopic? |  [`sns.Topic`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)  | Returns an instance of the SNS topic created for asynchronous task completion notifications when asyncJobs is true. |
| notificationTopicEncryptionKey? |  [`kms.IKey`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.IKey.html)  | Returns an instance of kms.IKey used for the SNS Topic. |
| vpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + (default) OUTPUT\_BUCKET\_NAME (when asyncJobs is true)
  + (default) SNS\_TOPIC\_ARN (when asyncJobs is true)
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)
+ Grant permissions to use Amazon Polly service (['polly:SynthesizeSpeech'] by default)
+ When asyncJobs is true, grant permissions to start and monitor asynchronous synthesis tasks (['polly:StartSpeechSynthesisTask', 'polly:GetSpeechSynthesisTask', 'polly:ListSpeechSynthesisTasks']), and read/write to the S3 bucket

### Amazon S3 Bucket (when asyncJobs is true)
<a name="_amazon_s3_bucket_when_asyncjobs_is_true"></a>
+ Configure Access logging for S3 Bucket
+ Enable server-side encryption for S3 Bucket using AWS managed KMS Key
+ Enforce encryption of data in transit
+ Turn on the versioning for S3 Bucket
+ Don’t allow public access for S3 Bucket
+ Retain the S3 Bucket when deleting the CloudFormation stack
+ Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon SNS Topic (when asyncJobs is true)
<a name="_amazon_sns_topic_when_asyncjobs_is_true"></a>
+ Configure server-side encryption using AWS managed KMS Key
+ Create topic for asynchronous task completion notifications

### Amazon Polly Service
<a name="_amazon_polly_service"></a>
+ Lambda function will have permissions to call ['polly:SynthesizeSpeech'] operation

 **When asyncJobs is true**
+ Lambda function will add permissions to call ['polly:StartSpeechSynthesisTask', 'polly:GetSpeechSynthesisTask', 'polly:ListSpeechSynthesisTasks']
+ When asyncJobs is true, an SNS topic will be created and the Lambda function is granted permission to call ['sns:Publish']

### Amazon VPC
<a name="_amazon_vpc"></a>
+ If deployVpc is true, a minimal VPC will be created with:
  + Interface Endpoints for Amazon Polly
  + Gateway Endpoints for Amazon S3 (when asyncJobs is true)
  + Private subnets for Lambda function
  + Appropriate security groups and routing

## Architecture
<a name="_architecture"></a>

 **Default Implementation**

![Diagram showing the Lambda function, Amazon Polly service, and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-polly.png)

 **Default Implementation when asyncJobs = true**

![Diagram showing the Lambda function, destination S3 bucket (when asyncJobs is true), SNS topic, Amazon Polly service, and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-polly-async.png)

## Example Lambda Function Implementation
<a name="_example_lambda_function_implementation"></a>

While Solutions Constructs does not publish code for the Lambda function to call Polly, here are examples of calling Polly: [examples](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/polly/general-examples/src/polly_synthesize_to_s3.js). (these examples are in JavaScript, but examples in other languages can also be found at this site)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-lambda-polly) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
