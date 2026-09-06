---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_HTTPHeader.html
---

# HTTPHeader
<a name="API_wafRegional_HTTPHeader"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The response from a [GetSampledRequests](API_wafRegional_GetSampledRequests.md) request includes an `HTTPHeader` complex type that appears as `Headers` in the response syntax. `HTTPHeader` contains the names and values of all of the headers that appear in one of the web requests that were returned by `GetSampledRequests`.

## Contents
<a name="API_wafRegional_HTTPHeader_Contents"></a>

 ** Name **   <a name="WAF-Type-wafRegional_HTTPHeader-Name"></a>
The name of one of the headers in the sampled web request.
Type: String
Required: No

 ** Value **   <a name="WAF-Type-wafRegional_HTTPHeader-Value"></a>
The value of one of the headers in the sampled web request.
Type: String
Required: No

## See Also
<a name="API_wafRegional_HTTPHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/HTTPHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/HTTPHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/HTTPHeader)
