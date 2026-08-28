---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-statisticsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule StatisticsResource
<a name="aws-properties-sagemaker-monitoringschedule-statisticsresource"></a>

The baseline statistics file in Amazon S3 that the current monitoring job should be validated against.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-statisticsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-statisticsresource-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-monitoringschedule-statisticsresource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-statisticsresource-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-monitoringschedule-statisticsresource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-statisticsresource-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-monitoringschedule-statisticsresource-s3uri"></a>
The S3 URI for the statistics resource.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
