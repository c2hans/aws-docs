---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-artifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Artifact
<a name="aws-resource-sagemaker-artifact"></a>

Creates an *artifact*. An artifact is a lineage tracking entity that represents a URI addressable object or data. Some examples are the S3 URI of a dataset and the ECR registry path of an image. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Syntax
<a name="aws-resource-sagemaker-artifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-artifact-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Artifact",
  "Properties" : {
      "[ArtifactName](#cfn-sagemaker-artifact-artifactname)" : {{String}},
      "[ArtifactType](#cfn-sagemaker-artifact-artifacttype)" : {{String}},
      "[MetadataProperties](#cfn-sagemaker-artifact-metadataproperties)" : {{MetadataProperties}},
      "[Properties](#cfn-sagemaker-artifact-properties)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Source](#cfn-sagemaker-artifact-source)" : {{ArtifactSource}},
      "[Tags](#cfn-sagemaker-artifact-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-artifact-syntax.yaml"></a>

```
Type: AWS::SageMaker::Artifact
Properties:
  [ArtifactName](#cfn-sagemaker-artifact-artifactname): {{String}}
  [ArtifactType](#cfn-sagemaker-artifact-artifacttype): {{String}}
  [MetadataProperties](#cfn-sagemaker-artifact-metadataproperties): {{
    MetadataProperties}}
  [Properties](#cfn-sagemaker-artifact-properties): {{
    {{Key}}: {{Value}}}}
  [Source](#cfn-sagemaker-artifact-source): {{
    ArtifactSource}}
  [Tags](#cfn-sagemaker-artifact-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-artifact-properties"></a>

`ArtifactName`  <a name="cfn-sagemaker-artifact-artifactname"></a>
The name of the artifact.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ArtifactType`  <a name="cfn-sagemaker-artifact-artifacttype"></a>
The type of the artifact.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetadataProperties`  <a name="cfn-sagemaker-artifact-metadataproperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
*Required*: No
*Type*: [MetadataProperties](aws-properties-sagemaker-artifact-metadataproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Properties`  <a name="cfn-sagemaker-artifact-properties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-sagemaker-artifact-source"></a>
The source of the artifact.
*Required*: Yes
*Type*: [ArtifactSource](aws-properties-sagemaker-artifact-artifactsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-artifact-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-artifact-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-artifact-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-artifact-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-artifact-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-artifact-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the artifact was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the artifact was last modified.
