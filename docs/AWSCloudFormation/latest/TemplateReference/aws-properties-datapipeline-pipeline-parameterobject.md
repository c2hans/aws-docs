---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datapipeline-pipeline-parameterobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataPipeline::Pipeline ParameterObject
<a name="aws-properties-datapipeline-pipeline-parameterobject"></a>

Contains information about a parameter object.

## Syntax
<a name="aws-properties-datapipeline-pipeline-parameterobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datapipeline-pipeline-parameterobject-syntax.json"></a>

```
{
  "[Attributes](#cfn-datapipeline-pipeline-parameterobject-attributes)" : {{[ ParameterAttribute, ... ]}},
  "[Id](#cfn-datapipeline-pipeline-parameterobject-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-datapipeline-pipeline-parameterobject-syntax.yaml"></a>

```
  [Attributes](#cfn-datapipeline-pipeline-parameterobject-attributes): {{
    - ParameterAttribute}}
  [Id](#cfn-datapipeline-pipeline-parameterobject-id): {{String}}
```

## Properties
<a name="aws-properties-datapipeline-pipeline-parameterobject-properties"></a>

`Attributes`  <a name="cfn-datapipeline-pipeline-parameterobject-attributes"></a>
The attributes of the parameter object.
*Required*: Yes
*Type*: Array of [ParameterAttribute](aws-properties-datapipeline-pipeline-parameterattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-datapipeline-pipeline-parameterobject-id"></a>
The ID of the parameter object.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
