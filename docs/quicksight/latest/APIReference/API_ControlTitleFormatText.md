---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ControlTitleFormatText.html
---

# ControlTitleFormatText
<a name="API_ControlTitleFormatText"></a>

The title format text configuration for a sheet control. This is a tagged union type. Specify either `PlainText` or `RichText`, but not both.

## Contents
<a name="API_ControlTitleFormatText_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PlainText **   <a name="QS-Type-ControlTitleFormatText-PlainText"></a>
The plain text format of the title text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** RichText **   <a name="QS-Type-ControlTitleFormatText-RichText"></a>
The rich text format of the title text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_ControlTitleFormatText_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ControlTitleFormatText)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ControlTitleFormatText)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ControlTitleFormatText)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
