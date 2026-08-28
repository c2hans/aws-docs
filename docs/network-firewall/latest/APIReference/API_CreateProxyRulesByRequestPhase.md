---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateProxyRulesByRequestPhase.html
---

# CreateProxyRulesByRequestPhase
<a name="API_CreateProxyRulesByRequestPhase"></a>

Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied.

This data type is used specifically for the [CreateProxyRules](API_CreateProxyRules.md) API.

Pre-DNS - before domain resolution.

Pre-Request - after DNS, before request.

Post-Response - after receiving response.

## Contents
<a name="API_CreateProxyRulesByRequestPhase_Contents"></a>

 ** PostRESPONSE **   <a name="networkfirewall-Type-CreateProxyRulesByRequestPhase-PostRESPONSE"></a>
After receiving response.
Type: Array of [CreateProxyRule](API_CreateProxyRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** PreDNS **   <a name="networkfirewall-Type-CreateProxyRulesByRequestPhase-PreDNS"></a>
Before domain resolution.
Type: Array of [CreateProxyRule](API_CreateProxyRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** PreREQUEST **   <a name="networkfirewall-Type-CreateProxyRulesByRequestPhase-PreREQUEST"></a>
After DNS, before request.
Type: Array of [CreateProxyRule](API_CreateProxyRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_CreateProxyRulesByRequestPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateProxyRulesByRequestPhase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateProxyRulesByRequestPhase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateProxyRulesByRequestPhase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
