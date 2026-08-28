---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html
---

# CreateSecret
<a name="API_CreateSecret"></a>

Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager. The secret also includes the connection information to access a database or other service, which Secrets Manager doesn't encrypt. A secret in Secrets Manager consists of both the protected secret data and the important information needed to manage the secret.

For secrets that use *managed rotation*, you need to create the secret through the managing service. For more information, see [Secrets Manager secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).

For information about creating a secret in the console, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html).

To create a secret, you can provide the secret value to be encrypted in either the `SecretString` parameter or the `SecretBinary` parameter, but not both. If you include `SecretString` or `SecretBinary` then Secrets Manager creates an initial secret version and automatically attaches the staging label `AWSCURRENT` to it.

For database credentials you want to rotate, for Secrets Manager to be able to rotate the secret, you must make sure the JSON you store in the `SecretString` matches the [JSON structure of a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_secret_json_structure.html).

If you don't specify an AWS KMS encryption key, Secrets Manager uses the AWS managed key `aws/secretsmanager`. If this key doesn't already exist in your account, then Secrets Manager creates it for you automatically. All users and roles in the AWS account automatically have access to use `aws/secretsmanager`. Creating `aws/secretsmanager` can result in a one-time significant delay in returning the result.

If the secret is in a different AWS account from the credentials calling the API, then you can't use `aws/secretsmanager` to encrypt the secret, and you must create and use a customer managed AWS KMS key.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters except `SecretBinary` or `SecretString` because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:CreateSecret`. If you include tags in the secret, you also need `secretsmanager:TagResource`. To add replica Regions, you must also have `secretsmanager:ReplicateSecretToRegions`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

To encrypt the secret with a KMS key other than `aws/secretsmanager`, you need `kms:GenerateDataKey` and `kms:Decrypt` permission to the key.

**Important**
When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to [Mitigate the risks of using command-line tools to store AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html).

## Request Syntax
<a name="API_CreateSecret_RequestSyntax"></a>

```
{
   "AddReplicaRegions": [
      {
         "KmsKeyId": "{{string}}",
         "Region": "{{string}}"
      }
   ],
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "ForceOverwriteReplicaSecret": {{boolean}},
   "KmsKeyId": "{{string}}",
   "Name": "{{string}}",
   "SecretBinary": {{blob}},
   "SecretString": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddReplicaRegions](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-AddReplicaRegions"></a>
A list of Regions and AWS KMS keys to replicate secrets.
Type: Array of [ReplicaRegionType](API_ReplicaRegionType.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [ClientRequestToken](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-ClientRequestToken"></a>
If you include `SecretString` or `SecretBinary`, then Secrets Manager creates an initial version for the secret, and this parameter specifies the unique identifier for the new version.
If you use the AWS CLI or one of the AWS SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request.
If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a `ClientRequestToken` and include it in the request.
This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value to ensure uniqueness of your versions within the specified secret.
+ If the `ClientRequestToken` value isn't already associated with a version of the secret then a new version of the secret is created.
+ If a version with this value already exists and the version `SecretString` and `SecretBinary` values are the same as those in the request, then the request is ignored.
+ If a version with this value already exists and that version's `SecretString` and `SecretBinary` values are different from those in the request, then the request fails because you cannot modify an existing version. Instead, use [PutSecretValue](API_PutSecretValue.md) to create a new version.
This value becomes the `VersionId` of the new version.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** [Description](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-Description"></a>
The description of the secret.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [ForceOverwriteReplicaSecret](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-ForceOverwriteReplicaSecret"></a>
Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.
Type: Boolean
Required: No

 ** [KmsKeyId](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-KmsKeyId"></a>
The ARN, key ID, or alias of the AWS KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by `alias/`, for example `alias/aws/secretsmanager`. For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html).
To use a AWS KMS key in a different account, use the key ARN or the alias ARN.
If you don't specify this value, then Secrets Manager uses the key `aws/secretsmanager`. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.
If the secret is in a different AWS account from the credentials calling the API, then you can't use `aws/secretsmanager` to encrypt the secret, and you must create and use a customer managed AWS KMS key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [Name](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-Name"></a>
The name of the new secret.
The secret name can contain ASCII letters, numbers, and the following characters: /\_\+=.@-
Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [SecretBinary](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-SecretBinary"></a>
The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter.
Either `SecretString` or `SecretBinary` must have a value, but not both.
This parameter is not available in the Secrets Manager console.
Sensitive: This field contains sensitive information, so the service does not include it in AWS CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** [SecretString](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-SecretString"></a>
The text data to encrypt and store in this new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value.
Either `SecretString` or `SecretBinary` must have a value, but not both.
If you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the `SecretString` parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that a Lambda rotation function can parse.
Sensitive: This field contains sensitive information, so the service does not include it in AWS CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** [Tags](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-Tags"></a>
A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:
 `[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`
Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".
If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an `Access Denied` error. For more information, see [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and [Limit access to identities with tags that match secrets' tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2).
For information about how to format a JSON parameter for the various command line tool environments, see [Using JSON for Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json). If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
For tag quotas and naming restrictions, see [Service quotas for Tagging](https://docs.aws.amazon.com/general/latest/gr/arg.html#taged-reference-quotas) in the * AWS General Reference guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [Type](#API_CreateSecret_RequestSyntax) **   <a name="SecretsManager-CreateSecret-request-Type"></a>
The exact string that identifies the partner that holds the external secret. For more information, see [Using Secrets Manager managed external secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSecret_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "Name": "string",
   "ReplicationStatus": [
      {
         "KmsKeyId": "string",
         "LastAccessedDate": number,
         "Region": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "VersionId": "string"
}
```

## Response Elements
<a name="API_CreateSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_CreateSecret_ResponseSyntax) **   <a name="SecretsManager-CreateSecret-response-ARN"></a>
The ARN of the new secret. The ARN includes the name of the secret followed by six random characters. This ensures that if you create a new secret with the same name as a deleted secret, then users with access to the old secret don't get access to the new secret because the ARNs are different.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Name](#API_CreateSecret_ResponseSyntax) **   <a name="SecretsManager-CreateSecret-response-Name"></a>
The name of the new secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ReplicationStatus](#API_CreateSecret_ResponseSyntax) **   <a name="SecretsManager-CreateSecret-response-ReplicationStatus"></a>
A list of the replicas of this secret and their status:
+  `Failed`, which indicates that the replica was not created.
+  `InProgress`, which indicates that Secrets Manager is in the process of creating the replica.
+  `InSync`, which indicates that the replica was created.
Type: Array of [ReplicationStatusType](API_ReplicationStatusType.md) objects

 ** [VersionId](#API_CreateSecret_ResponseSyntax) **   <a name="SecretsManager-CreateSecret-response-VersionId"></a>
The unique identifier associated with the version of the new secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.

## Errors
<a name="API_CreateSecret_Errors"></a>

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
<a name="API_CreateSecret_Examples"></a>

### Example
<a name="API_CreateSecret_Example_1"></a>

The following example shows how to create a secret. Secrets Manager retrieves the credentials stored in the encrypted secret value from a file on disk named mycreds.json. For an example of mycreds.json, see [Creating a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html#proc-create-api). The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_CreateSecret_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.CreateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "Name": "MyTestDatabaseSecret",
  "Description": "My test database secret created with the CLI",
  "SecretString": "{\"username\":\"david\",\"password\":\"EXAMPLE-PASSWORD\"}", "ClientRequestToken": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

#### Sample Response
<a name="API_CreateSecret_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name":"MyTestDatabaseSecret",
  "VersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

## See Also
<a name="API_CreateSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/CreateSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/CreateSecret)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
