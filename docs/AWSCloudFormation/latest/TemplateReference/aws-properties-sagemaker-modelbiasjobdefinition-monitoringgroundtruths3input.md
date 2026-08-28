---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelBiasJobDefinition MonitoringGroundTruthS3Input
<a name="aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input"></a>

The ground truth labels for the dataset used for the monitoring job.

## Syntax
<a name="aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri"></a>
The address of the Amazon S3 location of the ground truth labels.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
