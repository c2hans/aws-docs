---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListGatewayClusterAssociations.html
---

# ListGatewayClusterAssociations
<a name="API_ListGatewayClusterAssociations"></a>

Returns a list of the associations between gateways and clusters. You can filter the results by gateway, cluster, and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListGatewayClusterAssociations_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "gateway": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListGatewayClusterAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_ListGatewayClusterAssociations_RequestSyntax) **   <a name="ECS-ListGatewayClusterAssociations-request-cluster"></a>
The name or Amazon Resource Name (ARN) of a cluster to filter the results by.
Type: String
Required: No

 ** [gateway](#API_ListGatewayClusterAssociations_RequestSyntax) **   <a name="ECS-ListGatewayClusterAssociations-request-gateway"></a>
The name or Amazon Resource Name (ARN) of a gateway to filter the results by.
Type: String
Required: No

 ** [maxResults](#API_ListGatewayClusterAssociations_RequestSyntax) **   <a name="ECS-ListGatewayClusterAssociations-request-maxResults"></a>
The maximum number of results that the operation returns in a single page. The default is 100.
Type: Integer
Required: No

 ** [nextToken](#API_ListGatewayClusterAssociations_RequestSyntax) **   <a name="ECS-ListGatewayClusterAssociations-request-nextToken"></a>
The `nextToken` value returned from a previous paginated request.
Type: String
Required: No

 ** [status](#API_ListGatewayClusterAssociations_RequestSyntax) **   <a name="ECS-ListGatewayClusterAssociations-request-status"></a>
The association status to filter the results by.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `ACTIVE | DISASSOCIATING | INACTIVE`
Required: No

## Response Syntax
<a name="API_ListGatewayClusterAssociations_ResponseSyntax"></a>

```
{
   "gatewayClusterAssociations": [
      {
         "clusterArn": "string",
         "gatewayArn": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGatewayClusterAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayClusterAssociations](#API_ListGatewayClusterAssociations_ResponseSyntax) **   <a name="ECS-ListGatewayClusterAssociations-response-gatewayClusterAssociations"></a>
The gateway-cluster associations that match the request.
Type: Array of [GatewayClusterAssociationSummary](API_GatewayClusterAssociationSummary.md) objects

 ** [nextToken](#API_ListGatewayClusterAssociations_ResponseSyntax) **   <a name="ECS-ListGatewayClusterAssociations-response-nextToken"></a>
The `nextToken` value to include in a future request to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListGatewayClusterAssociations_Errors"></a>

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
<a name="API_ListGatewayClusterAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListGatewayClusterAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListGatewayClusterAssociations)
