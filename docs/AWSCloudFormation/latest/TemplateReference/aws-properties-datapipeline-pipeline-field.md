---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datapipeline-pipeline-field.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataPipeline::Pipeline Field
<a name="aws-properties-datapipeline-pipeline-field"></a>

A key-value pair that describes a property of a `PipelineObject`. The value is specified as either a string value (`StringValue`) or a reference to another object (`RefValue`) but not as both. To view fields for a data pipeline object, see [Pipeline Object Reference](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-objects.html) in the *AWS Data Pipeline Developer Guide*.

## Syntax
<a name="aws-properties-datapipeline-pipeline-field-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datapipeline-pipeline-field-syntax.json"></a>

```
{
  "[Key](#cfn-datapipeline-pipeline-field-key)" : {{String}},
  "[RefValue](#cfn-datapipeline-pipeline-field-refvalue)" : {{String}},
  "[StringValue](#cfn-datapipeline-pipeline-field-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-datapipeline-pipeline-field-syntax.yaml"></a>

```
  [Key](#cfn-datapipeline-pipeline-field-key): {{String}}
  [RefValue](#cfn-datapipeline-pipeline-field-refvalue): {{String}}
  [StringValue](#cfn-datapipeline-pipeline-field-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-datapipeline-pipeline-field-properties"></a>

`Key`  <a name="cfn-datapipeline-pipeline-field-key"></a>
Specifies the name of a field for a particular object. To view valid values for a particular field, see [Pipeline Object Reference](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-objects.html) in the *AWS Data Pipeline Developer Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefValue`  <a name="cfn-datapipeline-pipeline-field-refvalue"></a>
A field value that you specify as an identifier of another object in the same pipeline definition.
You can specify the field value as either a string value (`StringValue`) or a reference to another object (`RefValue`), but not both.
Required if the key that you are using requires it.
*Required*: Conditional
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-datapipeline-pipeline-field-stringvalue"></a>
A field value that you specify as a string. To view valid values for a particular field, see [Pipeline Object Reference](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-pipeline-objects.html) in the *AWS Data Pipeline Developer Guide*.
You can specify the field value as either a string value (`StringValue`) or a reference to another object (`RefValue`), but not both.
Required if the key that you are using requires it.
*Required*: Conditional
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
