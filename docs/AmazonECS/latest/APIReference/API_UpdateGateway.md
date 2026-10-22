---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateGateway.html
---

# UpdateGateway
<a name="API_UpdateGateway"></a>

Modifies the configuration of a gateway. You can change only the properties that can be applied without interrupting traffic, and the configuration variant that you provide must match the gateway's type. `UpdateGateway` is an asynchronous operation: the changes are applied to each load balancer the gateway manages, and the gateway reports a status of `UPDATE_IN_PROGRESS` until the update completes. If Amazon ECS can't update one or more resources, it makes a best effort to update the rest and the gateway status changes to `UPDATE_FAILED`. Use `DescribeGateway` to inspect the gateway's `statusReason` and failures list, which gives the ARN of each load balancer that was not updated and the operation, error code, and message for each failure.

If you specify `infrastructureRoleArn`, you must have the `iam:PassRole` permission for that role.

## Request Syntax
<a name="API_UpdateGateway_RequestSyntax"></a>

```
{
   "configuration": { ... },
   "deletionProtection": {{boolean}},
   "gateway": "{{string}}",
   "infrastructureRoleArn": "{{string}}",
   "propagateTags": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateGateway_RequestSyntax) **   <a name="ECS-UpdateGateway-request-configuration"></a>
The updated type-specific configuration for the gateway. The configuration variant must match the gateway's existing type, and only mutable fields can be changed.
Type: [UpdateGatewayConfiguration](API_UpdateGatewayConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [deletionProtection](#API_UpdateGateway_RequestSyntax) **   <a name="ECS-UpdateGateway-request-deletionProtection"></a>
Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted.
Type: Boolean
Required: No

 ** [gateway](#API_UpdateGateway_RequestSyntax) **   <a name="ECS-UpdateGateway-request-gateway"></a>
The name or Amazon Resource Name (ARN) of the gateway to update.
Type: String
Required: Yes

 ** [infrastructureRoleArn](#API_UpdateGateway_RequestSyntax) **   <a name="ECS-UpdateGateway-request-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to manage infrastructure on your behalf.
Type: String
Required: No

 ** [propagateTags](#API_UpdateGateway_RequestSyntax) **   <a name="ECS-UpdateGateway-request-propagateTags"></a>
Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. If you don't specify a value, the gateway's existing setting is unchanged.
Type: String
Valid Values: `NONE | GATEWAY`
Required: No

## Response Syntax
<a name="API_UpdateGateway_ResponseSyntax"></a>

```
{
   "gatewayArn": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayArn](#API_UpdateGateway_ResponseSyntax) **   <a name="ECS-UpdateGateway-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String

 ** [name](#API_UpdateGateway_ResponseSyntax) **   <a name="ECS-UpdateGateway-response-name"></a>
The name of the gateway.
Type: String

 ** [status](#API_UpdateGateway_ResponseSyntax) **   <a name="ECS-UpdateGateway-response-status"></a>
The status of the gateway. After a successful update request, the status is `UPDATE_IN_PROGRESS`.
Type: String
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETED`

## Errors
<a name="API_UpdateGateway_Errors"></a>

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
<a name="API_UpdateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateGateway)
