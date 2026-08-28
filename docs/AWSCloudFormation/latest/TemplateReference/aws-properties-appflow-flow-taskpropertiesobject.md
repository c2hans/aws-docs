---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-taskpropertiesobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow TaskPropertiesObject
<a name="aws-properties-appflow-flow-taskpropertiesobject"></a>

 A map used to store task-related information. The execution service looks for particular information based on the `TaskType`.

## Syntax
<a name="aws-properties-appflow-flow-taskpropertiesobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-taskpropertiesobject-syntax.json"></a>

```
{
  "[Key](#cfn-appflow-flow-taskpropertiesobject-key)" : {{String}},
  "[Value](#cfn-appflow-flow-taskpropertiesobject-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-taskpropertiesobject-syntax.yaml"></a>

```
  [Key](#cfn-appflow-flow-taskpropertiesobject-key): {{String}}
  [Value](#cfn-appflow-flow-taskpropertiesobject-value): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-taskpropertiesobject-properties"></a>

`Key`  <a name="cfn-appflow-flow-taskpropertiesobject-key"></a>
 The task property key.
*Required*: Yes
*Type*: String
*Allowed values*: `VALUE | VALUES | DATA_TYPE | UPPER_BOUND | LOWER_BOUND | SOURCE_DATA_TYPE | DESTINATION_DATA_TYPE | VALIDATION_ACTION | MASK_VALUE | MASK_LENGTH | TRUNCATE_LENGTH | MATH_OPERATION_FIELDS_ORDER | CONCAT_FORMAT | SUBFIELD_CATEGORY_MAP | EXCLUDE_SOURCE_FIELDS_LIST | INCLUDE_NEW_FIELDS | ORDERED_PARTITION_KEYS_LIST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appflow-flow-taskpropertiesobject-value"></a>
 The task property value.
*Required*: Yes
*Type*: String
*Pattern*: `.+`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
