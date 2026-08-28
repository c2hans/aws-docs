---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_WebACL.html
---

# WebACL
<a name="API_WebACL"></a>

 A web ACL defines a collection of rules to use to inspect and control web requests. Each rule has a statement that defines what to look for in web requests and an action that AWS WAF applies to requests that match the statement. In the web ACL, you assign a default action to take (allow, block) for any request that does not match any of the rules. The rules in a web ACL can be a combination of the types [Rule](API_Rule.md), [RuleGroup](API_RuleGroup.md), and managed rule group. You can associate a web ACL with one or more AWS resources to protect. The resource types include Amazon CloudFront distribution, Amazon API Gateway REST API, Application Load Balancer, AWS AppSync GraphQL API, Amazon Cognito user pool, AWS App Runner service, AWS Amplify application, AWS Verified Access instance, and Amazon Bedrock AgentCore Gateway.

## Contents
<a name="API_WebACL_Contents"></a>

 ** ARN **   <a name="WAF-Type-WebACL-ARN"></a>
The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** DefaultAction **   <a name="WAF-Type-WebACL-DefaultAction"></a>
The action to perform if none of the `Rules` contained in the `WebACL` match.
Type: [DefaultAction](API_DefaultAction.md) object
Required: Yes

 ** Id **   <a name="WAF-Type-WebACL-Id"></a>
A unique identifier for the `WebACL`. This ID is returned in the responses to create and list commands. You use this ID to do things like get, update, and delete a `WebACL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** Name **   <a name="WAF-Type-WebACL-Name"></a>
The name of the web ACL. You cannot change the name of a web ACL after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** VisibilityConfig **   <a name="WAF-Type-WebACL-VisibilityConfig"></a>
Defines and enables Amazon CloudWatch metrics and web request sample collection.
Type: [VisibilityConfig](API_VisibilityConfig.md) object
Required: Yes

 ** ApplicationConfig **   <a name="WAF-Type-WebACL-ApplicationConfig"></a>
Returns a list of `ApplicationAttribute`s.
Type: [ApplicationConfig](API_ApplicationConfig.md) object
Required: No

 ** AssociationConfig **   <a name="WAF-Type-WebACL-AssociationConfig"></a>
Specifies custom configurations for the associations between the web ACL and protected resources.
Use this to customize the maximum size of the request body that your protected resources forward to AWS WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes).
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](http://aws.amazon.com/waf/pricing/).
For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
Type: [AssociationConfig](API_AssociationConfig.md) object
Required: No

 ** Capacity **   <a name="WAF-Type-WebACL-Capacity"></a>
The web ACL capacity units (WCUs) currently being used by this web ACL.
 AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [AWS WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the * AWS WAF Developer Guide*.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** CaptchaConfig **   <a name="WAF-Type-WebACL-CaptchaConfig"></a>
Specifies how AWS WAF should handle `CAPTCHA` evaluations for rules that don't have their own `CaptchaConfig` settings. If you don't specify this, AWS WAF uses its default settings for `CaptchaConfig`.
Type: [CaptchaConfig](API_CaptchaConfig.md) object
Required: No

 ** ChallengeConfig **   <a name="WAF-Type-WebACL-ChallengeConfig"></a>
Specifies how AWS WAF should handle challenge evaluations for rules that don't have their own `ChallengeConfig` settings. If you don't specify this, AWS WAF uses its default settings for `ChallengeConfig`.
Type: [ChallengeConfig](API_ChallengeConfig.md) object
Required: No

 ** CustomResponseBodies **   <a name="WAF-Type-WebACL-CustomResponseBodies"></a>
A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: String to [CustomResponseBody](API_CustomResponseBody.md) object map
Map Entries: Maximum number of items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[\w\-]+$`
Required: No

 ** DataProtectionConfig **   <a name="WAF-Type-WebACL-DataProtectionConfig"></a>
Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option.
The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your AWS WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging.
Type: [DataProtectionConfig](API_DataProtectionConfig.md) object
Required: No

 ** Description **   <a name="WAF-Type-WebACL-Description"></a>
