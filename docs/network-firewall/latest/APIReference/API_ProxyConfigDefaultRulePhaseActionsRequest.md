---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ProxyConfigDefaultRulePhaseActionsRequest.html
---

# ProxyConfigDefaultRulePhaseActionsRequest
<a name="API_ProxyConfigDefaultRulePhaseActionsRequest"></a>

Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied.

This data type is used specifically for the [CreateProxyConfiguration](API_CreateProxyConfiguration.md) and [UpdateProxyConfiguration](API_UpdateProxyConfiguration.md) APIs.

## Contents
<a name="API_ProxyConfigDefaultRulePhaseActionsRequest_Contents"></a>

 ** PostRESPONSE **   <a name="networkfirewall-Type-ProxyConfigDefaultRulePhaseActionsRequest-PostRESPONSE"></a>
After receiving response.
Type: String
Valid Values: `ALLOW | DENY | ALERT`
Required: No

 ** PreDNS **   <a name="networkfirewall-Type-ProxyConfigDefaultRulePhaseActionsRequest-PreDNS"></a>
Before domain resolution.
Type: String
Valid Values: `ALLOW | DENY | ALERT`
Required: No

 ** PreREQUEST **   <a name="networkfirewall-Type-ProxyConfigDefaultRulePhaseActionsRequest-PreREQUEST"></a>
After DNS, before request.
Type: String
Valid Values: `ALLOW | DENY | ALERT`
Required: No

## See Also
<a name="API_ProxyConfigDefaultRulePhaseActionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxyConfigDefaultRulePhaseActionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxyConfigDefaultRulePhaseActionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxyConfigDefaultRulePhaseActionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
