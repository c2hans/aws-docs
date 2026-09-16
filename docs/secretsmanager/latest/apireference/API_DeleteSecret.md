---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html
---

# DeleteSecret
<a name="API_DeleteSecret"></a>

Deletes a secret and all of its versions. You can specify a recovery window during which you can restore the secret. The minimum recovery window is 7 days. The default recovery window is 30 days. Secrets Manager attaches a `DeletionDate` stamp to the secret that specifies the end of the recovery window. At the end of the recovery window, Secrets Manager deletes the secret permanently.

You can't delete a primary secret that is replicated to other Regions. You must first delete the replicas using [RemoveRegionsFromReplication](API_RemoveRegionsFromReplication.md), and then delete the primary secret. When you delete a replica, it is deleted immediately.

You can't directly delete a version of a secret. Instead, you remove all staging labels from the version using [UpdateSecretVersionStage](API_UpdateSecretVersionStage.md). This marks the version as deprecated, and then Secrets Manager can automatically delete the version in the background.

To determine whether an application still uses a secret, you can create an Amazon CloudWatch alarm to alert you to any attempts to access a secret during the recovery window. For more information, see [ Monitor secrets scheduled for deletion](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring_cloudwatch_deleted-secrets.html).

Secrets Manager performs the permanent secret deletion at the end of the waiting period as a background task with low priority. There is no guarantee of a specific time after the recovery window for the permanent delete to occur.

At any time before recovery window ends, you can use [RestoreSecret](API_RestoreSecret.md) to remove the `DeletionDate` and cancel the deletion of the secret.

When a secret is scheduled for deletion, you cannot retrieve the secret value. You must first cancel the deletion with [RestoreSecret](API_RestoreSecret.md) and then you can retrieve the secret.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:DeleteSecret`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_DeleteSecret_RequestSyntax"></a>

```
{
   "ForceDeleteWithoutRecovery": {{boolean}},
   "RecoveryWindowInDays": {{number}},
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ForceDeleteWithoutRecovery](#API_DeleteSecret_RequestSyntax) **   <a name="SecretsManager-DeleteSecret-request-ForceDeleteWithoutRecovery"></a>
Specifies whether to delete the secret without any recovery window. You can't use both this parameter and `RecoveryWindowInDays` in the same call. If you don't use either, then by default Secrets Manager uses a 30 day recovery window.
Secrets Manager performs the actual deletion with an asynchronous background process, so there might be a short delay before the secret is permanently deleted. If you delete a secret and then immediately create a secret with the same name, use appropriate back off and retry logic.
If you forcibly delete an already deleted or nonexistent secret, the operation does not return `ResourceNotFoundException`.
Use this parameter with caution. This parameter causes the operation to skip the normal recovery window before the permanent deletion that Secrets Manager would normally impose with the `RecoveryWindowInDays` parameter. If you delete a secret with the `ForceDeleteWithoutRecovery` parameter, then you have no opportunity to recover the secret. You lose the secret permanently.
Type: Boolean
Required: No

 ** [RecoveryWindowInDays](#API_DeleteSecret_RequestSyntax) **   <a name="SecretsManager-DeleteSecret-request-RecoveryWindowInDays"></a>
The number of days from 7 to 30 that Secrets Manager waits before permanently deleting the secret. You can't use both this parameter and `ForceDeleteWithoutRecovery` in the same call. If you don't use either, then by default Secrets Manager uses a 30 day recovery window.
Type: Long
Required: No

 ** [SecretId](#API_DeleteSecret_RequestSyntax) **   <a name="SecretsManager-DeleteSecret-request-SecretId"></a>
The ARN or name of the secret to delete.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_DeleteSecret_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "DeletionDate": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_DeleteSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_DeleteSecret_ResponseSyntax) **   <a name="SecretsManager-DeleteSecret-response-ARN"></a>
The ARN of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [DeletionDate](#API_DeleteSecret_ResponseSyntax) **   <a name="SecretsManager-DeleteSecret-response-DeletionDate"></a>
The date and time after which this secret Secrets Manager can permanently delete this secret, and it can no longer be restored. This value is the date and time of the delete request plus the number of days in `RecoveryWindowInDays`.
Type: Timestamp

 ** [Name](#API_DeleteSecret_ResponseSyntax) **   <a name="SecretsManager-DeleteSecret-response-Name"></a>
The name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_DeleteSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidParameterException **
The parameter name or value is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
A parameter value is not valid for the current state of the resource.
Possible causes:
+ The secret is scheduled for deletion.
+ You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
+ The secret is managed by another service, and you must use that service to update it. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_DeleteSecret_Examples"></a>

### Example
<a name="API_DeleteSecret_Example_1"></a>

The following example shows how to delete a secret with a recovery window of 7 days. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_DeleteSecret_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.DeleteSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "RecoveryWindowInDays": 7
}
```

#### Sample Response
<a name="API_DeleteSecret_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "DeletionDate":1.524085349095E9,
  "Name":"MyTestDatabaseSecret"
}
```

## See Also
<a name="API_DeleteSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/DeleteSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/DeleteSecret)
