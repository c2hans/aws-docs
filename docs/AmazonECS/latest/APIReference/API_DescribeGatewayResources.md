---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeGatewayResources.html
---

# DescribeGatewayResources
<a name="API_DescribeGatewayResources"></a>

Returns the infrastructure that a gateway has created and manages, so that you can follow the traffic path from top-level shared resources, such as load balancers, to the service-specific resources represented as gateway routes. Responses include only the Amazon Resource Names (ARNs) of gateway-managed infrastructure. For the current state of a resource, describe it with the corresponding AWS service (Elastic Load Balancing, Amazon EC2, or AWS Certificate Manager). The results are paginated.

## Request Syntax
<a name="API_DescribeGatewayResources_RequestSyntax"></a>

```
{
   "gateway": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGatewayResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [gateway](#API_DescribeGatewayResources_RequestSyntax) **   <a name="ECS-DescribeGatewayResources-request-gateway"></a>
The name or Amazon Resource Name (ARN) of the gateway.
Type: String
Required: Yes

 ** [maxResults](#API_DescribeGatewayResources_RequestSyntax) **   <a name="ECS-DescribeGatewayResources-request-maxResults"></a>
The maximum number of results that the operation returns in a single page. The maximum value is 20 and the default is 10.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeGatewayResources_RequestSyntax) **   <a name="ECS-DescribeGatewayResources-request-nextToken"></a>
The `nextToken` value returned from a previous paginated request.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeGatewayResources_ResponseSyntax"></a>

```
{
   "gatewayResources": {
      "gatewayArn": "string",
      "resources": { ... }
   },
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeGatewayResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayResources](#API_DescribeGatewayResources_ResponseSyntax) **   <a name="ECS-DescribeGatewayResources-response-gatewayResources"></a>
The infrastructure resources that the gateway manages, grouped by gateway type.
Type: [GatewayResources](API_GatewayResources.md) object

 ** [nextToken](#API_DescribeGatewayResources_ResponseSyntax) **   <a name="ECS-DescribeGatewayResources-response-nextToken"></a>
The `nextToken` value to include in a future request to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeGatewayResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** GatewayNotFoundException **
The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeGatewayResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeGatewayResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeGatewayResources)
