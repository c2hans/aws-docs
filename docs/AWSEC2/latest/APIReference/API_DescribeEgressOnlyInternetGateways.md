---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeEgressOnlyInternetGateways.html
---

# DescribeEgressOnlyInternetGateways
<a name="API_DescribeEgressOnlyInternetGateways"></a>

Describes your egress-only internet gateways. The default is to describe all your egress-only internet gateways. Alternatively, you can specify specific egress-only internet gateway IDs or filter the results to include only the egress-only internet gateways that match specific criteria.

## Request Parameters
<a name="API_DescribeEgressOnlyInternetGateways_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EgressOnlyInternetGatewayId.N**
The IDs of the egress-only internet gateways.
Type: Array of strings
Required: No

 **Filter.N**
The filters.
+  `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 255.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeEgressOnlyInternetGateways_ResponseElements"></a>

The following elements are returned by the service.

 **egressOnlyInternetGatewaySet**
Information about the egress-only internet gateways.
Type: Array of [EgressOnlyInternetGateway](API_EgressOnlyInternetGateway.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeEgressOnlyInternetGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEgressOnlyInternetGateways_Examples"></a>

### Example
<a name="API_DescribeEgressOnlyInternetGateways_Example_1"></a>

This example describes all of your egress-only internet gateways.

#### Sample Request
<a name="API_DescribeEgressOnlyInternetGateways_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeEgressOnlyInternetGateways
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeEgressOnlyInternetGateways_Example_1_Response"></a>

```
<DescribeEgressOnlyInternetGatewaysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ec441b4c-357f-4483-b4a7-example</requestId>
    <egressOnlyInternetGatewaySet>
        <item>
            <attachmentSet>
                <item>
                    <state>attached</state>
                    <vpcId>vpc-0c62a468</vpcId>
                </item>
            </attachmentSet>
            <egressOnlyInternetGatewayId>eigw-015e0e244e24dfe8a</egressOnlyInternetGatewayId>
        </item>
    </egressOnlyInternetGatewaySet>
</DescribeEgressOnlyInternetGatewaysResponse>
```

## See Also
<a name="API_DescribeEgressOnlyInternetGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeEgressOnlyInternetGateways)
