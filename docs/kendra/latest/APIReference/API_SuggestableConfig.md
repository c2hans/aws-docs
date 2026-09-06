---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_SuggestableConfig.html
---

# SuggestableConfig
<a name="API_SuggestableConfig"></a>

Provides the configuration information for a document field/attribute that you want to base query suggestions on.

## Contents
<a name="API_SuggestableConfig_Contents"></a>

 ** AttributeName **   <a name="kendra-Type-SuggestableConfig-AttributeName"></a>
The name of the document field/attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
Required: No

 ** Suggestable **   <a name="kendra-Type-SuggestableConfig-Suggestable"></a>
 `TRUE` means the document field/attribute is suggestible, so the contents within the field can be used for query suggestions.
Type: Boolean
Required: No

## See Also
<a name="API_SuggestableConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/SuggestableConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/SuggestableConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/SuggestableConfig)
