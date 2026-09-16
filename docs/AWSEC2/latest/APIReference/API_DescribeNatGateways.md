---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html
---

# DescribeNatGateways
<a name="API_DescribeNatGateways"></a>

Describes your NAT gateways. The default is to describe all your NAT gateways. Alternatively, you can specify specific NAT gateway IDs or filter the results to include only the NAT gateways that match specific criteria.

## Request Parameters
<a name="API_DescribeNatGateways_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `nat-gateway-id` - The ID of the NAT gateway.
+  `state` - The state of the NAT gateway (`pending` \| `failed` \| `available` \| `deleting` \| `deleted`).
+  `subnet-id` - The ID of the subnet in which the NAT gateway resides.
+  `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `vpc-id` - The ID of the VPC in which the NAT gateway resides.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NatGatewayId.N**
The IDs of the NAT gateways.
Type: Array of strings
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeNatGateways_ResponseElements"></a>

The following elements are returned by the service.

 **natGatewaySet**
Information about the NAT gateways.
Type: Array of [NatGateway](API_NatGateway.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeNatGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeNatGateways_Examples"></a>

### Example
<a name="API_DescribeNatGateways_Example_1"></a>

This example describes all of your NAT gateways.

#### Sample Request
<a name="API_DescribeNatGateways_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNatGateways
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNatGateways_Example_1_Response"></a>

```
<DescribeNatGatewaysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>fcb1ea98-1c04-4f9f-a96d-61442example</requestId>
    <natGatewaySet>
        <item>
            <createTime>2017-02-22T09:30:33.000Z</createTime>
            <natGatewayAddressSet>
                <item>
                    <allocationId>eipalloc-8f409cb1</allocationId>
                    <networkInterfaceId>eni-1c8fa2fc</networkInterfaceId>
                    <privateIp>10.0.0.174</privateIp>
                    <publicIp>203.0.113.5</publicIp>
                </item>
            </natGatewayAddressSet>
            <natGatewayId>nat-05a4fd8a2a3e2574d</natGatewayId>
            <state>available</state>
            <subnetId>subnet-7b16de0c</subnetId>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>MyNatGateway</value>
                </item>
            </tagSet>
            <vpcId>vpc-1a2b3c4d</vpcId>
        </item>
    </natGatewaySet>
</DescribeNatGatewaysResponse>
```

## See Also
<a name="API_DescribeNatGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNatGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNatGateways)
