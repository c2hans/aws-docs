---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FlowFilter.html
---

# FlowFilter
<a name="API_FlowFilter"></a>

Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.

## Contents
<a name="API_FlowFilter_Contents"></a>

 ** DestinationAddress **   <a name="networkfirewall-Type-FlowFilter-DestinationAddress"></a>
A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.
Type: [Address](API_Address.md) object
Required: No

 ** DestinationPort **   <a name="networkfirewall-Type-FlowFilter-DestinationPort"></a>
The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

 ** Protocols **   <a name="networkfirewall-Type-FlowFilter-Protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `^.*$`
Required: No

 ** SourceAddress **   <a name="networkfirewall-Type-FlowFilter-SourceAddress"></a>
A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.
Type: [Address](API_Address.md) object
Required: No

 ** SourcePort **   <a name="networkfirewall-Type-FlowFilter-SourcePort"></a>
The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

## See Also
<a name="API_FlowFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FlowFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FlowFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FlowFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
