---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SourceIpConditionConfig.html
---

# SourceIpConditionConfig
<a name="API_SourceIpConditionConfig"></a>

Information about a source IP condition.

You can use this condition to route based on the IP address of the source that connects to the load balancer. If a client is behind a proxy, this is the IP address of the proxy not the IP address of the client.

For Application Load Balancers, use `Values` to specify CIDR ranges. For Network Load Balancers, use `IpAddressType` to match on the IP address type of the source traffic.

## Contents
<a name="API_SourceIpConditionConfig_Contents"></a>

 ** IpAddressType **
The IP address type for Network Load Balancers.
The valid values are:
+  `ipv4` – IPv4 addresses only.
+  `ipv6` – IPv6 addresses only.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** Values.member.N **
The source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.
If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use an [HTTP header condition](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#http-header-conditions).
The total number of values must be less than, or equal to five.
Type: Array of strings
Required: No

## See Also
<a name="API_SourceIpConditionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SourceIpConditionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SourceIpConditionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SourceIpConditionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
