---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_apigateway_sagemakerendpoint.html
---

# aws-apigateway-sagemakerendpoint
<a name="aws_apigateway_sagemakerendpoint"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_apigateway_sagemakerendpoint`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-apigateway-sagemakerendpoint`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.apigatewaysagemakerendpoint`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon API Gateway connected to an Amazon SageMaker endpoint pattern.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { ApiGatewayToSageMakerEndpoint, ApiGatewayToSageMakerEndpointProps } from '@aws-solutions-constructs/aws-apigateway-sagemakerendpoint';

// Below is an example VTL (Velocity Template Language) mapping template for mapping the Api GET request to the Sagemaker POST request
const requestTemplate = `
{
    "instances": [
        # set( $user_id = $input.params("user_id") )
        # set( $items = $input.params("items") )
        # foreach( $item in $items.split(",") )
        # if( $foreach.hasNext ),#end
        {"in0": [$user_id], "in1": [$item]}
            $esc.newline
        # end
    ]
}`

// Replace 'my-endpoint' with your Sagemaker Inference Endpoint
new ApiGatewayToSageMakerEndpoint(this, 'test-apigw-sagemakerendpoint', {
  endpointName: 'my-endpoint',
  resourcePath: '{user_id}',
  requestMappingTemplate: requestTemplate
});
```

```
from aws_solutions_constructs.aws_apigateway_sagemakerendpoint import ApiGatewayToSageMakerEndpoint
from aws_cdk import Stack
from constructs import Construct

# Below is an example VTL (Velocity Template Language) mapping template for mapping the Api GET request to the Sagemaker POST request
request_template = """
{
    "instances": [
        # set( $user_id = $input.params("user_id") )
        # set( $items = $input.params("items") )
        # foreach( $item in $items.split(",") )
        # if( $foreach.hasNext ),#end
        {"in0": [$user_id], "in1": [$item]}
            $esc.newline
        # end
    ]
}"""

# Replace 'my-endpoint' with your Sagemaker Inference Endpoint
ApiGatewayToSageMakerEndpoint(self, 'test-apigw-sagemakerendpoint',
                                endpoint_name='my-endpoint',
                                resource_path='{user_id}',
                                request_mapping_template=request_template
                                )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.apigatewaysagemakerendpoint.*;

// Create an example VTL (Velocity Template Language) mapping template for mapping the Api GET request to the Sagemaker POST request
final String requestTemplate = "{"
        + "\"instances\": ["
        + "# set( $user_id = $input.params(\"user_id\") )"
        + "# set( $items = $input.params(\"items\") )"
        + "# foreach( $item in $items.split(\",\") )"
        + "# if( $foreach.hasNext ),#end"
        + "{\"in0\": [$user_id], \"in1\": [$item]}"
        + "    $esc.newline"
        + "# end"
        + "]"
        + "}";

// Replace ""my-endpoint"" with your Sagemaker Inference Endpoint
new ApiGatewayToSageMakerEndpoint(this, "ApiGatewayToSageMakerEndpointPattern",
        new ApiGatewayToSageMakerEndpointProps.Builder()
                .endpointName("my-endpoint")
                .resourcePath("{user_id}")
                .requestMappingTemplate(requestTemplate)
                .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| apiGatewayProps? |  [`api.RestApiProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApiProps.html)  | Optional - user provided props to override the default props for the API Gateway. |
| createUsagePlan? | boolean | Whether to create a Usage Plan attached to the API. Must be true if apiGatewayProps.defaultMethodOptions.apiKeyRequired is true. @default - true (to match legacy behavior) |
| apiGatewayExecutionRole? |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | IAM Role used by API Gateway to invoke the SageMaker endpoint. If not specified, a default role is created with access to `endpointName`. |
| endpointName |  `string`  | Name of the deployed SageMaker inference endpoint. |
| resourceName? |  `string`  | Optional resource name where the GET method will be available. |
| resourcePath |  `string`  | Resource path for the GET method. The variable defined here can be referenced in `requestMappingTemplate`. |
| requestMappingTemplate |  `string`  | Mapping template to convert GET requests for the default `application/json` content-type received on the REST API to POST requests expected by the SageMaker endpoint. |
| additionalRequestTemplates |  `{ [contentType: string]: string; }`  | Optional Request Templates for content-types other than `application/json`. Use the `requestMappingTemplate` property to set the request template for the `application/json` content-type. |
| responseMappingTemplate? |  `string`  | Optional mapping template to convert responses received from the SageMaker endpoint. |
| logGroupProps? |  [`logs.LogGroupProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)  | User provided props to override the default props for for the CloudWatchLogs LogGroup. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| apiGateway |  [`api.RestApi`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway.RestApi.html)  | Returns an instance of the API Gateway REST API created by the pattern. |
| apiGatewayRole |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway. |
| apiGatewayCloudWatchRole? |  [`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)  | Returns an instance of the iam.Role created by the construct for API Gateway for CloudWatch access. |
| apiGatewayLogGroup |  [`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)  | Returns an instance of the LogGroup created by the construct for API Gateway access logging to CloudWatch. |

## Sample API Usage
<a name="_sample_api_usage"></a>

 **Note**: Each SageMaker endpoint is unique, and the response from the API will depend on the deployed model. The example given below assumes the sample from [this blog post](https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker/). For a reference on how that’d be implemented, please refer to [integ.apigateway-sagemakerendpoint-overwrite.ts](test/integ.apigateway-sagemakerendpoint-overwrite.ts).

|  **Method**  |  **Request Path**  |  **Query String**  |  **SageMaker Action**  |  **Description**  |
| --- | --- | --- | --- | --- |
| GET |  `/321`  |  `items=101,131,162`  |  `sagemaker:InvokeEndpoint`  | Retrieves the predictions for a specific user and items. |

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
+ Validate request parameters before passing data to SageMaker

## Architecture
<a name="_architecture"></a>

![Diagram showing Amazon CloudWatch, API Gateway, SageMaker AI endpoint, and IAM roles connections.](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-apigateway-sagemakerendpoint.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-apigateway-sagemakerendpoint) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
