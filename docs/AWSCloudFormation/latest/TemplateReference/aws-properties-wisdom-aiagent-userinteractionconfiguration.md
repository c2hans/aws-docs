---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-userinteractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent UserInteractionConfiguration
<a name="aws-properties-wisdom-aiagent-userinteractionconfiguration"></a>

Configuration for user interaction settings.

## Syntax
<a name="aws-properties-wisdom-aiagent-userinteractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-userinteractionconfiguration-syntax.json"></a>

```
{
  "[IsUserConfirmationRequired](#cfn-wisdom-aiagent-userinteractionconfiguration-isuserconfirmationrequired)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-userinteractionconfiguration-syntax.yaml"></a>

```
  [IsUserConfirmationRequired](#cfn-wisdom-aiagent-userinteractionconfiguration-isuserconfirmationrequired): {{Boolean}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-userinteractionconfiguration-properties"></a>

`IsUserConfirmationRequired`  <a name="cfn-wisdom-aiagent-userinteractionconfiguration-isuserconfirmationrequired"></a>
Indicates whether user confirmation is required for the interaction.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
