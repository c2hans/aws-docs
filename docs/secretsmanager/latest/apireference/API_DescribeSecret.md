---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html
---

# DescribeSecret
<a name="API_DescribeSecret"></a>

Retrieves the details of a secret. It does not include the encrypted secret value. Secrets Manager only returns fields that have a value in the response.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:DescribeSecret`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_DescribeSecret_RequestSyntax"></a>

```
{
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSecret_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SecretId](#API_DescribeSecret_RequestSyntax) **   <a name="SecretsManager-DescribeSecret-request-SecretId"></a>
The ARN or name of the secret.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_DescribeSecret_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "CreatedDate": number,
   "DeletedDate": number,
   "Description": "string",
   "ExternalSecretRotationMetadata": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "ExternalSecretRotationRoleArn": "string",
   "KmsKeyId": "string",
   "LastAccessedDate": number,
   "LastChangedDate": number,
   "LastRotatedDate": number,
   "Name": "string",
   "NextRotationDate": number,
   "OwningService": "string",
   "PrimaryRegion": "string",
   "ReplicationStatus": [
      {
         "KmsKeyId": "string",
         "LastAccessedDate": number,
         "Region": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "RotationEnabled": boolean,
   "RotationLambdaARN": "string",
   "RotationRules": {
      "AutomaticallyAfterDays": number,
      "Duration": "string",
      "ScheduleExpression": "string"
   },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ],
   "Type": "string",
   "VersionIdsToStages": {
      "string" : [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeSecret_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-ARN"></a>
The ARN of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [CreatedDate](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-CreatedDate"></a>
The date the secret was created.
Type: Timestamp

 ** [DeletedDate](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-DeletedDate"></a>
The date the secret is scheduled for deletion. If it is not scheduled for deletion, this field is omitted. When you delete a secret, Secrets Manager requires a recovery window of at least 7 days before deleting the secret. Some time after the deleted date, Secrets Manager deletes the secret, including all of its versions.
If a secret is scheduled for deletion, then its details, including the encrypted secret value, is not accessible. To cancel a scheduled deletion and restore access to the secret, use [RestoreSecret](API_RestoreSecret.md).
Type: Timestamp

 ** [Description](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-Description"></a>
The description of the secret.
Type: String
Length Constraints: Maximum length of 2048.

 ** [ExternalSecretRotationMetadata](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-ExternalSecretRotationMetadata"></a>
The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see [Managed external secrets partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).
Type: Array of [ExternalSecretRotationMetadataItem](API_ExternalSecretRotationMetadataItem.md) objects

 ** [ExternalSecretRotationRoleArn](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-ExternalSecretRotationRoleArn"></a>
The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held by a third-party partner. For more information, see [Security and permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [KmsKeyId](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-KmsKeyId"></a>
The key ID or alias ARN of the AWS KMS key that Secrets Manager uses to encrypt the secret value. If the secret is encrypted with the AWS managed key `aws/secretsmanager`, this field is omitted. Secrets created using the console use an AWS KMS key ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [LastAccessedDate](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-LastAccessedDate"></a>
The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.
Type: Timestamp

 ** [LastChangedDate](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-LastChangedDate"></a>
The last date and time that this secret was modified in any way.
Type: Timestamp

 ** [LastRotatedDate](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-LastRotatedDate"></a>
The last date and time that Secrets Manager rotated the secret. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null.
Type: Timestamp

 ** [Name](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-Name"></a>
The name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [NextRotationDate](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-NextRotationDate"></a>
The next rotation is scheduled to occur on or before this date. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null. If rotation fails, Secrets Manager retries the entire rotation process multiple times. If rotation is unsuccessful, this date may be in the past.
This date represents the latest date that rotation will occur, but it is not an approximate rotation date. In some cases, for example if you turn off automatic rotation and then turn it back on, the next rotation may occur much sooner than this date.
Type: Timestamp

 ** [OwningService](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-OwningService"></a>
The ID of the service that created this secret. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [PrimaryRegion](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-PrimaryRegion"></a>
The Region the secret is in. If a secret is replicated to other Regions, the replicas are listed in `ReplicationStatus`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([a-z]+-)+\d+$`

 ** [ReplicationStatus](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-ReplicationStatus"></a>
A list of the replicas of this secret and their status:
+  `Failed`, which indicates that the replica was not created.
+  `InProgress`, which indicates that Secrets Manager is in the process of creating the replica.
+  `InSync`, which indicates that the replica was created.
Type: Array of [ReplicationStatusType](API_ReplicationStatusType.md) objects

 ** [RotationEnabled](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-RotationEnabled"></a>
Specifies whether automatic rotation is turned on for this secret. If the secret has never been configured for rotation, Secrets Manager returns null.
To turn on rotation, use [RotateSecret](API_RotateSecret.md). To turn off rotation, use [CancelRotateSecret](API_CancelRotateSecret.md).
Type: Boolean

 ** [RotationLambdaARN](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-RotationLambdaARN"></a>
The ARN of the Lambda function that Secrets Manager invokes to rotate the secret.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [RotationRules](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-RotationRules"></a>
The rotation schedule and Lambda function for this secret. If the secret previously had rotation turned on, but it is now turned off, this field shows the previous rotation schedule and rotation function. If the secret never had rotation turned on, this field is omitted.
Type: [RotationRulesType](API_RotationRulesType.md) object

 ** [Tags](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-Tags"></a>
The list of tags attached to the secret. To add tags to a secret, use [TagResource](API_TagResource.md). To remove tags, use [UntagResource](API_UntagResource.md).
Type: Array of [Tag](API_Tag.md) objects

 ** [Type](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-Type"></a>
The exact string that identifies the partner that holds the external secret. For more information, see [Using Secrets Manager managed external secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [VersionIdsToStages](#API_DescribeSecret_ResponseSyntax) **   <a name="SecretsManager-DescribeSecret-response-VersionIdsToStages"></a>
A list of the versions of the secret that have staging labels attached. Versions that don't have staging labels are considered deprecated and Secrets Manager can delete them.
Secrets Manager uses staging labels to indicate the status of a secret version during rotation. The three staging labels for rotation are:
+  `AWSCURRENT`, which indicates the current version of the secret.
+  `AWSPENDING`, which indicates the version of the secret that contains new secret information that will become the next current version when rotation finishes.

  During rotation, Secrets Manager creates an `AWSPENDING` version ID before creating the new secret version. To check if a secret version exists, call [GetSecretValue](API_GetSecretValue.md).
+  `AWSPREVIOUS`, which indicates the previous current version of the secret. You can use this as the *last known good* version.
For more information about rotation and staging labels, see [How rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html).
Type: String to array of strings map
Key Length Constraints: Minimum length of 32. Maximum length of 64.
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_DescribeSecret_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidParameterException **
The parameter name or value is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_DescribeSecret_Examples"></a>

### Example
<a name="API_DescribeSecret_Example_1"></a>

The following example shows how to get the details about a secret. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_DescribeSecret_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.DescribeSecret
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
<a name="API_DescribeSecret_Example_1_Response"></a>

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
  "Description": "My test database secret created with the CLI",
  "LastChangedDate": 1523477145.729,
  "LastAccessedDate": 1606269226,
  "RotationEnabled": true,
  "RotationLambdaARN": "arn:aws:lambda:us-west-2:123456789012:function:MyTestRotationLambda",
  "RotationRules": {
    "AutomaticallyAfterDays": 14,
    "ScheduleExpression": "cron(0 16 1,15 * ? *)",
    "Duration": "2h"
  },
  "LastRotatedDate": 1525747253.72,
  "NextRotationDate": 1665165599000,
  "Tags": [
    {
      "Key": "SecondTag",
      "Value": "AnotherValue"
    },
    {
      "Key": "FirstTag",
      "Value": "SomeValue"
    }
  ],
  "VersionIdsToStages": {
    "EXAMPLE1-90ab-cdef-fedc-ba987SECRET1": [
      "AWSPREVIOUS"
    ],
    "EXAMPLE2-90ab-cdef-fedc-ba987SECRET2": [
      "AWSCURRENT"
    ]
  }
}
```

## See Also
<a name="API_DescribeSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/DescribeSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/DescribeSecret)
