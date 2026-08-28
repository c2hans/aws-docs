---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html
---

# DescribeNetworkInterfaces
<a name="API_DescribeNetworkInterfaces"></a>

Describes the specified network interfaces or all your network interfaces.

If you have a large number of network interfaces, the operation fails unless you use pagination or one of the following filters: `group-id`, `mac-address`, `private-dns-name`, `private-ip-address`, `subnet-id`, or `vpc-id`.

**Important**
We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

## Request Parameters
<a name="API_DescribeNetworkInterfaces_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `association.allocation-id` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface.
+  `association.association-id` - The association ID returned when the network interface was associated with an IPv4 address.
+  `addresses.association.owner-id` - The owner ID of the addresses associated with the network interface.
+  `addresses.association.public-ip` - The association ID returned when the network interface was associated with the Elastic IP address (IPv4).
+  `addresses.primary` - Whether the private IPv4 address is the primary IP address associated with the network interface.
+  `addresses.private-ip-address` - The private IPv4 addresses associated with the network interface.
+  `association.ip-owner-id` - The owner of the Elastic IP address (IPv4) associated with the network interface.
+  `association.public-ip` - The address of the Elastic IP address (IPv4) bound to the network interface.
+  `association.public-dns-name` - The public DNS name for the network interface (IPv4).
+  `attachment.attach-time` - The time that the network interface was attached to an instance.
+  `attachment.attachment-id` - The ID of the interface attachment.
+  `attachment.delete-on-termination` - Indicates whether the attachment is deleted when an instance is terminated.
+  `attachment.device-index` - The device index to which the network interface is attached.
+  `attachment.instance-id` - The ID of the instance to which the network interface is attached.
+  `attachment.instance-owner-id` - The owner ID of the instance to which the network interface is attached.
+  `attachment.status` - The status of the attachment (`attaching` \| `attached` \| `detaching` \| `detached`).
+  `availability-zone` - The Availability Zone of the network interface.
+  `availability-zone-id` - The ID of the Availability Zone of the network interface.
+  `description` - The description of the network interface.
+  `group-id` - The ID of a security group associated with the network interface.
+  `ipv6-addresses.ipv6-address` - An IPv6 address associated with the network interface.
+  `interface-type` - The type of network interface (`api_gateway_managed` \| `aws_codestar_connections_managed` \| `branch` \| `ec2_instance_connect_endpoint` \| `efa` \| `efa-only` \| `efs` \| `evs` \| `gateway_load_balancer` \| `gateway_load_balancer_endpoint` \| `global_accelerator_managed` \| `interface` \| `iot_rules_managed` \| `lambda` \| `load_balancer` \| `nat_gateway` \| `network_load_balancer` \| `quicksight` \| `transit_gateway` \| `trunk` \| `vpc_endpoint`).
+  `mac-address` - The MAC address of the network interface.
+  `network-interface-id` - The ID of the network interface.
+  `operator.managed` - A Boolean that indicates whether this is a managed network interface.
+  `operator.principal` - The principal that manages the network interface. Only valid for managed network interfaces, where `managed` is `true`.
+  `owner-id` - The AWS account ID of the network interface owner.
+  `private-dns-name` - The private DNS name of the network interface (IPv4).
+  `private-ip-address` - The private IPv4 address or addresses of the network interface.
+  `requester-id` - The alias or AWS account ID of the principal or service that created the network interface.
+  `requester-managed` - Indicates whether the network interface is being managed by an AWS service (for example, AWS Management Console, Auto Scaling, and so on).
+  `source-dest-check` - Indicates whether the network interface performs source/destination checking. A value of `true` means checking is enabled, and `false` means checking is disabled. The value must be `false` for the network interface to perform network address translation (NAT) in your VPC.
+  `status` - The status of the network interface. If the network interface is not attached to an instance, the status is `available`; if a network interface is attached to an instance the status is `in-use`.
+  `subnet-id` - The ID of the subnet for the network interface.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `vpc-id` - The ID of the VPC for the network interface.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludeManagedResources**
Indicates whether to include managed resources in the output. If this parameter is set to `true`, the output includes resources that are managed by AWS services, even if managed resource visibility is set to hidden.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. You cannot specify this parameter and the network interface IDs parameter in the same request. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NetworkInterfaceId.N**
The network interface IDs.
Default: Describes all your network interfaces.
Type: Array of strings
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeNetworkInterfaces_ResponseElements"></a>

The following elements are returned by the service.

 **networkInterfaceSet**
Information about the network interfaces.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeNetworkInterfaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeNetworkInterfaces_Examples"></a>

