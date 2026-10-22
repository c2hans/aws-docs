---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeGatewayRoute.html
---

# DescribeGatewayRoute
<a name="API_DescribeGatewayRoute"></a>

Describes a gateway route, including its status, the service it routes traffic to, and the service-specific infrastructure, such as target groups and listener rules, that the gateway manages for it.

## Request Syntax
<a name="API_DescribeGatewayRoute_RequestSyntax"></a>

```
{
   "gatewayRouteArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGatewayRoute_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [gatewayRouteArn](#API_DescribeGatewayRoute_RequestSyntax) **   <a name="ECS-DescribeGatewayRoute-request-gatewayRouteArn"></a>
The Amazon Resource Name (ARN) of the gateway route to describe.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeGatewayRoute_ResponseSyntax"></a>

```
{
   "gatewayRoute": {
      "gatewayRouteArn": "string",
      "resources": { ... },
      "serviceArn": "string",
      "serviceContainerPortName": "string",
      "serviceUrl": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeGatewayRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayRoute](#API_DescribeGatewayRoute_ResponseSyntax) **   <a name="ECS-DescribeGatewayRoute-response-gatewayRoute"></a>
The details of the gateway route.
Type: [GatewayRoute](API_GatewayRoute.md) object

## Errors
<a name="API_DescribeGatewayRoute_Errors"></a>

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

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource wasn't found.
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
<a name="API_DescribeGatewayRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeGatewayRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeGatewayRoute)
