---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-retrycriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job RetryCriteria
<a name="aws-properties-iot-job-retrycriteria"></a>

The criteria that determines how many retries are allowed for each failure type for a job.

## Syntax
<a name="aws-properties-iot-job-retrycriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-retrycriteria-syntax.json"></a>

```
{
  "[FailureType](#cfn-iot-job-retrycriteria-failuretype)" : {{String}},
  "[NumberOfRetries](#cfn-iot-job-retrycriteria-numberofretries)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-job-retrycriteria-syntax.yaml"></a>

```
  [FailureType](#cfn-iot-job-retrycriteria-failuretype): {{String}}
  [NumberOfRetries](#cfn-iot-job-retrycriteria-numberofretries): {{Integer}}
```

## Properties
<a name="aws-properties-iot-job-retrycriteria-properties"></a>

`FailureType`  <a name="cfn-iot-job-retrycriteria-failuretype"></a>
The type of job execution failures that can initiate a job retry.
*Required*: Yes
*Type*: String
*Allowed values*: `FAILED | TIMED_OUT | ALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NumberOfRetries`  <a name="cfn-iot-job-retrycriteria-numberofretries"></a>
The number of retries allowed for a failure type for the job.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
