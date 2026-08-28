---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ReplaceNetworkAclAssociationAction.html
---

# ReplaceNetworkAclAssociationAction
<a name="API_ReplaceNetworkAclAssociationAction"></a>

Information about the `ReplaceNetworkAclAssociation` action in Amazon EC2. This is a remediation option in `RemediationAction`.

## Contents
<a name="API_ReplaceNetworkAclAssociationAction_Contents"></a>

 ** AssociationId **   <a name="fms-Type-ReplaceNetworkAclAssociationAction-AssociationId"></a>
Describes a remediation action target.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

 ** Description **   <a name="fms-Type-ReplaceNetworkAclAssociationAction-Description"></a>
Brief description of this remediation action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FMSCanRemediate **   <a name="fms-Type-ReplaceNetworkAclAssociationAction-FMSCanRemediate"></a>
Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.
Type: Boolean
Required: No

 ** NetworkAclId **   <a name="fms-Type-ReplaceNetworkAclAssociationAction-NetworkAclId"></a>
The network ACL that's associated with the remediation action.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

## See Also
<a name="API_ReplaceNetworkAclAssociationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ReplaceNetworkAclAssociationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ReplaceNetworkAclAssociationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ReplaceNetworkAclAssociationAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
