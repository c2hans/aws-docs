---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-transformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource Transformation
<a name="aws-properties-bedrock-datasource-transformation"></a>

A custom processing step for documents moving through a data source ingestion pipeline. To process documents after they have been converted into chunks, set the step to apply to `POST_CHUNKING`.

## Syntax
<a name="aws-properties-bedrock-datasource-transformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-transformation-syntax.json"></a>

```
{
  "[StepToApply](#cfn-bedrock-datasource-transformation-steptoapply)" : {{String}},
  "[TransformationFunction](#cfn-bedrock-datasource-transformation-transformationfunction)" : {{TransformationFunction}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-transformation-syntax.yaml"></a>

```
  [StepToApply](#cfn-bedrock-datasource-transformation-steptoapply): {{String}}
  [TransformationFunction](#cfn-bedrock-datasource-transformation-transformationfunction): {{
    TransformationFunction}}
```

## Properties
<a name="aws-properties-bedrock-datasource-transformation-properties"></a>

`StepToApply`  <a name="cfn-bedrock-datasource-transformation-steptoapply"></a>
When the service applies the transformation.
*Required*: Yes
*Type*: String
*Allowed values*: `POST_CHUNKING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransformationFunction`  <a name="cfn-bedrock-datasource-transformation-transformationfunction"></a>
A Lambda function that processes documents.
*Required*: Yes
*Type*: [TransformationFunction](aws-properties-bedrock-datasource-transformationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
