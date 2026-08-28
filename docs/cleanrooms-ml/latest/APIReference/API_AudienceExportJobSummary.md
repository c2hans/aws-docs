---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AudienceExportJobSummary.html
---

# AudienceExportJobSummary
<a name="API_AudienceExportJobSummary"></a>

Provides information about the audience export job.

## Contents
<a name="API_AudienceExportJobSummary_Contents"></a>

 ** audienceGenerationJobArn **   <a name="API-Type-AudienceExportJobSummary-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job that was exported.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** audienceSize **   <a name="API-Type-AudienceExportJobSummary-audienceSize"></a>
The size of the generated audience. Must match one of the sizes in the configured audience model.
Type: [AudienceSize](API_AudienceSize.md) object
Required: Yes

 ** createTime **   <a name="API-Type-AudienceExportJobSummary-createTime"></a>
The time at which the audience export job was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-AudienceExportJobSummary-name"></a>
The name of the audience export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-AudienceExportJobSummary-status"></a>
The status of the audience export job.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE`
Required: Yes

 ** updateTime **   <a name="API-Type-AudienceExportJobSummary-updateTime"></a>
The most recent time at which the audience export job was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-AudienceExportJobSummary-description"></a>
The description of the audience export job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** outputLocation **   <a name="API-Type-AudienceExportJobSummary-outputLocation"></a>
The Amazon S3 bucket where the audience export is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1285.
Pattern: `s3://.+`
Required: No

 ** statusDetails **   <a name="API-Type-AudienceExportJobSummary-statusDetails"></a>
Details about the status of a resource.
Type: [StatusDetails](API_StatusDetails.md) object
Required: No

## See Also
<a name="API_AudienceExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AudienceExportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AudienceExportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AudienceExportJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
