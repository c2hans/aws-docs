---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxySummary.html
---

# ProxySummary

Summary information about a proxy.

## Contents
<a name="API_ProxySummary_Contents"></a>

 ** arn **   <a name="elasticloadbalancing-Type-ProxySummary-arn"></a>
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** createdAt **   <a name="elasticloadbalancing-Type-ProxySummary-createdAt"></a>
The date and time that the proxy was created.
Type: Timestamp
Required: No

 ** dnsName **   <a name="elasticloadbalancing-Type-ProxySummary-dnsName"></a>
The DNS name of the proxy.
Type: String
Required: No

 ** name **   <a name="elasticloadbalancing-Type-ProxySummary-name"></a>
The name of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*(^[a-zA-Z0-9]+$|^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$).*`
Required: No

 ** status **   <a name="elasticloadbalancing-Type-ProxySummary-status"></a>
The status of the proxy.
Type: [ProxyStatus](API_ProxyStatus.md) object
Required: No

 ** type **   <a name="elasticloadbalancing-Type-ProxySummary-type"></a>
The type of proxy.
Type: String
Valid Values: `envoy`
Required: No

 ** vpcId **   <a name="elasticloadbalancing-Type-ProxySummary-vpcId"></a>
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_ProxySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxySummary)
