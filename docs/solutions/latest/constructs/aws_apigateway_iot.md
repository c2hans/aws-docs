---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_apigateway_iot.html
---

# aws-apigateway-iot
<a name="aws_apigateway_iot"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_apigateway_iot`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-apigateway-iot`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.apigatewayiot`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon API Gateway REST API connected to AWS IoT pattern.

This construct creates a scalable HTTPS proxy between API Gateway and AWS IoT. This comes in handy when wanting to allow legacy devices that do not support the MQTT or MQTT/Websocket protocol to interact with the AWS IoT platform.

This implementation enables write-only messages to be published on given MQTT topics, and also supports shadow updates of HTTPS devices to allowed things in the device registry. It does not involve Lambda functions for proxying messages, and instead relies on direct API Gateway to AWS IoT integration which supports both JSON messages as well as binary messages.

Here is a minimal deployable pattern definition, note that the ATS endpoint for IoT must be used to avoid SSL certificate issues:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { ApiGatewayToIot } from '@aws-solutions-constructs/aws-apigateway-iot';

new ApiGatewayToIot(this, 'ApiGatewayToIotPattern', {
    iotEndpoint: 'a1234567890123-ats'
});
```

```
from aws_solutions_constructs.aws_apigateway_iot import ApiGatewayToIot
from aws_cdk import Stack
from constructs import Construct

ApiGatewayToIot(self, 'ApiGatewayToIotPattern',
    iot_endpoint='a1234567890123-ats'
)
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.apigatewayiot.*;

new ApiGatewayToIot(this, "ApiGatewayToIotPattern", new ApiGatewayToIotProps.Builder()
        .iotEndpoint("a1234567890123-ats")
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| iotEndpoint |  `string`  | The AWS IoT endpoint subdomain to integrate the API Gateway with (e.g a1234567890123-ats). Note that this must point to the ATS endpoint to avoid SSL certificate trust issues. The endpoint can be retrieved by running `aws iot describe-endpoint --endpoint-type iot:Data-ATS`. |
| apiGatewayCreateApiKey? |  `boolean`  | If set to `true`, an API Key is created and associated to a UsagePlan. User should specify `x-api-key` header while accessing RestApi. Default value set to `false`  |
| apiGatewayExecutionRole? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | IAM Role used by the API Gateway to access AWS IoT. If not specified, a default role is created with wildcard (’\*’) access to all topics and things. |
| apiGatewayProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApiProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApiProps.html)  | Optional user-provided props to override the default props for the API Gateway. |
| createUsagePlan? | boolean | Whether to create a Usage Plan attached to the API. Must be true if apiGatewayProps.defaultMethodOptions.apiKeyRequired is true. @default - true (to match legacy behavior) |
| logGroupProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| apiGateway |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html)  | Returns an instance of the API Gateway REST API created by the pattern. |
| apiGatewayRole |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway. |
| apiGatewayCloudWatchRole? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway for CloudWatch access. |
| apiGatewayLogGroup |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for API Gateway access logging to CloudWatch. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon API Gateway
<a name="_amazon_api_gateway"></a>
+ Deploy an edge-optimized API Endpoint
+ Creates API Resources with `POST` Method to publish messages to IoT Topics
+ Creates API Resources with `POST` Method to publish messages to ThingShadow & NamedShadows
+ Enable CloudWatch logging for API Gateway
+ Configure IAM role for API Gateway with access to all topics and things
+ Set the default authorizationType for all API methods to IAM
+ Enable X-Ray Tracing
+ Creates a UsagePlan and associates to `prod` stage

Below is a description of the different resources and methods exposed by the API Gateway after deploying the Construct.

| Method | Resource | Query parameter(s) | Return code(s) | Description |
| --- | --- | --- | --- | --- |
|  **POST**  |  `/message/<topics>`  |  **qos**  |  `200/403/500`  | By calling this endpoint, you need to pass the topics on which you would like to publish (e.g `/message/device/foo`). |
|  **POST**  |  `/shadow/<thingName>`  |  **None**  |  `200/403/500`  | This route allows to update the shadow document of a thing, given its `thingName` using Unnamed (classic) shadow type. The body shall comply with the standard shadow structure comprising a `state` node and associated `desired` and `reported` nodes. |
|  **POST**  |  `/shadow/<thingName>/<shadowName>`  |  **None**  |  `200/403/500`  | This route allows to update the named shadow document of a thing, given its `thingName` and the `shadowName` using the Named shadow type. The body shall comply with the standard shadow structure comprising a `state` node and associated `desired` and `reported` nodes. |

## Architecture
<a name="_architecture"></a>

![IoT architecture diagram showing device, API Gateway, IoT Core, and related components.](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-apigateway-iot.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-apigateway-iot) for this pattern to view the code, read/create issues and pull requests and more.
