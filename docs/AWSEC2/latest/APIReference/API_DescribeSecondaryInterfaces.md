---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecondaryInterfaces.html
---

# DescribeSecondaryInterfaces
<a name="API_DescribeSecondaryInterfaces"></a>

Describes one or more of your secondary interfaces.

## Request Parameters
<a name="API_DescribeSecondaryInterfaces_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `attachment.attachment-id` - The ID of the secondary interface attachment.
+  `attachment.instance-id` - The ID of the instance to which the secondary interface is attached.
+  `attachment.instance-owner-id` - The ID of the AWS account that owns the instance to which the secondary interface is attached.
+  `attachment.status` - The attachment status (`attaching` \| `attached` \| `detaching` \| `detached`).
+  `private-ipv4-addresses.private-ip-address` - The private IPv4 address associated with the secondary interface.
+  `owner-id` - The ID of the AWS account that owns the secondary interface.
+  `secondary-interface-arn` - The ARN of the secondary interface.
+  `secondary-interface-id` - The ID of the secondary interface.
+  `secondary-interface-type` - The type of secondary interface (`secondary`).
+  `secondary-network-id` - The ID of the secondary network.
+  `secondary-network-type` - The type of the secondary network (`rdma`).
+  `secondary-subnet-id` - The ID of the secondary subnet.
+  `status` - The status of the secondary interface (`available` \| `in-use`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **SecondaryInterfaceId.N**
The IDs of the secondary interfaces.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeSecondaryInterfaces_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **secondaryInterfaceSet**
Information about the secondary interfaces.
Type: Array of [SecondaryInterface](API_SecondaryInterface.md) objects

## Errors
<a name="API_DescribeSecondaryInterfaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSecondaryInterfaces_Examples"></a>

### Example 1
<a name="API_DescribeSecondaryInterfaces_Example_1"></a>

This example describes all secondary interfaces in the current Region.

#### Sample Request
<a name="API_DescribeSecondaryInterfaces_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSecondaryInterfaces
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSecondaryInterfaces_Example_1_Response"></a>

```
<DescribeSecondaryInterfacesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <secondaryInterfaceSet>
      <item>
         <secondaryInterfaceId>si-0123456789abcdef0</secondaryInterfaceId>
         <secondaryInterfaceArn>arn:aws:ec2:us-east-2:123456789012:secondary-interface/si-0123456789abcdef0</secondaryInterfaceArn>
         <ownerId>123456789012</ownerId>
         <secondarySubnetId>ss-0123456789abcdef0</secondarySubnetId>
         <secondaryNetworkId>sn-0123456789abcdef0</secondaryNetworkId>
         <secondaryNetworkType>rdma</secondaryNetworkType>
         <availabilityZoneId>use2-az1</availabilityZoneId>
         <availabilityZone>us-east-2a</availabilityZone>
         <macAddress>02:2f:8f:b0:cf:75</macAddress>
         <sourceDestCheck>true</sourceDestCheck>
         <status>in-use</status>
         <secondaryInterfaceType>secondary</secondaryInterfaceType>
         <privateIpv4Addresses>
            <item>
               <privateIpAddress>10.0.1.17</privateIpAddress>
            </item>
         </privateIpv4Addresses>
         <attachment>
            <status>attached</status>
            <deviceIndex>0</deviceIndex>
            <networkCardIndex>1</networkCardIndex>
            <instanceId>i-1234567890abcdef0</instanceId>
            <deleteOnTermination>true</deleteOnTermination>
            <attachmentId>si-attach-0123456789abcdef0</attachmentId>
            <instanceOwnerId>123456789012</instanceOwnerId>
            <attachTime>2026-02-28T23:35:33.000Z</attachTime>
         </attachment>
         <tagSet>
            <item>
               <key>Name</key>
               <value>Prod Secondary Interface</value>
            </item>
         </tagSet>
      </item>
   </secondaryInterfaceSet>
</DescribeSecondaryInterfacesResponse>
```

### Example 2
<a name="API_DescribeSecondaryInterfaces_Example_2"></a>

This example uses filters to describe secondary interfaces attached to a specific instance.

#### Sample Request
<a name="API_DescribeSecondaryInterfaces_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSecondaryInterfaces
&Filter.1.Name=attachment.instance-id
&Filter.1.Value.1=i-1234567890abcdef0
&AUTHPARAMS
```

## See Also
<a name="API_DescribeSecondaryInterfaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSecondaryInterfaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSecondaryInterfaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
