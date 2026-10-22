---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateGateway.html
---

# CreateGateway
<a name="API_CreateGateway"></a>

Creates a gateway. A gateway defines and dynamically manages ingress paths for your Amazon ECS services, handling traffic routing and infrastructure across multiple services while optimizing infrastructure usage. `CreateGateway` is a synchronous operation and the gateway is returned with a status of `ACTIVE`. The load balancers and other infrastructure that a gateway manages aren't created until a service in an associated cluster begins using the gateway.

To use this operation, you must have the `iam:PassRole` permission for the infrastructure role that you specify in `infrastructureRoleArn`.

## Request Syntax
<a name="API_CreateGateway_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "deletionProtection": {{boolean}},
   "infrastructureRoleArn": "{{string}}",
   "name": "{{string}}",
   "propagateTags": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
Type: String
Required: No

 ** [configuration](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-configuration"></a>
The type-specific configuration for the gateway. Exactly one configuration variant must be set, and it determines the gateway type. For example, `hostSharedAlb` configures a gateway that uses Application Load Balancers with host-based routing.
Type: [GatewayConfiguration](API_GatewayConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [deletionProtection](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-deletionProtection"></a>
Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted, and the gateway propagates this setting to the load balancers it manages. The default is `true`.
Type: Boolean
Required: No

 ** [infrastructureRoleArn](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-infrastructureRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to create and manage infrastructure on your behalf.
Type: String
Required: Yes

 ** [name](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-name"></a>
The name for the gateway. The name must be unique within your account and can be up to 255 characters.
Type: String
Required: Yes

 ** [propagateTags](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-propagateTags"></a>
Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. The default is `GATEWAY`.
Type: String
Valid Values: `NONE | GATEWAY`
Required: No

 ** [tags](#API_CreateGateway_RequestSyntax) **   <a name="ECS-CreateGateway-request-tags"></a>
The metadata that you apply to the gateway to help you categorize and organize it. Each tag consists of a key and an optional value. Depending on `propagateTags`, these tags can be applied to the infrastructure the gateway manages.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateGateway_ResponseSyntax"></a>

```
{
   "gatewayArn": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayArn](#API_CreateGateway_ResponseSyntax) **   <a name="ECS-CreateGateway-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String

 ** [name](#API_CreateGateway_ResponseSyntax) **   <a name="ECS-CreateGateway-response-name"></a>
The name of the gateway.
Type: String

 ** [status](#API_CreateGateway_ResponseSyntax) **   <a name="ECS-CreateGateway-response-status"></a>
The status of the gateway. A newly created gateway is always `ACTIVE`.
Type: String
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETED`

## Errors
<a name="API_CreateGateway_Errors"></a>

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
<a name="API_CreateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreateGateway)
