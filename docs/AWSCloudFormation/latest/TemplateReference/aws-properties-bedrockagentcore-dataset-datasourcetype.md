---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-dataset-datasourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Dataset DataSourceType
<a name="aws-properties-bedrockagentcore-dataset-datasourcetype"></a>

 Source of examples to add to the dataset.

## Syntax
<a name="aws-properties-bedrockagentcore-dataset-datasourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-dataset-datasourcetype-syntax.json"></a>

```
{
  "[InlineExamples](#cfn-bedrockagentcore-dataset-datasourcetype-inlineexamples)" : {{InlineExamplesSource}},
  "[S3Source](#cfn-bedrockagentcore-dataset-datasourcetype-s3source)" : {{S3Source}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-dataset-datasourcetype-syntax.yaml"></a>

```
  [InlineExamples](#cfn-bedrockagentcore-dataset-datasourcetype-inlineexamples): {{
    InlineExamplesSource}}
  [S3Source](#cfn-bedrockagentcore-dataset-datasourcetype-s3source): {{
    S3Source}}
```

## Properties
<a name="aws-properties-bedrockagentcore-dataset-datasourcetype-properties"></a>

`InlineExamples`  <a name="cfn-bedrockagentcore-dataset-datasourcetype-inlineexamples"></a>
 Inline examples provided directly in the request body.
*Required*: No
*Type*: [InlineExamplesSource](aws-properties-bedrockagentcore-dataset-inlineexamplessource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Source`  <a name="cfn-bedrockagentcore-dataset-datasourcetype-s3source"></a>
 Amazon S3 URI pointing to a JSONL file in the customer's bucket.
*Required*: No
*Type*: [S3Source](aws-properties-bedrockagentcore-dataset-s3source.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
