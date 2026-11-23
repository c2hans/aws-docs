---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_RotateWebhookCredentials.html
---

# RotateWebhookCredentials

Sets a new credential on a webhook EventSource. If you supply Credential, EventBridge uses that value. Otherwise, EventBridge generates one. For HTTP Basic authentication, only the password changes. The username does not change. EventBridge never returns the credential. To read a generated value, call secretsmanager:GetSecretValue on the secret that SecretArn identifies.

You can rotate the credential of an EventSource in the ACTIVE, UPDATING, or UPDATE\_FAILED state. For a revoked EventSource or an EventSource in any other state, EventBridge returns InvalidStateException. EventBridge also returns InvalidStateException if the secret of the EventSource is scheduled for deletion or has been deleted.

If you rotate the credential of one EventSource too many times in 24 hours, EventBridge returns LimitExceededException. Retry later. The limit becomes available again automatically.

If AWS Secrets Manager throttles the call, EventBridge returns ThrottlingException. Retry later.

To use this operation, you must have the following permissions in your IAM policy:
+ secretsmanager:PutSecretValue on the secret of the EventSource
+ secretsmanager:GetSecretValue on the secret of the EventSource, for HTTP Basic authentication only
+ kms:GenerateDataKey and kms:Decrypt on the AWS Key Management Service (AWS KMS) key that encrypts the secret

The resource policy of the secret must not deny the secretsmanager actions.

EventBridge accepts the new credential when this call returns. In rare cases, the new credential takes up to 2 minutes to reach every EventBridge endpoint.

EventBridge also accepts the previous credential for 15 minutes after the rotation. The window ends at the CreatedDate of the AWSCURRENT secret version plus 15 minutes. Only the credential that the most recent rotation replaced stays valid. If you rotate again within 15 minutes, the older credential stops working immediately.

A retry with the same ClientToken within 8 hours returns the same result and does not rotate again. A retry of a rotation that supplied a value can arrive after a later rotation completed. In that case, the retried value becomes the current credential, and the credential it replaces does not stay valid.

## Request Parameters
<a name="API_RotateWebhookCredentials_RequestParameters"></a>

 ** ClientToken **
Unique, case-sensitive identifier that ensures the idempotency of the request. The SDK generates one automatically when the field is omitted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** Credential **
The new credential. Set the member that matches the authentication type of the EventSource:
+ BasicHttpPassword – For HTTP Basic authentication.
+ HmacSecretValue – For HMAC authentication.
+ StaticTokenSecretValue – For static token authentication.
If you set a member that does not match the authentication type, EventBridge returns InvalidInputException. If you omit Credential, EventBridge generates a value.
Type: [WebhookCredential](API_WebhookCredential.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** EventSourceArn **
The ARN of the webhook EventSource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-sourcev2\/webhook\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: Yes

## Response Elements
<a name="API_RotateWebhookCredentials_ResponseElements"></a>

The following element is returned by the service.

 ** SecretArn **
The ARN of the AWS Secrets Manager secret that holds the credential. It doesn't change when the credential is rotated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z0-9]+)*:secretsmanager:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):secret:events-webhook(-preprod)?[!/].+`

## Errors
<a name="API_RotateWebhookCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
HTTP Status Code: 403

 ** ConcurrentModificationException **
Another change to the resource is already in progress. Retry the request.
HTTP Status Code: 409

 ** IdempotentParameterMismatchException **
The request reuses the client token of an earlier request with different parameters. Use a new client token, or resend the earlier request unchanged.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an internal service error. Retry the request.
HTTP Status Code: 500

 ** InvalidInputException **
A request parameter is missing or not valid.
HTTP Status Code: 400

 ** InvalidStateException **
The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
HTTP Status Code: 409

 ** LimitExceededException **
The request would exceed a service quota for the account.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_RotateWebhookCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/RotateWebhookCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/RotateWebhookCredentials)
