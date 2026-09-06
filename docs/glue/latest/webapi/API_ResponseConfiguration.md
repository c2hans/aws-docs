---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ResponseConfiguration.html
---

# ResponseConfiguration
<a name="API_ResponseConfiguration"></a>

Configuration that defines how to parse JSON responses from REST API calls, including paths to result data and error information.

## Contents
<a name="API_ResponseConfiguration_Contents"></a>

 ** ResultPath **   <a name="Glue-Type-ResponseConfiguration-ResultPath"></a>
The JSON path expression that identifies where the actual result data is located within the API response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\$(\.[a-zA-Z0-9_.@\[\]\(\)-]+)*`
Required: Yes

 ** ErrorPath **   <a name="Glue-Type-ResponseConfiguration-ErrorPath"></a>
The JSON path expression that identifies where error information is located within API responses when requests fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\$(\.[a-zA-Z0-9_.@\[\]\(\)-]+)*`
Required: No

## See Also
<a name="API_ResponseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ResponseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ResponseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ResponseConfiguration)
