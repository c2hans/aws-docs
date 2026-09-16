---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayVirtualInterfaces.html
---

# DescribeLocalGatewayVirtualInterfaces
<a name="API_DescribeLocalGatewayVirtualInterfaces"></a>

Describes the specified local gateway virtual interfaces.

## Request Parameters
<a name="API_DescribeLocalGatewayVirtualInterfaces_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `local-address` - The local address.
+  `local-bgp-asn` - The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway.
+  `local-gateway-id` - The ID of the local gateway.
+  `local-gateway-virtual-interface-id` - The ID of the virtual interface.
+  `owner-id` - The ID of the AWS account that owns the local gateway virtual interface.
+  `peer-address` - The peer address.
+  `peer-bgp-asn` - The peer BGP ASN.
+  `vlan` - The ID of the VLAN.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **LocalGatewayVirtualInterfaceId.N**
The IDs of the virtual interfaces.
Type: Array of strings
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

## Response Elements
<a name="API_DescribeLocalGatewayVirtualInterfaces_ResponseElements"></a>

The following elements are returned by the service.

 **localGatewayVirtualInterfaceSet**
Information about the virtual interfaces.
Type: Array of [LocalGatewayVirtualInterface](API_LocalGatewayVirtualInterface.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeLocalGatewayVirtualInterfaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeLocalGatewayVirtualInterfaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeLocalGatewayVirtualInterfaces)
