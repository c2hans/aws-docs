---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_JsonataConfiguration.html
---

# JsonataConfiguration
<a name="API_JsonataConfiguration"></a>

JSONata transform settings for a subscriber.

## Contents
<a name="API_JsonataConfiguration_Contents"></a>

 ** Expression **   <a name="eventbridgev2-Type-JsonataConfiguration-Expression"></a>
JSONata expression to transform the event. Must be wrapped in {% %} delimiters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\{%[\s\S]+?%\}(?![\s\S]).*`
Required: Yes

## See Also
<a name="API_JsonataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/JsonataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/JsonataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/JsonataConfiguration)
