---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53recoverycontrol-controlpanel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53RecoveryControl::ControlPanel
<a name="aws-resource-route53recoverycontrol-controlpanel"></a>

Creates a new control panel in Amazon Route 53 Application Recovery Controller. A control panel represents a group of routing controls that can be changed together in a single transaction. You can use a control panel to centrally view the operational status of applications across your organization, and trigger multi-app failovers in a single transaction, for example, to fail over from one AWS Region (cell) to another.

## Syntax
<a name="aws-resource-route53recoverycontrol-controlpanel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53recoverycontrol-controlpanel-syntax.json"></a>

```
{
  "Type" : "AWS::Route53RecoveryControl::ControlPanel",
  "Properties" : {
      "[ClusterArn](#cfn-route53recoverycontrol-controlpanel-clusterarn)" : {{String}},
      "[Name](#cfn-route53recoverycontrol-controlpanel-name)" : {{String}},
      "[Tags](#cfn-route53recoverycontrol-controlpanel-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53recoverycontrol-controlpanel-syntax.yaml"></a>

```
Type: AWS::Route53RecoveryControl::ControlPanel
Properties:
  [ClusterArn](#cfn-route53recoverycontrol-controlpanel-clusterarn): {{String}}
  [Name](#cfn-route53recoverycontrol-controlpanel-name): {{String}}
  [Tags](#cfn-route53recoverycontrol-controlpanel-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53recoverycontrol-controlpanel-properties"></a>

`ClusterArn`  <a name="cfn-route53recoverycontrol-controlpanel-clusterarn"></a>
The Amazon Resource Name (ARN) of the cluster for the control panel.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9:\/_-]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53recoverycontrol-controlpanel-name"></a>
The name of the control panel. You can use any non-white space character in the name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53recoverycontrol-controlpanel-tags"></a>
The tags associated with the control panel.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53recoverycontrol-controlpanel-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53recoverycontrol-controlpanel-return-values"></a>

### Ref
<a name="aws-resource-route53recoverycontrol-controlpanel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ControlPanelArn` object.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53recoverycontrol-controlpanel-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53recoverycontrol-controlpanel-return-values-fn--getatt-fn--getatt"></a>

`ControlPanelArn`  <a name="ControlPanelArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the control panel.

`DefaultControlPanel`  <a name="DefaultControlPanel-fn::getatt"></a>
The boolean flag that is set to true for the default control panel in the cluster.

`RoutingControlCount`  <a name="RoutingControlCount-fn::getatt"></a>
The number of routing controls in the control panel.

`Status`  <a name="Status-fn::getatt"></a>
The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
