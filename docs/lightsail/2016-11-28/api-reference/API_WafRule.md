---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_WafRule.html
---

# WafRule
<a name="API_WafRule"></a>

Describes a Web Application Firewall (WAF) rule group for a Lightsail distribution. A WAF rule group is a set of rules managed by AWS. The rules inspect viewer requests and block requests that match them.

## Contents
<a name="API_WafRule_Contents"></a>

 ** name **   <a name="Lightsail-Type-WafRule-name"></a>
The name of the WAF rule group (for example, `AWSManagedRulesCommonRuleSet`).
For the WAF rule groups that you can specify for each bundle, see the `wafRules` parameter of the `CreateDistribution` action.
Type: String
Required: Yes

 ** acfpConfig **   <a name="Lightsail-Type-WafRule-acfpConfig"></a>
An object that describes the configuration of the account creation fraud prevention rule group.
Constraints:
+ Define this parameter only when the `name` is `AWSManagedRulesACFPRuleSet`.
+ This parameter is required when the `name` is `AWSManagedRulesACFPRuleSet`.
Type: [WafAcfpConfig](API_WafAcfpConfig.md) object
Required: No

 ** atpConfig **   <a name="Lightsail-Type-WafRule-atpConfig"></a>
An object that describes the configuration of the account takeover prevention rule group.
Constraints:
+ Define this parameter only when the `name` is `AWSManagedRulesATPRuleSet`.
+ This parameter is required when the `name` is `AWSManagedRulesATPRuleSet`.
Type: [WafAtpConfig](API_WafAtpConfig.md) object
Required: No

 ** botControlConfig **   <a name="Lightsail-Type-WafRule-botControlConfig"></a>
An object that describes the configuration of the bot control rule group.
Constraints:
+ Define this parameter only when the `name` is `AWSManagedRulesBotControlRuleSet`.
+ This parameter is required when the `name` is `AWSManagedRulesBotControlRuleSet`.
Type: [WafBotControlConfig](API_WafBotControlConfig.md) object
Required: No

## See Also
<a name="API_WafRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/WafRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/WafRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/WafRule)
