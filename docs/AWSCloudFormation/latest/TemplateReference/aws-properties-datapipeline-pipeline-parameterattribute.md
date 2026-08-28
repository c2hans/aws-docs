---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datapipeline-pipeline-parameterattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataPipeline::Pipeline ParameterAttribute
<a name="aws-properties-datapipeline-pipeline-parameterattribute"></a>

`Attribute` is a property of `ParameterObject` that defines the attributes of a parameter object as key-value pairs.

## Syntax
<a name="aws-properties-datapipeline-pipeline-parameterattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datapipeline-pipeline-parameterattribute-syntax.json"></a>

```
{
  "[Key](#cfn-datapipeline-pipeline-parameterattribute-key)" : {{String}},
  "[StringValue](#cfn-datapipeline-pipeline-parameterattribute-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-datapipeline-pipeline-parameterattribute-syntax.yaml"></a>

```
  [Key](#cfn-datapipeline-pipeline-parameterattribute-key): {{String}}
  [StringValue](#cfn-datapipeline-pipeline-parameterattribute-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-datapipeline-pipeline-parameterattribute-properties"></a>

`Key`  <a name="cfn-datapipeline-pipeline-parameterattribute-key"></a>
The field identifier.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-datapipeline-pipeline-parameterattribute-stringvalue"></a>
The field value, expressed as a String.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
