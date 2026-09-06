---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomPromptInterface.html
---

# CustomPromptInterface
<a name="API_CustomPromptInterface"></a>

The custom prompt interface configuration that defines how an agent's prompt is configured.

## Contents
<a name="API_CustomPromptInterface_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ModelProfileId **   <a name="QS-Type-CustomPromptInterface-ModelProfileId"></a>
The identifier of the model profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** QbsAwsAccountId **   <a name="QS-Type-CustomPromptInterface-QbsAwsAccountId"></a>
The AWS account ID for the Q Business service.
Type: String
Length Constraints: Fixed length of 15.
Pattern: `QBS[0-9]{12}`
Required: Yes

 ** SubscriptionId **   <a name="QS-Type-CustomPromptInterface-SubscriptionId"></a>
The subscription identifier.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]+`
Required: Yes

 ** CustomInstructions **   <a name="QS-Type-CustomPromptInterface-CustomInstructions"></a>
Custom instructions for the agent's behavior.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** Identity **   <a name="QS-Type-CustomPromptInterface-Identity"></a>
Instructions that define the agent's identity and persona.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** OutputStyle **   <a name="QS-Type-CustomPromptInterface-OutputStyle"></a>
Instructions for the desired output style.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** promptSummary **   <a name="QS-Type-CustomPromptInterface-promptSummary"></a>
A summary of the custom prompt configuration.
Type: String
Required: No

 ** ResponseLength **   <a name="QS-Type-CustomPromptInterface-ResponseLength"></a>
Instructions for the desired response length.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

 ** Tone **   <a name="QS-Type-CustomPromptInterface-Tone"></a>
Instructions for the desired tone of responses.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 350000.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CustomPromptInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomPromptInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomPromptInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomPromptInterface)
