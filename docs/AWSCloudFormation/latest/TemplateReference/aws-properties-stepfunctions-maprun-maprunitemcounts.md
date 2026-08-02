---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-maprun-maprunitemcounts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::MapRun MapRunItemCounts
<a name="aws-properties-stepfunctions-maprun-maprunitemcounts"></a>

Contains details about items that were processed in all of the child workflow executions that were started by a Map Run.

## Syntax
<a name="aws-properties-stepfunctions-maprun-maprunitemcounts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-maprun-maprunitemcounts-syntax.json"></a>

```
{
  "[Aborted](#cfn-stepfunctions-maprun-maprunitemcounts-aborted)" : {{Integer}},
  "[Failed](#cfn-stepfunctions-maprun-maprunitemcounts-failed)" : {{Integer}},
  "[FailuresNotRedrivable](#cfn-stepfunctions-maprun-maprunitemcounts-failuresnotredrivable)" : {{Integer}},
  "[Pending](#cfn-stepfunctions-maprun-maprunitemcounts-pending)" : {{Integer}},
  "[PendingRedrive](#cfn-stepfunctions-maprun-maprunitemcounts-pendingredrive)" : {{Integer}},
  "[ResultsWritten](#cfn-stepfunctions-maprun-maprunitemcounts-resultswritten)" : {{Integer}},
  "[Running](#cfn-stepfunctions-maprun-maprunitemcounts-running)" : {{Integer}},
  "[Succeeded](#cfn-stepfunctions-maprun-maprunitemcounts-succeeded)" : {{Integer}},
  "[TimedOut](#cfn-stepfunctions-maprun-maprunitemcounts-timedout)" : {{Integer}},
  "[Total](#cfn-stepfunctions-maprun-maprunitemcounts-total)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-stepfunctions-maprun-maprunitemcounts-syntax.yaml"></a>

```
  [Aborted](#cfn-stepfunctions-maprun-maprunitemcounts-aborted): {{Integer}}
  [Failed](#cfn-stepfunctions-maprun-maprunitemcounts-failed): {{Integer}}
  [FailuresNotRedrivable](#cfn-stepfunctions-maprun-maprunitemcounts-failuresnotredrivable): {{Integer}}
  [Pending](#cfn-stepfunctions-maprun-maprunitemcounts-pending): {{Integer}}
  [PendingRedrive](#cfn-stepfunctions-maprun-maprunitemcounts-pendingredrive): {{Integer}}
  [ResultsWritten](#cfn-stepfunctions-maprun-maprunitemcounts-resultswritten): {{Integer}}
  [Running](#cfn-stepfunctions-maprun-maprunitemcounts-running): {{Integer}}
  [Succeeded](#cfn-stepfunctions-maprun-maprunitemcounts-succeeded): {{Integer}}
  [TimedOut](#cfn-stepfunctions-maprun-maprunitemcounts-timedout): {{Integer}}
  [Total](#cfn-stepfunctions-maprun-maprunitemcounts-total): {{Integer}}
```

## Properties
<a name="aws-properties-stepfunctions-maprun-maprunitemcounts-properties"></a>

`Aborted`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-aborted"></a>
The total number of items processed in child workflow executions that were either stopped by the user or by Step Functions, because the Map Run failed.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Failed`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-failed"></a>
The total number of items processed in child workflow executions that have failed.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailuresNotRedrivable`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-failuresnotredrivable"></a>
The number of `FAILED`, `ABORTED`, or `TIMED_OUT` items in child workflow executions that cannot be redriven because the execution status of those child workflows is terminal. For example, child workflows with an execution status of `FAILED`, `ABORTED`, or `TIMED_OUT` and a `redriveStatus` of `NOT_REDRIVABLE`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pending`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-pending"></a>
The total number of items to process in child workflow executions that haven't started running yet.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PendingRedrive`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-pendingredrive"></a>
The number of unsuccessful items in child workflow executions currently waiting to be redriven.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultsWritten`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-resultswritten"></a>
Returns the count of items whose results were written by `ResultWriter`. For more information, see [ResultWriter](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html) in the *AWS Step Functions Developer Guide*.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Running`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-running"></a>
The total number of items being processed in child workflow executions that are currently in-progress.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Succeeded`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-succeeded"></a>
The total number of items processed in child workflow executions that have completed successfully.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedOut`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-timedout"></a>
The total number of items processed in child workflow executions that have timed out.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Total`  <a name="cfn-stepfunctions-maprun-maprunitemcounts-total"></a>
The total number of items processed in all the child workflow executions started by a Map Run.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
