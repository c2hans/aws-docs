---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_cloudfront_apigateway_lambda.html
---

# aws-cloudfront-apigateway-lambda
<a name="aws_cloudfront_apigateway_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_cloudfront_apigateway_lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-cloudfront-apigateway-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.cloudfrontapigatewaylambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS CloudFront fronting an Amazon API Gateway Lambda backed REST API.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { CloudFrontToApiGatewayToLambda } from '@aws-solutions-constructs/aws-cloudfront-apigateway-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new CloudFrontToApiGatewayToLambda(this, 'test-cloudfront-apigateway-lambda', {
  lambdaFunctionProps: {
    code: lambda.Code.fromAsset(`lambda`),
    runtime: lambda.Runtime.NODEJS_22_X,
    handler: 'index.handler'
  },
  apiGatewayProps: {
    defaultMethodOptions: {
      authorizationType: api.AuthorizationType.NONE
    }
  },
});
```

```
from aws_solutions_constructs.aws_cloudfront_apigateway_lambda import CloudFrontToApiGatewayToLambda
from aws_cdk import (
  aws_lambda as _lambda,
  aws_apigateway as apigw,
  Stack
)
from constructs import Construct

        CloudFrontToApiGatewayToLambda(
            self, 'CloudFrontApiGatewayToLambda',
            lambda_function_props=_lambda.FunctionProps(
                runtime=_lambda.Runtime.PYTHON_3_14,
                code=_lambda.Code.from_asset('lambda'),
                handler='hello.handler',
            ),
            # NOTE - we use RestApiProps here because the actual type, LambdaRestApiProps requires
            # the handler function which does not yet exist. As RestApiProps is a subset of of LambdaRestApiProps
            # (although does not *extend* that interface) this works fine when the props object reaches the
            # underlying TypeScript code that implements Constructs
            api_gateway_props=apigw.RestApiProps(
                default_method_options=apigw.MethodOptions(
                    authorization_type=apigw.AuthorizationType.NONE
                )
            )
        )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.cloudfrontapigatewaylambda.*;
import software.amazon.awsconstructs.services.cloudfrontapigatewaylambda.CloudFrontToApiGatewayToLambdaProps;

new CloudFrontToApiGatewayToLambda(this, "ApiGatewayToLambdaPattern", new CloudFrontToApiGatewayToLambdaProps.Builder()
        .lambdaFunctionProps(new FunctionProps.Builder()
                .runtime(Runtime.NODEJS_22_X) // execution environment
                .code(Code.fromAsset("lambda")) // code loaded from the `lambda` directory (under root, next to `src`)
                .handler("hello.handler") // file is `hello`, function is `handler`
                .build())
        // NOTE - we use RestApiProps here because the actual type, LambdaRestApiProps requires
        // the handler function which does not yet exist. As RestApiProps is a subset of of LambdaRestApiProps
        // (although does not *extend* that interface) this works fine when the props object reaches the
        // underlying TypeScript code that implements Constructs
        .apiGatewayProps(new RestApiProps.Builder()
                .defaultMethodOptions(new MethodOptions.Builder()
                        .authorizationType(AuthorizationType.NONE)
                        .build())
                .build())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Existing instance of Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional user provided props to override the default props for the Lambda function. |
| apiGatewayProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.LambdaRestApiProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.LambdaRestApiProps.html)  | User provided props to override the default props for the API Gateway. As of release 2.48.0, clients must include this property with `defaultMethodOptions: { authorizationType: string }` specified. See Issue1043 in the github repo https://github.com/awslabs/aws-solutions-constructs/issues/1043 |
| cloudFrontDistributionProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.DistributionProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.DistributionProps.html)  | Optional user provided props to override the default props for CloudFront Distribution |
| insertHttpSecurityHeaders? |  `boolean`  | Optional user provided props to turn on/off the automatic injection of best practice HTTP security headers in all responses from CloudFront |
| responseHeadersPolicyProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.ResponseHeadersPolicyProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.ResponseHeadersPolicyProps.html)  | Optional user provided configuration that cloudfront applies to all http responses. |
| logGroupProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | Optional user provided props to override the default props for for the CloudWatchLogs LogGroup. |
| cloudFrontLoggingBucketProps? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional user provided props to override the default props for the CloudFront Logging Bucket. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| cloudFrontWebDistribution |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Distribution.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Distribution.html)  | Returns an instance of cloudfront.Distribution created by the construct |
| cloudFrontFunction? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Function.html)  | Returns an instance of the Cloudfront function created by the pattern. |
| cloudFrontLoggingBucket |  [https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3-readme.html](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3-readme.html)  | Returns an instance of the logging bucket for CloudFront Distribution. |
| apiGateway |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html)  | Returns an instance of the API Gateway REST API created by the pattern. |
| apiGatewayCloudWatchRole? |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway for CloudWatch access. |
| apiGatewayLogGroup |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for API Gateway access logging to CloudWatch. |
| lambdaFunction |  [https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of the Lambda function created by the pattern. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon CloudFront
<a name="_amazon_cloudfront"></a>
+ Configure Access logging for CloudFront Distribution
+ Enable automatic injection of best practice HTTP security headers in all responses from CloudFront Distribution

### Amazon API Gateway
<a name="_amazon_api_gateway"></a>
+ Deploy a regional API endpoint
+ Enable CloudWatch logging for API Gateway
+ Configure least privilege access IAM role for API Gateway
+ Set the default authorizationType for all API methods to NONE
+ Enable X-Ray Tracing

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for NodeJs Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED (for Node 10.x and higher functions)

## Architecture
<a name="_architecture"></a>

![Diagram showing data flow between AWS services including CloudFront, Api Gateway and Lambda](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-cloudfront-apigateway-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-cloudfront-apigateway-lambda) for this pattern to view the code, read/create issues and pull requests and more.
