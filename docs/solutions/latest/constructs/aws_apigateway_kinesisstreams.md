---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_apigateway_kinesisstreams.html
---

# aws-apigateway-kinesisstreams
<a name="aws_apigateway_kinesisstreams"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_apigateway_kinesisstreams`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-apigateway-kinesisstreams`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.apigatewaykinesisstreams`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon API Gateway connected to an Amazon Kinesis Data Stream pattern.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { ApiGatewayToKinesisStreams, ApiGatewayToKinesisStreamsProps } from '@aws-solutions-constructs/aws-apigateway-kinesisstreams';

new ApiGatewayToKinesisStreams(this, 'test-apigw-kinesis', {});
```

```
from aws_solutions_constructs.aws_apigateway_kinesisstreams import ApiGatewayToKinesisStreams
from aws_cdk import Stack
from constructs import Construct

ApiGatewayToKinesisStreams(self, 'test-apigw-kinesis')
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.apigatewaykinesisstreams.*;

new ApiGatewayToKinesisStreams(this, "test-apigw-kinesis", new ApiGatewayToKinesisStreamsProps.Builder()
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| apiGatewayProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApiProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApiProps.html)  | Optional - user provided props to override the default props for the API Gateway. |
| putRecordRequestTemplate? |  `string`  | API Gateway request template for the PutRecord action. If not provided, a default one will be used. |
| createUsagePlan? | boolean | Whether to create a Usage Plan attached to the API. Must be true if apiGatewayProps.defaultMethodOptions.apiKeyRequired is true. @default - true (to match legacy behavior) |
| additionalPutRecordRequestTemplates? |  `{ [contentType: string]: string; }`  | Optional PutRecord Request Templates for content-types other than `application/json`. Use the `putRecordRequestTemplate` property to set the request template for the `application/json` content-type. |
| putRecordRequestModel? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.ModelOptions.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.ModelOptions.html)  | API Gateway request model for the PutRecord action. If not provided, a default one will be created. |
| putRecordIntegrationResponses? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.IntegrationResponse.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.IntegrationResponse.html)  | Optional, custom API Gateway Integration Response for the PutRecord action. |
| putRecordMethodResponses? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.MethodResponse.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.MethodResponse.html)  | Optional, custom API Gateway Method Responses for the putRecord action. default: [{ statusCode: "200", responseParameters: { "method.response.header.Content-Type": true }},{ statusCode: "500", responseParameters: { "method.response.header.Content-Type": true } } ] |
| putRecordsRequestTemplate? |  `string`  | API Gateway request template for the PutRecords action. If not provided, a default one will be used. |
| additionalPutRecordsRequestTemplates? |  `{ [contentType: string]: string; }`  | Optional PutRecords Request Templates for content-types other than `application/json`. Use the `putRecordsRequestTemplate` property to set the request template for the `application/json` content-type. |
| putRecordsRequestModel? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.ModelOptions.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.ModelOptions.html)  | API Gateway request model for the PutRecords action. If not provided, a default one will be created. |
| putRecordsIntegrationResponses? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.IntegrationResponse.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.IntegrationResponse.html)  | Optional, custom API Gateway Integration Response for the PutRecords action. |
| putRecordsMethodResponses? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.MethodResponse.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.MethodResponse.html)  | Optional, custom API Gateway Method Responses for the putRecords action. default: [{ statusCode: "200", responseParameters: { "method.response.header.Content-Type": true }},{ statusCode: "500", responseParameters: { "method.response.header.Content-Type": true } } ] |
| existingStreamObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Existing instance of Kinesis Stream, providing both this and `kinesisStreamProps` will cause an error. |
| kinesisStreamProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.StreamProps.html)  | Optional user-provided props to override the default props for the Kinesis stream. |
| logGroupProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |
| createCloudWatchAlarms |  `boolean`  | Whether to create recommended CloudWatch alarms for Kinesis Data Stream. Default value is set to `true`  |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| apiGateway |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html)  | Returns an instance of the API Gateway REST API created by the pattern. |
| apiGatewayRole |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway. |
| apiGatewayCloudWatchRole? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway for CloudWatch access. |
| apiGatewayLogGroup |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for API Gateway access logging to CloudWatch. |
| kinesisStream |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesis.Stream.html)  | Returns an instance of the Kinesis stream created or used by the pattern. |
| cloudwatchAlarms? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns an array of recommended CloudWatch Alarms created by the construct for Kinesis Data stream |

## Sample API Usage
<a name="_sample_api_usage"></a>

|  **Method**  |  **Request Path**  |  **Request Body**  |  **Stream Action**  |  **Description**  |
| --- | --- | --- | --- | --- |
| POST |  `/record`  |  `{ "data": "Hello World!", "partitionKey": "pk001" }`  |  `kinesis:PutRecord`  | Writes a single data record into the stream. |
| POST |  `/records`  |  `{ "records": [{ "data": "abc", "partitionKey": "pk001" }, { "data": "xyz", "partitionKey": "pk001" }] }`  |  `kinesis:PutRecords`  | Writes multiple data records into the stream in a single call. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon API Gateway
<a name="_amazon_api_gateway"></a>
+ Deploy an edge-optimized API endpoint
+ Enable CloudWatch logging for API Gateway
+ Configure least privilege access IAM role for API Gateway
+ Set the default authorizationType for all API methods to IAM
+ Enable X-Ray Tracing
+ Validate request body before passing data to Kinesis

### Amazon Kinesis Data Stream
<a name="_amazon_kinesis_data_stream"></a>
+ Configure least privilege access IAM role for Kinesis Stream
+ Enable server-side encryption for Kinesis Stream using AWS Managed KMS Key

## Architecture
<a name="_architecture"></a>

![Diagram showing data flow between cloud search, code analysis, and network components.](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-apigateway-kinesisstreams.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-apigateway-kinesisstreams) for this pattern to view the code, read/create issues and pull requests and more.
