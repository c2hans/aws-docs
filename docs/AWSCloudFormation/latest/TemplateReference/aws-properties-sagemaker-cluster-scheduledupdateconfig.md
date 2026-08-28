---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-scheduledupdateconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ScheduledUpdateConfig
<a name="aws-properties-sagemaker-cluster-scheduledupdateconfig"></a>

The configuration object of the schedule that SageMaker follows when updating the AMI.

## Syntax
<a name="aws-properties-sagemaker-cluster-scheduledupdateconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-scheduledupdateconfig-syntax.json"></a>

```
{
  "[DeploymentConfig](#cfn-sagemaker-cluster-scheduledupdateconfig-deploymentconfig)" : {{DeploymentConfig}},
  "[ScheduleExpression](#cfn-sagemaker-cluster-scheduledupdateconfig-scheduleexpression)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-scheduledupdateconfig-syntax.yaml"></a>

```
  [DeploymentConfig](#cfn-sagemaker-cluster-scheduledupdateconfig-deploymentconfig): {{
    DeploymentConfig}}
  [ScheduleExpression](#cfn-sagemaker-cluster-scheduledupdateconfig-scheduleexpression): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-scheduledupdateconfig-properties"></a>

`DeploymentConfig`  <a name="cfn-sagemaker-cluster-scheduledupdateconfig-deploymentconfig"></a>
The configuration to use when updating the AMI versions.
*Required*: No
*Type*: [DeploymentConfig](aws-properties-sagemaker-cluster-deploymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-sagemaker-cluster-scheduledupdateconfig-scheduleexpression"></a>
A cron expression that specifies the schedule that SageMaker follows when updating the AMI.
*Required*: Yes
*Type*: String
*Pattern*: `cron\((?:[0-5][0-9]|[0-9]|) (?:[01][0-9]|2[0-3]|[0-9]) (?:[1-9]|0[1-9]|[12][0-9]|3[01]|\?) (?:[1-9]|0[1-9]|1[0-2]|\*|\*/(?:[1-9]|1[0-2])|) (?:MON|TUE|WED|THU|FRI|SAT|SUN|[1-7]|\?|L|(?:[1-7]#[1-5])|(?:[1-7]L)) (?:20[2-9][0-9]|\*|)\)`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
