---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomPromptInputParameters.html
---

# CustomPromptInputParameters
<a name="API_CustomPromptInputParameters"></a>

The parameters for configuring a custom prompt for an agent.

## Contents
<a name="API_CustomPromptInputParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomInstructions **   <a name="QS-Type-CustomPromptInputParameters-CustomInstructions"></a>
Custom instructions for the agent's behavior.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** Identity **   <a name="QS-Type-CustomPromptInputParameters-Identity"></a>
Instructions that define the agent's identity and persona.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** OutputStyle **   <a name="QS-Type-CustomPromptInputParameters-OutputStyle"></a>
Instructions for the desired output style.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** ResponseLength **   <a name="QS-Type-CustomPromptInputParameters-ResponseLength"></a>
Instructions for the desired response length.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** Tone **   <a name="QS-Type-CustomPromptInputParameters-Tone"></a>
Instructions for the desired tone of responses.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CustomPromptInputParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomPromptInputParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomPromptInputParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomPromptInputParameters)
