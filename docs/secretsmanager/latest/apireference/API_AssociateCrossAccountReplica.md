---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html
---

# AssociateCrossAccountReplica

Links a primary secret in your account to a replica secret in a different AWS account and starts replication to this replica. The replica secret must already exist in the other AWS account. Create the replica with [CreateSecret](API_CreateSecret.md) and set its `CrossAccountPrimaryARN` field set to this primary secret's ARN. When you call AssociateCrossAccountReplica, Secrets Manager calls AcceptCrossAccountReplication on the replica secret on your behalf.

The primary and replica secrets must be in the same AWS Region and partition, and you must call this operation from the account that owns the primary secret. A primary secret can have at most one cross-account replica. This operation is idempotent, so you can call it again for the same replica to repair replication. If the association fails, Secrets Manager does not modify either the primary or replica secret.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:AssociateCrossAccountReplica`, `secretsmanager:GetSecretValue` on the primary secret, and `secretsmanager:AcceptCrossAccountReplication` on the replica secret. You must also have `kms:Decrypt` permission for the AWS Key Management Service (AWS KMS) key that encrypts the primary secret, and `kms:Encrypt` permission for the AWS AWS KMS key that encrypts the replica secret. If you supply `ReplicationRoleARN`, you also need `iam:PassRole` for that role. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_AssociateCrossAccountReplica_RequestSyntax"></a>

```
{
   "CrossAccountReplicaARN": "{{string}}",
   "ReplicaRestriction": "{{string}}",
   "ReplicationRoleARN": "{{string}}",
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateCrossAccountReplica_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CrossAccountReplicaARN](#API_AssociateCrossAccountReplica_RequestSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-request-CrossAccountReplicaARN"></a>
The ARN of the replica secret in the other AWS account. The replica secret must be in the same Region and partition as the primary secret. Additionally, the replica account owner must have created the replica secret as a cross-account replica of the primary secret. For more information see [CreateSecret](API_CreateSecret.md).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [ReplicaRestriction](#API_AssociateCrossAccountReplica_RequestSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-request-ReplicaRestriction"></a>
Whether the replica account must belong to the same AWS organization as the primary account:
+  `SameOrg`, which requires the replica account to be in the same organization as the primary account. This is the default.
+  `NoRestriction`, which allows the replica account to be in any organization.
Type: String
Valid Values: `SameOrg | NoRestriction`
Required: No

 ** [ReplicationRoleARN](#API_AssociateCrossAccountReplica_RequestSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-request-ReplicationRoleARN"></a>
The ARN of an IAM role in the primary account that Secrets Manager assumes to perform replication. If you don't include this field, Secrets Manager replicates using the credentials of caller who updates the primary secret. For more information, see [ Cross-account replication permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/cross-account-replicate-permissions.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [SecretId](#API_AssociateCrossAccountReplica_RequestSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-request-SecretId"></a>
The ARN or name of the primary secret in your account to replicate.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_AssociateCrossAccountReplica_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "CrossAccountReplicaARN": "string",
   "ReplicationStatus": "string"
}
```

## Response Elements
<a name="API_AssociateCrossAccountReplica_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_AssociateCrossAccountReplica_ResponseSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-response-ARN"></a>
The ARN of the primary secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [CrossAccountReplicaARN](#API_AssociateCrossAccountReplica_ResponseSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-response-CrossAccountReplicaARN"></a>
The ARN of the replica secret in the other account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [ReplicationStatus](#API_AssociateCrossAccountReplica_ResponseSyntax) **   <a name="SecretsManager-AssociateCrossAccountReplica-response-ReplicationStatus"></a>
The status of replication to the replica secret. Possible values:
+  `InSync`, which indicates that replication to the replica completed successfully and the replica is up to date.
+  `Failed`, which indicates that replication to the replica did not succeed.
+  `InProgress`, which indicates that Secrets Manager is replicating to the replica.
+  `Pending`, which indicates that replication has not yet started.
+  `Detached`, which indicates that primary secret is no longer linked to the replica secret.
Type: String
Valid Values: `InSync | Failed | InProgress | Pending | Detached`

## Errors
<a name="API_AssociateCrossAccountReplica_Errors"></a>

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
<a name="API_AssociateCrossAccountReplica_Examples"></a>

### Example
<a name="API_AssociateCrossAccountReplica_Example_1"></a>

The following example links a primary secret to a replica secret in another account and starts replication. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_AssociateCrossAccountReplica_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.AssociateCrossAccountReplica
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3",
  "ReplicationRoleARN": "arn:aws:iam::123456789012:role/CrossAccountReplicationRole"
}
```

#### Sample Response
<a name="API_AssociateCrossAccountReplica_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-west-2:222222222222:secret:MyReplicaSecret-a1b2c3",
  "ReplicationStatus": "InProgress"
}
```

## See Also
<a name="API_AssociateCrossAccountReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/AssociateCrossAccountReplica)
