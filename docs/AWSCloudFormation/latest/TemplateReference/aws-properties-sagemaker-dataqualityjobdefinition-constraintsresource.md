---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition ConstraintsResource
<a name="aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource"></a>

The constraints resource for a monitoring job.

## Syntax
<a name="aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri"></a>
The Amazon S3 URI for the constraints resource.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
