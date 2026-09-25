---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_SpaceSummary.html
---

# SpaceSummary
<a name="API_SpaceSummary"></a>

Summary of a space. Call GetSpace for the full space.

## Contents
<a name="API_SpaceSummary_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-SpaceSummary-createdAt"></a>
The timestamp when the space was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-SpaceSummary-name"></a>
A name that identifies the space.
Type: String
Required: Yes

 ** ownerAccountId **   <a name="cloudwatchomni-Type-SpaceSummary-ownerAccountId"></a>
AWS account ID that owns this space.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** region **   <a name="cloudwatchomni-Type-SpaceSummary-region"></a>
The region where this space was created.
Type: String
Required: Yes

 ** spaceArn **   <a name="cloudwatchomni-Type-SpaceSummary-spaceArn"></a>
The Amazon Resource Name (ARN) of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** spaceId **   <a name="cloudwatchomni-Type-SpaceSummary-spaceId"></a>
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** status **   <a name="cloudwatchomni-Type-SpaceSummary-status"></a>
The status of the space.
Type: String
Valid Values: `ACTIVE | SUSPENDED | MOVING`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-SpaceSummary-updatedAt"></a>
The timestamp when the space was last updated.
Type: Timestamp
Required: Yes

 ** domainArn **   <a name="cloudwatchomni-Type-SpaceSummary-domainArn"></a>
The Amazon Resource Name (ARN) of the domain the space belongs to. Absent when the space is not associated with a domain, so callers must tolerate its absence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** statusReason **   <a name="cloudwatchomni-Type-SpaceSummary-statusReason"></a>
Reason for the current space status.
Type: String
Required: No

## See Also
<a name="API_SpaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/SpaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/SpaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/SpaceSummary)
