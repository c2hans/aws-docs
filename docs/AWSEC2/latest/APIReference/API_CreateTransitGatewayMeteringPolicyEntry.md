---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayMeteringPolicyEntry.html
---

# CreateTransitGatewayMeteringPolicyEntry
<a name="API_CreateTransitGatewayMeteringPolicyEntry"></a>

Creates an entry in a transit gateway metering policy to define traffic measurement rules.

## Request Parameters
<a name="API_CreateTransitGatewayMeteringPolicyEntry_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DestinationCidrBlock**
The destination CIDR block for traffic matching.
Type: String
Required: No

 **DestinationPortRange**
The destination port range for traffic matching.
Type: String
Required: No

 **DestinationTransitGatewayAttachmentId**
The ID of the destination transit gateway attachment for traffic matching.
Type: String
Required: No

 **DestinationTransitGatewayAttachmentType**
The type of the destination transit gateway attachment for traffic matching. Note that the `tgw-peering` resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MeteredAccount**
The AWS account ID to which the metered traffic should be attributed.
Type: String
Valid Values: `source-attachment-owner | destination-attachment-owner | transit-gateway-owner`
Required: Yes

 **PolicyRuleNumber**
The rule number for the metering policy entry. Rules are processed in order from lowest to highest number.
Type: Integer
Required: Yes

 **Protocol**
The protocol for traffic matching (1, 6, 17, etc.).
Type: String
Required: No

 **SourceCidrBlock**
The source CIDR block for traffic matching.
Type: String
Required: No

 **SourcePortRange**
The source port range for traffic matching.
Type: String
Required: No

 **SourceTransitGatewayAttachmentId**
The ID of the source transit gateway attachment for traffic matching.
Type: String
Required: No

 **SourceTransitGatewayAttachmentType**
The type of the source transit gateway attachment for traffic matching. Note that the `tgw-peering` resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 **TransitGatewayMeteringPolicyId**
The ID of the transit gateway metering policy to add the entry to.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTransitGatewayMeteringPolicyEntry_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayMeteringPolicyEntry**
Information about the created transit gateway metering policy entry.
Type: [TransitGatewayMeteringPolicyEntry](API_TransitGatewayMeteringPolicyEntry.md) object

## Errors
<a name="API_CreateTransitGatewayMeteringPolicyEntry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateTransitGatewayMeteringPolicyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayMeteringPolicyEntry)
