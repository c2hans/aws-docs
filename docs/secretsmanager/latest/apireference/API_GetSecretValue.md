---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
---

# GetSecretValue
<a name="API_GetSecretValue"></a>

Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary` from the specified version of a secret, whichever contains content.

To retrieve the values for a group of secrets, call [BatchGetSecretValue](API_BatchGetSecretValue.md).

We recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs. For more information, see [Cache secrets for your applications](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html).

To retrieve the previous version of a secret, use `VersionStage` and specify AWSPREVIOUS. To revert to the previous version of a secret, call [UpdateSecretVersionStage](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/update-secret-version-stage.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:GetSecretValue`. If the secret is encrypted using a customer-managed key instead of the AWS managed key `aws/secretsmanager`, then you also need `kms:Decrypt` permissions for that key. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_GetSecretValue_RequestSyntax"></a>

```
{
   "SecretId": "{{string}}",
   "VersionId": "{{string}}",
   "VersionStage": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSecretValue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SecretId](#API_GetSecretValue_RequestSyntax) **   <a name="SecretsManager-GetSecretValue-request-SecretId"></a>
The ARN or name of the secret to retrieve. To retrieve a secret from another account, you must use an ARN.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [VersionId](#API_GetSecretValue_RequestSyntax) **   <a name="SecretsManager-GetSecretValue-request-VersionId"></a>
The unique identifier of the version of the secret to retrieve. If you include both this parameter and `VersionStage`, the two parameters must refer to the same secret version. If you don't specify either a `VersionStage` or `VersionId`, then Secrets Manager returns the `AWSCURRENT` version.
This value is typically a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value with 32 hexadecimal digits.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** [VersionStage](#API_GetSecretValue_RequestSyntax) **   <a name="SecretsManager-GetSecretValue-request-VersionStage"></a>
The staging label of the version of the secret to retrieve.
Secrets Manager uses staging labels to keep track of different versions during the rotation process. If you include both this parameter and `VersionId`, the two parameters must refer to the same secret version. If you don't specify either a `VersionStage` or `VersionId`, Secrets Manager returns the `AWSCURRENT` version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_GetSecretValue_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "CreatedDate": number,
   "Name": "string",
   "SecretBinary": blob,
   "SecretString": "string",
   "VersionId": "string",
   "VersionStages": [ "string" ]
}
```

## Response Elements
<a name="API_GetSecretValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-ARN"></a>
The ARN of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [CreatedDate](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-CreatedDate"></a>
The date and time that this version of the secret was created. If you don't specify which version in `VersionId` or `VersionStage`, then Secrets Manager uses the `AWSCURRENT` version.
Type: Timestamp

 ** [Name](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-Name"></a>
The friendly name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [SecretBinary](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-SecretBinary"></a>
The decrypted secret value, if the secret value was originally provided as binary data in the form of a byte array. When you retrieve a `SecretBinary` using the HTTP API, the Python SDK, or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
If the secret was created by using the Secrets Manager console, or if the secret value was originally provided as a string, then this field is omitted. The secret value appears in `SecretString` instead.
Sensitive: This field contains sensitive information, so the service does not include it in AWS CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [SecretString](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-SecretString"></a>
The decrypted secret value, if the secret value was originally provided as a string or through the Secrets Manager console.
If this secret was created by using the console, then Secrets Manager stores the information as a JSON structure of key/value pairs.
Sensitive: This field contains sensitive information, so the service does not include it in AWS CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [VersionId](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-VersionId"></a>
The unique identifier of this version of the secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.

 ** [VersionStages](#API_GetSecretValue_ResponseSyntax) **   <a name="SecretsManager-GetSecretValue-response-VersionStages"></a>
A list of all of the staging labels currently attached to this version of the secret.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetSecretValue_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** DecryptionFailure **
Secrets Manager can't decrypt the protected secret text using the provided KMS key.
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

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_GetSecretValue_Examples"></a>

### Example
<a name="API_GetSecretValue_Example_1"></a>

The following example shows how to retrieve the secret value from a secret. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_GetSecretValue_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.GetSecretValue
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
}
```

#### Sample Response
<a name="API_GetSecretValue_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "CreatedDate":1.523477145713E9,
  "Name":"MyTestDatabaseSecret",
  "SecretString":"{\n  \"username\":\"david\",\n  \"password\":\"EXAMPLE-PASSWORD\"\n}\n",
  "VersionId":"EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

## See Also
<a name="API_GetSecretValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/GetSecretValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/GetSecretValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
