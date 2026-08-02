---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedulealert-monitoringalertactions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringScheduleAlert MonitoringAlertActions
<a name="aws-properties-sagemaker-monitoringschedulealert-monitoringalertactions"></a>

A list of alert actions taken in response to an alert going into `InAlert` status.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedulealert-monitoringalertactions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedulealert-monitoringalertactions-syntax.json"></a>

```
{
  "[ModelDashboardIndicator](#cfn-sagemaker-monitoringschedulealert-monitoringalertactions-modeldashboardindicator)" : {{ModelDashboardIndicatorAction}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedulealert-monitoringalertactions-syntax.yaml"></a>

```
  [ModelDashboardIndicator](#cfn-sagemaker-monitoringschedulealert-monitoringalertactions-modeldashboardindicator): {{
    ModelDashboardIndicatorAction}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedulealert-monitoringalertactions-properties"></a>

`ModelDashboardIndicator`  <a name="cfn-sagemaker-monitoringschedulealert-monitoringalertactions-modeldashboardindicator"></a>
An alert action taken to light up an icon on the Model Dashboard when an alert goes into `InAlert` status.
*Required*: No
*Type*: [ModelDashboardIndicatorAction](aws-properties-sagemaker-monitoringschedulealert-modeldashboardindicatoraction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
