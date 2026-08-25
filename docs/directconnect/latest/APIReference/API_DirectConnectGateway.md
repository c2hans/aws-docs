---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGateway.html
---

# DirectConnectGateway
<a name="API_DirectConnectGateway"></a>

Information about a Direct Connect gateway, which enables you to connect virtual interfaces and virtual private gateway or transit gateways.

## Contents
<a name="API_DirectConnectGateway_Contents"></a>

 ** amazonSideAsn **   <a name="DX-Type-DirectConnectGateway-amazonSideAsn"></a>
The autonomous system number (AS) for the Amazon side of the connection.
Type: Long
Required: No

 ** directConnectGatewayId **   <a name="DX-Type-DirectConnectGateway-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** directConnectGatewayName **   <a name="DX-Type-DirectConnectGateway-directConnectGatewayName"></a>
The name of the Direct Connect gateway.
Type: String
Required: No

 ** directConnectGatewayState **   <a name="DX-Type-DirectConnectGateway-directConnectGatewayState"></a>
The state of the Direct Connect gateway. The following are the possible values:
+  `pending`: The initial state after calling [CreateDirectConnectGateway](API_CreateDirectConnectGateway.md).
+  `available`: The Direct Connect gateway is ready for use.
+  `deleting`: The initial state after calling [DeleteDirectConnectGateway](API_DeleteDirectConnectGateway.md).
+  `deleted`: The Direct Connect gateway is deleted and cannot pass traffic.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** ownerAccount **   <a name="DX-Type-DirectConnectGateway-ownerAccount"></a>
The ID of the AWS account that owns the Direct Connect gateway.
Type: String
Required: No

 ** stateChangeError **   <a name="DX-Type-DirectConnectGateway-stateChangeError"></a>
The error message if the state of an object failed to advance.
Type: String
Required: No

 ** tags **   <a name="DX-Type-DirectConnectGateway-tags"></a>
Information about a tag.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** totalPrefixPoolAllocations **   <a name="DX-Type-DirectConnectGateway-totalPrefixPoolAllocations"></a>
The total number of inbound route prefixes allocated to the attachments on the Direct Connect gateway. The count combines the IPv4 and IPv6 address families.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DirectConnectGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DirectConnectGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DirectConnectGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DirectConnectGateway)
