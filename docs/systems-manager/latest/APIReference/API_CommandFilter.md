---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CommandFilter.html
---

# CommandFilter
<a name="API_CommandFilter"></a>

Describes a command filter.

**Note**
A managed node ID can't be specified when a command status is `Pending` because the command hasn't run on the node yet.

## Contents
<a name="API_CommandFilter_Contents"></a>

 ** key **   <a name="systemsmanager-Type-CommandFilter-key"></a>
The name of the filter.
The `ExecutionStage` filter can't be used with the `ListCommandInvocations` operation, only with `ListCommands`.
Type: String
Valid Values: `InvokedAfter | InvokedBefore | Status | ExecutionStage | DocumentName`
Required: Yes

 ** value **   <a name="systemsmanager-Type-CommandFilter-value"></a>
The filter value. Valid values for each filter key are as follows:
+  **InvokedAfter**: Specify a timestamp to limit your results. For example, specify `2024-07-07T00:00:00Z` to see a list of command executions occurring July 7, 2021, and later.
+  **InvokedBefore**: Specify a timestamp to limit your results. For example, specify `2024-07-07T00:00:00Z` to see a list of command executions from before July 7, 2021.
+  **Status**: Specify a valid command status to see a list of all command executions with that status. The status choices depend on the API you call.

  The status values you can specify for `ListCommands` are:
  +  `Pending`
  +  `InProgress`
  +  `Success`
  +  `Cancelled`
  +  `Failed`
  +  `TimedOut` (this includes both Delivery and Execution time outs)
  +  `AccessDenied`
  +  `DeliveryTimedOut`
  +  `ExecutionTimedOut`
  +  `Incomplete`
  +  `NoInstancesInTag`
  +  `LimitExceeded`

  The status values you can specify for `ListCommandInvocations` are:
  +  `Pending`
  +  `InProgress`
  +  `Delayed`
  +  `Success`
  +  `Cancelled`
  +  `Failed`
  +  `TimedOut` (this includes both Delivery and Execution time outs)
  +  `AccessDenied`
  +  `DeliveryTimedOut`
  +  `ExecutionTimedOut`
  +  `Undeliverable`
  +  `InvalidPlatform`
  +  `Terminated`
+  **DocumentName**: Specify name of the AWS Systems Manager document (SSM document) for which you want to see command execution results. For example, specify `AWS-RunPatchBaseline` to see command executions that used this SSM document to perform security patching operations on managed nodes.
+  **ExecutionStage**: Specify one of the following values (`ListCommands` operations only):
  +  `Executing`: Returns a list of command executions that are currently still running.
  +  `Complete`: Returns a list of command executions that have already completed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_CommandFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CommandFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CommandFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CommandFilter)
