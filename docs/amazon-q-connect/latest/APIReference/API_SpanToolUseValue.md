---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SpanToolUseValue.html
---

# SpanToolUseValue
<a name="API_amazon-q-connect_SpanToolUseValue"></a>

Tool invocation message content

## Contents
<a name="API_amazon-q-connect_SpanToolUseValue_Contents"></a>

 ** arguments **   <a name="connect-Type-amazon-q-connect_SpanToolUseValue-arguments"></a>
The tool input arguments
Type: JSON value
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_SpanToolUseValue-name"></a>
The tool name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** toolUseId **   <a name="connect-Type-amazon-q-connect_SpanToolUseValue-toolUseId"></a>
Unique ID for this tool invocation
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_amazon-q-connect_SpanToolUseValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanToolUseValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanToolUseValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanToolUseValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
