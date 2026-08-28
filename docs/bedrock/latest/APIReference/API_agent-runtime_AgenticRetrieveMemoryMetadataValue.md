---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemoryMetadataValue.html
---

# AgenticRetrieveMemoryMetadataValue
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataValue"></a>

A metadata value that a filter expression compares against. Set exactly one member.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dateTimeValue **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataValue-dateTimeValue"></a>
A timestamp value in ISO 8601 UTC format.
Type: Timestamp
Required: No

 ** numberValue **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataValue-numberValue"></a>
A numeric value.
Type: Double
Required: No

 ** stringListValue **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataValue-stringListValue"></a>
A list of string values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Required: No

 ** stringValue **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataValue-stringValue"></a>
A string value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
