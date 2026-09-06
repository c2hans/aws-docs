---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-artifact-artifactsourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Artifact ArtifactSourceType
<a name="aws-properties-sagemaker-artifact-artifactsourcetype"></a>

The ID and ID type of an artifact source.

## Syntax
<a name="aws-properties-sagemaker-artifact-artifactsourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-artifact-artifactsourcetype-syntax.json"></a>

```
{
  "[SourceIdType](#cfn-sagemaker-artifact-artifactsourcetype-sourceidtype)" : {{String}},
  "[Value](#cfn-sagemaker-artifact-artifactsourcetype-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-artifact-artifactsourcetype-syntax.yaml"></a>

```
  [SourceIdType](#cfn-sagemaker-artifact-artifactsourcetype-sourceidtype): {{String}}
  [Value](#cfn-sagemaker-artifact-artifactsourcetype-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-artifact-artifactsourcetype-properties"></a>

`SourceIdType`  <a name="cfn-sagemaker-artifact-artifactsourcetype-sourceidtype"></a>
The type of ID.
*Required*: Yes
*Type*: String
*Allowed values*: `MD5Hash | S3ETag | S3Version | Custom`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-sagemaker-artifact-artifactsourcetype-value"></a>
The ID.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
