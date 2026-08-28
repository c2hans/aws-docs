---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_FMSPolicyUpdateFirewallCreationConfigAction.html
---

# FMSPolicyUpdateFirewallCreationConfigAction
<a name="API_FMSPolicyUpdateFirewallCreationConfigAction"></a>

Contains information about the actions that you can take to remediate scope violations caused by your policy's `FirewallCreationConfig`. `FirewallCreationConfig` is an optional configuration that you can use to choose which Availability Zones Firewall Manager creates Network Firewall endpoints in.

## Contents
<a name="API_FMSPolicyUpdateFirewallCreationConfigAction_Contents"></a>

 ** Description **   <a name="fms-Type-FMSPolicyUpdateFirewallCreationConfigAction-Description"></a>
Describes the remedial action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FirewallCreationConfig **   <a name="fms-Type-FMSPolicyUpdateFirewallCreationConfigAction-FirewallCreationConfig"></a>
A `FirewallCreationConfig` that you can copy into your current policy's [SecurityServiceData](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html) in order to remedy scope violations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30000.
Pattern: `^((?!\\[nr]).)+`
Required: No

## See Also
<a name="API_FMSPolicyUpdateFirewallCreationConfigAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/FMSPolicyUpdateFirewallCreationConfigAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/FMSPolicyUpdateFirewallCreationConfigAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/FMSPolicyUpdateFirewallCreationConfigAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
