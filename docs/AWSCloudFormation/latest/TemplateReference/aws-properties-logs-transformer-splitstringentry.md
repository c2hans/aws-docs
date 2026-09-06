---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-splitstringentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer SplitStringEntry
<a name="aws-properties-logs-transformer-splitstringentry"></a>

This object defines one log field that will be split with the [ splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString) processor.

## Syntax
<a name="aws-properties-logs-transformer-splitstringentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-splitstringentry-syntax.json"></a>

```
{
  "[Delimiter](#cfn-logs-transformer-splitstringentry-delimiter)" : {{String}},
  "[Source](#cfn-logs-transformer-splitstringentry-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-splitstringentry-syntax.yaml"></a>

```
  [Delimiter](#cfn-logs-transformer-splitstringentry-delimiter): {{String}}
  [Source](#cfn-logs-transformer-splitstringentry-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-splitstringentry-properties"></a>

`Delimiter`  <a name="cfn-logs-transformer-splitstringentry-delimiter"></a>
The separator characters to split the string entry on.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-splitstringentry-source"></a>
The key of the field to split.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
