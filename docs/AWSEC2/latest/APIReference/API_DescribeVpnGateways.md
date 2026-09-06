---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html
---

# DescribeVpnGateways
<a name="API_DescribeVpnGateways"></a>

Describes one or more of your virtual private gateways.

For more information, see [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the * AWS Site-to-Site VPN User Guide*.

## Request Parameters
<a name="API_DescribeVpnGateways_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `amazon-side-asn` - The Autonomous System Number (ASN) for the Amazon side of the gateway.
+  `attachment.state` - The current state of the attachment between the gateway and the VPC (`attaching` \| `attached` \| `detaching` \| `detached`).
+  `attachment.vpc-id` - The ID of an attached VPC.
+  `availability-zone` - The Availability Zone for the virtual private gateway (if applicable).
+  `state` - The state of the virtual private gateway (`pending` \| `available` \| `deleting` \| `deleted`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `type` - The type of virtual private gateway. Currently the only supported type is `ipsec.1`.
+  `vpn-gateway-id` - The ID of the virtual private gateway.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **VpnGatewayId.N**
One or more virtual private gateway IDs.
Default: Describes all your virtual private gateways.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVpnGateways_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpnGatewaySet**
Information about one or more virtual private gateways.
Type: Array of [VpnGateway](API_VpnGateway.md) objects

## Errors
<a name="API_DescribeVpnGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpnGateways_Examples"></a>

### Example 1
<a name="API_DescribeVpnGateways_Example_1"></a>

This example describes the specified virtual private gateway.

#### Sample Request
<a name="API_DescribeVpnGateways_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpnGateways
&VpnGatewayId.1=vgw-8db04f81
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpnGateways_Example_1_Response"></a>

```
<DescribeVpnGatewaysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <vpnGatewaySet>
        <item>
            <vpnGatewayId>vgw-8db04f81</vpnGatewayId>
            <state>available</state>
            <type>ipsec.1</type>
            <attachments>
                <item>
                    <vpcId>vpc-4c090c2a</vpcId>
                    <state>attached</state>
                </item>
            </attachments>
            <amazonSideAsn>65001</amazonSideAsn>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>NYOffice</value>
                </item>
            </tagSet>
        </item>
    </vpnGatewaySet>
</DescribeVpnGatewaysResponse>
```

### Example 2
<a name="API_DescribeVpnGateways_Example_2"></a>

This example uses filters to describe any virtual private gateway you own whose state is either `pending` or `available`.

#### Sample Request
<a name="API_DescribeVpnGateways_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpnGateways
&Filter.1.Name=state
&Filter.1.Value.1=pending
&Filter.1.Value.2=available
&AUTHPARAMS
```

## See Also
<a name="API_DescribeVpnGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpnGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpnGateways)
