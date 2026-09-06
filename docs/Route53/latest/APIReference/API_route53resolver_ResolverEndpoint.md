---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverEndpoint.html
---

# ResolverEndpoint
<a name="API_route53resolver_ResolverEndpoint"></a>

In the response to a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html), [DeleteResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverEndpoint.html), [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html), Updates the name, or ResolverEndpointType for an endpoint, or [UpdateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html) request, a complex type that contains settings for an existing inbound or outbound Resolver endpoint.

## Contents
<a name="API_route53resolver_ResolverEndpoint_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Arn"></a>
The ARN (Amazon Resource Name) for the Resolver endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-CreationTime"></a>
The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-CreatorRequestId"></a>
A unique string that identifies the request that created the Resolver endpoint. The `CreatorRequestId` allows failed requests to be retried without the risk of running the operation twice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Direction **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Direction"></a>
Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:
+  `INBOUND`: allows DNS queries to your VPC from your network
+  `OUTBOUND`: allows DNS queries from your VPC to your network
+  `INBOUND_DELEGATION`: Resolver delegates queries to Route 53 private hosted zones from your network.
Type: String
Valid Values: `INBOUND | OUTBOUND | INBOUND_DELEGATION`
Required: No

 ** Dns64Enabled **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Dns64Enabled"></a>
Indicates whether DNS64 is enabled for the inbound Resolver endpoint. When `true`, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the `64:ff9b::/96` prefix to the IPv4 address.
Type: Boolean
Required: No

 ** HostVPCId **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-HostVPCId"></a>
The ID of the VPC that you want to create the Resolver endpoint in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Id"></a>
The ID of the Resolver endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** IpAddressCount **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-IpAddressCount"></a>
The number of IP addresses that the Resolver endpoint can use for DNS queries.
Type: Integer
Required: No

 ** Ipv6InternetAccessEnabled **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Ipv6InternetAccessEnabled"></a>
Indicates whether IPv6 internet access is enabled for the outbound Resolver endpoint. When `true`, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway.
Type: Boolean
Required: No

 ** ModificationTime **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-ModificationTime"></a>
The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Name"></a>
The name that you assigned to the Resolver endpoint when you submitted a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OutpostArn **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-OutpostArn"></a>
The ARN (Amazon Resource Name) for the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** PreferredInstanceType **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-PreferredInstanceType"></a>
 The Amazon EC2 instance type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Protocols **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Protocols"></a>
 Protocols used for the endpoint. DoH-FIPS is applicable for a default inbound endpoints only.
For an inbound endpoint you can apply the protocols as follows:
+  Do53 and DoH in combination.
+ Do53 and DoH-FIPS in combination.
+ Do53 alone.
+ DoH alone.
+ DoH-FIPS alone.
+ None, which is treated as Do53.
For a delegation inbound endpoint you can use Do53 only.
For an outbound endpoint you can apply the protocols as follows:
+  Do53 and DoH in combination.
+ Do53 alone.
+ DoH alone.
+ None, which is treated as Do53.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `DoH | Do53 | DoH-FIPS`
Required: No

 ** ResolverEndpointType **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-ResolverEndpointType"></a>
 The Resolver endpoint IP address type.
Type: String
Valid Values: `IPV6 | IPV4 | DUALSTACK`
Required: No

 ** RniEnhancedMetricsEnabled **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-RniEnhancedMetricsEnabled"></a>
Indicates whether RNI enhanced metrics are enabled for the Resolver endpoint. When enabled, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When disabled, these metrics are not published.
Type: Boolean
Required: No

 ** SecurityGroupIds **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-SecurityGroupIds"></a>
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-Status"></a>
A code that specifies the current status of the Resolver endpoint. Valid values include the following:
+  `CREATING`: Resolver is creating and configuring one or more Amazon VPC network interfaces for this endpoint.
+  `OPERATIONAL`: The Amazon VPC network interfaces for this endpoint are correctly configured and able to pass inbound or outbound DNS queries between your network and Resolver.
+  `UPDATING`: Resolver is associating or disassociating one or more network interfaces with this endpoint.
+  `AUTO_RECOVERING`: Resolver is trying to recover one or more of the network interfaces that are associated with this endpoint. During the recovery process, the endpoint functions with limited capacity because of the limit on the number of DNS queries per IP address (per network interface). For the current limit, see [Limits on Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-resolver).
+  `ACTION_NEEDED`: This endpoint is unhealthy, and Resolver can't automatically recover it. To resolve the problem, we recommend that you check each IP address that you associated with the endpoint. For each IP address that isn't available, add another IP address and then delete the IP address that isn't available. (An endpoint must always include at least two IP addresses.) A status of `ACTION_NEEDED` can have a variety of causes. Here are two common causes:
  + One or more of the network interfaces that are associated with the endpoint were deleted using Amazon VPC.
  + The network interface couldn't be created for some reason that's outside the control of Resolver.
+  `DELETING`: Resolver is deleting this endpoint and the associated network interfaces.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | AUTO_RECOVERING | ACTION_NEEDED | DELETING`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-StatusMessage"></a>
A detailed description of the status of the Resolver endpoint.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** TargetNameServerMetricsEnabled **   <a name="Route53Resolver-Type-route53resolver_ResolverEndpoint-TargetNameServerMetricsEnabled"></a>
Indicates whether target name server metrics are enabled for the outbound Resolver endpoint. When enabled, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When disabled, these metrics are not published. This feature is not supported for inbound Resolver endpoint.
Type: Boolean
Required: No

## See Also
<a name="API_route53resolver_ResolverEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverEndpoint)
