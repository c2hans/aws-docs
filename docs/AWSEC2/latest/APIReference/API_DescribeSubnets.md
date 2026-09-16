---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html
---

# DescribeSubnets
<a name="API_DescribeSubnets"></a>

Describes your subnets. The default is to describe all your subnets. Alternatively, you can specify specific subnet IDs or filter the results to include only the subnets that match specific criteria.

For more information, see [Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_DescribeSubnets_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone` - The Availability Zone for the subnet. You can also use `availabilityZone` as the filter name.
+  `availability-zone-id` - The ID of the Availability Zone for the subnet. You can also use `availabilityZoneId` as the filter name.
+  `available-ip-address-count` - The number of IPv4 addresses in the subnet that are available.
+  `cidr-block` - The IPv4 CIDR block of the subnet. The CIDR block you specify must exactly match the subnet's CIDR block for information to be returned for the subnet. You can also use `cidr` or `cidrBlock` as the filter names.
+  `customer-owned-ipv4-pool` - The customer-owned IPv4 address pool associated with the subnet.
+  `default-for-az` - Indicates whether this is the default subnet for the Availability Zone (`true` \| `false`). You can also use `defaultForAz` as the filter name.
+  `enable-dns64` - Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.
+  `enable-lni-at-device-index` - Indicates the device position for local network interfaces in this subnet. For example, `1` indicates local network interfaces in this subnet are the secondary network interface (eth1).
+  `ipv6-cidr-block-association.ipv6-cidr-block` - An IPv6 CIDR block associated with the subnet.
+  `ipv6-cidr-block-association.association-id` - An association ID for an IPv6 CIDR block associated with the subnet.
+  `ipv6-cidr-block-association.state` - The state of an IPv6 CIDR block associated with the subnet.
+  `ipv6-native` - Indicates whether this is an IPv6 only subnet (`true` \| `false`).
+  `map-customer-owned-ip-on-launch` - Indicates whether a network interface created in this subnet (including a network interface created by [RunInstances](API_RunInstances.md)) receives a customer-owned IPv4 address.
+  `map-public-ip-on-launch` - Indicates whether instances launched in this subnet receive a public IPv4 address.
+  `outpost-arn` - The Amazon Resource Name (ARN) of the Outpost.
+  `owner-id` - The ID of the AWS account that owns the subnet.
+  `private-dns-name-options-on-launch.hostname-type` - The type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnets, an instance DNS name can be based on the instance IPv4 address (ip-name) or the instance ID (resource-name). For IPv6 only subnets, an instance DNS name must be based on the instance ID (resource-name).
+  `private-dns-name-options-on-launch.enable-resource-name-dns-a-record` - Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
+  `private-dns-name-options-on-launch.enable-resource-name-dns-aaaa-record` - Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
+  `state` - The state of the subnet (`pending` \| `available`).
+  `subnet-arn` - The Amazon Resource Name (ARN) of the subnet.
+  `subnet-id` - The ID of the subnet.
+  `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `vpc-id` - The ID of the VPC for the subnet.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **SubnetId.N**
The IDs of the subnets.
Default: Describes all your subnets.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeSubnets_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **subnetSet**
Information about the subnets.
Type: Array of [Subnet](API_Subnet.md) objects

## Errors
<a name="API_DescribeSubnets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSubnets_Examples"></a>

### Example 1
<a name="API_DescribeSubnets_Example_1"></a>

This example describes the subnets.

#### Sample Request
<a name="API_DescribeSubnets_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSubnets
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSubnets_Example_1_Response"></a>

```
<DescribeSubnetsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1927e20c-0ed0-4a02-a6d7-d955fbd2d13c</requestId>
    <subnetSet>
        <item>
            <subnetId>subnet-0bb1c79de301436ee</subnetId>
            <subnetArn>arn:aws:ec2:us-east-2:111122223333:subnet/subnet-0bb1c79de3EXAMPLE</subnetArn>
            <state>available</state>
            <ownerId>111122223333</ownerId>
            <vpcId>vpc-0ee975135dEXAMPLE</vpcId>
            <cidrBlock>10.0.2.0/24</cidrBlock>
            <ipv6CidrBlockAssociationSet/>
            <availableIpAddressCount>251</availableIpAddressCount>
            <availabilityZone>us-east-2c</availabilityZone>
            <availabilityZoneId>use2-az3</availabilityZoneId>
            <defaultForAz>false</defaultForAz>
            <mapPublicIpOnLaunch>false</mapPublicIpOnLaunch>
            <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation>
        </item>
        <item>
            <subnetId>subnet-02bf4c428bf44ebce</subnetId>
            <subnetArn>arn:aws:ec2:us-east-2:111122223333:subnet/subnet-02bf4c428bEXAMPLE</subnetArn>
            <state>available</state>
            <ownerId>111122223333</ownerId>
            <vpcId>vpc-07e8ffd50fEXAMPLE</vpcId>
            <cidrBlock>10.0.0.0/24</cidrBlock>
            <ipv6CidrBlockAssociationSet>
                <item>
                    <ipv6CidrBlock>2600:1f16:115:200::/64</ipv6CidrBlock>
                    <associationId>subnet-cidr-assoc-002afb9f3cEXAMPLE</associationId>
                    <ipv6CidrBlockState>
                        <state>associated</state>
                    </ipv6CidrBlockState>
                </item>
            </ipv6CidrBlockAssociationSet>
            <availableIpAddressCount>251</availableIpAddressCount>
            <availabilityZone>us-east-2b</availabilityZone>
            <availabilityZoneId>use2-az2</availabilityZoneId>
            <defaultForAz>false</defaultForAz>
            <mapPublicIpOnLaunch>false</mapPublicIpOnLaunch>
            <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation>
        </item>
    </subnetSet>
</DescribeSubnetsResponse>
```

### Example 2
<a name="API_DescribeSubnets_Example_2"></a>

This example uses filters to describe any subnet you own that is in the VPC with the ID `vpc-0056ae9ffdEXAMPLE` or `vpc-0096ae9ffdEXAMPLE`, and whose state is `available`.

#### Sample Request
<a name="API_DescribeSubnets_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSubnets
&Filter.1.Name=vpc-id
&Filter.1.Value.1=vpc-0056ae9ffdEXAMPLE
&Filter.1.Value.2=vpc-0096ae9ffdEXAMPLE
&Filter.2.Name=state
&Filter.2.Value.1=available
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSubnets_Example_2_Response"></a>

```
<DescribeSubnetsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>43e9cb52-0e10-40fe-b457-988c8fbfea26</requestId>
    <subnetSet>
        <item>
            <subnetId>subnet-0f8c6c2f37EXAMPLE</subnetId>
            <subnetArn>arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0f8c6c2f37903e9dc</subnetArn>
            <state>available</state>
            <ownerId>123456789012</ownerId>
            <vpcId>vpc-0056ae9ffdEXAMPLE</vpcId>
            <cidrBlock>172.168.0.0/16</cidrBlock>
            <ipv6CidrBlockAssociationSet/>
            <availableIpAddressCount>65531</availableIpAddressCount>
            <availabilityZone>us-west-2b</availabilityZone>
            <availabilityZoneId>usw2-az2</availabilityZoneId>
            <defaultForAz>false</defaultForAz>
            <mapPublicIpOnLaunch>false</mapPublicIpOnLaunch>
            <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation>
        </item>
    </subnetSet>
</DescribeSubnetsResponse>
```

## See Also
<a name="API_DescribeSubnets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSubnets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSubnets)
