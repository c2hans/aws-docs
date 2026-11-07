---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FilterStringConfiguration.html
---

# FilterStringConfiguration
<a name="API_FilterStringConfiguration"></a>

Configuration for constructing filter expression strings when using the `FILTER_STRING` filter mode.

## Contents
<a name="API_FilterStringConfiguration_Contents"></a>

 ** QueryParameterName **   <a name="Glue-Type-FilterStringConfiguration-QueryParameterName"></a>
The query parameter name used to send the constructed filter expression string in API requests.
Type: String
Required: Yes

 ** QuoteCharacter **   <a name="Glue-Type-FilterStringConfiguration-QuoteCharacter"></a>
The character used to quote values when `QuoteStringValues` is true. Defaults to double quotes if not specified.
Type: String
Required: No

 ** QuoteStringValues **   <a name="Glue-Type-FilterStringConfiguration-QuoteStringValues"></a>
Indicates whether string and date values should be wrapped with a quote character in the filter expression.
Type: Boolean
Required: No

## See Also
<a name="API_FilterStringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FilterStringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FilterStringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FilterStringConfiguration)
