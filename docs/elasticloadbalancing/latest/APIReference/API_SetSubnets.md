---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetSubnets.html
---

# SetSubnets
<a name="API_SetSubnets"></a>

Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer, Network Load Balancer or Gateway Load Balancer. The specified subnets replace the previously enabled subnets.

## Request Parameters
<a name="API_SetSubnets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnablePrefixForIpv6SourceNat **
[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be `dualstack`. The default value is `off`.
Type: String
Valid Values: `on | off`
Required: No

 ** IpAddressType **
The IP address type.
[Application Load Balancers] The possible values are `ipv4` (IPv4 addresses), `dualstack` (IPv4 and IPv6 addresses), and `dualstack-without-public-ipv4` (public IPv6 addresses and private IPv4 and IPv6 addresses).
[Network Load Balancers and Gateway Load Balancers] The possible values are `ipv4` (IPv4 addresses) and `dualstack` (IPv4 and IPv6 addresses).
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`
Required: No

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

 **SubnetMappings.member.N**
The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.
[Application Load Balancers on Outposts] You must specify one Outpost subnet.
[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.
[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.
[Gateway Load Balancers] You can specify subnets from one or more Availability Zones.
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects
Required: No

 **Subnets.member.N**
The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
[Application Load Balancers] You must specify subnets from at least two Availability Zones.
[Application Load Balancers on Outposts] You must specify one Outpost subnet.
[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.
[Network Load Balancers] You can specify subnets from one or more Availability Zones.
[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.
Type: Array of strings
Required: No

## Response Elements
<a name="API_SetSubnets_ResponseElements"></a>

The following elements are returned by the service.

 **AvailabilityZones.member.N**
Information about the subnets.
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects

 ** EnablePrefixForIpv6SourceNat **
[Network Load Balancers] Indicates whether to use an IPv6 prefix from each subnet for source NAT.
Type: String
Valid Values: `on | off`

 ** IpAddressType **
The IP address type.
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`

## Errors
<a name="API_SetSubnets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AllocationIdNotFound **
The specified allocation ID does not exist.
HTTP Status Code: 400

 ** AvailabilityZoneNotSupported **
The specified Availability Zone is not supported.
HTTP Status Code: 400

 ** CapacityReservationPending **
There is a pending capacity reservation.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** InvalidSubnet **
The specified subnet is out of available addresses.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** SubnetNotFound **
The specified subnet does not exist.
HTTP Status Code: 400

## Examples
<a name="API_SetSubnets_Examples"></a>

### Enable Availability Zones for a load balancer
<a name="API_SetSubnets_Example_1"></a>

This example enables the Availability Zone for the specified subnet for the specified load balancer.

#### Sample Request
<a name="API_SetSubnets_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetSubnets
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Subnets.member.1=subnet-8360a9e7
&Subnets.member.2=subnet-b7d581c0
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetSubnets_Example_1_Response"></a>

```
<SetSubnetsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <SetSubnetsResult>
    <AvailabilityZones>
      <member>
        <SubnetId>subnet-8360a9e7</SubnetId>
        <ZoneName>us-west-2a</ZoneName>
      </member>
      <member>
        <SubnetId>subnet-b7d581c0</SubnetId>
        <ZoneName>us-west-2b</ZoneName>
      </member>
    </AvailabilityZones>
  </SetSubnetsResult>
  <ResponseMetadata>
    <RequestId>c1a80803-f3ab-11e5-b673-8d4a8a9e6f48</RequestId>
  </ResponseMetadata>
</SetSubnetsResponse>
```

## See Also
<a name="API_SetSubnets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/SetSubnets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SetSubnets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
