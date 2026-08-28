---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-customtransformationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource CustomTransformationConfiguration
<a name="aws-properties-bedrock-datasource-customtransformationconfiguration"></a>

Settings for customizing steps in the data source content ingestion pipeline.

You can configure the data source to process documents with a Lambda function after they are parsed and converted into chunks. When you add a post-chunking transformation, the service stores chunked documents in an S3 bucket and invokes a Lambda function to process them.

To process chunked documents with a Lambda function, define an S3 bucket path for input and output objects, and a transformation that specifies the Lambda function to invoke. You can use the Lambda function to customize how chunks are split, and the metadata for each chunk.

## Syntax
<a name="aws-properties-bedrock-datasource-customtransformationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-customtransformationconfiguration-syntax.json"></a>

```
{
  "[IntermediateStorage](#cfn-bedrock-datasource-customtransformationconfiguration-intermediatestorage)" : {{IntermediateStorage}},
  "[Transformations](#cfn-bedrock-datasource-customtransformationconfiguration-transformations)" : {{[ Transformation, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-customtransformationconfiguration-syntax.yaml"></a>

```
  [IntermediateStorage](#cfn-bedrock-datasource-customtransformationconfiguration-intermediatestorage): {{
    IntermediateStorage}}
  [Transformations](#cfn-bedrock-datasource-customtransformationconfiguration-transformations): {{
    - Transformation}}
```

## Properties
<a name="aws-properties-bedrock-datasource-customtransformationconfiguration-properties"></a>

`IntermediateStorage`  <a name="cfn-bedrock-datasource-customtransformationconfiguration-intermediatestorage"></a>
An S3 bucket path for input and output objects.
*Required*: Yes
*Type*: [IntermediateStorage](aws-properties-bedrock-datasource-intermediatestorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transformations`  <a name="cfn-bedrock-datasource-customtransformationconfiguration-transformations"></a>
A Lambda function that processes documents.
*Required*: Yes
*Type*: Array of [Transformation](aws-properties-bedrock-datasource-transformation.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
