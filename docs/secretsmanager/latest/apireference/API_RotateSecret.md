---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html
---

# RotateSecret
<a name="API_RotateSecret"></a>

Configures and starts the asynchronous process of rotating the secret. For information about rotation, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *Secrets Manager User Guide*. If you include the configuration parameters, the operation sets the values for the secret and then immediately starts a rotation. If you don't include the configuration parameters, the operation starts a rotation with the values already stored in the secret.

When rotation is successful, the `AWSPENDING` staging label might be attached to the same version as the `AWSCURRENT` version, or it might not be attached to any version. If the `AWSPENDING` staging label is present but not attached to the same version as `AWSCURRENT`, then any later invocation of `RotateSecret` assumes that a previous rotation request is still in progress and returns an error. When rotation is unsuccessful, the `AWSPENDING` staging label might be attached to an empty secret version. For more information, see [Troubleshoot rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_rotation.html) in the *Secrets Manager User Guide*.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:RotateSecret`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html). You also need `lambda:InvokeFunction` permissions on the rotation function. For more information, see [ Permissions for rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-required-permissions-function.html).

## Request Syntax
<a name="API_RotateSecret_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "ExternalSecretRotationMetadata": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ExternalSecretRotationRoleArn": "{{string}}",
   "RotateImmediately": {{boolean}},
   "RotationLambdaARN": "{{string}}",
   "RotationRules": {
      "AutomaticallyAfterDays": {{number}},
      "Duration": "{{string}}",
      "ScheduleExpression": "{{string}}"
   },
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_RotateSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-ClientRequestToken"></a>
A unique identifier for the new version of the secret. You only need to specify this value if you implement your own retry logic and you want to ensure that Secrets Manager doesn't attempt to create a secret version twice.
If you use the AWS CLI or one of the AWS SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request.
If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a `ClientRequestToken` and include it in the request.
This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value to ensure uniqueness of your versions within the specified secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** [ExternalSecretRotationMetadata](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-ExternalSecretRotationMetadata"></a>
The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see [Using Secrets Manager managed external secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html)
Type: Array of [ExternalSecretRotationMetadataItem](API_ExternalSecretRotationMetadataItem.md) objects
Required: No

 ** [ExternalSecretRotationRoleArn](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-ExternalSecretRotationRoleArn"></a>
The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held by a third-party partner. For more information, see [Security and permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [RotateImmediately](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-RotateImmediately"></a>
Specifies whether to rotate the secret immediately or wait until the next scheduled rotation window. The rotation schedule is defined in [RotateSecret:RotationRules](#SecretsManager-RotateSecret-request-RotationRules).
The default for `RotateImmediately` is `true`. If you don't specify this value, Secrets Manager rotates the secret immediately.
If you set `RotateImmediately` to `false`, Secrets Manager tests the rotation configuration by running the [`testSecret` step](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html) of the Lambda rotation function. This test creates an `AWSPENDING` version of the secret and then removes it.
When changing an existing rotation schedule and setting `RotateImmediately` to `false`:
+ If using `AutomaticallyAfterDays` or a `ScheduleExpression` with `rate()`, the previously scheduled rotation might still occur.
+ To prevent unintended rotations, use a `ScheduleExpression` with `cron()` for granular control over rotation windows.
Rotation is an asynchronous process. For more information, see [How rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html).
Type: Boolean
Required: No

 ** [RotationLambdaARN](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-RotationLambdaARN"></a>
For secrets that use a Lambda rotation function to rotate, the ARN of the Lambda rotation function.
For secrets that use *managed rotation*, omit this field. For more information, see [Managed rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html) in the *Secrets Manager User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [RotationRules](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-RotationRules"></a>
A structure that defines the rotation configuration for this secret.
When changing an existing rotation schedule and setting `RotateImmediately` to `false`:
+ If using `AutomaticallyAfterDays` or a `ScheduleExpression` with `rate()`, the previously scheduled rotation might still occur.
+ To prevent unintended rotations, use a `ScheduleExpression` with `cron()` for granular control over rotation windows.
Type: [RotationRulesType](API_RotationRulesType.md) object
Required: No

 ** [SecretId](#API_RotateSecret_RequestSyntax) **   <a name="SecretsManager-RotateSecret-request-SecretId"></a>
The ARN or name of the secret to rotate.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_RotateSecret_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "Name": "string",
   "VersionId": "string"
}
```

