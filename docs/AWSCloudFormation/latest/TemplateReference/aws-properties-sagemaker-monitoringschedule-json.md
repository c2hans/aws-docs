---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-json.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule Json
<a name="aws-properties-sagemaker-monitoringschedule-json"></a>

The JSON dataset format configuration.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-json-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-json-syntax.json"></a>

```
{
  "[Line](#cfn-sagemaker-monitoringschedule-json-line)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-json-syntax.yaml"></a>

```
  [Line](#cfn-sagemaker-monitoringschedule-json-line): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-json-properties"></a>

`Line`  <a name="cfn-sagemaker-monitoringschedule-json-line"></a>
Indicates whether the JSON data is in line-delimited format.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
