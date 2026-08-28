---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallPolicy.html
---

# NetworkFirewallPolicy
<a name="API_NetworkFirewallPolicy"></a>

Configures the firewall policy deployment model of AWS Network Firewall. For information about Network Firewall deployment models, see [AWS Network Firewall example architectures with routing](https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html) in the *Network Firewall Developer Guide*.

## Contents
<a name="API_NetworkFirewallPolicy_Contents"></a>

 ** FirewallDeploymentModel **   <a name="fms-Type-NetworkFirewallPolicy-FirewallDeploymentModel"></a>
Defines the deployment model to use for the firewall policy. To use a distributed model, set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `NULL`.
Type: String
Valid Values: `CENTRALIZED | DISTRIBUTED`
Required: No

## See Also
<a name="API_NetworkFirewallPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
