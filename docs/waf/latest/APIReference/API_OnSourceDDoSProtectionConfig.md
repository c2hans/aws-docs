---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_OnSourceDDoSProtectionConfig.html
---

# OnSourceDDoSProtectionConfig
<a name="API_OnSourceDDoSProtectionConfig"></a>

Configures the level of DDoS protection that applies to web ACLs associated with Application Load Balancers.

## Contents
<a name="API_OnSourceDDoSProtectionConfig_Contents"></a>

 ** ALBLowReputationMode **   <a name="WAF-Type-OnSourceDDoSProtectionConfig-ALBLowReputationMode"></a>
The level of DDoS protection that applies to web ACLs associated with Application Load Balancers. `ACTIVE_UNDER_DDOS` protection is enabled by default whenever a web ACL is associated with an Application Load Balancer. In the event that an Application Load Balancer experiences high-load conditions or suspected DDoS attacks, the `ACTIVE_UNDER_DDOS` protection automatically rate limits traffic from known low reputation sources without disrupting Application Load Balancer availability. `ALWAYS_ON` protection provides constant, always-on monitoring of known low reputation sources for suspected DDoS attacks. While this provides a higher level of protection, there may be potential impacts on legitimate traffic.
Type: String
Valid Values: `ACTIVE_UNDER_DDOS | ALWAYS_ON`
Required: Yes

## See Also
<a name="API_OnSourceDDoSProtectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/OnSourceDDoSProtectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/OnSourceDDoSProtectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/OnSourceDDoSProtectionConfig)