### Example 1
<a name="API_DescribeNetworkInterfaces_Example_1"></a>

This example describes all your network interfaces.

#### Sample Request
<a name="API_DescribeNetworkInterfaces_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNetworkInterfaces
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNetworkInterfaces_Example_1_Response"></a>

```
<DescribeNetworkInterfacesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>fc45294c-006b-457b-bab9-012f5b3b0e40</requestId>
     <networkInterfaceSet>
       <item>
         <networkInterfaceId>eni-0f62d866</networkInterfaceId>
         <subnetId>subnet-c53c87ac</subnetId>
         <vpcId>vpc-cc3c87a5</vpcId>
         <availabilityZone>api-southeast-1b</availabilityZone>
         <description/>
         <ownerId>053230519467</ownerId>
         <requesterManaged>false</requesterManaged>
         <status>in-use</status>
         <macAddress>02:81:60:cb:27:37</macAddress>
         <privateIpAddress>10.0.0.146</privateIpAddress>
         <sourceDestCheck>true</sourceDestCheck>
         <groupSet>
           <item>
             <groupId>sg-3f4b5653</groupId>
             <groupName>default</groupName>
           </item>
         </groupSet>
         <attachment>
           <attachmentId>eni-attach-6537fc0c</attachmentId>
           <instanceId>i-1234567890abcdef0</instanceId>
           <instanceOwnerId>053230519467</instanceOwnerId>
           <deviceIndex>0</deviceIndex>
           <status>attached</status>
           <attachTime>2012-07-01T21:45:27.000Z</attachTime>
           <deleteOnTermination>true</deleteOnTermination>
         </attachment>
         <tagSet/>
         <privateIpAddressesSet>
           <item>
             <privateIpAddress>10.0.0.146</privateIpAddress>
             <primary>true</primary>
           </item>
           <item>
             <privateIpAddress>10.0.0.148</privateIpAddress>
             <primary>false</primary>
           </item>
           <item>
             <privateIpAddress>10.0.0.150</privateIpAddress>
             <primary>false</primary>
           </item>
         </privateIpAddressesSet>
         <ipv6AddressesSet/>
       </item>
       <item>
         <networkInterfaceId>eni-a66ed5cf</networkInterfaceId>
         <subnetId>subnet-cd8a35a4</subnetId>
         <vpcId>vpc-f28a359b</vpcId>
         <availabilityZone>ap-southeast-1b</availabilityZone>
         <description>Primary network interface</description>
         <ownerId>053230519467</ownerId>
         <requesterManaged>false</requesterManaged>
         <status>in-use</status>
         <macAddress>02:78:d7:00:8a:1e</macAddress>
         <privateIpAddress>10.0.1.233</privateIpAddress>
         <sourceDestCheck>true</sourceDestCheck>
         <groupSet>
           <item>
             <groupId>sg-a2a0b2ce</groupId>
             <groupName>quick-start-1</groupName>
           </item>
         </groupSet>
         <attachment>
           <attachmentId>eni-attach-a99c57c0</attachmentId>
           <instanceId>i-0598c7d356eba48d7</instanceId>
           <instanceOwnerId>053230519467</instanceOwnerId>
           <deviceIndex>0</deviceIndex>
           <status>attached</status>
           <attachTime>2012-06-27T20:08:44.000Z</attachTime>
           <deleteOnTermination>true</deleteOnTermination>
         </attachment>
         <tagSet/>
         <privateIpAddressesSet>
           <item>
             <privateIpAddress>10.0.1.233</privateIpAddress>
             <primary>true</primary>
           </item>
           <item>
             <privateIpAddress>10.0.1.20</privateIpAddress>
             <primary>false</primary>
           </item>
         </privateIpAddressesSet>
         <ipv6AddressesSet>
          <item>
            <ipv6Address>2001:db8:1234:1a00::123</ipv6Address>
          </item>
          <item>
            <ipv6Address>2001:db8:1234:1a00::456</ipv6Address>
          </item>
        </ipv6AddressesSet>
       </item>
     </networkInterfaceSet>
</DescribeNetworkInterfacesResponse>
```

### Example 2
<a name="API_DescribeNetworkInterfaces_Example_2"></a>

This example uses a filter to describe only network interfaces that are in Availability Zone `us-east-2a`.

#### Sample Request
<a name="API_DescribeNetworkInterfaces_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNetworkInterfaces
&Filter.1.Name=availability-zone
&Filter.1.Value.1=us-east-2a
&AUTHPARAMS
```

## See Also
<a name="API_DescribeNetworkInterfaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNetworkInterfaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNetworkInterfaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
