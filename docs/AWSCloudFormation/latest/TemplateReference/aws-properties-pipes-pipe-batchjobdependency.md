---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-batchjobdependency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe BatchJobDependency
<a name="aws-properties-pipes-pipe-batchjobdependency"></a>

An object that represents an AWS Batch job dependency.

## Syntax
<a name="aws-properties-pipes-pipe-batchjobdependency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-batchjobdependency-syntax.json"></a>

```
{
  "[JobId](#cfn-pipes-pipe-batchjobdependency-jobid)" : {{String}},
  "[Type](#cfn-pipes-pipe-batchjobdependency-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-batchjobdependency-syntax.yaml"></a>

```
  [JobId](#cfn-pipes-pipe-batchjobdependency-jobid): {{String}}
  [Type](#cfn-pipes-pipe-batchjobdependency-type): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-batchjobdependency-properties"></a>

`JobId`  <a name="cfn-pipes-pipe-batchjobdependency-jobid"></a>
The job ID of the AWS Batch job that's associated with this dependency.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-pipes-pipe-batchjobdependency-type"></a>
The type of the job dependency.
*Required*: No
*Type*: String
*Allowed values*: `N_TO_N | SEQUENTIAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
