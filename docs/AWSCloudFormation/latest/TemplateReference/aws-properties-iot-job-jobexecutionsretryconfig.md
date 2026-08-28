---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-jobexecutionsretryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job JobExecutionsRetryConfig
<a name="aws-properties-iot-job-jobexecutionsretryconfig"></a>

The configuration that determines how many retries are allowed for each failure type for a job.

## Syntax
<a name="aws-properties-iot-job-jobexecutionsretryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-jobexecutionsretryconfig-syntax.json"></a>

```
{
  "[CriteriaList](#cfn-iot-job-jobexecutionsretryconfig-criterialist)" : {{[ RetryCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-job-jobexecutionsretryconfig-syntax.yaml"></a>

```
  [CriteriaList](#cfn-iot-job-jobexecutionsretryconfig-criterialist): {{
    - RetryCriteria}}
```

## Properties
<a name="aws-properties-iot-job-jobexecutionsretryconfig-properties"></a>

`CriteriaList`  <a name="cfn-iot-job-jobexecutionsretryconfig-criterialist"></a>
The list of criteria that determines how many retries are allowed for each failure type for a job.
*Required*: Yes
*Type*: Array of [RetryCriteria](aws-properties-iot-job-retrycriteria.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
