---
source_url: https://docs.aws.amazon.com/routing-control/latest/APIReference/API_RoutingControl.html
---

# RoutingControl
<a name="API_RoutingControl"></a>

A routing control, which is a simple on/off switch that you can use to route traffic to cells. When a routing control state is set to ON, traffic flows to a cell. When the state is set to OFF, traffic does not flow.

## Contents
<a name="API_RoutingControl_Contents"></a>

 ** ControlPanelArn **   <a name="r53recovery-Type-RoutingControl-ControlPanelArn"></a>
The Amazon Resource Name (ARN) of the control panel where the routing control is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Za-z0-9:.\/_-]*$`
Required: No

 ** ControlPanelName **   <a name="r53recovery-Type-RoutingControl-ControlPanelName"></a>
The name of the control panel where the routing control is located. Only ASCII characters are supported for control panel names.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^\S+$`
Required: No

 ** Owner **   <a name="r53recovery-Type-RoutingControl-Owner"></a>
The AWS account ID of the routing control owner.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** RoutingControlArn **   <a name="r53recovery-Type-RoutingControl-RoutingControlArn"></a>
The Amazon Resource Name (ARN) of the routing control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Za-z0-9:.\/_-]*$`
Required: No

 ** RoutingControlName **   <a name="r53recovery-Type-RoutingControl-RoutingControlName"></a>
The name of the routing control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^\S+$`
Required: No

 ** RoutingControlState **   <a name="r53recovery-Type-RoutingControl-RoutingControlState"></a>
The current state of the routing control. When a routing control state is set to ON, traffic flows to a cell. When the state is set to OFF, traffic does not flow.
Type: String
Valid Values: `On | Off`
Required: No

## See Also
<a name="API_RoutingControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-recovery-cluster-2019-12-02/RoutingControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-recovery-cluster-2019-12-02/RoutingControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-recovery-cluster-2019-12-02/RoutingControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query routing-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
