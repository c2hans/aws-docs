---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-rollingupdatepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster RollingUpdatePolicy
<a name="aws-properties-sagemaker-cluster-rollingupdatepolicy"></a>

Specifies a rolling deployment strategy for updating a SageMaker endpoint.

## Syntax
<a name="aws-properties-sagemaker-cluster-rollingupdatepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-rollingupdatepolicy-syntax.json"></a>

```
{
  "[MaximumBatchSize](#cfn-sagemaker-cluster-rollingupdatepolicy-maximumbatchsize)" : {{CapacitySizeConfig}},
  "[RollbackMaximumBatchSize](#cfn-sagemaker-cluster-rollingupdatepolicy-rollbackmaximumbatchsize)" : {{CapacitySizeConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-rollingupdatepolicy-syntax.yaml"></a>

```
  [MaximumBatchSize](#cfn-sagemaker-cluster-rollingupdatepolicy-maximumbatchsize): {{
    CapacitySizeConfig}}
  [RollbackMaximumBatchSize](#cfn-sagemaker-cluster-rollingupdatepolicy-rollbackmaximumbatchsize): {{
    CapacitySizeConfig}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-rollingupdatepolicy-properties"></a>

`MaximumBatchSize`  <a name="cfn-sagemaker-cluster-rollingupdatepolicy-maximumbatchsize"></a>
Batch size for each rolling step to provision capacity and turn on traffic on the new endpoint fleet, and terminate capacity on the old endpoint fleet. Value must be between 5% to 50% of the variant's total instance count.
*Required*: Yes
*Type*: [CapacitySizeConfig](aws-properties-sagemaker-cluster-capacitysizeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollbackMaximumBatchSize`  <a name="cfn-sagemaker-cluster-rollingupdatepolicy-rollbackmaximumbatchsize"></a>
Batch size for rollback to the old endpoint fleet. Each rolling step to provision capacity and turn on traffic on the old endpoint fleet, and terminate capacity on the new endpoint fleet. If this field is absent, the default value will be set to 100% of total capacity which means to bring up the whole capacity of the old fleet at once during rollback.
*Required*: No
*Type*: [CapacitySizeConfig](aws-properties-sagemaker-cluster-capacitysizeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
