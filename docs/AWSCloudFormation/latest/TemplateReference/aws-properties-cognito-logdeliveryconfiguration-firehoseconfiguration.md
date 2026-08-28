---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::LogDeliveryConfiguration FirehoseConfiguration
<a name="aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration"></a>

Configuration for the Amazon Data Firehose stream destination of user activity log export with threat protection.

## Syntax
<a name="aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration-syntax.json"></a>

```
{
  "[StreamArn](#cfn-cognito-logdeliveryconfiguration-firehoseconfiguration-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration-syntax.yaml"></a>

```
  [StreamArn](#cfn-cognito-logdeliveryconfiguration-firehoseconfiguration-streamarn): {{String}}
```

## Properties
<a name="aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration-properties"></a>

`StreamArn`  <a name="cfn-cognito-logdeliveryconfiguration-firehoseconfiguration-streamarn"></a>
The ARN of an Amazon Data Firehose stream that's the destination for threat protection log export.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
