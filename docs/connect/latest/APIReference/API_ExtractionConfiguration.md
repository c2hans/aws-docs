---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ExtractionConfiguration.html
---

# ExtractionConfiguration
<a name="API_ExtractionConfiguration"></a>

The extraction configuration that defines how data is extracted from customer interactions.

## Contents
<a name="API_ExtractionConfiguration_Contents"></a>

 ** PromptHint **   <a name="connect-Type-ExtractionConfiguration-PromptHint"></a>
The prompt hint that guides the extraction. This text tells the generative AI model what data to look for in the customer interaction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** NotFoundBehavior **   <a name="connect-Type-ExtractionConfiguration-NotFoundBehavior"></a>
The behavior when the extraction cannot find the specified data in the interaction.
Type: [ExtractionDefinitionNotFoundBehavior](API_ExtractionDefinitionNotFoundBehavior.md) object
Required: No

## See Also
<a name="API_ExtractionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ExtractionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ExtractionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ExtractionConfiguration)
