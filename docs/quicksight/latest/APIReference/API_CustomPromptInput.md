---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomPromptInput.html
---

# CustomPromptInput
<a name="API_CustomPromptInput"></a>

The custom prompt input for an agent. This is a union type that can be either an existing prompt profile or new prompt parameters.

## Contents
<a name="API_CustomPromptInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ExistingPrompt **   <a name="QS-Type-CustomPromptInput-ExistingPrompt"></a>
An existing custom prompt profile to use for the agent.
Type: [CustomPromptProfile](API_CustomPromptProfile.md) object
Required: No

 ** NewPrompt **   <a name="QS-Type-CustomPromptInput-NewPrompt"></a>
New custom prompt parameters to configure for the agent.
Type: [CustomPromptInputParameters](API_CustomPromptInputParameters.md) object
Required: No

## See Also
<a name="API_CustomPromptInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomPromptInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomPromptInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomPromptInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
