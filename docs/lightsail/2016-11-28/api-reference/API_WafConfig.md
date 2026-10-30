---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_WafConfig.html
---

# WafConfig
<a name="API_WafConfig"></a>

Describes the Web Application Firewall (WAF) configuration of a Lightsail distribution.

## Contents
<a name="API_WafConfig_Contents"></a>

 ** isWafEnabled **   <a name="Lightsail-Type-WafConfig-isWafEnabled"></a>
Specifies whether WAF is enabled for the distribution.
Type: Boolean
Required: No

 ** wafRules **   <a name="Lightsail-Type-WafConfig-wafRules"></a>
An array of objects that describe the WAF rule groups enabled for the distribution.
Type: Array of [WafRule](API_WafRule.md) objects
Required: No

## See Also
<a name="API_WafConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/WafConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/WafConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/WafConfig)
