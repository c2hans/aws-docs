---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AssociateGatewayWithCluster.html
---

# AssociateGatewayWithCluster
<a name="API_AssociateGatewayWithCluster"></a>

Associates a gateway with an Amazon ECS cluster. After a cluster is associated with a gateway, services in that cluster can use the gateway for ingress. No changes take effect until you update a service in the cluster to use the gateway. A single cluster can be associated with up to 5 gateways.

## Request Syntax
<a name="API_AssociateGatewayWithCluster_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "gateway": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateGatewayWithCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_AssociateGatewayWithCluster_RequestSyntax) **   <a name="ECS-AssociateGatewayWithCluster-request-cluster"></a>
The name or Amazon Resource Name (ARN) of the cluster to associate the gateway with.
Type: String
Required: Yes

 ** [gateway](#API_AssociateGatewayWithCluster_RequestSyntax) **   <a name="ECS-AssociateGatewayWithCluster-request-gateway"></a>
The name or Amazon Resource Name (ARN) of the gateway to associate.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateGatewayWithCluster_ResponseSyntax"></a>

```
{
   "clusterArn": "string",
   "gatewayArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_AssociateGatewayWithCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusterArn](#API_AssociateGatewayWithCluster_ResponseSyntax) **   <a name="ECS-AssociateGatewayWithCluster-response-clusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.
Type: String

 ** [gatewayArn](#API_AssociateGatewayWithCluster_ResponseSyntax) **   <a name="ECS-AssociateGatewayWithCluster-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String

 ** [status](#API_AssociateGatewayWithCluster_ResponseSyntax) **   <a name="ECS-AssociateGatewayWithCluster-response-status"></a>
The status of the association. A new association is `ACTIVE`.
Type: String
Valid Values: `ACTIVE | DISASSOCIATING | INACTIVE`

## Errors
<a name="API_AssociateGatewayWithCluster_Errors"></a>

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

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
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
<a name="API_AssociateGatewayWithCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/AssociateGatewayWithCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AssociateGatewayWithCluster)
