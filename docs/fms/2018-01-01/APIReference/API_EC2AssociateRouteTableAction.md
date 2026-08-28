---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EC2AssociateRouteTableAction.html
---

# EC2AssociateRouteTableAction
<a name="API_EC2AssociateRouteTableAction"></a>

The action of associating an EC2 resource, such as a subnet or internet gateway, with a route table.

## Contents
<a name="API_EC2AssociateRouteTableAction_Contents"></a>

 ** RouteTableId **   <a name="fms-Type-EC2AssociateRouteTableAction-RouteTableId"></a>
The ID of the EC2 route table that is associated with the remediation action.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** Description **   <a name="fms-Type-EC2AssociateRouteTableAction-Description"></a>
A description of the EC2 route table that is associated with the remediation action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** GatewayId **   <a name="fms-Type-EC2AssociateRouteTableAction-GatewayId"></a>
The ID of the gateway to be used with the EC2 route table that is associated with the remediation action.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

 ** SubnetId **   <a name="fms-Type-EC2AssociateRouteTableAction-SubnetId"></a>
The ID of the subnet for the EC2 route table that is associated with the remediation action.
Type: [ActionTarget](API_ActionTarget.md) object
Required: No

## See Also
<a name="API_EC2AssociateRouteTableAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EC2AssociateRouteTableAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EC2AssociateRouteTableAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EC2AssociateRouteTableAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
