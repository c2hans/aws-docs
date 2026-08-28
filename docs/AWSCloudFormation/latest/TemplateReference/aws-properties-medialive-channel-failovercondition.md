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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
