---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGatewayAssociationProposal.html
---

# DirectConnectGatewayAssociationProposal
<a name="API_DirectConnectGatewayAssociationProposal"></a>

Information about the proposal request to attach a virtual private gateway to a Direct Connect gateway.

## Contents
<a name="API_DirectConnectGatewayAssociationProposal_Contents"></a>

 ** associatedGateway **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-associatedGateway"></a>
Information about the associated gateway.
Type: [AssociatedGateway](API_AssociatedGateway.md) object
Required: No

 ** directConnectGatewayId **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** directConnectGatewayOwnerAccount **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-directConnectGatewayOwnerAccount"></a>
The ID of the AWS account that owns the Direct Connect gateway.
Type: String
Required: No

 ** existingAllowedPrefixesToDirectConnectGateway **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-existingAllowedPrefixesToDirectConnectGateway"></a>
The existing Amazon VPC prefixes advertised to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

 ** proposalId **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-proposalId"></a>
The ID of the association proposal.
Type: String
Required: No

 ** proposalState **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-proposalState"></a>
The state of the proposal. The following are possible values:
+  `accepted`: The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
+  `deleted`: The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
+  `requested`: The proposal has been requested. The Direct Connect gateway association cannot be used in this state.
Type: String
Valid Values: `requested | accepted | deleted`
Required: No

 ** requestedAllowedPrefixesToDirectConnectGateway **   <a name="DX-Type-DirectConnectGatewayAssociationProposal-requestedAllowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to advertise to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

## See Also
<a name="API_DirectConnectGatewayAssociationProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DirectConnectGatewayAssociationProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DirectConnectGatewayAssociationProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DirectConnectGatewayAssociationProposal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
