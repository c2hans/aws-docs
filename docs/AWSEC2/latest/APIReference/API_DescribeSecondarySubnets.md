---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecondarySubnets.html
---

# DescribeSecondarySubnets
<a name="API_DescribeSecondarySubnets"></a>

Describes one or more of your secondary subnets.

## Request Parameters
<a name="API_DescribeSecondarySubnets_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `ipv4-cidr-block-association.association-id` - The association ID for an IPv4 CIDR block associated with the secondary subnet.
+  `ipv4-cidr-block-association.cidr-block` - An IPv4 CIDR block associated with the secondary subnet.
+  `ipv4-cidr-block-association.state` - The state of an IPv4 CIDR block associated with the secondary subnet.
+  `owner-id` - The ID of the AWS account that owns the secondary subnet.
+  `secondary-network-id` - The ID of the secondary network.
+  `secondary-network-type` - The type of the secondary network (`rdma`).
+  `secondary-subnet-id` - The ID of the secondary subnet.
+  `secondary-subnet-arn` - The ARN of the secondary subnet.
+  `state` - The state of the secondary subnet (`create-in-progress` \| `create-complete` \| `create-failed` \| `delete-in-progress` \| `delete-complete` \| `delete-failed`).
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

 **SecondarySubnetId.N**
The IDs of the secondary subnets.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeSecondarySubnets_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **secondarySubnetSet**
Information about the secondary subnets.
Type: Array of [SecondarySubnet](API_SecondarySubnet.md) objects

## Errors
<a name="API_DescribeSecondarySubnets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSecondarySubnets_Examples"></a>

### Example
<a name="API_DescribeSecondarySubnets_Example_1"></a>

This example describes the specified secondary subnets.

#### Sample Request
<a name="API_DescribeSecondarySubnets_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSecondarySubnets
&SecondarySubnetId.1=ss-0123456789abcdef0
&SecondarySubnetId.2=ss-0987654321fedcba0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSecondarySubnets_Example_1_Response"></a>

```
<DescribeSecondarySubnetsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <secondarySubnetSet>
      <item>
         <secondarySubnetId>ss-0123456789abcdef0</secondarySubnetId>
         <secondarySubnetArn>arn:aws:ec2:us-east-2:123456789012:secondary-subnet/ss-0123456789abcdef0</secondarySubnetArn>
         <secondaryNetworkId>sn-0123456789abcdef0</secondaryNetworkId>
         <secondaryNetworkType>rdma</secondaryNetworkType>
         <ownerId>123456789012</ownerId>
         <availabilityZoneId>use2-az1</availabilityZoneId>
         <availabilityZone>us-east-2a</availabilityZone>
         <ipv4CidrBlockAssociations>
            <item>
               <associationId>ss-cidr-assoc-56789901234abcdef0</associationId>
               <cidrBlock>10.0.0.0/24</cidrBlock>
               <state>associated</state>
            </item>
         </ipv4CidrBlockAssociations>
         <state>create-complete</state>
         <tagSet>
            <item>
               <key>Name</key>
               <value>Prod Secondary Subnet</value>
            </item>
         </tagSet>
      </item>
      <item>
         <secondarySubnetId>ss-0987654321fedcba0</secondarySubnetId>
         <secondarySubnetArn>arn:aws:ec2:us-east-2:123456789012:secondary-subnet/ss-0987654321fedcba0</secondarySubnetArn>
         <secondaryNetworkId>sn-0123456789abcdef0</secondaryNetworkId>
         <secondaryNetworkType>rdma</secondaryNetworkType>
         <ownerId>123456789012</ownerId>
         <availabilityZoneId>use2-az1</availabilityZoneId>
         <availabilityZone>us-east-2a</availabilityZone>
         <ipv4CidrBlockAssociations>
            <item>
               <associationId>ss-cidr-assoc-09876543210fedcba0</associationId>
               <cidrBlock>10.0.1.0/24</cidrBlock>
               <state>associated</state>
            </item>
         </ipv4CidrBlockAssociations>
         <state>create-complete</state>
         <tagSet>
            <item>
               <key>Name</key>
               <value>Dev Secondary Subnet</value>
            </item>
         </tagSet>
      </item>
   </secondarySubnetSet>
</DescribeSecondarySubnetsResponse>
```

## See Also
<a name="API_DescribeSecondarySubnets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSecondarySubnets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSecondarySubnets)
