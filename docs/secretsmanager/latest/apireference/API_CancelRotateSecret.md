---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CancelRotateSecret.html
---

# CancelRotateSecret
<a name="API_CancelRotateSecret"></a>

Turns off automatic rotation, and if a rotation is currently in progress, cancels the rotation.

If you cancel a rotation in progress, it can leave the `VersionStage` labels in an unexpected state. You might need to remove the staging label `AWSPENDING` from the partially created version. You also need to determine whether to roll back to the previous version of the secret by moving the staging label `AWSCURRENT` to the version that has `AWSPENDING`. To determine which version has a specific staging label, call [ListSecretVersionIds](API_ListSecretVersionIds.md). Then use [UpdateSecretVersionStage](API_UpdateSecretVersionStage.md) to change staging labels. For more information, see [How rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html).

To turn on automatic rotation again, call [RotateSecret](API_RotateSecret.md).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:CancelRotateSecret`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_CancelRotateSecret_RequestSyntax"></a>

```
{
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelRotateSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SecretId](#API_CancelRotateSecret_RequestSyntax) **   <a name="SecretsManager-CancelRotateSecret-request-SecretId"></a>
The ARN or name of the secret.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_CancelRotateSecret_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "Name": "string",
   "VersionId": "string"
}
```

## Response Elements
<a name="API_CancelRotateSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_CancelRotateSecret_ResponseSyntax) **   <a name="SecretsManager-CancelRotateSecret-response-ARN"></a>
The ARN of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Name](#API_CancelRotateSecret_ResponseSyntax) **   <a name="SecretsManager-CancelRotateSecret-response-Name"></a>
The name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [VersionId](#API_CancelRotateSecret_ResponseSyntax) **   <a name="SecretsManager-CancelRotateSecret-response-VersionId"></a>
The unique identifier of the version of the secret created during the rotation. This version might not be complete, and should be evaluated for possible deletion. We recommend that you remove the `VersionStage` value `AWSPENDING` from this version so that Secrets Manager can delete it. Failing to clean up a cancelled rotation can block you from starting future rotations.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.

## Errors
<a name="API_CancelRotateSecret_Errors"></a>

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
<a name="API_CancelRotateSecret_Examples"></a>

### Example
<a name="API_CancelRotateSecret_Example_1"></a>

The following example shows how to cancel rotation for a secret.

#### Sample Request
<a name="API_CancelRotateSecret_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.CancelRotateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret"
}
```

#### Sample Response
<a name="API_CancelRotateSecret_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name":"MyTestDatabaseSecret"
}
```

## See Also
<a name="API_CancelRotateSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/CancelRotateSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/CancelRotateSecret)
