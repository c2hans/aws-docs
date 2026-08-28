---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-alarmdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster AlarmDetails
<a name="aws-properties-sagemaker-cluster-alarmdetails"></a>

The details of the alarm to monitor during the AMI update.

## Syntax
<a name="aws-properties-sagemaker-cluster-alarmdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-alarmdetails-syntax.json"></a>

```
{
  "[AlarmName](#cfn-sagemaker-cluster-alarmdetails-alarmname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-alarmdetails-syntax.yaml"></a>

```
  [AlarmName](#cfn-sagemaker-cluster-alarmdetails-alarmname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-alarmdetails-properties"></a>

`AlarmName`  <a name="cfn-sagemaker-cluster-alarmdetails-alarmname"></a>
The name of the alarm.
*Required*: Yes
*Type*: String
*Pattern*: `(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
