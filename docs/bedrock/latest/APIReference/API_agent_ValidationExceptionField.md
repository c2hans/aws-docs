---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_agent_ValidationExceptionField"></a>

Stores information about a field passed inside a request that resulted in an validation error.

## Contents
<a name="API_agent_ValidationExceptionField_Contents"></a>

 ** message **   <a name="bedrock-Type-agent_ValidationExceptionField-message"></a>
A message describing why this field failed validation.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** name **   <a name="bedrock-Type-agent_ValidationExceptionField-name"></a>
The name of the field.
Type: String
Pattern: `[\s\S]+`
Required: Yes

## See Also
<a name="API_agent_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ValidationExceptionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
