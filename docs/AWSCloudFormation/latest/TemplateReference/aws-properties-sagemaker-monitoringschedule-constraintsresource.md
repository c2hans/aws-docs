---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-constraintsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule ConstraintsResource
<a name="aws-properties-sagemaker-monitoringschedule-constraintsresource"></a>

The Amazon S3 URI for the constraints resource.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-constraintsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-constraintsresource-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-monitoringschedule-constraintsresource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-constraintsresource-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-monitoringschedule-constraintsresource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-constraintsresource-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-monitoringschedule-constraintsresource-s3uri"></a>
The Amazon S3 URI for the constraints resource.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
