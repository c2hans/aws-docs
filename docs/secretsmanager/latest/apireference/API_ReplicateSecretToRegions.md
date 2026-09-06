---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicateSecretToRegions.html
---

# ReplicateSecretToRegions
<a name="API_ReplicateSecretToRegions"></a>

Replicates the secret to a new Regions. See [Multi-Region secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:ReplicateSecretToRegions`. If the primary secret is encrypted with a KMS key other than `aws/secretsmanager`, you also need `kms:Decrypt` permission to the key. To encrypt the replicated secret with a KMS key other than `aws/secretsmanager`, you need `kms:GenerateDataKey` and `kms:Encrypt` to the key. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_ReplicateSecretToRegions_RequestSyntax"></a>

```
{
   "AddReplicaRegions": [
      {
         "KmsKeyId": "{{string}}",
         "Region": "{{string}}"
      }
   ],
   "ForceOverwriteReplicaSecret": {{boolean}},
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_ReplicateSecretToRegions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddReplicaRegions](#API_ReplicateSecretToRegions_RequestSyntax) **   <a name="SecretsManager-ReplicateSecretToRegions-request-AddReplicaRegions"></a>
A list of Regions in which to replicate the secret.
Type: Array of [ReplicaRegionType](API_ReplicaRegionType.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [ForceOverwriteReplicaSecret](#API_ReplicateSecretToRegions_RequestSyntax) **   <a name="SecretsManager-ReplicateSecretToRegions-request-ForceOverwriteReplicaSecret"></a>
Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.
Type: Boolean
Required: No

 ** [SecretId](#API_ReplicateSecretToRegions_RequestSyntax) **   <a name="SecretsManager-ReplicateSecretToRegions-request-SecretId"></a>
The ARN or name of the secret to replicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_ReplicateSecretToRegions_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "ReplicationStatus": [
      {
         "KmsKeyId": "string",
         "LastAccessedDate": number,
         "Region": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ReplicateSecretToRegions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_ReplicateSecretToRegions_ResponseSyntax) **   <a name="SecretsManager-ReplicateSecretToRegions-response-ARN"></a>
The ARN of the primary secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [ReplicationStatus](#API_ReplicateSecretToRegions_ResponseSyntax) **   <a name="SecretsManager-ReplicateSecretToRegions-response-ReplicationStatus"></a>
The status of replication.
Type: Array of [ReplicationStatusType](API_ReplicationStatusType.md) objects

## Errors
<a name="API_ReplicateSecretToRegions_Errors"></a>

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
<a name="API_ReplicateSecretToRegions_Examples"></a>

### Example
<a name="API_ReplicateSecretToRegions_Example_1"></a>

The following example replicates a secret to eu-west-3. The replica is encrypted with the AWS managed key `aws/secretsmanager`. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_ReplicateSecretToRegions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.ReplicateSecretToRegions
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestSecret",
  "AddReplicaRegions": [ { "Region": "eu-west-3" }] ,
  "ForceOverwriteReplicaSecret": true
}
```

#### Sample Response
<a name="API_ReplicateSecretToRegions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-1a2b3c",
  "ReplicationStatus": [
        {
            "Region": "eu-west-3",
            "KmsKeyId": "alias/aws/secretsmanager",
            "Status": "InProgress"
        }
    ]
}
```

## See Also
<a name="API_ReplicateSecretToRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/ReplicateSecretToRegions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ReplicateSecretToRegions)
