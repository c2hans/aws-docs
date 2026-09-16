---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DistributionCustomErrorResponse.html
---

# DistributionCustomErrorResponse
<a name="API_DistributionCustomErrorResponse"></a>

Describes a custom error response for a Lightsail distribution. A custom error response specifies the page that the distribution returns to the viewer. It also specifies the HTTP status code that the distribution sends when the origin responds with a given HTTP error code.

## Contents
<a name="API_DistributionCustomErrorResponse_Contents"></a>

 ** errorCachingMinTTL **   <a name="Lightsail-Type-DistributionCustomErrorResponse-errorCachingMinTTL"></a>
The minimum time, in seconds, that the distribution caches the custom error response before requesting the object again from the origin. If you don't specify a value, the default is `10` seconds.
Type: Long
Required: No

 ** errorCode **   <a name="Lightsail-Type-DistributionCustomErrorResponse-errorCode"></a>
The HTTP error code from the origin that triggers the custom error response (for example, `403` or `404`).
Type: Integer
Required: No

 ** responseCode **   <a name="Lightsail-Type-DistributionCustomErrorResponse-responseCode"></a>
The HTTP status code that the distribution returns to the viewer for the custom error response.
Type: String
Required: No

 ** responsePagePath **   <a name="Lightsail-Type-DistributionCustomErrorResponse-responsePagePath"></a>
The path to the custom error page that the distribution returns to the viewer (for example, `/404.html`). The path must begin with a forward slash (`/`) and reference an object that is available from the origin.
Type: String
Required: No

## See Also
<a name="API_DistributionCustomErrorResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DistributionCustomErrorResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DistributionCustomErrorResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DistributionCustomErrorResponse)
