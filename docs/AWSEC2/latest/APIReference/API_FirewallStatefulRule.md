---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FirewallStatefulRule.html
---

# FirewallStatefulRule
<a name="API_FirewallStatefulRule"></a>

Describes a stateful rule.

## Contents
<a name="API_FirewallStatefulRule_Contents"></a>

 ** DestinationPortSet.N **
The destination ports.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

 ** DestinationSet.N **
The destination IP addresses, in CIDR notation.
Type: Array of strings
Required: No

 ** direction **
The direction. The possible values are `FORWARD` and `ANY`.
Type: String
Required: No

 ** protocol **
The protocol.
Type: String
Required: No

 ** ruleAction **
The rule action. The possible values are `pass`, `drop`, and `alert`.
Type: String
Required: No

 ** ruleGroupArn **
The ARN of the stateful rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** SourcePortSet.N **
The source ports.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

 ** SourceSet.N **
The source IP addresses, in CIDR notation.
Type: Array of strings
Required: No

## See Also
<a name="API_FirewallStatefulRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FirewallStatefulRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FirewallStatefulRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FirewallStatefulRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
