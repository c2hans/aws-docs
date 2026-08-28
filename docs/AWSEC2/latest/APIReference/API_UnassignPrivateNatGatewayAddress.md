---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateNatGatewayAddress.html
---

# UnassignPrivateNatGatewayAddress
<a name="API_UnassignPrivateNatGatewayAddress"></a>

Unassigns secondary private IPv4 addresses from a private NAT gateway. You cannot unassign your primary private IP. For more information, see [Edit secondary IP address associations](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html#nat-gateway-edit-secondary) in the *Amazon VPC User Guide*.

While unassigning is in progress, you cannot assign/unassign additional IP addresses while the connections are being drained. You are, however, allowed to delete the NAT gateway.

A private IP address will only be released at the end of MaxDrainDurationSeconds. The private IP addresses stay associated and support the existing connections, but do not support any new connections (new connections are distributed across the remaining assigned private IP address). After the existing connections drain out, the private IP addresses are released.

## Request Parameters
<a name="API_UnassignPrivateNatGatewayAddress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxDrainDurationSeconds**
The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4000.
Required: No

 **NatGatewayId**
The ID of the NAT gateway.
Type: String
Required: Yes

 **PrivateIpAddress.N**
The private IPv4 addresses you want to unassign.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_UnassignPrivateNatGatewayAddress_ResponseElements"></a>

The following elements are returned by the service.

 **natGatewayAddressSet**
Information about the NAT gateway IP addresses.
Type: Array of [NatGatewayAddress](API_NatGatewayAddress.md) objects

 **natGatewayId**
The ID of the NAT gateway.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_UnassignPrivateNatGatewayAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UnassignPrivateNatGatewayAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UnassignPrivateNatGatewayAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
