---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelQualityJobDefinition MonitoringGroundTruthS3Input
<a name="aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input"></a>

The ground truth labels for the dataset used for the monitoring job.

## Syntax
<a name="aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri"></a>
The address of the Amazon S3 location of the ground truth labels.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
