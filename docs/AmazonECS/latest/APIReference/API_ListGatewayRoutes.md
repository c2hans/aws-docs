---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListGatewayRoutes.html
---

# ListGatewayRoutes
<a name="API_ListGatewayRoutes"></a>

Returns a list of gateway routes. A gateway route represents the association between a service and a gateway and the service-specific infrastructure the gateway manages for it. You can filter the results by gateway, cluster, service, container port name, and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListGatewayRoutes_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "gateway": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "service": "{{string}}",
   "serviceContainerPortName": "{{string}}",
   "status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListGatewayRoutes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-cluster"></a>
The name or Amazon Resource Name (ARN) of a cluster to filter the results by.
Type: String
Required: No

 ** [gateway](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-gateway"></a>
The name or Amazon Resource Name (ARN) of a gateway to filter the results by.
Type: String
Required: No

 ** [maxResults](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-maxResults"></a>
The maximum number of results that the operation returns in a single page. The default is 100.
Type: Integer
Required: No

 ** [nextToken](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-nextToken"></a>
The `nextToken` value returned from a previous paginated request.
Type: String
Required: No

 ** [service](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-service"></a>
The name or Amazon Resource Name (ARN) of a service to filter the results by. Because services can span clusters, a service name isn't necessarily unique and can match multiple services.
Type: String
Required: No

 ** [serviceContainerPortName](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-serviceContainerPortName"></a>
The name of a task definition container port to filter the results by.
Type: String
Required: No

 ** [status](#API_ListGatewayRoutes_RequestSyntax) **   <a name="ECS-ListGatewayRoutes-request-status"></a>
The gateway route status to filter the results by.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 7 items.
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

## Response Syntax
<a name="API_ListGatewayRoutes_ResponseSyntax"></a>

```
{
   "gatewayRoutes": [
      {
         "clusterArn": "string",
         "gatewayArn": "string",
         "gatewayRouteArn": "string",
         "serviceArn": "string",
         "serviceContainerPortName": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGatewayRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayRoutes](#API_ListGatewayRoutes_ResponseSyntax) **   <a name="ECS-ListGatewayRoutes-response-gatewayRoutes"></a>
The gateway routes that match the request.
Type: Array of [GatewayRouteSummary](API_GatewayRouteSummary.md) objects

 ** [nextToken](#API_ListGatewayRoutes_ResponseSyntax) **   <a name="ECS-ListGatewayRoutes-response-nextToken"></a>
The `nextToken` value to include in a future request to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListGatewayRoutes_Errors"></a>

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
<a name="API_ListGatewayRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListGatewayRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListGatewayRoutes)
