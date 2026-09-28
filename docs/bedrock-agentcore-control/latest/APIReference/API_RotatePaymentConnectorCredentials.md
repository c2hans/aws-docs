---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_RotatePaymentConnectorCredentials.html
---

# RotatePaymentConnectorCredentials
<a name="API_RotatePaymentConnectorCredentials"></a>

Replaces the service-managed credentials of a payment connector with newly issued credentials.

Use this operation only for payment connectors with a `provisionMode` of `QUICK_CREATE`. For payment connectors with a `provisionMode` of `MANUAL`, call `UpdatePaymentCredentialProvider` instead after rotating credentials with the payment provider directly.

The rotation finishes before the response is returned, and only one rotation runs at a time for a given payment connector. When it succeeds, the new credential is in effect and the payment connector stays in the `READY` state. When it fails, an error is returned, the payment connector and its existing credential are left unchanged, and you can retry the request.

Rotation replaces the credential on the connector's credential provider, so every payment connector that uses that provider is affected. Replace any copy of the previous credential that you use outside AgentCore.

## Request Syntax
<a name="API_RotatePaymentConnectorCredentials_RequestSyntax"></a>

```
POST /payments/managers/{{paymentManagerId}}/connectors/{{paymentConnectorId}}/rotate-credentials HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "credentialsToRotate": { ... }
}
```

## URI Request Parameters
<a name="API_RotatePaymentConnectorCredentials_RequestParameters"></a>

The request uses the following URI parameters.

 ** [paymentConnectorId](#API_RotatePaymentConnectorCredentials_RequestSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-request-uri-paymentConnectorId"></a>
The unique identifier of the payment connector whose credentials you want to rotate.
Length Constraints: Minimum length of 12. Maximum length of 211.
Pattern: `([0-9a-z_][-]?){1,100}-[0-9a-z]{10}`
Required: Yes

 ** [paymentManagerId](#API_RotatePaymentConnectorCredentials_RequestSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-request-uri-paymentManagerId"></a>
The unique identifier of the parent payment manager.
Length Constraints: Minimum length of 12. Maximum length of 211.
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`
Required: Yes

## Request Body
<a name="API_RotatePaymentConnectorCredentials_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_RotatePaymentConnectorCredentials_RequestSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [credentialsToRotate](#API_RotatePaymentConnectorCredentials_RequestSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-request-credentialsToRotate"></a>
The credentials to rotate. Specify the member that matches the payment connector's `type`. Each credential that you select is rotated independently.
Type: [CredentialRotationConfig](API_CredentialRotationConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_RotatePaymentConnectorCredentials_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "lastUpdatedAt": "string",
   "paymentConnectorId": "string",
   "paymentManagerId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_RotatePaymentConnectorCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedAt](#API_RotatePaymentConnectorCredentials_ResponseSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-response-lastUpdatedAt"></a>
The timestamp when the payment connector was last updated, which is when the rotation completed.
Type: Timestamp

 ** [paymentConnectorId](#API_RotatePaymentConnectorCredentials_ResponseSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-response-paymentConnectorId"></a>
The unique identifier of the payment connector.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 211.
Pattern: `([0-9a-z_][-]?){1,100}-[0-9a-z]{10}`

 ** [paymentManagerId](#API_RotatePaymentConnectorCredentials_ResponseSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-response-paymentManagerId"></a>
The unique identifier of the parent payment manager.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 211.
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

 ** [status](#API_RotatePaymentConnectorCredentials_ResponseSyntax) **   <a name="bedrockagentcorecontrol-RotatePaymentConnectorCredentials-response-status"></a>
The current status of the payment connector, which is `READY` after a successful rotation.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | READY | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED | AWS_MARKETPLACE_SUBSCRIPTION_REQUIRED | PENDING_AUTHENTICATION | PROVISIONING | AUTHENTICATION_EXPIRED | AUTHENTICATION_FAILED`

## Errors
<a name="API_RotatePaymentConnectorCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This exception is thrown when a request is denied per access permissions
HTTP Status Code: 403

 ** ConflictException **
This exception is thrown when there is a conflict performing an operation
HTTP Status Code: 409

 ** InternalServerException **
This exception is thrown if there was an unexpected error during processing of request
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception is thrown when a resource referenced by the operation does not exist
HTTP Status Code: 404

 ** ThrottlingException **
This exception is thrown when the number of requests exceeds the limit
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_RotatePaymentConnectorCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)
