---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteGateway.html
---

# DeleteGateway
<a name="API_DeleteGateway"></a>

Deletes a gateway. Before you can delete a gateway, deletion protection must be disabled and the gateway must not have any cluster associations that are in the `ACTIVE` or `DISASSOCIATING` state. If associations exist, the operation fails; disassociate all clusters first. `DeleteGateway` is a synchronous operation. After you delete a gateway, subsequent requests for it return a `GatewayNotFoundException`.

## Request Syntax
<a name="API_DeleteGateway_RequestSyntax"></a>

```
{
   "gateway": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [gateway](#API_DeleteGateway_RequestSyntax) **   <a name="ECS-DeleteGateway-request-gateway"></a>
The name or Amazon Resource Name (ARN) of the gateway to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteGateway_ResponseSyntax"></a>

```
{
   "gatewayArn": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayArn](#API_DeleteGateway_ResponseSyntax) **   <a name="ECS-DeleteGateway-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the deleted gateway.
Type: String

 ** [name](#API_DeleteGateway_ResponseSyntax) **   <a name="ECS-DeleteGateway-response-name"></a>
The name of the deleted gateway.
Type: String

 ** [status](#API_DeleteGateway_ResponseSyntax) **   <a name="ECS-DeleteGateway-response-status"></a>
The status of the gateway. After a successful delete, the status is `DELETED`.
Type: String
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETED`

## Errors
<a name="API_DeleteGateway_Errors"></a>

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
<a name="API_DeleteGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeleteGateway)
