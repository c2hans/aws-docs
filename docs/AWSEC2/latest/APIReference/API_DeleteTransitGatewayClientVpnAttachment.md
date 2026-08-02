---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayClientVpnAttachment.html
---

# DeleteTransitGatewayClientVpnAttachment
<a name="API_DeleteTransitGatewayClientVpnAttachment"></a>

Deletes a Transit Gateway attachment for a Client VPN endpoint. The Transit Gateway owner can delete the attachment to remove the association between the Client VPN endpoint and the Transit Gateway.

## Request Parameters
<a name="API_DeleteTransitGatewayClientVpnAttachment_RequestParameters"></a>

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
<a name="API_DeleteTransitGatewayClientVpnAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayClientVpnAttachment**
Information about the Transit Gateway Client VPN attachment.
Type: [TransitGatewayClientVpnAttachment](API_TransitGatewayClientVpnAttachment.md) object

## Errors
<a name="API_DeleteTransitGatewayClientVpnAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteTransitGatewayClientVpnAttachment_Examples"></a>

### Example
<a name="API_DeleteTransitGatewayClientVpnAttachment_Example_1"></a>

This example deletes a Transit Gateway Client VPN attachment.

#### Sample Request
<a name="API_DeleteTransitGatewayClientVpnAttachment_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteTransitGatewayClientVpnAttachment
&TransitGatewayAttachmentId=tgw-attach-0a34fe6b4fEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteTransitGatewayClientVpnAttachment_Example_1_Response"></a>

```
<DeleteTransitGatewayClientVpnAttachmentResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>00d80748-708d-40f7-8635-f34acEXAMPLE</requestId>
    <transitGatewayClientVpnAttachment>
        <transitGatewayAttachmentId>tgw-attach-0a34fe6b4fEXAMPLE</transitGatewayAttachmentId>
        <transitGatewayId>tgw-0262a0e521EXAMPLE</transitGatewayId>
        <clientVpnEndpointId>cvpn-endpoint-00c5d11fc4EXAMPLE</clientVpnEndpointId>
        <state>deleting</state>
    </transitGatewayClientVpnAttachment>
</DeleteTransitGatewayClientVpnAttachmentResult>
```

## See Also
<a name="API_DeleteTransitGatewayClientVpnAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteTransitGatewayClientVpnAttachment)
