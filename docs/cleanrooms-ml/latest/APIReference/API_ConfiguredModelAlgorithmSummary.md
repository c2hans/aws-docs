---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ConfiguredModelAlgorithmSummary.html
---

# ConfiguredModelAlgorithmSummary
<a name="API_ConfiguredModelAlgorithmSummary"></a>

Provides summary information about a configured model algorithm.

## Contents
<a name="API_ConfiguredModelAlgorithmSummary_Contents"></a>

 ** configuredModelAlgorithmArn **   <a name="API-Type-ConfiguredModelAlgorithmSummary-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-ConfiguredModelAlgorithmSummary-createTime"></a>
The time at which the configured model algorithm was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="API-Type-ConfiguredModelAlgorithmSummary-name"></a>
The name of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** updateTime **   <a name="API-Type-ConfiguredModelAlgorithmSummary-updateTime"></a>
The most recent time at which the configured model algorithm was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-ConfiguredModelAlgorithmSummary-description"></a>
The description of the configured model algorithm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

## See Also
<a name="API_ConfiguredModelAlgorithmSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ConfiguredModelAlgorithmSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ConfiguredModelAlgorithmSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ConfiguredModelAlgorithmSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
