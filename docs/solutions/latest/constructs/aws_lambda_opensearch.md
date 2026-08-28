---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_opensearch.html
---

# aws-lambda-opensearch
<a name="aws_lambda_opensearch"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_lambda_opensearch`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-lambda-opensearch`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.lambdaopensearch`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Lambda function and Amazon OpenSearch Service with the least privileged permissions.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps, Aws } from 'aws-cdk-lib';
import { LambdaToOpenSearch } from '@aws-solutions-constructs/aws-lambda-opensearch';
import * as lambda from "aws-cdk-lib/aws-lambda";

const lambdaProps: lambda.FunctionProps = {
  code: lambda.Code.fromAsset(`lambda`),
  runtime: lambda.Runtime.NODEJS_22_X,
  handler: 'index.handler'
};

new LambdaToOpenSearch(this, 'sample', {
  lambdaFunctionProps: lambdaProps,
  openSearchDomainName: 'testdomain',
  // NOTE: Ensure the Cognito domain name is globally unique
  cognitoDomainName: 'globallyuniquedomain' + Aws.ACCOUNT_ID
});
```

```
from aws_solutions_constructs.aws_lambda_opensearch import LambdaToOpenSearch
from aws_cdk import (
    aws_lambda as _lambda,
    Aws,
    Stack
)
from constructs import Construct

lambda_props = _lambda.FunctionProps(
    code=_lambda.Code.from_asset('lambda'),
    runtime=_lambda.Runtime.PYTHON_3_14,
    handler='index.handler'
)

LambdaToOpenSearch(self, 'sample',
                            lambda_function_props=lambda_props,
                            open_search_domain_name='testdomain',
                            # NOTE: Ensure the Cognito domain name is globally unique
                            cognito_domain_name='globallyuniquedomain' + Aws.ACCOUNT_ID
                            )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.Aws;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awsconstructs.services.lambdaopensearch.*;

new LambdaToOpenSearch(this, "sample",
        new LambdaToOpenSearchProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_22_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .openSearchDomainName("testdomain")
                // NOTE: Ensure the Cognito domain name is globally unique
                .cognitoDomainName("globallyuniquedomain" + Aws.ACCOUNT_ID)
                .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingLambdaObj? |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Optional - instance of an existing Lambda Function object, providing both this and `lambdaFunctionProps` will cause an error. |
| lambdaFunctionProps? |  [`lambda.FunctionProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.FunctionProps.html)  | Optional - user provided props to override the default props for the Lambda function. Providing both this and `existingLambdaObj` causes an error. |
| openSearchDomainProps? |  [`opensearchservice.CfnDomainProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_opensearchservice.CfnDomainProps.html)  | Optional user provided props to override the default props for the OpenSearch Service. |
| openSearchDomainName |  `string`  | Domain name for the OpenSearch Service. |
| cognitoDomainName? |  `string`  | Optional Amazon Cognito domain name. If omitted the Amazon Cognito domain will default to the OpenSearch Service domain name. |
| createCloudWatchAlarms? |  `boolean`  | Whether to create the recommended CloudWatch alarms. |
| domainEndpointEnvironmentVariableName? |  `string`  | Optional name for the OpenSearch domain endpoint environment variable set for the Lambda function. Default is `DOMAIN_ENDPOINT`. |
| existingVpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An optional, existing VPC into which this pattern should be deployed. When deployed in a VPC, the Lambda function will use ENIs in the VPC to access network resources. If an existing VPC is provided, the `deployVpc` property cannot be `true`. This uses `ec2.IVpc` to allow clients to supply VPCs that exist outside the stack using the [`ec2.Vpc.fromLookup()`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html#static-fromwbrlookupscope-id-options) method. |
| vpcProps? |  [`ec2.VpcProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional user provided properties to override the default properties for the new VPC. `enableDnsHostnames`, `enableDnsSupport`, `natGateways` and `subnetConfiguration` are set by the pattern, so any values for those properties supplied here will be overridden. If `deployVpc` is not `true` then this property will be ignored. |
| deployVpc? |  `boolean`  | Whether to create a new VPC based on `vpcProps` into which to deploy this pattern. Setting this to true will deploy the minimal, most private VPC to run the pattern: |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| lambdaFunction |  [`lambda.Function`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda.Function.html)  | Returns an instance of `lambda.Function` created by the construct |
| userPool |  [`cognito.UserPool`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPool.html)  | Returns an instance of `cognito.UserPool` created by the construct |
| userPoolClient |  [`cognito.UserPoolClient`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.UserPoolClient.html)  | Returns an instance of `cognito.UserPoolClient` created by the construct |
| identityPool |  [`cognito.CfnIdentityPool`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cognito.CfnIdentityPool.html)  | Returns an instance of `cognito.CfnIdentityPool` created by the construct |
| openSearchDomain |  [`opensearchservice.CfnDomain`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_opensearchservice.CfnDomain.html)  | Returns an instance of `opensearch.CfnDomain` created by the construct |
| openSearchRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of `iam.Role` created by the construct for `opensearch.CfnDomain`  |
| cloudWatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of `cloudwatch.Alarm` created by the construct |
| vpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor. |

## Lambda Function
<a name="_lambda_function"></a>

This pattern requires a lambda function that can post data into the OpenSearch. A sample function is provided [here](https://github.com/awslabs/aws-solutions-constructs/blob/master/source/patterns/%40aws-solutions-constructs/aws-lambda-opensearch/test/lambda/index.js).

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any overrides will set the following defaults:

### AWS Lambda Function
<a name="_aws_lambda_function"></a>
+ Configure limited privilege access IAM role for Lambda function
+ Enable reusing connections with Keep-Alive for Node.js Lambda function
+ Enable X-Ray Tracing
+ Set Environment Variables
  + (default) DOMAIN\_ENDPOINT
  + AWS\_NODEJS\_CONNECTION\_REUSE\_ENABLED

### Amazon Cognito
<a name="_amazon_cognito"></a>
+ Set password policy for User Pools
+ Enforce the advanced security mode for User Pools

### Amazon OpenSearch Service
<a name="_amazon_opensearch_service"></a>
+ Deploy best practices CloudWatch Alarms for the OpenSearch Service domain
+ Secure the OpenSearch Service dashboard access with Cognito User Pools
+ Enable server-side encryption for OpenSearch Service domain using AWS managed KMS Key
+ Enable node-to-node encryption for the OpenSearch Service domain
+ Configure the cluster for the OpenSearch Service domain

## Architecture
<a name="_architecture"></a>

![Diagram showing the Lambda function, OpenSearch domain, Cognito domain, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-opensearch.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-lambda-opensearch) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
