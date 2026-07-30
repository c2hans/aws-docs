---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-updatepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment UpdatePolicy
<a name="aws-properties-batch-computeenvironment-updatepolicy"></a>

Specifies the infrastructure update policy for the Amazon EC2 compute environment. For more information about infrastructure updates, see [Updating compute environments](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *AWS Batch User Guide*.

## Syntax
<a name="aws-properties-batch-computeenvironment-updatepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-updatepolicy-syntax.json"></a>

```
{
  "[JobExecutionTimeoutMinutes](#cfn-batch-computeenvironment-updatepolicy-jobexecutiontimeoutminutes)" : {{Integer}},
  "[TerminateJobsOnUpdate](#cfn-batch-computeenvironment-updatepolicy-terminatejobsonupdate)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-updatepolicy-syntax.yaml"></a>

```
  [JobExecutionTimeoutMinutes](#cfn-batch-computeenvironment-updatepolicy-jobexecutiontimeoutminutes): {{Integer}}
  [TerminateJobsOnUpdate](#cfn-batch-computeenvironment-updatepolicy-terminatejobsonupdate): {{Boolean}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-updatepolicy-properties"></a>

`JobExecutionTimeoutMinutes`  <a name="cfn-batch-computeenvironment-updatepolicy-jobexecutiontimeoutminutes"></a>
Specifies the job timeout (in minutes) when the compute environment infrastructure is updated. The default value is 30. The maximum value is 7200.
Increasing `jobExecutionTimeoutMinutes` during infrastructure updates delays the replacement of instances with new instances that include updates such as security patches, but provides more time for jobs to execute. Consider the security implications of this tradeoff when setting timeout values.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TerminateJobsOnUpdate`  <a name="cfn-batch-computeenvironment-updatepolicy-terminatejobsonupdate"></a>
Specifies whether jobs are automatically terminated when the compute environment infrastructure is updated. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
