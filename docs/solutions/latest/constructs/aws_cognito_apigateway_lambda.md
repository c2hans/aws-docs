---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_cognito_apigateway_lambda.html
---

# aws-cognito-apigateway-lambda
<a name="aws_cognito_apigateway_lambda"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_cognito_apigateway_lambda`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-cognito-apigateway-lambda`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.cognitoapigatewaylambda`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon Cognito securing an Amazon API Gateway Lambda backed REST APIs pattern.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { CognitoToApiGatewayToLambda } from '@aws-solutions-constructs/aws-cognito-apigateway-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';

new CognitoToApiGatewayToLambda(this, 'test-cognito-apigateway-lambda', {
  lambdaFunctionProps: {
    code: lambda.Code.fromAsset(`lambda`),
    runtime: lambda.Runtime.NODEJS_22_X,
    handler: 'index.handler'
  }
});
```

```
from aws_solutions_constructs.aws_cognito_apigateway_lambda import CognitoToApiGatewayToLambda
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
from constructs import Construct

CognitoToApiGatewayToLambda(self, 'test-cognito-apigateway-lambda',
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
import software.amazon.awsconstructs.services.cognitoapigatewaylambda.*;

new CognitoToApiGatewayToLambda(this, "test-cognito-apigateway-lambda",
        new CognitoToApiGatewayToLambdaProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_22_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .build());
```

If you are defining resources and methods on your API (e.g. proxy = false), then you must call addAuthorizers() after the API is fully defined to ensure every method is protected. Here is an example:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { CognitoToApiGatewayToLambda } from '@aws-solutions-constructs/aws-cognito-apigateway-lambda';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const construct = new CognitoToApiGatewayToLambda(this, 'test-cognito-apigateway-lambda', {
    lambdaFunctionProps: {
        code: lambda.Code.fromAsset(`lambda`),
        runtime: lambda.Runtime.NODEJS_22_X,
        handler: 'index.handler'
    },
    apiGatewayProps: {
        proxy: false
    }
});

const resource = construct.apiGateway.root.addResource('foobar');
resource.addMethod('POST');

// Mandatory to call this method to Apply the Cognito Authorizers on all API methods
construct.addAuthorizers();
```

```
from aws_solutions_constructs.aws_cognito_apigateway_lambda import CognitoToApiGatewayToLambda
from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as api,
    Stack
)
from constructs import Construct
from typing import Any

# Overriding LambdaRestApiProps with type Any
gateway_props = dict[Any, Any]

construct = CognitoToApiGatewayToLambda(self, 'test-cognito-apigateway-lambda',
                                        lambda_function_props=_lambda.FunctionProps(
                                            code=_lambda.Code.from_asset(
                                                'lambda'),
                                            runtime=_lambda.Runtime.PYTHON_3_14,
                                            handler='index.handler'
                                        ),
                                        api_gateway_props=gateway_props(
                                            proxy=False
                                        )
                                        )

resource = construct.api_gateway.root.add_resource('foobar')
resource.add_method('POST')

# Mandatory to call this method to Apply the Cognito Authorizers on all API methods
construct.add_authorizers()
```

```
import software.constructs.Construct;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.apigateway.IResource;
import software.amazon.awsconstructs.services.cognitoapigatewaylambda.*;

// Overriding LambdaRestApiProps with type Any
Map<String, Optional<?>> gatewayProps = new HashMap<String, Optional<?>>();
gatewayProps.put("proxy", Optional.of(false));

final CognitoToApiGatewayToLambda construct = new CognitoToApiGatewayToLambda(this,
        "test-cognito-apigateway-lambda",
        new CognitoToApiGatewayToLambdaProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_22_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .apiGatewayProps(gatewayProps)
                .build());

final IResource resource = construct.getApiGateway().getRoot().addResource("foobar");
resource.addMethod("POST");

// Mandatory to call this method to Apply the Cognito Authorizers on all API methods
construct.addAuthorizers();
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - instance of an existing Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. |
| apiGatewayProps? |  [`api.LambdaRestApiProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.LambdaRestApi.html)  | Optional - user-provided props to override the default props for the API Gateway API. |
| cognitoUserPoolProps? |  [`cognito.UserPoolProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPoolProps.html)  | Optional user provided props to override the default props for Cognito User Pool |
| cognitoUserPoolClientProps? |  [`cognito.UserPoolClientProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPoolClientProps.html)  | Optional user provided props to override the default props for Cognito User Pool Client |
| logGroupProps? |  [`logs.LogGroupProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| userPool |  [`cognito.UserPool`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPool.html)  | Returns an instance of cognito.UserPool created by the construct |
| userPoolClient |  [`cognito.UserPoolClient`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPoolClient.html)  | Returns an instance of cognito.UserPoolClient created by the construct |
| apiGateway |  [`api.RestApi`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html)  | Returns an instance of api.RestApi created by the construct |
| apiGatewayCloudWatchRole? |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway for CloudWatch access. |
| apiGatewayLogGroup |  [`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for API Gateway access logging to CloudWatch. |
| apiGatewayAuthorizer |  [`api.CfnAuthorizer`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.CfnAuthorizer.html)  | Returns an instance of the api.CfnAuthorizer created by the construct for API Gateway methods authorization. |
| lambdaFunction |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of lambda.Function created by the construct |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon Cognito
<a name="_amazon_cognito"></a>
+ Set password policy for User Pools
+ Enforce the advanced security mode for User Pools

### Amazon API Gateway
<a name="_amazon_api_gateway"></a>
+ Deploy an edge-optimized API endpoint
+ Enable CloudWatch logging for API Gateway
+ Configure least privilege access IAM role for API Gateway
+ Set the default authorizationType for all API methods to Cognito User Pool
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

![Diagram showing data flow between AWS services including Cognito, API Gateway, Lambda, CloudWatch and IAM Roles](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-cognito-apigateway-lambda.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-cognito-apigateway-lambda) for this pattern to view the code, read/create issues and pull requests and more.
