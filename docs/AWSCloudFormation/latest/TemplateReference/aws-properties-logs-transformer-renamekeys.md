---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-renamekeys.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer RenameKeys
<a name="aws-properties-logs-transformer-renamekeys"></a>

Use this processor to rename keys in a log event.

For more information about this processor including examples, see [ renameKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-renameKeys) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-renamekeys-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-renamekeys-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-renamekeys-entries)" : {{[ RenameKeyEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-renamekeys-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-renamekeys-entries): {{
    - RenameKeyEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-renamekeys-properties"></a>

`Entries`  <a name="cfn-logs-transformer-renamekeys-entries"></a>
An array of `RenameKeyEntry` objects, where each object contains the information about a single key to rename.
*Required*: Yes
*Type*: Array of [RenameKeyEntry](aws-properties-logs-transformer-renamekeyentry.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
