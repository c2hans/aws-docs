---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_IssueArtifactItem.html
---

# IssueArtifactItem
<a name="API_IssueArtifactItem"></a>

A summary of an artifact returned in list responses.

## Contents
<a name="API_IssueArtifactItem_Contents"></a>

 ** artifactId **   <a name="continuum-Type-IssueArtifactItem-artifactId"></a>
The identifier of the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** artifactType **   <a name="continuum-Type-IssueArtifactItem-artifactType"></a>
The artifact Type.
Type: String
Valid Values: `EVIDENCE | AGENT_COMMUNICATION | VALIDATION_EVIDENCE | REMEDIATION_PROPOSAL | DECISION | PATCH`
Required: Yes

 ** contentSizeBytes **   <a name="continuum-Type-IssueArtifactItem-contentSizeBytes"></a>
The content Size Bytes.
Type: Long
Required: Yes

 ** createdAt **   <a name="continuum-Type-IssueArtifactItem-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** mediaType **   <a name="continuum-Type-IssueArtifactItem-mediaType"></a>
The media Type.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** producer **   <a name="continuum-Type-IssueArtifactItem-producer"></a>
The producer.
Type: [IssueArtifactProducerSummary](API_IssueArtifactProducerSummary.md) object
Required: Yes

## See Also
<a name="API_IssueArtifactItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/IssueArtifactItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/IssueArtifactItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/IssueArtifactItem)
