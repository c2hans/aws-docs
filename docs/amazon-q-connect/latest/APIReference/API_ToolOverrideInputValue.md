---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ToolOverrideInputValue.html
---

# ToolOverrideInputValue
<a name="API_amazon-q-connect_ToolOverrideInputValue"></a>

An input value override for tools.

## Contents
<a name="API_amazon-q-connect_ToolOverrideInputValue_Contents"></a>

 ** jsonPath **   <a name="connect-Type-amazon-q-connect_ToolOverrideInputValue-jsonPath"></a>
The JSON path for the input value override.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** value **   <a name="connect-Type-amazon-q-connect_ToolOverrideInputValue-value"></a>
The override input value.
Type: [ToolOverrideInputValueConfiguration](API_amazon-q-connect_ToolOverrideInputValueConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_amazon-q-connect_ToolOverrideInputValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ToolOverrideInputValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ToolOverrideInputValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ToolOverrideInputValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
