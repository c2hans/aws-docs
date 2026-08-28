---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ConfiguredAudienceModelSummary.html
---

# ConfiguredAudienceModelSummary
<a name="API_ConfiguredAudienceModelSummary"></a>

Information about the configured audience model.

## Contents
<a name="API_ConfiguredAudienceModelSummary_Contents"></a>

 ** audienceModelArn **   <a name="API-Type-ConfiguredAudienceModelSummary-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model that was used to create the configured audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** configuredAudienceModelArn **   <a name="API-Type-ConfiguredAudienceModelSummary-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that you are interested in.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredAudienceModelSummary-createTime"></a>
The time at which the configured audience model was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-ConfiguredAudienceModelSummary-name"></a>
The name of the configured audience model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** outputConfig **   <a name="API-Type-ConfiguredAudienceModelSummary-outputConfig"></a>
The output configuration of the configured audience model.
Type: [ConfiguredAudienceModelOutputConfig](API_ConfiguredAudienceModelOutputConfig.md) object
Required: Yes

 ** status **   <a name="API-Type-ConfiguredAudienceModelSummary-status"></a>
The status of the configured audience model.
Type: String
Valid Values: `ACTIVE`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredAudienceModelSummary-updateTime"></a>
The most recent time at which the configured audience model was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-ConfiguredAudienceModelSummary-description"></a>
The description of the configured audience model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_ConfiguredAudienceModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ConfiguredAudienceModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ConfiguredAudienceModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ConfiguredAudienceModelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
