---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53RecoveryControl::SafetyRule GatingRule
<a name="aws-properties-route53recoverycontrol-safetyrule-gatingrule"></a>

A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.

For example, if you specify one gating routing control and you set the `Type` in the rule configuration to `OR`, that indicates that you must set the gating routing control to `On` for the rule to evaluate as true; that is, for the gating control switch to be On. When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.

## Syntax
<a name="aws-properties-route53recoverycontrol-safetyrule-gatingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53recoverycontrol-safetyrule-gatingrule-syntax.json"></a>

```
{
  "[GatingControls](#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols)" : {{[ String, ... ]}},
  "[TargetControls](#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols)" : {{[ String, ... ]}},
  "[WaitPeriodMs](#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-route53recoverycontrol-safetyrule-gatingrule-syntax.yaml"></a>

```
  [GatingControls](#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols): {{
    - String}}
  [TargetControls](#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols): {{
    - String}}
  [WaitPeriodMs](#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms): {{Integer}}
```

## Properties
<a name="aws-properties-route53recoverycontrol-safetyrule-gatingrule-properties"></a>

`GatingControls`  <a name="cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols"></a>
An array of gating routing control Amazon Resource Names (ARNs). For a simple on-off switch, specify the ARN for one routing control. The gating routing controls are evaluated by the rule configuration that you specify to determine if the target routing control states can be changed.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`TargetControls`  <a name="cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols"></a>
An array of target routing control Amazon Resource Names (ARNs) for which the states can only be updated if the rule configuration that you specify evaluates to true for the gating routing control. As a simple example, if you have a single gating control, it acts as an overall on-off switch for a set of target routing controls. You can use this to manually override automated failover, for example.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`WaitPeriodMs`  <a name="cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms"></a>
An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent flapping of state. The wait period is 5000 ms by default, but you can choose a custom value.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
