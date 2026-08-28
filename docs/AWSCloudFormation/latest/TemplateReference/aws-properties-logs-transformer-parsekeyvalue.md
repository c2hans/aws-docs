---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parsekeyvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParseKeyValue
<a name="aws-properties-logs-transformer-parsekeyvalue"></a>

This processor parses a specified field in the original log event into key-value pairs.

For more information about this processor including examples, see [ parseKeyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-parsekeyvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parsekeyvalue-syntax.json"></a>

```
{
  "[Destination](#cfn-logs-transformer-parsekeyvalue-destination)" : {{String}},
  "[FieldDelimiter](#cfn-logs-transformer-parsekeyvalue-fielddelimiter)" : {{String}},
  "[KeyPrefix](#cfn-logs-transformer-parsekeyvalue-keyprefix)" : {{String}},
  "[KeyValueDelimiter](#cfn-logs-transformer-parsekeyvalue-keyvaluedelimiter)" : {{String}},
  "[NonMatchValue](#cfn-logs-transformer-parsekeyvalue-nonmatchvalue)" : {{String}},
  "[OverwriteIfExists](#cfn-logs-transformer-parsekeyvalue-overwriteifexists)" : {{Boolean}},
  "[Source](#cfn-logs-transformer-parsekeyvalue-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parsekeyvalue-syntax.yaml"></a>

```
  [Destination](#cfn-logs-transformer-parsekeyvalue-destination): {{String}}
  [FieldDelimiter](#cfn-logs-transformer-parsekeyvalue-fielddelimiter): {{String}}
  [KeyPrefix](#cfn-logs-transformer-parsekeyvalue-keyprefix): {{String}}
  [KeyValueDelimiter](#cfn-logs-transformer-parsekeyvalue-keyvaluedelimiter): {{String}}
  [NonMatchValue](#cfn-logs-transformer-parsekeyvalue-nonmatchvalue): {{String}}
  [OverwriteIfExists](#cfn-logs-transformer-parsekeyvalue-overwriteifexists): {{Boolean}}
  [Source](#cfn-logs-transformer-parsekeyvalue-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parsekeyvalue-properties"></a>

`Destination`  <a name="cfn-logs-transformer-parsekeyvalue-destination"></a>
The destination field to put the extracted key-value pairs into
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldDelimiter`  <a name="cfn-logs-transformer-parsekeyvalue-fielddelimiter"></a>
The field delimiter string that is used between key-value pairs in the original log events. If you omit this, the ampersand `&` character is used.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPrefix`  <a name="cfn-logs-transformer-parsekeyvalue-keyprefix"></a>
If you want to add a prefix to all transformed keys, specify it here.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyValueDelimiter`  <a name="cfn-logs-transformer-parsekeyvalue-keyvaluedelimiter"></a>
The delimiter string to use between the key and value in each pair in the transformed log event.
 If you omit this, the equal `=` character is used.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NonMatchValue`  <a name="cfn-logs-transformer-parsekeyvalue-nonmatchvalue"></a>
A value to insert into the value field in the result, when a key-value pair is not successfully split.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverwriteIfExists`  <a name="cfn-logs-transformer-parsekeyvalue-overwriteifexists"></a>
Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-parsekeyvalue-source"></a>
Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, `store.book`
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
