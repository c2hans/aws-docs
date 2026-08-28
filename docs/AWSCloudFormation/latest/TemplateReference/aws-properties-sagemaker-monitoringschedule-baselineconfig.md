---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-baselineconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule BaselineConfig
<a name="aws-properties-sagemaker-monitoringschedule-baselineconfig"></a>

Baseline configuration used to validate that the data conforms to the specified constraints and statistics.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-baselineconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-baselineconfig-syntax.json"></a>

```
{
  "[ConstraintsResource](#cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource)" : {{ConstraintsResource}},
  "[StatisticsResource](#cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource)" : {{StatisticsResource}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-baselineconfig-syntax.yaml"></a>

```
  [ConstraintsResource](#cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource): {{
    ConstraintsResource}}
  [StatisticsResource](#cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource): {{
    StatisticsResource}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-baselineconfig-properties"></a>

`ConstraintsResource`  <a name="cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource"></a>
The Amazon S3 URI for the constraints resource.
*Required*: No
*Type*: [ConstraintsResource](aws-properties-sagemaker-monitoringschedule-constraintsresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatisticsResource`  <a name="cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource"></a>
The baseline statistics file in Amazon S3 that the current monitoring job should be validated against.
*Required*: No
*Type*: [StatisticsResource](aws-properties-sagemaker-monitoringschedule-statisticsresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
