---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_HttpContext.html
---

# HttpContext
<a name="API_HttpContext"></a>

Specifies the HTTP context to use for the test authorizer request.

## Contents
<a name="API_HttpContext_Contents"></a>

 ** headers **   <a name="iot-Type-HttpContext-headers"></a>
The header keys and values in an HTTP authorization request.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 8192.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 1. Maximum length of 8192.
Value Pattern: `[\s\S]*`
Required: No

 ** queryString **   <a name="iot-Type-HttpContext-queryString"></a>
The query string keys and values in an HTTP authorization request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_HttpContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/HttpContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/HttpContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/HttpContext)
