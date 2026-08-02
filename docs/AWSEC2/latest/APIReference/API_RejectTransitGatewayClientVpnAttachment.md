---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectTransitGatewayClientVpnAttachment.html
---

# RejectTransitGatewayClientVpnAttachment
<a name="API_RejectTransitGatewayClientVpnAttachment"></a>

Rejects a Transit Gateway attachment request for a Client VPN endpoint. The Transit Gateway owner can reject the attachment request to prevent the Client VPN endpoint from routing traffic through the Transit Gateway.

## Request Parameters
<a name="API_RejectTransitGatewayClientVpnAttachment_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TransitGatewayAttachmentId**
The ID of the Transit Gateway attachment.
Type: String
Required: Yes

## Response Elements
<a name="API_RejectTransitGatewayClientVpnAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayClientVpnAttachment**
Information about the Transit Gateway Client VPN attachment.
Type: [TransitGatewayClientVpnAttachment](API_TransitGatewayClientVpnAttachment.md) object

## Errors
<a name="API_RejectTransitGatewayClientVpnAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RejectTransitGatewayClientVpnAttachment_Examples"></a>

### Example
<a name="API_RejectTransitGatewayClientVpnAttachment_Example_1"></a>

This example rejects a Transit Gateway Client VPN attachment.

#### Sample Request
<a name="API_RejectTransitGatewayClientVpnAttachment_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RejectTransitGatewayClientVpnAttachment
&TransitGatewayAttachmentId=tgw-attach-0a34fe6b4fEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_RejectTransitGatewayClientVpnAttachment_Example_1_Response"></a>

```
<RejectTransitGatewayClientVpnAttachmentResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>691de4ea-32ef-447b-b4f8-d8463EXAMPLE</requestId>
    <transitGatewayClientVpnAttachment>
        <transitGatewayAttachmentId>tgw-attach-0a34fe6b4fEXAMPLE</transitGatewayAttachmentId>
        <transitGatewayId>tgw-0262a0e521EXAMPLE</transitGatewayId>
        <clientVpnEndpointId>cvpn-endpoint-00c5d11fc4EXAMPLE</clientVpnEndpointId>
        <state>rejected</state>
    </transitGatewayClientVpnAttachment>
</RejectTransitGatewayClientVpnAttachmentResult>
```

## See Also
<a name="API_RejectTransitGatewayClientVpnAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RejectTransitGatewayClientVpnAttachment)
