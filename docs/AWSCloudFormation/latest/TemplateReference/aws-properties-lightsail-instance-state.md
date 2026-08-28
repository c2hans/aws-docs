---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-instance-state.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Instance State
<a name="aws-properties-lightsail-instance-state"></a>

`State` is a property of the [AWS::Lightsail::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html) resource. It describes the status code and the state (for example, `running`) of an instance.

## Syntax
<a name="aws-properties-lightsail-instance-state-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-instance-state-syntax.json"></a>

```
{
  "[Code](#cfn-lightsail-instance-state-code)" : {{Integer}},
  "[Name](#cfn-lightsail-instance-state-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-instance-state-syntax.yaml"></a>

```
  [Code](#cfn-lightsail-instance-state-code): {{Integer}}
  [Name](#cfn-lightsail-instance-state-name): {{String}}
```

## Properties
<a name="aws-properties-lightsail-instance-state-properties"></a>

`Code`  <a name="cfn-lightsail-instance-state-code"></a>
The status code of the instance.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lightsail-instance-state-name"></a>
The state of the instance (for example, `running` or `pending`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
