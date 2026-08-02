---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-failovercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FailoverCondition
<a name="aws-properties-medialive-channel-failovercondition"></a>

Failover Condition settings. There can be multiple failover conditions inside AutomaticInputFailoverSettings.

The parent of this entity is AutomaticInputFailoverSettings.

## Syntax
<a name="aws-properties-medialive-channel-failovercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-failovercondition-syntax.json"></a>

```
{
  "[FailoverConditionSettings](#cfn-medialive-channel-failovercondition-failoverconditionsettings)" : {{FailoverConditionSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-failovercondition-syntax.yaml"></a>

```
  [FailoverConditionSettings](#cfn-medialive-channel-failovercondition-failoverconditionsettings): {{
    FailoverConditionSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-failovercondition-properties"></a>

`FailoverConditionSettings`  <a name="cfn-medialive-channel-failovercondition-failoverconditionsettings"></a>
Settings for a specific failover condition.
*Required*: No
*Type*: [FailoverConditionSettings](aws-properties-medialive-channel-failoverconditionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
