---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateLoadBalancer.html
---

# CreateLoadBalancer
<a name="API_CreateLoadBalancer"></a>

Creates an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

To create listeners for your load balancer, use [CreateListener](API_CreateListener.md). To describe your current load balancers, see [DescribeLoadBalancers](API_DescribeLoadBalancers.md). When you are finished with a load balancer, you can delete it using [DeleteLoadBalancer](API_DeleteLoadBalancer.md).

For more information, see the following:
+  [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html)
+  [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html)
+  [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html)

This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.

## Request Parameters
<a name="API_CreateLoadBalancer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CustomerOwnedIpv4Pool **
[Application Load Balancers on Outposts] The ID of the customer-owned address pool (CoIP pool).
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(ipv4pool-coip-)[a-zA-Z0-9]+$`
Required: No

 ** EnablePrefixForIpv6SourceNat **
[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be `dualstack`. The default value is `off`.
Type: String
Valid Values: `on | off`
Required: No

 ** IpAddressType **
The IP address type. Internal load balancers must use `ipv4`.
[Application Load Balancers] The possible values are `ipv4` (IPv4 addresses), `dualstack` (IPv4 and IPv6 addresses), and `dualstack-without-public-ipv4` (public IPv6 addresses and private IPv4 and IPv6 addresses).
[Network Load Balancers and Gateway Load Balancers] The possible values are `ipv4` (IPv4 addresses) and `dualstack` (IPv4 and IPv6 addresses).
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`
Required: No

 ** IpamPools **
[Application Load Balancers] The IPAM pools to use with the load balancer.
Type: [IpamPools](API_IpamPools.md) object
Required: No

 ** Name **
The name of the load balancer.
This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with "internal-".
Type: String
Required: Yes

 ** Scheme **
The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.
The default is an Internet-facing load balancer.
You can't specify a scheme for a Gateway Load Balancer.
Type: String
Valid Values: `internet-facing | internal`
Required: No

 **SecurityGroups.member.N**
[Application Load Balancers and Network Load Balancers] The IDs of the security groups for the load balancer.
Type: Array of strings
Required: No

 **SubnetMappings.member.N**
