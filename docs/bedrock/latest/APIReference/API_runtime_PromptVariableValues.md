---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_PromptVariableValues.html
---

# PromptVariableValues
<a name="API_runtime_PromptVariableValues"></a>

Contains a map of variables in a prompt from Prompt management to an object containing the values to fill in for them when running model invocation. For more information, see [How Prompt management works](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-how.html).

## Contents
<a name="API_runtime_PromptVariableValues_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="bedrock-Type-runtime_PromptVariableValues-text"></a>
The text value that the variable maps to.
Type: String
Required: No

## See Also
<a name="API_runtime_PromptVariableValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/PromptVariableValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/PromptVariableValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/PromptVariableValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
