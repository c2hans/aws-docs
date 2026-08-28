---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-job-executionproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Job ExecutionProperty
<a name="aws-properties-glue-job-executionproperty"></a>

An execution property of a job.

## Syntax
<a name="aws-properties-glue-job-executionproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-job-executionproperty-syntax.json"></a>

```
{
  "[MaxConcurrentRuns](#cfn-glue-job-executionproperty-maxconcurrentruns)" : {{Number}}
}
```

### YAML
<a name="aws-properties-glue-job-executionproperty-syntax.yaml"></a>

```
  [MaxConcurrentRuns](#cfn-glue-job-executionproperty-maxconcurrentruns): {{Number}}
```

## Properties
<a name="aws-properties-glue-job-executionproperty-properties"></a>

`MaxConcurrentRuns`  <a name="cfn-glue-job-executionproperty-maxconcurrentruns"></a>
The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
