---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EC2ReplaceRouteTableAssociationAction.html
---

# EC2ReplaceRouteTableAssociationAction
<a name="API_EC2ReplaceRouteTableAssociationAction"></a>

Information about the ReplaceRouteTableAssociation action in Amazon EC2.

## Contents
<a name="API_EC2ReplaceRouteTableAssociationAction_Contents"></a>

 ** AssociationId **   <a name="fms-Type-EC2ReplaceRouteTableAssociationAction-AssociationId"></a>
Information about the association ID.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** RouteTableId **   <a name="fms-Type-EC2ReplaceRouteTableAssociationAction-RouteTableId"></a>
Information about the ID of the new route table to associate with the subnet.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** Description **   <a name="fms-Type-EC2ReplaceRouteTableAssociationAction-Description"></a>
A description of the ReplaceRouteTableAssociation action in Amazon EC2.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_EC2ReplaceRouteTableAssociationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EC2ReplaceRouteTableAssociationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EC2ReplaceRouteTableAssociationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EC2ReplaceRouteTableAssociationAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