The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.
[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.
[Application Load Balancers on Outposts] You must specify one Outpost subnet.
[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.
[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.
[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You can't specify Elastic IP addresses for your subnets.
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects
Required: No

 **Subnets.member.N**
The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.
[Application Load Balancers] You must specify subnets from at least two Availability Zones.
[Application Load Balancers on Outposts] You must specify one Outpost subnet.
[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.
[Network Load Balancers and Gateway Load Balancers] You can specify subnets from one or more Availability Zones.
Type: Array of strings
Required: No

 **Tags.member.N**
The tags to assign to the load balancer.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Type **
The type of load balancer. The default is `application`.
Type: String
Valid Values: `application | network | gateway`
Required: No

## Response Elements
<a name="API_CreateLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 **LoadBalancers.member.N**
Information about the load balancer.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects

## Errors
<a name="API_CreateLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AllocationIdNotFound **
The specified allocation ID does not exist.
HTTP Status Code: 400

 ** AvailabilityZoneNotSupported **
The specified Availability Zone is not supported.
HTTP Status Code: 400

 ** DuplicateLoadBalancerName **
A load balancer with the specified name already exists.
HTTP Status Code: 400

 ** DuplicateTagKeys **
A tag key was specified more than once.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** InvalidScheme **
The requested scheme is not valid.
HTTP Status Code: 400

 ** InvalidSecurityGroup **
The specified security group does not exist.
HTTP Status Code: 400

 ** InvalidSubnet **
The specified subnet is out of available addresses.
HTTP Status Code: 400

 ** OperationNotPermitted **
This operation is not allowed.
HTTP Status Code: 400

 ** ResourceInUse **
A specified resource is in use.
HTTP Status Code: 400

 ** SubnetNotFound **
The specified subnet does not exist.
HTTP Status Code: 400

 ** TooManyLoadBalancers **
You've reached the limit on the number of load balancers for your AWS account.
HTTP Status Code: 400

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

## Examples
<a name="API_CreateLoadBalancer_Examples"></a>

### Create an Internet-facing load balancer
<a name="API_CreateLoadBalancer_Example_1"></a>

This example creates an Internet-facing load balancer and enables the Availability Zones for the specified subnets.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&Name=my-load-balancer
&Subnets.member.1=subnet-8360a9e7
&Subnets.member.2=subnet-b7d581c0
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoadBalancer_Example_1_Response"></a>

```
<CreateLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <CreateLoadBalancerResult>
    <LoadBalancers>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-internal-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <Scheme>internet-facing</Scheme>
        <LoadBalancerName>my-load-balancer</LoadBalancerName>
        <VpcId>vpc-3ac0fb5f</VpcId>
        <CanonicalHostedZoneId>Z2P70J7EXAMPLE</CanonicalHostedZoneId>
        <CreatedTime>2016-03-25T21:29:48.850Z</CreatedTime>
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
        <SecurityGroups>
          <member>sg-5943793c</member>
        </SecurityGroups>
        <DNSName>my-load-balancer-424835706.us-west-2.elb.amazonaws.com</DNSName>
        <State>
          <Code>provisioning</Code>
        </State>
        <Type>application</Type>
      </member>
    </LoadBalancers>
  </CreateLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>32d531b2-f2d0-11e5-9192-3fff33344cfa</RequestId>
  </ResponseMetadata>
</CreateLoadBalancerResponse>
```

### Create an internal load balancer
<a name="API_CreateLoadBalancer_Example_2"></a>

This example creates an internal load balancer and enables the Availability Zones for the specified subnets.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&Name=my-internal-load-balancer
&Scheme=internal
&Subnets.member.1=subnet-8360a9e7
&Subnets.member.2=subnet-b7d581c0
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoadBalancer_Example_2_Response"></a>

```
<CreateLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <CreateLoadBalancerResult>
    <LoadBalancers>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-internal-load-balancer/5b49b8d4303115c2</LoadBalancerArn>
        <Scheme>internal</Scheme>
        <LoadBalancerName>my-internal-load-balancer</LoadBalancerName>
        <VpcId>vpc-3ac0fb5f</VpcId>
        <CanonicalHostedZoneId>Z2P70J7EXAMPLE</CanonicalHostedZoneId>
        <CreatedTime>2016-03-25T21:29:48.850Z</CreatedTime>
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
        <SecurityGroups>
          <member>sg-5943793c</member>
        </SecurityGroups>
        <DNSName>internal-my-internal-load-balancer-1529930873.us-west-2.elb.amazonaws.com</DNSName>
        <State>
          <Code>provisioning</Code>
        </State>
        <Type>application</Type>
      </member>
    </LoadBalancers>
  </CreateLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>b37b9c3e-f2d0-11e5-a53c-67205c0d10fd</RequestId>
  </ResponseMetadata>
</CreateLoadBalancerResponse>
```

### Create a Network Load Balancer
<a name="API_CreateLoadBalancer_Example_3"></a>

This example creates a Network Load Balancer and associates an Elastic IP address with each of the specified subnets.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&Name=my-network-load-balancer
&Type=network
&SubnetMappings.member.1.SubnetId=subnet-8360a9e7
&SubnetMappings.member.1.AllocationId=eipalloc-5723d13e
&SubnetMappings.member.2.SubnetId=subnet-b7d581c0
&SubnetMappings.member.2.AllocationId=eipalloc-fc5ca095
&Version=2015-12-01
&AUTHPARAMS
```

### Create a Gateway Load Balancer
<a name="API_CreateLoadBalancer_Example_4"></a>

This example creates a Gateway Load Balancer.

#### Sample Request
<a name="API_CreateLoadBalancer_Example_4_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateLoadBalancer
&Name=my-gateway-load-balancer
&Type=gateway
&Subnets.member.1.SubnetId=subnet-066877671789bd71b
&Subnets.member.2.SubnetId=subnet-09ed24a70bc19bbe4
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
