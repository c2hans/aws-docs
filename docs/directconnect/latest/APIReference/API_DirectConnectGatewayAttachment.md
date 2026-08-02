---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGatewayAttachment.html
---

# DirectConnectGatewayAttachment
<a name="API_DirectConnectGatewayAttachment"></a>

Information about an attachment between a Direct Connect gateway and a virtual interface.

## Contents
<a name="API_DirectConnectGatewayAttachment_Contents"></a>

 ** attachmentState **   <a name="DX-Type-DirectConnectGatewayAttachment-attachmentState"></a>
The state of the attachment. The following are the possible values:
+  `attaching`: The initial state after a virtual interface is created using the Direct Connect gateway.
+  `attached`: The Direct Connect gateway and virtual interface are attached and ready to pass traffic.
+  `detaching`: The initial state after calling [DeleteVirtualInterface](API_DeleteVirtualInterface.md).
+  `detached`: The virtual interface is detached from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual interface is stopped.
Type: String
Valid Values: `attaching | attached | detaching | detached`
Required: No

 ** attachmentType **   <a name="DX-Type-DirectConnectGatewayAttachment-attachmentType"></a>
The type of attachment.
Type: String
Valid Values: `TransitVirtualInterface | PrivateVirtualInterface`
Required: No

 ** directConnectGatewayId **   <a name="DX-Type-DirectConnectGatewayAttachment-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** stateChangeError **   <a name="DX-Type-DirectConnectGatewayAttachment-stateChangeError"></a>
The error message if the state of an object failed to advance.
Type: String
Required: No

 ** virtualInterfaceId **   <a name="DX-Type-DirectConnectGatewayAttachment-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

 ** virtualInterfaceOwnerAccount **   <a name="DX-Type-DirectConnectGatewayAttachment-virtualInterfaceOwnerAccount"></a>
The ID of the AWS account that owns the virtual interface.
Type: String
Required: No

 ** virtualInterfaceRegion **   <a name="DX-Type-DirectConnectGatewayAttachment-virtualInterfaceRegion"></a>
The AWS Region where the virtual interface is located.
Type: String
Required: No

## See Also
<a name="API_DirectConnectGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DirectConnectGatewayAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DirectConnectGatewayAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DirectConnectGatewayAttachment)
