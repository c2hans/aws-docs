---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-monitoringschedulealert.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringScheduleAlert
<a name="aws-resource-sagemaker-monitoringschedulealert"></a>

<a name="aws-resource-sagemaker-monitoringschedulealert-description"></a>The `AWS::SageMaker::MonitoringScheduleAlert` resource Property description not available. for SageMaker.

## Syntax
<a name="aws-resource-sagemaker-monitoringschedulealert-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-monitoringschedulealert-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::MonitoringScheduleAlert",
  "Properties" : {
      "[DatapointsToAlert](#cfn-sagemaker-monitoringschedulealert-datapointstoalert)" : {{Integer}},
      "[EvaluationPeriod](#cfn-sagemaker-monitoringschedulealert-evaluationperiod)" : {{Integer}},
      "[MonitoringAlertName](#cfn-sagemaker-monitoringschedulealert-monitoringalertname)" : {{String}},
      "[MonitoringScheduleName](#cfn-sagemaker-monitoringschedulealert-monitoringschedulename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-monitoringschedulealert-syntax.yaml"></a>

```
Type: AWS::SageMaker::MonitoringScheduleAlert
Properties:
  [DatapointsToAlert](#cfn-sagemaker-monitoringschedulealert-datapointstoalert): {{Integer}}
  [EvaluationPeriod](#cfn-sagemaker-monitoringschedulealert-evaluationperiod): {{Integer}}
  [MonitoringAlertName](#cfn-sagemaker-monitoringschedulealert-monitoringalertname): {{String}}
  [MonitoringScheduleName](#cfn-sagemaker-monitoringschedulealert-monitoringschedulename): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-monitoringschedulealert-properties"></a>

`DatapointsToAlert`  <a name="cfn-sagemaker-monitoringschedulealert-datapointstoalert"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EvaluationPeriod`  <a name="cfn-sagemaker-monitoringschedulealert-evaluationperiod"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MonitoringAlertName`  <a name="cfn-sagemaker-monitoringschedulealert-monitoringalertname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MonitoringScheduleName`  <a name="cfn-sagemaker-monitoringschedulealert-monitoringschedulename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-monitoringschedulealert-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-monitoringschedulealert-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-monitoringschedulealert-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-monitoringschedulealert-return-values-fn--getatt-fn--getatt"></a>

`AlertStatus`  <a name="AlertStatus-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Property description not available.
