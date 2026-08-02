---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ResponseExtractionMapping.html
---

# ResponseExtractionMapping
<a name="API_ResponseExtractionMapping"></a>

Configuration that defines how to extract values from HTTP response content or headers for use in subsequent requests or parameter mapping.

## Contents
<a name="API_ResponseExtractionMapping_Contents"></a>

 ** ContentPath **   <a name="Glue-Type-ResponseExtractionMapping-ContentPath"></a>
A JSON path expression that specifies how to extract a value from the response body content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\$(\.[a-zA-Z0-9_.@\[\]\(\)-]+)*`
Required: No

 ** HeaderKey **   <a name="Glue-Type-ResponseExtractionMapping-HeaderKey"></a>
The name of an HTTP response header from which to extract the value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_ResponseExtractionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ResponseExtractionMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ResponseExtractionMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ResponseExtractionMapping)
