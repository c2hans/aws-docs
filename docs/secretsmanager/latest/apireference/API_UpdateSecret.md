---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html
---

# UpdateSecret
<a name="API_UpdateSecret"></a>

Modifies the details of a secret, including metadata and the secret value. To change the secret value, you can also use [PutSecretValue](API_PutSecretValue.md).

To change the rotation configuration of a secret, use [RotateSecret](API_RotateSecret.md) instead.

To change a secret so that it is managed by another service, you need to recreate the secret in that service. See [Secrets Manager secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).

We recommend you avoid calling `UpdateSecret` at a sustained rate of more than once every 10 minutes. When you call `UpdateSecret` to update the secret value, Secrets Manager creates a new version of the secret. Secrets Manager removes outdated versions when there are more than 100, but it does not remove versions created less than 24 hours ago. If you update the secret value more than once every 10 minutes, you create more versions than Secrets Manager removes, and you will reach the quota for secret versions.

If you include `SecretString` or `SecretBinary` to create a new secret version, Secrets Manager automatically moves the staging label `AWSCURRENT` to the new version. Then it attaches the label `AWSPREVIOUS` to the version that `AWSCURRENT` was removed from.

If you call this operation with a `ClientRequestToken` that matches an existing version's `VersionId`, the operation results in an error. You can't modify an existing version, you can only create a new version. To remove a version, remove all staging labels from it. See [UpdateSecretVersionStage](API_UpdateSecretVersionStage.md).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters except `SecretBinary` or `SecretString` because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:UpdateSecret`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html). If you use a customer managed key, you must also have `kms:GenerateDataKey`, `kms:Encrypt`, and `kms:Decrypt` permissions on the key. If you change the KMS key and you don't have `kms:Encrypt` permission to the new key, Secrets Manager does not re-encrypt existing secret versions with the new key. For more information, see [ Secret encryption and decryption](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).

**Important**
When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to [Mitigate the risks of using command-line tools to store AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html).

## Request Syntax
<a name="API_UpdateSecret_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "KmsKeyId": "{{string}}",
   "SecretBinary": {{blob}},
   "SecretId": "{{string}}",
   "SecretString": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-ClientRequestToken"></a>
If you include `SecretString` or `SecretBinary`, then Secrets Manager creates a new version for the secret, and this parameter specifies the unique identifier for the new version.
If you use the AWS CLI or one of the AWS SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request.
If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a `ClientRequestToken` and include it in the request.
This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value to ensure uniqueness of your versions within the specified secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** [Description](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-Description"></a>
The description of the secret.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [KmsKeyId](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-KmsKeyId"></a>
The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt new secret versions as well as any existing versions with the staging labels `AWSCURRENT`, `AWSPENDING`, or `AWSPREVIOUS`. If you don't have `kms:Encrypt` permission to the new key, Secrets Manager does not re-encrypt existing secret versions with the new key. For more information about versions and staging labels, see [Concepts: Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version).
A key alias is always prefixed by `alias/`, for example `alias/aws/secretsmanager`. For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).
If you set this to an empty string, Secrets Manager uses the AWS managed key `aws/secretsmanager`. If this key doesn't already exist in your account, then Secrets Manager creates it for you automatically. All users and roles in the AWS account automatically have access to use `aws/secretsmanager`. Creating `aws/secretsmanager` can result in a one-time significant delay in returning the result.
You can only use the AWS managed key `aws/secretsmanager` if you call this operation using credentials from the same AWS account that owns the secret. If the secret is in a different account, then you must use a customer managed key and provide the ARN of that KMS key in this field. The user making the call must have permissions to both the secret and the KMS key in their respective accounts.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [SecretBinary](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-SecretBinary"></a>
The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter.
Either `SecretBinary` or `SecretString` must have a value, but not both.
You can't access this parameter in the Secrets Manager console.
Sensitive: This field contains sensitive information, so the service does not include it in AWS CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** [SecretId](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-SecretId"></a>
The ARN or name of the secret.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [SecretString](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-SecretString"></a>
The text data to encrypt and store in the new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value.
Either `SecretBinary` or `SecretString` must have a value, but not both.
Sensitive: This field contains sensitive information, so the service does not include it in AWS CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** [Type](#API_UpdateSecret_RequestSyntax) **   <a name="SecretsManager-UpdateSecret-request-Type"></a>
The exact string that identifies the third-party partner that holds the external secret. For more information, see [Managed external secret partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateSecret_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "Name": "string",
   "VersionId": "string"
}
```

## Response Elements
<a name="API_UpdateSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_UpdateSecret_ResponseSyntax) **   <a name="SecretsManager-UpdateSecret-response-ARN"></a>
The ARN of the secret that was updated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Name](#API_UpdateSecret_ResponseSyntax) **   <a name="SecretsManager-UpdateSecret-response-Name"></a>
The name of the secret that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [VersionId](#API_UpdateSecret_ResponseSyntax) **   <a name="SecretsManager-UpdateSecret-response-VersionId"></a>
If Secrets Manager created a new version of the secret during this operation, then `VersionId` contains the unique identifier of the new version.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.

## Errors
<a name="API_UpdateSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** DecryptionFailure **
Secrets Manager can't decrypt the protected secret text using the provided KMS key.
HTTP Status Code: 400

 ** EncryptionFailure **
Secrets Manager can't encrypt the protected secret text using the provided KMS key. Check that the KMS key is available, enabled, and not in an invalid state. For more information, see [Key state: Effect on your KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html).
HTTP Status Code: 400

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

 ** LimitExceededException **
The request failed because it would exceed one of the Secrets Manager quotas.
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **
The resource policy has syntax errors.
HTTP Status Code: 400

 ** PreconditionNotMetException **
The request failed because you did not complete all the prerequisite steps.
HTTP Status Code: 400

 ** ResourceExistsException **
A resource with the ID you requested already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_UpdateSecret_Examples"></a>

### Example
<a name="API_UpdateSecret_Example_1"></a>

The following example shows how to change the description of a secret. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_UpdateSecret_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.UpdateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "Description": "This is a new description for the secret.",
  "ClientRequestToken": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateSecret_Example_1_Response"></a>

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

### Example
<a name="API_UpdateSecret_Example_2"></a>

This example shows how to update the KMS key that Secrets Manager uses to encrypt the secret value. The KMS key must be in the same Region as the secret. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_UpdateSecret_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.UpdateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateSecret_Example_2_Response"></a>

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

### Example
<a name="API_UpdateSecret_Example_3"></a>

The following example shows how to create a new version of the secret by updating the `SecretString` field. The `ClientRequestToken` parameter becomes the `VersionId` of the new version. Alternatively, you can use the [PutSecretValue](API_PutSecretValue.md) operation. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_UpdateSecret_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.UpdateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "SecretString": "{<JSON STRING WITH CREDENTIALS>}",
  "ClientRequestToken": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

#### Sample Response
<a name="API_UpdateSecret_Example_3_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name":"MyTestDatabaseSecret",
  "VersionId":"EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

## See Also
<a name="API_UpdateSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/UpdateSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/UpdateSecret)
