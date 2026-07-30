---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-retrystrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition RetryStrategy
<a name="aws-properties-batch-jobdefinition-retrystrategy"></a>

The retry strategy that's associated with a job. For more information, see [Automated job retries](https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html) in the *AWS Batch User Guide*.

## Syntax
<a name="aws-properties-batch-jobdefinition-retrystrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-retrystrategy-syntax.json"></a>

```
{
  "[Attempts](#cfn-batch-jobdefinition-retrystrategy-attempts)" : {{Integer}},
  "[EvaluateOnExit](#cfn-batch-jobdefinition-retrystrategy-evaluateonexit)" : {{[ EvaluateOnExit, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-retrystrategy-syntax.yaml"></a>

```
  [Attempts](#cfn-batch-jobdefinition-retrystrategy-attempts): {{Integer}}
  [EvaluateOnExit](#cfn-batch-jobdefinition-retrystrategy-evaluateonexit): {{
    - EvaluateOnExit}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-retrystrategy-properties"></a>

`Attempts`  <a name="cfn-batch-jobdefinition-retrystrategy-attempts"></a>
The number of times to move a job to the `RUNNABLE` status. You can specify between 1 and 10 attempts. If the value of `attempts` is greater than one, the job is retried on failure the same number of attempts as the value.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluateOnExit`  <a name="cfn-batch-jobdefinition-retrystrategy-evaluateonexit"></a>
Array of up to 5 objects that specify the conditions where jobs are retried or failed. If this parameter is specified, then the `attempts` parameter must also be specified. If none of the listed conditions match, then the job is retried.
*Required*: No
*Type*: [Array](aws-properties-batch-jobdefinition-evaluateonexit.md) of [EvaluateOnExit](aws-properties-batch-jobdefinition-evaluateonexit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-batch-jobdefinition-retrystrategy--examples"></a>

### Retrying jobs
<a name="aws-properties-batch-jobdefinition-retrystrategy--examples--Retrying_jobs"></a>

This example will retry the job attempt up to 3 times if the job status reason is either `AGENT` or `Task failed to start`. The final rule matches all other job failures and exits. If none of the entries in `EvaluateOnExit` match the job failure, the job will be retried.

#### JSON
<a name="aws-properties-batch-jobdefinition-retrystrategy--examples--Retrying_jobs--json"></a>

```
{
  "Attempts": 3,
  "EvaluateOnExit": [
    {
      "Action": "RETRY",
      "OnReason": "AGENT"
    },
    {
      "Action": "RETRY",
      "OnReason": "Task failed to start"
    },
    {
      "Action": "EXIT",
      "OnReason": "*"
    }
  ]
}
```

#### YAML
<a name="aws-properties-batch-jobdefinition-retrystrategy--examples--Retrying_jobs--yaml"></a>

```
Attempts: 3
EvaluateOnExit:
  - Action: RETRY
    OnReason: AGENT
  - Action: RETRY
    OnReason: Task failed to start
  - Action: EXIT
    OnReason: '*'
```
