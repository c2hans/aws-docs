---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_RemediationAction.html
---

# RemediationAction
<a name="API_RemediationAction"></a>

Information about an individual action you can take to remediate a violation.

## Contents
<a name="API_RemediationAction_Contents"></a>

 ** CreateNetworkAclAction **   <a name="fms-Type-RemediationAction-CreateNetworkAclAction"></a>
Information about the `CreateNetworkAcl` action in Amazon EC2.
Type: [CreateNetworkAclAction](API_CreateNetworkAclAction.md) object
Required: No

 ** CreateNetworkAclEntriesAction **   <a name="fms-Type-RemediationAction-CreateNetworkAclEntriesAction"></a>
Information about the `CreateNetworkAclEntries` action in Amazon EC2.
Type: [CreateNetworkAclEntriesAction](API_CreateNetworkAclEntriesAction.md) object
Required: No

 ** DeleteNetworkAclEntriesAction **   <a name="fms-Type-RemediationAction-DeleteNetworkAclEntriesAction"></a>
Information about the `DeleteNetworkAclEntries` action in Amazon EC2.
Type: [DeleteNetworkAclEntriesAction](API_DeleteNetworkAclEntriesAction.md) object
Required: No

 ** Description **   <a name="fms-Type-RemediationAction-Description"></a>
A description of a remediation action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** EC2AssociateRouteTableAction **   <a name="fms-Type-RemediationAction-EC2AssociateRouteTableAction"></a>
Information about the AssociateRouteTable action in the Amazon EC2 API.
Type: [EC2AssociateRouteTableAction](API_EC2AssociateRouteTableAction.md) object
Required: No

 ** EC2CopyRouteTableAction **   <a name="fms-Type-RemediationAction-EC2CopyRouteTableAction"></a>
Information about the CopyRouteTable action in the Amazon EC2 API.
Type: [EC2CopyRouteTableAction](API_EC2CopyRouteTableAction.md) object
Required: No

 ** EC2CreateRouteAction **   <a name="fms-Type-RemediationAction-EC2CreateRouteAction"></a>
Information about the CreateRoute action in the Amazon EC2 API.
Type: [EC2CreateRouteAction](API_EC2CreateRouteAction.md) object
Required: No

 ** EC2CreateRouteTableAction **   <a name="fms-Type-RemediationAction-EC2CreateRouteTableAction"></a>
Information about the CreateRouteTable action in the Amazon EC2 API.
Type: [EC2CreateRouteTableAction](API_EC2CreateRouteTableAction.md) object
Required: No

 ** EC2DeleteRouteAction **   <a name="fms-Type-RemediationAction-EC2DeleteRouteAction"></a>
Information about the DeleteRoute action in the Amazon EC2 API.
Type: [EC2DeleteRouteAction](API_EC2DeleteRouteAction.md) object
Required: No

 ** EC2ReplaceRouteAction **   <a name="fms-Type-RemediationAction-EC2ReplaceRouteAction"></a>
Information about the ReplaceRoute action in the Amazon EC2 API.
Type: [EC2ReplaceRouteAction](API_EC2ReplaceRouteAction.md) object
Required: No

 ** EC2ReplaceRouteTableAssociationAction **   <a name="fms-Type-RemediationAction-EC2ReplaceRouteTableAssociationAction"></a>
Information about the ReplaceRouteTableAssociation action in the Amazon EC2 API.
Type: [EC2ReplaceRouteTableAssociationAction](API_EC2ReplaceRouteTableAssociationAction.md) object
Required: No

 ** FMSPolicyUpdateFirewallCreationConfigAction **   <a name="fms-Type-RemediationAction-FMSPolicyUpdateFirewallCreationConfigAction"></a>
The remedial action to take when updating a firewall configuration.
Type: [FMSPolicyUpdateFirewallCreationConfigAction](API_FMSPolicyUpdateFirewallCreationConfigAction.md) object
Required: No

 ** ReplaceNetworkAclAssociationAction **   <a name="fms-Type-RemediationAction-ReplaceNetworkAclAssociationAction"></a>
Information about the `ReplaceNetworkAclAssociation` action in Amazon EC2.
Type: [ReplaceNetworkAclAssociationAction](API_ReplaceNetworkAclAssociationAction.md) object
Required: No

## See Also
<a name="API_RemediationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/RemediationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/RemediationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/RemediationAction)