## Response Elements
<a name="API_RotateSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_RotateSecret_ResponseSyntax) **   <a name="SecretsManager-RotateSecret-response-ARN"></a>
The ARN of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Name](#API_RotateSecret_ResponseSyntax) **   <a name="SecretsManager-RotateSecret-response-Name"></a>
The name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [VersionId](#API_RotateSecret_ResponseSyntax) **   <a name="SecretsManager-RotateSecret-response-VersionId"></a>
The ID of the new version of the secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.

## Errors
<a name="API_RotateSecret_Errors"></a>

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
<a name="API_RotateSecret_Examples"></a>

### Example
<a name="API_RotateSecret_Example_1"></a>

The following example configures rotation for a secret using a cron expression. The first rotation happens immediately after the changes are stored in the secret. The rotation schedule is the first and 15th day of every month. The rotation window begins at 4:00 PM UTC and ends at 6:00 PM. The `ClientRequestToken` field becomes the `VersionId` of the new version created during the rotation. The rotation function runs asynchronously in the background.

The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_RotateSecret_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.RotateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "RotationLambdaARN": "arn:aws:lambda:us-west-2:123456789012:function:MyTestDatabaseRotationLambda",
  "RotationRules": {"ScheduleExpression": "cron(0 16 1,15 * ? *)", "Duration": "2h"},
  "RotateImmediately": true,
  "ClientRequestToken": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

#### Sample Response
<a name="API_RotateSecret_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

### Example
<a name="API_RotateSecret_Example_2"></a>

The following example shows how to change a rotation schedule safely when setting `RotateImmediately` to `false` and using `cron()` for precise control over rotation timing. This example schedules rotation for the 1st day of each month at 4:00 PM UTC. Setting `RotateImmediately` to `false` prevents an immediate rotation, while using `cron()` prevents unintended rotations that might occur with `rate()` expressions when changing schedules. The `ClientRequestToken` field becomes the `VersionId` of the new version created during the rotation. The rotation function runs asynchronously in the background.

The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_RotateSecret_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.RotateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "RotationLambdaARN": "arn:aws:lambda:us-west-2:123456789012:function:MyTestDatabaseRotationLambda",
  "RotationRules": {"ScheduleExpression": "cron(0 16 1 * ? *)"},
  "RotateImmediately": false,
  "ClientRequestToken": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

#### Sample Response
<a name="API_RotateSecret_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

### Example
<a name="API_RotateSecret_Example_3"></a>

The following example configures rotation for a secret using a rate expression. The first rotation happens immediately after the changes are stored in the secret. The rotation schedule is every 10 days. The `ClientRequestToken` field becomes the `VersionId` of the new version created during the rotation. The rotation function runs asynchronously in the background.

The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_RotateSecret_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.RotateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "RotationLambdaARN": "arn:aws:lambda:us-west-2:123456789012:function:MyTestDatabaseRotationLambda",
  "RotationRules": {"ScheduleExpression": "rate(10 days)"},
  "RotateImmediately": true,
  "ClientRequestToken": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

#### Sample Response
<a name="API_RotateSecret_Example_3_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

### Example
<a name="API_RotateSecret_Example_4"></a>

The following example starts an immediate rotation, so the secret must already have rotation configured. The `ClientRequestToken` field becomes the `VersionId` of the new version created during the rotation. The rotation function runs asynchronously in the background.

The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_RotateSecret_Example_4_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.RotateSecret
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "ClientRequestToken": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

#### Sample Response
<a name="API_RotateSecret_Example_4_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name": "MyTestDatabaseSecret",
  "VersionId": "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2"
}
```

## See Also
<a name="API_RotateSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/RotateSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/RotateSecret)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
