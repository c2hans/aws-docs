---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnTargetNetworks.html
---

# DescribeClientVpnTargetNetworks
<a name="API_DescribeClientVpnTargetNetworks"></a>

Describes the target networks associated with the specified Client VPN endpoint.

## Request Parameters
<a name="API_DescribeClientVpnTargetNetworks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationIds.N**
The IDs of the target network associations.
Type: Array of strings
Required: No

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `association-id` - The ID of the association.
+  `target-network-id` - The ID of the subnet specified as the target network.
+  `vpc-id` - The ID of the VPC in which the target network is located.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeClientVpnTargetNetworks_ResponseElements"></a>

The following elements are returned by the service.

 **clientVpnTargetNetworks**
Information about the associated target networks.
Type: Array of [TargetNetwork](API_TargetNetwork.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeClientVpnTargetNetworks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeClientVpnTargetNetworks_Examples"></a>

### Example
<a name="API_DescribeClientVpnTargetNetworks_Example_1"></a>

This example describes the target networks associated with a Client VPN endpoint.

#### Sample Request
<a name="API_DescribeClientVpnTargetNetworks_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeClientVpnTargetNetworks
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeClientVpnTargetNetworks_Example_1_Response"></a>

```
<DescribeClientVpnTargetNetworksResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1f92d56a-4494-4cbe-ad85-d9387EXAMPLE</requestId>
    <clientVpnTargetNetworks>
        <item>
            <associationId>cvpn-assoc-0822b0983cEXAMPLE</associationId>
            <clientVpnEndpointId>cvpn-endpoint-00c5d11fc4EXAMPLE</clientVpnEndpointId>
            <targetNetworkId>subnet-057fa0918fEXAMPLE</targetNetworkId>
            <securityGroups>
                <item>sg-123456EXAMPLE</item>
            </securityGroups>
            <status>
                <code>associated</code>
            </status>
            <vpcId>vpc-3db97056EXAMPLE</vpcId>
        </item>
    </clientVpnTargetNetworks>
</DescribeClientVpnTargetNetworksRespons>
```

## See Also
<a name="API_DescribeClientVpnTargetNetworks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeClientVpnTargetNetworks)
