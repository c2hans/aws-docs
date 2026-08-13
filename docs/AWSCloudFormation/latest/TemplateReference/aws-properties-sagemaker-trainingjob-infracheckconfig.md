---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-infracheckconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob InfraCheckConfig
<a name="aws-properties-sagemaker-trainingjob-infracheckconfig"></a>

Configuration information for the infrastructure health check of a training job. A SageMaker-provided health check tests the health of instance hardware and cluster network connectivity.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-infracheckconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-infracheckconfig-syntax.json"></a>

```
{
  "[EnableInfraCheck](#cfn-sagemaker-trainingjob-infracheckconfig-enableinfracheck)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-infracheckconfig-syntax.yaml"></a>

```
  [EnableInfraCheck](#cfn-sagemaker-trainingjob-infracheckconfig-enableinfracheck): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-infracheckconfig-properties"></a>

`EnableInfraCheck`  <a name="cfn-sagemaker-trainingjob-infracheckconfig-enableinfracheck"></a>
Enables an infrastructure health check.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
