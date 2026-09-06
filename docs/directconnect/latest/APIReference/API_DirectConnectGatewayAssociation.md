---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGatewayAssociation.html
---

# DirectConnectGatewayAssociation
<a name="API_DirectConnectGatewayAssociation"></a>

Information about an association between a Direct Connect gateway and a virtual private gateway or transit gateway.

## Contents
<a name="API_DirectConnectGatewayAssociation_Contents"></a>

 ** allowedPrefixesToDirectConnectGateway **   <a name="DX-Type-DirectConnectGatewayAssociation-allowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to advertise to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

 ** associatedCoreNetwork **   <a name="DX-Type-DirectConnectGatewayAssociation-associatedCoreNetwork"></a>
The ID of the Cloud WAN core network associated with the Direct Connect gateway attachment.
Type: [AssociatedCoreNetwork](API_AssociatedCoreNetwork.md) object
Required: No

 ** associatedGateway **   <a name="DX-Type-DirectConnectGatewayAssociation-associatedGateway"></a>
Information about the associated gateway.
Type: [AssociatedGateway](API_AssociatedGateway.md) object
Required: No

 ** associationId **   <a name="DX-Type-DirectConnectGatewayAssociation-associationId"></a>
The ID of the Direct Connect gateway association.
Type: String
Required: No

 ** associationState **   <a name="DX-Type-DirectConnectGatewayAssociation-associationState"></a>
The state of the association. The following are the possible values:
+  `associating`: The initial state after calling [CreateDirectConnectGatewayAssociation](API_CreateDirectConnectGatewayAssociation.md).
+  `associated`: The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
+  `disassociating`: The initial state after calling [DeleteDirectConnectGatewayAssociation](API_DeleteDirectConnectGatewayAssociation.md).
+  `disassociated`: The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
+  `updating`: The CIDR blocks for the virtual private gateway or transit gateway are currently being updated. This could be new CIDR blocks added or current CIDR blocks removed.
Type: String
Valid Values: `associating | associated | disassociating | disassociated | updating`
Required: No

 ** directConnectGatewayId **   <a name="DX-Type-DirectConnectGatewayAssociation-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** directConnectGatewayOwnerAccount **   <a name="DX-Type-DirectConnectGatewayAssociation-directConnectGatewayOwnerAccount"></a>
The ID of the AWS account that owns the associated gateway.
Type: String
Required: No

 ** stateChangeError **   <a name="DX-Type-DirectConnectGatewayAssociation-stateChangeError"></a>
The error message if the state of an object failed to advance.
Type: String
Required: No

 ** virtualGatewayId **   <a name="DX-Type-DirectConnectGatewayAssociation-virtualGatewayId"></a>
The ID of the virtual private gateway. Applies only to private virtual interfaces.
Type: String
Required: No

 ** virtualGatewayOwnerAccount **   <a name="DX-Type-DirectConnectGatewayAssociation-virtualGatewayOwnerAccount"></a>
The ID of the AWS account that owns the virtual private gateway.
Type: String
Required: No

 ** virtualGatewayRegion **   <a name="DX-Type-DirectConnectGatewayAssociation-virtualGatewayRegion"></a>
 *This member has been deprecated.*
The AWS Region where the virtual private gateway is located.
Type: String
Required: No

## See Also
<a name="API_DirectConnectGatewayAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DirectConnectGatewayAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DirectConnectGatewayAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DirectConnectGatewayAssociation)
