---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecretVersionStage.html
---

# UpdateSecretVersionStage
<a name="API_UpdateSecretVersionStage"></a>

Modifies the staging labels attached to a version of a secret. Secrets Manager uses staging labels to track a version as it progresses through the secret rotation process. Each staging label can be attached to only one version at a time. To add a staging label to a version when it is already attached to another version, Secrets Manager first removes it from the other version first and then attaches it to this one. For more information about versions and staging labels, see [Concepts: Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version).

The staging labels that you specify in the `VersionStage` parameter are added to the existing list of staging labels for the version.

You can move the `AWSCURRENT` staging label to this version by including it in this call.

**Note**
Whenever you move `AWSCURRENT`, Secrets Manager automatically moves the label `AWSPREVIOUS` to the version that `AWSCURRENT` was removed from.

If this action results in the last label being removed from a version, then the version is considered to be 'deprecated' and can be deleted by Secrets Manager.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:UpdateSecretVersionStage`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_UpdateSecretVersionStage_RequestSyntax"></a>

```
{
   "MoveToVersionId": "{{string}}",
   "RemoveFromVersionId": "{{string}}",
   "SecretId": "{{string}}",
   "VersionStage": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSecretVersionStage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MoveToVersionId](#API_UpdateSecretVersionStage_RequestSyntax) **   <a name="SecretsManager-UpdateSecretVersionStage-request-MoveToVersionId"></a>
The ID of the version to add the staging label to. To remove a label from a version, then do not specify this parameter.
If the staging label is already attached to a different version of the secret, then you must also specify the `RemoveFromVersionId` parameter.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** [RemoveFromVersionId](#API_UpdateSecretVersionStage_RequestSyntax) **   <a name="SecretsManager-UpdateSecretVersionStage-request-RemoveFromVersionId"></a>
The ID of the version that the staging label is to be removed from. If the staging label you are trying to attach to one version is already attached to a different version, then you must include this parameter and specify the version that the label is to be removed from. If the label is attached and you either do not specify this parameter, or the version ID does not match, then the operation fails.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** [SecretId](#API_UpdateSecretVersionStage_RequestSyntax) **   <a name="SecretsManager-UpdateSecretVersionStage-request-SecretId"></a>
The ARN or the name of the secret with the version and staging labelsto modify.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [VersionStage](#API_UpdateSecretVersionStage_RequestSyntax) **   <a name="SecretsManager-UpdateSecretVersionStage-request-VersionStage"></a>
The staging label to add to this version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_UpdateSecretVersionStage_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateSecretVersionStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_UpdateSecretVersionStage_ResponseSyntax) **   <a name="SecretsManager-UpdateSecretVersionStage-response-ARN"></a>
The ARN of the secret that was updated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Name](#API_UpdateSecretVersionStage_ResponseSyntax) **   <a name="SecretsManager-UpdateSecretVersionStage-response-Name"></a>
The name of the secret that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_UpdateSecretVersionStage_Errors"></a>

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

 ** LimitExceededException **
The request failed because it would exceed one of the Secrets Manager quotas.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_UpdateSecretVersionStage_Examples"></a>

### Example
<a name="API_UpdateSecretVersionStage_Example_1"></a>

The following example shows how to add a staging label to a version of a secret. You can review the results by calling [ListSecretVersionIds](API_ListSecretVersionIds.md). The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_UpdateSecretVersionStage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.UpdateSecretVersionStage
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "VersionStage": "STAGINGLABEL1",
  "MoveToVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

#### Sample Response
<a name="API_UpdateSecretVersionStage_Example_1_Response"></a>

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
<a name="API_UpdateSecretVersionStage_Example_2"></a>

The following example shows you how to remove a staging label from a version of a secret. You can review the results by calling [ListSecretVersionIds](API_ListSecretVersionIds.md). The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_UpdateSecretVersionStage_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.UpdateSecretVersionStage
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "VersionStage": "STAGINGLABEL1",
  "RemoveFromVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1"
}
```

#### Sample Response
<a name="API_UpdateSecretVersionStage_Example_2_Response"></a>

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
<a name="API_UpdateSecretVersionStage_Example_3"></a>

The following example shows you how to move a staging label from one version of a secret to another. You can review the results by calling [ListSecretVersionIds](API_ListSecretVersionIds.md). The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_UpdateSecretVersionStage_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.UpdateSecretVersionStage
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "VersionStage": "AWSCURRENT",
  "RemoveFromVersionId": "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1",
  "MoveToVersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

#### Sample Response
<a name="API_UpdateSecretVersionStage_Example_3_Response"></a>

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
<a name="API_UpdateSecretVersionStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/UpdateSecretVersionStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/UpdateSecretVersionStage)
