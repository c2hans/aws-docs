---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_TargetAddress.html
---

# TargetAddress
<a name="API_route53resolver_TargetAddress"></a>

In a [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html) request, an array of the IPs that you want to forward DNS queries to.

## Contents
<a name="API_route53resolver_TargetAddress_Contents"></a>

 ** Ip **   <a name="Route53Resolver-Type-route53resolver_TargetAddress-Ip"></a>
One IPv4 address that you want to forward DNS queries to.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 36.
Required: No

 ** Ipv6 **   <a name="Route53Resolver-Type-route53resolver_TargetAddress-Ipv6"></a>
 One IPv6 address that you want to forward DNS queries to.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 39.
Required: No

 ** Port **   <a name="Route53Resolver-Type-route53resolver_TargetAddress-Port"></a>
The port at `Ip` that you want to forward DNS queries to.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** Protocol **   <a name="Route53Resolver-Type-route53resolver_TargetAddress-Protocol"></a>
 The protocols for the target address. The protocol you choose needs to be supported by the outbound endpoint of the Resolver rule.
Type: String
Valid Values: `DoH | Do53 | DoH-FIPS`
Required: No

 ** ServerNameIndication **   <a name="Route53Resolver-Type-route53resolver_TargetAddress-ServerNameIndication"></a>
 The Server Name Indication of the DoH server that you want to forward queries to. This is only used if the Protocol of the `TargetAddress` is `DoH`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_route53resolver_TargetAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/TargetAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/TargetAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/TargetAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
