---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateSpace.html
---

# CreateSpace
<a name="API_CreateSpace"></a>

Creates a space in a domain.

Use GetSpace to retrieve the space, ListSpaces to enumerate spaces, UpdateSpace to modify it, and DeleteSpace to remove it.

## Request Parameters
<a name="API_CreateSpace_RequestParameters"></a>

 ** agentCoreEvaluationRoleArn **
The ARN of the IAM role used by AgentCore online evaluation. Must be in the caller's account. Omit if the space does not use AgentCore online evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** clientToken **
Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** dataAccessRoleArn **
The ARN of the IAM role used for data access. The role must be in the caller's account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** domainId **
The ID of the domain to create the space in.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** encryptionConfiguration **
How to encrypt the space's data at rest. Omit for service owned encryption, which is equivalent to passing `encryptionStrategy` AWS\_OWNED.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** name **
A name that identifies the space. Must be 3-64 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: Yes

 ** tags **
The tags to associate with the space.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateSpace_ResponseElements"></a>

The following element is returned by the service.

 ** space **
The details of the created space.
Type: [Space](API_Space.md) object

## Errors
<a name="API_CreateSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The operation could not be completed because of a conflict with the current state of the resource.
 ** conflictType **
The type of conflict that caused the request to fail. Not always present.
 ** errorCode **
The error code associated with the conflict. Not always present.
 ** message **
A human-readable description of the conflict.
 ** resourceId **
The identifier of the resource that is in conflict. Not always present.
 ** resourceType **
The type of the resource that is in conflict. Not always present.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** errorCode **
The error code associated with the failure.
 ** resourceId **
The identifier of the resource that could not be found. Not always present.
 ** resourceType **
The type of the resource that could not be found. Not always present.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_CreateSpace_Examples"></a>

### Create a space
<a name="API_CreateSpace_Example_1"></a>

The following example creates a space in a domain and encrypts its data at rest with a customer managed KMS key. The name must be 3-64 characters of lowercase letters, numbers, and hyphens. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateSpace_Example_1_Request"></a>

```
{
  "agentCoreEvaluationRoleArn": "arn:aws:iam::123456789012:role/CloudWatchAgentCoreEvaluationRole",
  "clientToken": "3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73",
  "dataAccessRoleArn": "arn:aws:iam::123456789012:role/CloudWatchSpaceDataAccessRole",
  "domainId": "d-1a2b3c4d5e",
  "encryptionConfiguration": {
    "encryptionStrategy": "CUSTOMER_MANAGED",
    "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
  },
  "name": "prod-observability",
  "tags": {
    "Team": "observability"
  }
}
```

#### Sample Response
<a name="API_CreateSpace_Example_1_Response"></a>

```
{
  "space": {
    "agentCoreEvaluationRoleArn": "arn:aws:iam::123456789012:role/CloudWatchAgentCoreEvaluationRole",
    "createdAt": "2026-09-16T14:22:31Z",
    "dataAccessRoleArn": "arn:aws:iam::123456789012:role/CloudWatchSpaceDataAccessRole",
    "domainArn": "arn:aws:cloudwatch:us-east-1:123456789012:domain/d-1a2b3c4d5e",
    "encryptionConfiguration": {
      "encryptionStrategy": "CUSTOMER_MANAGED",
      "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/1a2b3c4d-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
    },
    "name": "prod-observability",
    "ownerAccountId": "123456789012",
    "region": "us-east-1",
    "spaceArn": "arn:aws:cloudwatch:us-east-1:123456789012:space/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "status": "ACTIVE",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_CreateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateSpace)
