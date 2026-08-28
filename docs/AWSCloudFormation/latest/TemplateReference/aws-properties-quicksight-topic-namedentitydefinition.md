---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-namedentitydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic NamedEntityDefinition
<a name="aws-properties-quicksight-topic-namedentitydefinition"></a>

A structure that represents a named entity.

## Syntax
<a name="aws-properties-quicksight-topic-namedentitydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-namedentitydefinition-syntax.json"></a>

```
{
  "[FieldName](#cfn-quicksight-topic-namedentitydefinition-fieldname)" : {{String}},
  "[Metric](#cfn-quicksight-topic-namedentitydefinition-metric)" : {{NamedEntityDefinitionMetric}},
  "[PropertyName](#cfn-quicksight-topic-namedentitydefinition-propertyname)" : {{String}},
  "[PropertyRole](#cfn-quicksight-topic-namedentitydefinition-propertyrole)" : {{String}},
  "[PropertyUsage](#cfn-quicksight-topic-namedentitydefinition-propertyusage)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-namedentitydefinition-syntax.yaml"></a>

```
  [FieldName](#cfn-quicksight-topic-namedentitydefinition-fieldname): {{String}}
  [Metric](#cfn-quicksight-topic-namedentitydefinition-metric): {{
    NamedEntityDefinitionMetric}}
  [PropertyName](#cfn-quicksight-topic-namedentitydefinition-propertyname): {{String}}
  [PropertyRole](#cfn-quicksight-topic-namedentitydefinition-propertyrole): {{String}}
  [PropertyUsage](#cfn-quicksight-topic-namedentitydefinition-propertyusage): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-namedentitydefinition-properties"></a>

`FieldName`  <a name="cfn-quicksight-topic-namedentitydefinition-fieldname"></a>
The name of the entity.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metric`  <a name="cfn-quicksight-topic-namedentitydefinition-metric"></a>
The definition of a metric.
*Required*: No
*Type*: [NamedEntityDefinitionMetric](aws-properties-quicksight-topic-namedentitydefinitionmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyName`  <a name="cfn-quicksight-topic-namedentitydefinition-propertyname"></a>
The property name to be used for the named entity.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyRole`  <a name="cfn-quicksight-topic-namedentitydefinition-propertyrole"></a>
The property role. Valid values for this structure are `PRIMARY` and `ID`.
*Required*: No
*Type*: String
*Allowed values*: `PRIMARY | ID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyUsage`  <a name="cfn-quicksight-topic-namedentitydefinition-propertyusage"></a>
The property usage. Valid values for this structure are `INHERIT`, `DIMENSION`, and `MEASURE`.
*Required*: No
*Type*: String
*Allowed values*: `INHERIT | DIMENSION | MEASURE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
