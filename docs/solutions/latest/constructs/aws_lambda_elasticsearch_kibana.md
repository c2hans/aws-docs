---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_elasticsearch_kibana.html
---

# aws-lambda-elasticsearch-kibana
<a name="aws_lambda_elasticsearch_kibana"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_lambda_elasticsearch_kibana`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-lambda-elasticsearch-kibana`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.lambdaelasticsearchkibana`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS Lambda function and Amazon Elasticsearch Service with the least privileged permissions.

 **Some cluster configurations (e.g VPC access) require the existence of the `AWSServiceRoleForAmazonElasticsearchService` Service-Linked Role in your account.**

 **You will need to create the service-linked role using the AWS CLI once in any account using this construct (it may have already been run to support other stacks):**

```
aws iam create-service-linked-role --aws-service-name es.amazonaws.com
```

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps, Aws } from 'aws-cdk-lib';
import { LambdaToElasticSearchAndKibana } from '@aws-solutions-constructs/aws-lambda-elasticsearch-kibana';
import * as lambda from "aws-cdk-lib/aws-lambda";

const lambdaProps: lambda.FunctionProps = {
  code: lambda.Code.fromAsset(`lambda`),
  runtime: lambda.Runtime.NODEJS_22_X,
  handler: 'index.handler'
};

new LambdaToElasticSearchAndKibana(this, 'sample', {
  lambdaFunctionProps: lambdaProps,
  domainName: 'testdomain',
  // NOTE: Ensure the Cognito domain name is globally unique
  cognitoDomainName: 'globallyuniquedomain' + Aws.ACCOUNT_ID
});
```

```
from aws_solutions_constructs.aws_lambda_elasticsearch_kibana import LambdaToElasticSearchAndKibana
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

LambdaToElasticSearchAndKibana(self, 'sample',
                            lambda_function_props=lambda_props,
                            domain_name='testdomain',
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
import software.amazon.awsconstructs.services.lambdaelasticsearchkibana.*;

new LambdaToElasticSearchAndKibana(this, "sample",
        new LambdaToElasticSearchAndKibanaProps.Builder()
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.NODEJS_22_X)
                        .code(Code.fromAsset("lambda"))
                        .handler("index.handler")
                        .build())
                .domainName("testdomain")
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
| esDomainProps? |  [`elasticsearch.CfnDomainProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticsearch.CfnDomainProps.html)  | Optional user provided props to override the default props for the Elasticsearch Service |
| domainName |  `string`  | Domain name for the Cognito and the Elasticsearch Service |
| cognitoDomainName? |  `string`  | Optional Cognito Domain Name, if provided it will be used for Cognito Domain, and domainName will be used for the Elasticsearch Domain |
| createCloudWatchAlarms? |  `boolean`  | Whether to create recommended CloudWatch alarms |
| domainEndpointEnvironmentVariableName? |  `string`  | Optional Name for the ElasticSearch domain endpoint environment variable set for the Lambda function. |
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
| elasticsearchDomain |  [`elasticsearch.CfnDomain`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticsearch.CfnDomain.html)  | Returns an instance of `elasticsearch.CfnDomain` created by the construct |
| elasticsearchRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of `iam.Role` created by the construct for `elasticsearch.CfnDomain`  |
| cloudwatchAlarms? |  [`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudwatch.Alarm.html)  | Returns a list of `cloudwatch.Alarm` created by the construct |
| vpc? |  [`ec2.IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | Returns an interface on the VPC used by the pattern (if any). This may be a VPC created by the pattern or the VPC supplied to the pattern constructor. |

## Lambda Function
<a name="_lambda_function"></a>

This pattern requires a lambda function that can post data into the Elasticsearch. A sample function is provided [here](https://github.com/awslabs/aws-solutions-constructs/blob/master/source/patterns/%40aws-solutions-constructs/aws-lambda-elasticsearch-kibana/test/lambda/index.js).

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

### Amazon Elasticsearch Service
<a name="_amazon_elasticsearch_service"></a>
+ Deploy best practices CloudWatch Alarms for the Elasticsearch Service domain
+ Secure the Kibana dashboard access with Cognito User Pools
+ Enable server-side encryption for the Elasticsearch Service domain using AWS managed KMS Key
+ Enable node-to-node encryption for the Elasticsearch Service domain
+ Configure the cluster for the Elasticsearch Service domain

## Architecture
<a name="_architecture"></a>

![Diagram showing the Lambda function, Elasticsearch domain, Cognito domain, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-lambda-elasticsearch-kibana.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-lambda-elasticsearch-kibana) for this pattern to view the code, read/create issues and pull requests and more.
