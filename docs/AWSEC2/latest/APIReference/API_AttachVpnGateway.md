---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVpnGateway.html
---

# AttachVpnGateway
<a name="API_AttachVpnGateway"></a>

Attaches an available virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time.

For more information, see [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the * AWS Site-to-Site VPN User Guide*.

## Request Parameters
<a name="API_AttachVpnGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

 **VpnGatewayId**
The ID of the virtual private gateway.
Type: String
Required: Yes

## Response Elements
<a name="API_AttachVpnGateway_ResponseElements"></a>

The following elements are returned by the service.

 **attachment**
Information about the attachment.
Type: [VpcAttachment](API_VpcAttachment.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AttachVpnGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AttachVpnGateway_Examples"></a>

### Example
<a name="API_AttachVpnGateway_Example_1"></a>

This example attaches the virtual private gateway with the ID `vgw-8db04f81` to the VPC with the ID `vpc-1a2b3c4d`.

#### Sample Request
<a name="API_AttachVpnGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AttachVpnGateway
&VpnGatewayId=vgw-8db04f81
&VpcId=vpc-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_AttachVpnGateway_Example_1_Response"></a>

```
<AttachVpnGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <attachment>
      <vpcId>vpc-1a2b3c4d</vpcId>
      <state>attaching</state>
   </attachment>
</AttachVpnGatewayResponse>
```

## See Also
<a name="API_AttachVpnGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AttachVpnGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AttachVpnGateway)
