---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxyVersionSummary.html
---

# ProxyVersionSummary

Information about a proxy version.

## Contents
<a name="API_ProxyVersionSummary_Contents"></a>

 ** type **   <a name="elasticloadbalancing-Type-ProxyVersionSummary-type"></a>
The type of proxy.
Type: String
Valid Values: `envoy`
Required: Yes

 ** version **   <a name="elasticloadbalancing-Type-ProxyVersionSummary-version"></a>
The version of the proxy software, in `major.minor` format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\d+\.\d+`
Required: Yes

## See Also
<a name="API_ProxyVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxyVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxyVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxyVersionSummary)
