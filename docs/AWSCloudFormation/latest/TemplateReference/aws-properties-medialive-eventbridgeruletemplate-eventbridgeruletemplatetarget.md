---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::EventBridgeRuleTemplate EventBridgeRuleTemplateTarget
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget"></a>

The target to which to send matching events.

## Syntax
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-syntax.json"></a>

```
{
  "[Arn](#cfn-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-syntax.yaml"></a>

```
  [Arn](#cfn-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-arn): {{String}}
```

## Properties
<a name="aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-properties"></a>

`Arn`  <a name="cfn-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget-arn"></a>
Target ARNs must be either an SNS topic or CloudWatch log group.
*Required*: Yes
*Type*: String
*Pattern*: `^arn.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
