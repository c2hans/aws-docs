---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringScheduleAlert ModelDashboardIndicatorAction
<a name="aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction"></a>

An alert action taken to light up an icon on the Amazon SageMaker Model Dashboard when an alert goes into `InAlert` status.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-syntax.json"></a>

```
{
  "[Enabled](#cfn-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-syntax.yaml"></a>

```
  [Enabled](#cfn-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-properties"></a>

`Enabled`  <a name="cfn-sagemaker-monitoringschedulealert-modeldashboardindicatoraction-enabled"></a>
Indicates whether the alert action is turned on.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
