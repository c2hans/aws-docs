---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceGenerationJobSummary.html
---

# AudienceGenerationJobSummary
<a name="API_AudienceGenerationJobSummary"></a>

Provides information about the configured audience generation job.

## Contents
<a name="API_AudienceGenerationJobSummary_Contents"></a>

 ** audienceGenerationJobArn **   <a name="API-Type-AudienceGenerationJobSummary-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** configuredAudienceModelArn **   <a name="API-Type-AudienceGenerationJobSummary-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that was used for this audience generation job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-AudienceGenerationJobSummary-createTime"></a>
The time at which the audience generation job was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-AudienceGenerationJobSummary-name"></a>
The name of the audience generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-AudienceGenerationJobSummary-status"></a>
The status of the audience generation job.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: Yes

 ** updateTime **   <a name="API-Type-AudienceGenerationJobSummary-updateTime"></a>
The most recent time at which the audience generation job was updated.
Type: Timestamp
Required: Yes

 ** collaborationId **   <a name="API-Type-AudienceGenerationJobSummary-collaborationId"></a>
The identifier of the collaboration that contains this audience generation job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** description **   <a name="API-Type-AudienceGenerationJobSummary-description"></a>
The description of the audience generation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** startedBy **   <a name="API-Type-AudienceGenerationJobSummary-startedBy"></a>
The AWS Account that submitted the job.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_AudienceGenerationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceGenerationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceGenerationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceGenerationJobSummary)
