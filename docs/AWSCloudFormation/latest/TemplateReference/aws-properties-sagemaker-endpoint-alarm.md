---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpoint-alarm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Endpoint Alarm
<a name="aws-properties-sagemaker-endpoint-alarm"></a>

An Amazon CloudWatch alarm configured to monitor metrics on an endpoint.

## Syntax
<a name="aws-properties-sagemaker-endpoint-alarm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpoint-alarm-syntax.json"></a>

```
{
  "[AlarmName](#cfn-sagemaker-endpoint-alarm-alarmname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpoint-alarm-syntax.yaml"></a>

```
  [AlarmName](#cfn-sagemaker-endpoint-alarm-alarmname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpoint-alarm-properties"></a>

`AlarmName`  <a name="cfn-sagemaker-endpoint-alarm-alarmname"></a>
The name of a CloudWatch alarm in your account.
*Required*: Yes
*Type*: String
*Pattern*: `(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
