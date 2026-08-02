---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomPromptProfile.html
---

# CustomPromptProfile
<a name="API_CustomPromptProfile"></a>

A reference to an existing custom prompt profile.

## Contents
<a name="API_CustomPromptProfile_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ModelProfileId **   <a name="QS-Type-CustomPromptProfile-ModelProfileId"></a>
The identifier of the model profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** QbsAwsAccountId **   <a name="QS-Type-CustomPromptProfile-QbsAwsAccountId"></a>
The AWS account ID for the Q Business service.
Type: String
Length Constraints: Fixed length of 15.
Pattern: `QBS[0-9]{12}`
Required: Yes

 ** SubscriptionId **   <a name="QS-Type-CustomPromptProfile-SubscriptionId"></a>
The subscription identifier.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]+`
Required: Yes

## See Also
<a name="API_CustomPromptProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CustomPromptProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CustomPromptProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CustomPromptProfile)
