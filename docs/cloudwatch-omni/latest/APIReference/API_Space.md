---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Space.html
---

# Space
<a name="API_Space"></a>

Detailed information about a space.

## Contents
<a name="API_Space_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-Space-createdAt"></a>
The timestamp when the space was created.
Type: Timestamp
Required: Yes

 ** dataAccessRoleArn **   <a name="cloudwatchomni-Type-Space-dataAccessRoleArn"></a>
The ARN of the IAM role used for data access.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-Space-name"></a>
A name that identifies the space.
Type: String
Required: Yes

 ** ownerAccountId **   <a name="cloudwatchomni-Type-Space-ownerAccountId"></a>
AWS account ID that owns this space.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** region **   <a name="cloudwatchomni-Type-Space-region"></a>
The region where this space was created.
Type: String
Required: Yes

 ** spaceArn **   <a name="cloudwatchomni-Type-Space-spaceArn"></a>
The Amazon Resource Name (ARN) of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** spaceId **   <a name="cloudwatchomni-Type-Space-spaceId"></a>
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** status **   <a name="cloudwatchomni-Type-Space-status"></a>
The status of the space.
Type: String
Valid Values: `ACTIVE | SUSPENDED | MOVING`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-Space-updatedAt"></a>
The timestamp when the space was last updated.
Type: Timestamp
Required: Yes

 ** agentCoreEvaluationRoleArn **   <a name="cloudwatchomni-Type-Space-agentCoreEvaluationRoleArn"></a>
The ARN of the IAM role used by AgentCore online evaluation. Absent when the space was created without one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** domainArn **   <a name="cloudwatchomni-Type-Space-domainArn"></a>
The Amazon Resource Name (ARN) of the domain the space belongs to. Absent when the space is not associated with a domain, so callers must tolerate its absence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** encryptionConfiguration **   <a name="cloudwatchomni-Type-Space-encryptionConfiguration"></a>
How the space's data at rest is encrypted. Always populated: a space with no customer managed key reports `encryptionStrategy` AWS\_OWNED and no `kmsKeyArn`.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** statusReason **   <a name="cloudwatchomni-Type-Space-statusReason"></a>
Reason for the current space status.
Type: String
Required: No

## See Also
<a name="API_Space_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Space)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Space)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Space)
