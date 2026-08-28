---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule MonitoringOutput
<a name="aws-properties-sagemaker-monitoringschedule-monitoringoutput"></a>

The output object for a monitoring job.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-monitoringoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-monitoringoutput-syntax.json"></a>

```
{
  "[S3Output](#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output)" : {{S3Output}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-monitoringoutput-syntax.yaml"></a>

```
  [S3Output](#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output): {{
    S3Output}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-monitoringoutput-properties"></a>

`S3Output`  <a name="cfn-sagemaker-monitoringschedule-monitoringoutput-s3output"></a>
The Amazon S3 storage location where the results of a monitoring job are saved.
*Required*: Yes
*Type*: [S3Output](aws-properties-sagemaker-monitoringschedule-s3output.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
