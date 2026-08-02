---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-substitutestring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer SubstituteString
<a name="aws-properties-logs-transformer-substitutestring"></a>

This processor matches a key’s value against a regular expression and replaces all matches with a replacement string.

For more information about this processor including examples, see [ substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-substitutestring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-substitutestring-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-substitutestring-entries)" : {{[ SubstituteStringEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-substitutestring-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-substitutestring-entries): {{
    - SubstituteStringEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-substitutestring-properties"></a>

`Entries`  <a name="cfn-logs-transformer-substitutestring-entries"></a>
An array of objects, where each object contains the information about one key to match and replace.
*Required*: Yes
*Type*: Array of [SubstituteStringEntry](aws-properties-logs-transformer-substitutestringentry.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
