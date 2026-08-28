---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-renamekeyentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer RenameKeyEntry
<a name="aws-properties-logs-transformer-renamekeyentry"></a>

This object defines one key that will be renamed with the [ renameKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-renameKey) processor.

## Syntax
<a name="aws-properties-logs-transformer-renamekeyentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-renamekeyentry-syntax.json"></a>

```
{
  "[Key](#cfn-logs-transformer-renamekeyentry-key)" : {{String}},
  "[OverwriteIfExists](#cfn-logs-transformer-renamekeyentry-overwriteifexists)" : {{Boolean}},
  "[RenameTo](#cfn-logs-transformer-renamekeyentry-renameto)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-renamekeyentry-syntax.yaml"></a>

```
  [Key](#cfn-logs-transformer-renamekeyentry-key): {{String}}
  [OverwriteIfExists](#cfn-logs-transformer-renamekeyentry-overwriteifexists): {{Boolean}}
  [RenameTo](#cfn-logs-transformer-renamekeyentry-renameto): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-renamekeyentry-properties"></a>

`Key`  <a name="cfn-logs-transformer-renamekeyentry-key"></a>
The key to rename
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverwriteIfExists`  <a name="cfn-logs-transformer-renamekeyentry-overwriteifexists"></a>
Specifies whether to overwrite the existing value if the destination key already exists. The default is `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenameTo`  <a name="cfn-logs-transformer-renamekeyentry-renameto"></a>
The string to use for the new key name
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
