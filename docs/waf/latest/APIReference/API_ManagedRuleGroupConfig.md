---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleGroupConfig.html
---

# ManagedRuleGroupConfig
<a name="API_ManagedRuleGroupConfig"></a>

Additional information that's used by a managed rule group. Many managed rule groups don't require this.

The rule groups used for intelligent threat mitigation require additional configuration:
+ Use the `AWSManagedRulesACFPRuleSet` configuration object to configure the account creation fraud prevention managed rule group. The configuration includes the registration and sign-up pages of your application and the locations in the account creation request payload of data, such as the user email and phone number fields.
+ Use the `AWSManagedRulesAntiDDoSRuleSet` configuration object to configure the anti-DDoS managed rule group. The configuration includes the sensitivity levels to use in the rules that typically block and challenge requests that might be participating in DDoS attacks and the specification to use to indicate whether a request can handle a silent browser challenge.
+ Use the `AWSManagedRulesATPRuleSet` configuration object to configure the account takeover prevention managed rule group. The configuration includes the sign-in page of your application and the locations in the login request payload of data such as the username and password.
+ Use the `AWSManagedRulesBotControlRuleSet` configuration object to configure the protection level that you want the Bot Control rule group to use.

For example specifications, see the examples section of [CreateWebACL](API_CreateWebACL.md).

## Contents
<a name="API_ManagedRuleGroupConfig_Contents"></a>

 ** AWSManagedRulesACFPRuleSet **   <a name="WAF-Type-ManagedRuleGroupConfig-AWSManagedRulesACFPRuleSet"></a>
Additional configuration for using the account creation fraud prevention (ACFP) managed rule group, `AWSManagedRulesACFPRuleSet`. Use this to provide account creation request information to the rule group. For web ACLs that protect CloudFront distributions, use this to also provide the information about how your distribution responds to account creation requests.
For information about using the ACFP managed rule group, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-acfp.html) and [AWS WAF Fraud Control account creation fraud prevention (ACFP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp.html) in the * AWS WAF Developer Guide*.
Type: [AWSManagedRulesACFPRuleSet](API_AWSManagedRulesACFPRuleSet.md) object
Required: No

 ** AWSManagedRulesAntiDDoSRuleSet **   <a name="WAF-Type-ManagedRuleGroupConfig-AWSManagedRulesAntiDDoSRuleSet"></a>
Additional configuration for using the anti-DDoS managed rule group, `AWSManagedRulesAntiDDoSRuleSet`. Use this to configure anti-DDoS behavior for the rule group.
For information about using the anti-DDoS managed rule group, see [AWS WAF Anti-DDoS rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html) and [Distributed Denial of Service (DDoS) prevention](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos.html) in the * AWS WAF Developer Guide*.
Type: [AWSManagedRulesAntiDDoSRuleSet](API_AWSManagedRulesAntiDDoSRuleSet.md) object
Required: No

 ** AWSManagedRulesATPRuleSet **   <a name="WAF-Type-ManagedRuleGroupConfig-AWSManagedRulesATPRuleSet"></a>
Additional configuration for using the account takeover prevention (ATP) managed rule group, `AWSManagedRulesATPRuleSet`. Use this to provide login request information to the rule group. For web ACLs that protect CloudFront distributions, use this to also provide the information about how your distribution responds to login requests.
This configuration replaces the individual configuration fields in `ManagedRuleGroupConfig` and provides additional feature configuration.
For information about using the ATP managed rule group, see [AWS WAF Fraud Control account takeover prevention (ATP) rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-atp.html) and [AWS WAF Fraud Control account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp.html) in the * AWS WAF Developer Guide*.
Type: [AWSManagedRulesATPRuleSet](API_AWSManagedRulesATPRuleSet.md) object
Required: No

 ** AWSManagedRulesBotControlRuleSet **   <a name="WAF-Type-ManagedRuleGroupConfig-AWSManagedRulesBotControlRuleSet"></a>
Additional configuration for using the Bot Control managed rule group. Use this to specify the inspection level that you want to use. For information about using the Bot Control managed rule group, see [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) and [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html) in the * AWS WAF Developer Guide*.
Type: [AWSManagedRulesBotControlRuleSet](API_AWSManagedRulesBotControlRuleSet.md) object
Required: No

 ** LoginPath **   <a name="WAF-Type-ManagedRuleGroupConfig-LoginPath"></a>
 *This member has been deprecated.*
Instead of this setting, provide your configuration under `AWSManagedRulesATPRuleSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** PasswordField **   <a name="WAF-Type-ManagedRuleGroupConfig-PasswordField"></a>
 *This member has been deprecated.*
Instead of this setting, provide your configuration under the request inspection configuration for `AWSManagedRulesATPRuleSet` or `AWSManagedRulesACFPRuleSet`.
Type: [PasswordField](API_PasswordField.md) object
Required: No

 ** PayloadType **   <a name="WAF-Type-ManagedRuleGroupConfig-PayloadType"></a>
 *This member has been deprecated.*
Instead of this setting, provide your configuration under the request inspection configuration for `AWSManagedRulesATPRuleSet` or `AWSManagedRulesACFPRuleSet`.
Type: String
Valid Values: `JSON | FORM_ENCODED`
Required: No

 ** UsernameField **   <a name="WAF-Type-ManagedRuleGroupConfig-UsernameField"></a>
 *This member has been deprecated.*
Instead of this setting, provide your configuration under the request inspection configuration for `AWSManagedRulesATPRuleSet` or `AWSManagedRulesACFPRuleSet`.
Type: [UsernameField](API_UsernameField.md) object
Required: No

## See Also
<a name="API_ManagedRuleGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleGroupConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleGroupConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleGroupConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
