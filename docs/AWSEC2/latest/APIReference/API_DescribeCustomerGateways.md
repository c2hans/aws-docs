---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCustomerGateways.html
---

# DescribeCustomerGateways
<a name="API_DescribeCustomerGateways"></a>

Describes one or more of your VPN customer gateways.

For more information, see [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the * AWS Site-to-Site VPN User Guide*.

## Request Parameters
<a name="API_DescribeCustomerGateways_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CustomerGatewayId.N**
One or more customer gateway IDs.
Default: Describes all your customer gateways.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `bgp-asn` - The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
+  `customer-gateway-id` - The ID of the customer gateway.
+  `ip-address` - The IP address of the customer gateway device's external interface.
+  `state` - The state of the customer gateway (`pending` \| `available` \| `deleting` \| `deleted`).
+  `type` - The type of customer gateway. Currently, the only supported type is `ipsec.1`.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

## Response Elements
<a name="API_DescribeCustomerGateways_ResponseElements"></a>

The following elements are returned by the service.

 **customerGatewaySet**
Information about one or more customer gateways.
Type: Array of [CustomerGateway](API_CustomerGateway.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeCustomerGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeCustomerGateways_Examples"></a>

### Example 1
<a name="API_DescribeCustomerGateways_Example_1"></a>

This example request describes the specified customer gateway.

#### Sample Request
<a name="API_DescribeCustomerGateways_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeCustomerGateways
&CustomerGatewayId.1=cgw-b4dc3961
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeCustomerGateways_Example_1_Response"></a>

```
<DescribeCustomerGatewaysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <customerGatewaySet>
    <item>
       <customerGatewayId>cgw-b4dc3961</customerGatewayId>
       <state>available</state>
       <type>ipsec.1</type>
       <ipAddress>12.1.2.3</ipAddress>
       <bgpAsn>65534</bgpasn>
       <tagSet/>
    </item>
  </customerGatewaySet>
</DescribeCustomerGatewaysResponse>
```

### Example 2
<a name="API_DescribeCustomerGateways_Example_2"></a>

This example request uses filters to describe any customer gateway you own whose IP address is `12.1.2.3`, and whose state is either `pending` or `available`.

#### Sample Request
<a name="API_DescribeCustomerGateways_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeCustomerGateways
&Filter.1.Name=ip-address
&Filter.1.Value.1=12.1.2.3
&Filter.2.Name=state
&Filter.2.Value.1=pending
&Filter.2.Value.2=available
&AUTHPARAMS
```

## See Also
<a name="API_DescribeCustomerGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeCustomerGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeCustomerGateways)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
