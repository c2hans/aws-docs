---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HttpRequest.html
---

# HttpRequest
<a name="API_HttpRequest"></a>

HTTP request configuration parameters that define how MediaTailor communicates with the ad decision server.

## Contents
<a name="API_HttpRequest_Contents"></a>

 ** Body **   <a name="mediatailor-Type-HttpRequest-Body"></a>
The request body content to send with HTTP requests to the ad decision server. This value is only eligible for `POST` requests.
Type: String
Required: No

 ** CompressRequest **   <a name="mediatailor-Type-HttpRequest-CompressRequest"></a>
The compression method to apply to requests sent to the ad decision server. Supported values are `NONE` and `GZIP`. This value is only eligible for `POST` requests.
Type: String
Valid Values: `NONE | GZIP`
Required: No

 ** Headers **   <a name="mediatailor-Type-HttpRequest-Headers"></a>
Custom HTTP headers to include in requests to the ad decision server. Specify headers as key-value pairs. This value is only eligible for `POST` requests.
Type: String to string map
Required: No

 ** Method **   <a name="mediatailor-Type-HttpRequest-Method"></a>
The HTTP method to use when making requests to the ad decision server. Supported values are `GET` and `POST`.
Type: String
Valid Values: `GET | POST`
Required: No

## See Also
<a name="API_HttpRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/HttpRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/HttpRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/HttpRequest)
