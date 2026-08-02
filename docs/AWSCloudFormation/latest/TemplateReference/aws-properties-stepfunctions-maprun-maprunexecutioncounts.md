---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-maprun-maprunexecutioncounts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::MapRun MapRunExecutionCounts
<a name="aws-properties-stepfunctions-maprun-maprunexecutioncounts"></a>

Contains details about all of the child workflow executions started by a Map Run.

## Syntax
<a name="aws-properties-stepfunctions-maprun-maprunexecutioncounts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-maprun-maprunexecutioncounts-syntax.json"></a>

```
{
  "[Aborted](#cfn-stepfunctions-maprun-maprunexecutioncounts-aborted)" : {{Integer}},
  "[Failed](#cfn-stepfunctions-maprun-maprunexecutioncounts-failed)" : {{Integer}},
  "[FailuresNotRedrivable](#cfn-stepfunctions-maprun-maprunexecutioncounts-failuresnotredrivable)" : {{Integer}},
  "[Pending](#cfn-stepfunctions-maprun-maprunexecutioncounts-pending)" : {{Integer}},
  "[PendingRedrive](#cfn-stepfunctions-maprun-maprunexecutioncounts-pendingredrive)" : {{Integer}},
  "[ResultsWritten](#cfn-stepfunctions-maprun-maprunexecutioncounts-resultswritten)" : {{Integer}},
  "[Running](#cfn-stepfunctions-maprun-maprunexecutioncounts-running)" : {{Integer}},
  "[Succeeded](#cfn-stepfunctions-maprun-maprunexecutioncounts-succeeded)" : {{Integer}},
  "[TimedOut](#cfn-stepfunctions-maprun-maprunexecutioncounts-timedout)" : {{Integer}},
  "[Total](#cfn-stepfunctions-maprun-maprunexecutioncounts-total)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-stepfunctions-maprun-maprunexecutioncounts-syntax.yaml"></a>

```
  [Aborted](#cfn-stepfunctions-maprun-maprunexecutioncounts-aborted): {{Integer}}
  [Failed](#cfn-stepfunctions-maprun-maprunexecutioncounts-failed): {{Integer}}
  [FailuresNotRedrivable](#cfn-stepfunctions-maprun-maprunexecutioncounts-failuresnotredrivable): {{Integer}}
  [Pending](#cfn-stepfunctions-maprun-maprunexecutioncounts-pending): {{Integer}}
  [PendingRedrive](#cfn-stepfunctions-maprun-maprunexecutioncounts-pendingredrive): {{Integer}}
  [ResultsWritten](#cfn-stepfunctions-maprun-maprunexecutioncounts-resultswritten): {{Integer}}
  [Running](#cfn-stepfunctions-maprun-maprunexecutioncounts-running): {{Integer}}
  [Succeeded](#cfn-stepfunctions-maprun-maprunexecutioncounts-succeeded): {{Integer}}
  [TimedOut](#cfn-stepfunctions-maprun-maprunexecutioncounts-timedout): {{Integer}}
  [Total](#cfn-stepfunctions-maprun-maprunexecutioncounts-total): {{Integer}}
```

## Properties
<a name="aws-properties-stepfunctions-maprun-maprunexecutioncounts-properties"></a>

`Aborted`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-aborted"></a>
The total number of child workflow executions that were started by a Map Run and were running, but were either stopped by the user or by Step Functions because the Map Run failed.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Failed`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-failed"></a>
The total number of child workflow executions that were started by a Map Run, but have failed.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailuresNotRedrivable`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-failuresnotredrivable"></a>
The number of `FAILED`, `ABORTED`, or `TIMED_OUT` child workflow executions that cannot be redriven because their execution status is terminal. For example, child workflows with an execution status of `FAILED`, `ABORTED`, or `TIMED_OUT` and a `redriveStatus` of `NOT_REDRIVABLE`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pending`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-pending"></a>
The total number of child workflow executions that were started by a Map Run, but haven't started executing yet.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PendingRedrive`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-pendingredrive"></a>
The number of unsuccessful child workflow executions currently waiting to be redriven. The status of these child workflow executions could be `FAILED`, `ABORTED`, or `TIMED_OUT` in the original execution attempt or a previous redrive attempt.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultsWritten`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-resultswritten"></a>
Returns the count of child workflow executions whose results were written by `ResultWriter`. For more information, see [ResultWriter](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html) in the *AWS Step Functions Developer Guide*.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Running`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-running"></a>
The total number of child workflow executions that were started by a Map Run and are currently in-progress.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Succeeded`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-succeeded"></a>
The total number of child workflow executions that were started by a Map Run and have completed successfully.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedOut`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-timedout"></a>
The total number of child workflow executions that were started by a Map Run and have timed out.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Total`  <a name="cfn-stepfunctions-maprun-maprunexecutioncounts-total"></a>
The total number of child workflow executions that were started by a Map Run.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
