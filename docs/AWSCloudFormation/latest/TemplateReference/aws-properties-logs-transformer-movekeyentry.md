---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-movekeyentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer MoveKeyEntry
<a name="aws-properties-logs-transformer-movekeyentry"></a>

This object defines one key that will be moved with the [ moveKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKey) processor.

## Syntax
<a name="aws-properties-logs-transformer-movekeyentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-movekeyentry-syntax.json"></a>

```
{
  "[OverwriteIfExists](#cfn-logs-transformer-movekeyentry-overwriteifexists)" : {{Boolean}},
  "[Source](#cfn-logs-transformer-movekeyentry-source)" : {{String}},
  "[Target](#cfn-logs-transformer-movekeyentry-target)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-movekeyentry-syntax.yaml"></a>

```
  [OverwriteIfExists](#cfn-logs-transformer-movekeyentry-overwriteifexists): {{Boolean}}
  [Source](#cfn-logs-transformer-movekeyentry-source): {{String}}
  [Target](#cfn-logs-transformer-movekeyentry-target): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-movekeyentry-properties"></a>

`OverwriteIfExists`  <a name="cfn-logs-transformer-movekeyentry-overwriteifexists"></a>
Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-movekeyentry-source"></a>
The key to move.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-logs-transformer-movekeyentry-target"></a>
The key to move to.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
