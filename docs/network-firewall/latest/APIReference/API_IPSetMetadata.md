---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_IPSetMetadata.html
---

# IPSetMetadata
<a name="API_IPSetMetadata"></a>

General information about the IP set.

## Contents
<a name="API_IPSetMetadata_Contents"></a>

 ** ResolvedCIDRCount **   <a name="networkfirewall-Type-IPSetMetadata-ResolvedCIDRCount"></a>
Describes the total number of CIDR blocks currently in use by the IP set references in a firewall. To determine how many CIDR blocks are available for you to use in a firewall, you can call `AvailableCIDRCount`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

## See Also
<a name="API_IPSetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/IPSetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/IPSetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/IPSetMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
