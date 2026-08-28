---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LabelActionMapping.html
---

# LabelActionMapping
<a name="API_LabelActionMapping"></a>

Maps a sensitivity label from Microsoft Purview to an enforcement action.

## Contents
<a name="API_LabelActionMapping_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="QS-Type-LabelActionMapping-Action"></a>
The enforcement action to apply when content with this sensitivity label is detected. Valid values are `ALLOW`, `BLOCK`, and `WARN`.
Type: String
Valid Values: `ALLOW | WARN | BLOCK`
Required: Yes

 ** LabelId **   <a name="QS-Type-LabelActionMapping-LabelId"></a>
The identifier of the sensitivity label from the DLP provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** LabelName **   <a name="QS-Type-LabelActionMapping-LabelName"></a>
The display name of the sensitivity label from the DLP provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## See Also
<a name="API_LabelActionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LabelActionMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LabelActionMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LabelActionMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
