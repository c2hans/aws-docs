---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressResponse.html
---

# IpAddressResponse
<a name="API_route53resolver_IpAddressResponse"></a>

In the response to a [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html) request, information about the IP addresses that the Resolver endpoint uses for DNS queries.

## Contents
<a name="API_route53resolver_IpAddressResponse_Contents"></a>

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-CreationTime"></a>
The date and time that the IP address was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Ip **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-Ip"></a>
One IPv4 address that the Resolver endpoint uses for DNS queries.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 36.
Required: No

 ** IpId **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-IpId"></a>
The ID of one IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Ipv6 **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-Ipv6"></a>
 One IPv6 address that the Resolver endpoint uses for DNS queries.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 39.
Required: No

 ** ModificationTime **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-ModificationTime"></a>
The date and time that the IP address was last modified, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-Status"></a>
A status code that gives the current status of the request.
Type: String
Valid Values: `CREATING | FAILED_CREATION | FAILED_CREATION_INSUFFICIENT_EC2_CAPACITY_IN_OUTPOST | ATTACHING | ATTACHED | REMAP_DETACHING | REMAP_ATTACHING | DETACHING | FAILED_RESOURCE_GONE | DELETING | DELETE_FAILED_FAS_EXPIRED | UPDATING | UPDATE_FAILED | ISOLATED`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-StatusMessage"></a>
A message that provides additional information about the status of the request.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** SubnetId **   <a name="Route53Resolver-Type-route53resolver_IpAddressResponse-SubnetId"></a>
The ID of one subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

## See Also
<a name="API_route53resolver_IpAddressResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/IpAddressResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/IpAddressResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/IpAddressResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
