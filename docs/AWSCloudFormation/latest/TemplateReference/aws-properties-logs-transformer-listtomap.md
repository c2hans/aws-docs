---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-listtomap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ListToMap
<a name="aws-properties-logs-transformer-listtomap"></a>

This processor takes a list of objects that contain key fields, and converts them into a map of target keys.

For more information about this processor including examples, see [ listToMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-listtomap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-listtomap-syntax.json"></a>

```
{
  "[Flatten](#cfn-logs-transformer-listtomap-flatten)" : {{Boolean}},
  "[FlattenedElement](#cfn-logs-transformer-listtomap-flattenedelement)" : {{String}},
  "[Key](#cfn-logs-transformer-listtomap-key)" : {{String}},
  "[Source](#cfn-logs-transformer-listtomap-source)" : {{String}},
  "[Target](#cfn-logs-transformer-listtomap-target)" : {{String}},
  "[ValueKey](#cfn-logs-transformer-listtomap-valuekey)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-listtomap-syntax.yaml"></a>

```
  [Flatten](#cfn-logs-transformer-listtomap-flatten): {{Boolean}}
  [FlattenedElement](#cfn-logs-transformer-listtomap-flattenedelement): {{String}}
  [Key](#cfn-logs-transformer-listtomap-key): {{String}}
  [Source](#cfn-logs-transformer-listtomap-source): {{String}}
  [Target](#cfn-logs-transformer-listtomap-target): {{String}}
  [ValueKey](#cfn-logs-transformer-listtomap-valuekey): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-listtomap-properties"></a>

`Flatten`  <a name="cfn-logs-transformer-listtomap-flatten"></a>
A Boolean value to indicate whether the list will be flattened into single items. Specify `true` to flatten the list. The default is `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlattenedElement`  <a name="cfn-logs-transformer-listtomap-flattenedelement"></a>
If you set `flatten` to `true`, use `flattenedElement` to specify which element, `first` or `last`, to keep.
You must specify this parameter if `flatten` is `true`
*Required*: No
*Type*: String
*Allowed values*: `first | last`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-logs-transformer-listtomap-key"></a>
The key of the field to be extracted as keys in the generated map
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-listtomap-source"></a>
The key in the log event that has a list of objects that will be converted to a map.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-logs-transformer-listtomap-target"></a>
The key of the field that will hold the generated map
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueKey`  <a name="cfn-logs-transformer-listtomap-valuekey"></a>
If this is specified, the values that you specify in this parameter will be extracted from the `source` objects and put into the values of the generated map. Otherwise, original objects in the source list will be put into the values of the generated map.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
