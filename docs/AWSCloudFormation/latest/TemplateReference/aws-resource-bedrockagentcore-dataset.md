---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Dataset
<a name="aws-resource-bedrockagentcore-dataset"></a>

Specifies a dataset for Amazon Bedrock AgentCore. A dataset stores collections of examples used for agent evaluation, including inline examples or references to JSONL files in Amazon S3.

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-dataset-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Dataset",
  "Properties" : {
      "[DatasetName](#cfn-bedrockagentcore-dataset-datasetname)" : {{String}},
      "[Description](#cfn-bedrockagentcore-dataset-description)" : {{String}},
      "[KmsKeyArn](#cfn-bedrockagentcore-dataset-kmskeyarn)" : {{String}},
      "[SchemaType](#cfn-bedrockagentcore-dataset-schematype)" : {{String}},
      "[Source](#cfn-bedrockagentcore-dataset-source)" : {{DataSourceType}},
      "[Tags](#cfn-bedrockagentcore-dataset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-dataset-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Dataset
Properties:
  [DatasetName](#cfn-bedrockagentcore-dataset-datasetname): {{String}}
  [Description](#cfn-bedrockagentcore-dataset-description): {{String}}
  [KmsKeyArn](#cfn-bedrockagentcore-dataset-kmskeyarn): {{String}}
  [SchemaType](#cfn-bedrockagentcore-dataset-schematype): {{String}}
  [Source](#cfn-bedrockagentcore-dataset-source): {{
    DataSourceType}}
  [Tags](#cfn-bedrockagentcore-dataset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-dataset-properties"></a>

`DatasetName`  <a name="cfn-bedrockagentcore-dataset-datasetname"></a>
 Human-readable name for the dataset. Must be unique within the account. Immutable after creation.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrockagentcore-dataset-description"></a>
 A description of the dataset.
*Required*: No
*Type*: String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-bedrockagentcore-dataset-kmskeyarn"></a>
 Optional AWS KMS key ARN for server-side encryption on service Amazon S3 writes.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaType`  <a name="cfn-bedrockagentcore-dataset-schematype"></a>
 Versioned schema type governing the structure of examples. Immutable after creation.
*Required*: Yes
*Type*: String
*Allowed values*: `AGENTCORE_EVALUATION_PREDEFINED_V1 | AGENTCORE_EVALUATION_SIMULATED_V1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-bedrockagentcore-dataset-source"></a>
 Source of initial examples. Provide either inline examples or an S3 URI pointing to a JSONL file.
*Required*: No
*Type*: [DataSourceType](aws-properties-bedrockagentcore-dataset-datasourcetype.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-dataset-tags"></a>
 A map of tag keys and values to assign to the dataset.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-dataset-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-dataset-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-dataset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-dataset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-dataset-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the dataset was created.

`DatasetArn`  <a name="DatasetArn-fn::getatt"></a>
Property description not available.

`DatasetId`  <a name="DatasetId-fn::getatt"></a>
Property description not available.

`ExampleCount`  <a name="ExampleCount-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the dataset was last updated.