A description of the web ACL that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** LabelNamespace **   <a name="WAF-Type-WebACL-LabelNamespace"></a>
The label namespace prefix for this web ACL. All labels added by rules in this web ACL have this prefix.
+ The syntax for the label namespace prefix for a web ACL is the following:

   `awswaf:<account ID>:webacl:<web ACL name>:`
+ When a rule with a label matches a web request, AWS WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon:

   `<label namespace>:<label from rule>`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

 ** ManagedByFirewallManager **   <a name="WAF-Type-WebACL-ManagedByFirewallManager"></a>
Indicates whether this web ACL was created by AWS Firewall Manager and is being managed by Firewall Manager. If true, then only Firewall Manager can delete the web ACL or any Firewall Manager rule groups in the web ACL. See also the properties `RetrofittedByFirewallManager`, `PreProcessFirewallManagerRuleGroups`, and `PostProcessFirewallManagerRuleGroups`.
Type: Boolean
Required: No

 ** MonetizationConfig **   <a name="WAF-Type-WebACL-MonetizationConfig"></a>
The monetization configuration for the web ACL. Required when any rule in the web ACL uses the `Monetize` action. Specifies the cryptocurrency payment networks and currency mode for AI bot monetization.
Type: [MonetizationConfig](API_MonetizationConfig.md) object
Required: No

 ** OnSourceDDoSProtectionConfig **   <a name="WAF-Type-WebACL-OnSourceDDoSProtectionConfig"></a>
Configures the level of DDoS protection that applies to web ACLs associated with Application Load Balancers.
Type: [OnSourceDDoSProtectionConfig](API_OnSourceDDoSProtectionConfig.md) object
Required: No

 ** PostProcessFirewallManagerRuleGroups **   <a name="WAF-Type-WebACL-PostProcessFirewallManagerRuleGroups"></a>
The last set of rules for AWS WAF to process in the web ACL. This is defined in an AWS Firewall Manager AWS WAF policy and contains only rule group references. You can't alter these. Any rules and rule groups that you define for the web ACL are prioritized before these.
In the Firewall Manager AWS WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.
Type: Array of [FirewallManagerRuleGroup](API_FirewallManagerRuleGroup.md) objects
Required: No

 ** PreProcessFirewallManagerRuleGroups **   <a name="WAF-Type-WebACL-PreProcessFirewallManagerRuleGroups"></a>
The first set of rules for AWS WAF to process in the web ACL. This is defined in an AWS Firewall Manager AWS WAF policy and contains only rule group references. You can't alter these. Any rules and rule groups that you define for the web ACL are prioritized after these.
In the Firewall Manager AWS WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.
Type: Array of [FirewallManagerRuleGroup](API_FirewallManagerRuleGroup.md) objects
Required: No

 ** RetrofittedByFirewallManager **   <a name="WAF-Type-WebACL-RetrofittedByFirewallManager"></a>
Indicates whether this web ACL was created by a customer account and then retrofitted by AWS Firewall Manager. If true, then the web ACL is currently being managed by a Firewall Manager AWS WAF policy, and only Firewall Manager can manage any Firewall Manager rule groups in the web ACL. See also the properties `ManagedByFirewallManager`, `PreProcessFirewallManagerRuleGroups`, and `PostProcessFirewallManagerRuleGroups`.
Type: Boolean
Required: No

 ** Rules **   <a name="WAF-Type-WebACL-Rules"></a>
The [Rule](API_Rule.md) statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.
Type: Array of [Rule](API_Rule.md) objects
Required: No

 ** TokenDomains **   <a name="WAF-Type-WebACL-TokenDomains"></a>
Specifies the domains that AWS WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When AWS WAF provides a token, it uses the domain of the AWS resource that the web ACL is protecting. If you don't specify a list of token domains, AWS WAF accepts tokens only for the domain of the protected resource. With a token domain list, AWS WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `^[\w\.\-/]+$`
Required: No

## See Also
<a name="API_WebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/WebACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/WebACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/WebACL)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
