---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_PortRange.html
---

# PortRange
<a name="API_PortRange"></a>

A single port range specification. This is used for source and destination port ranges in the stateless rule [MatchAttributes](API_MatchAttributes.md), `SourcePorts`, and `DestinationPorts` settings.

## Contents
<a name="API_PortRange_Contents"></a>

 ** FromPort **   <a name="networkfirewall-Type-PortRange-FromPort"></a>
The lower limit of the port range. This must be less than or equal to the `ToPort` specification.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: Yes

 ** ToPort **   <a name="networkfirewall-Type-PortRange-ToPort"></a>
The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: Yes

## See Also
<a name="API_PortRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/PortRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/PortRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/PortRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
