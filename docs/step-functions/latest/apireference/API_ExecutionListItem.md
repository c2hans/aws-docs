---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionListItem.html
---

# ExecutionListItem
<a name="API_ExecutionListItem"></a>

Contains details about an execution.

## Contents
<a name="API_ExecutionListItem_Contents"></a>

 ** executionArn **   <a name="StepFunctions-Type-ExecutionListItem-executionArn"></a>
The Amazon Resource Name (ARN) that identifies the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** name **   <a name="StepFunctions-Type-ExecutionListItem-name"></a>
The name of the execution.
A name must *not* contain:
+ white space
+ brackets `< > { } [ ]`
+ wildcard characters `? *`
+ special characters `" # % \ ^ | ~ ` $ & , ; : /`
+ control characters (`U+0000-001F`, `U+007F-009F`, `U+FFFE-FFFF`)
+ surrogates (`U+D800-DFFF`)
+ invalid characters (` U+10FFFF`)
To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and \_.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** startDate **   <a name="StepFunctions-Type-ExecutionListItem-startDate"></a>
The date the execution started.
Type: Timestamp
Required: Yes

 ** stateMachineArn **   <a name="StepFunctions-Type-ExecutionListItem-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine that ran the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** status **   <a name="StepFunctions-Type-ExecutionListItem-status"></a>
The current status of the execution.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | ABORTED | PENDING_REDRIVE`
Required: Yes

 ** itemCount **   <a name="StepFunctions-Type-ExecutionListItem-itemCount"></a>
The total number of items processed in a child workflow execution. This field is returned only if `mapRunArn` was specified in the `ListExecutions` API action. If `stateMachineArn` was specified in `ListExecutions`, the `itemCount` field isn't returned.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** mapRunArn **   <a name="StepFunctions-Type-ExecutionListItem-mapRunArn"></a>
The Amazon Resource Name (ARN) of a Map Run. This field is returned only if `mapRunArn` was specified in the `ListExecutions` API action. If `stateMachineArn` was specified in `ListExecutions`, the `mapRunArn` isn't returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** redriveCount **   <a name="StepFunctions-Type-ExecutionListItem-redriveCount"></a>
The number of times you've redriven an execution. If you have not yet redriven an execution, the `redriveCount` is 0. This count is only updated when you successfully redrive an execution.
Type: Integer
Required: No

 ** redriveDate **   <a name="StepFunctions-Type-ExecutionListItem-redriveDate"></a>
The date the execution was last redriven.
Type: Timestamp
Required: No

 ** stateMachineAliasArn **   <a name="StepFunctions-Type-ExecutionListItem-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) of the state machine alias used to start an execution.
If the state machine execution was started with an unqualified ARN or a version ARN, it returns null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** stateMachineVersionArn **   <a name="StepFunctions-Type-ExecutionListItem-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) of the state machine version associated with the execution.
If the state machine execution was started with an unqualified ARN, it returns null.
If the execution was started using a `stateMachineAliasArn`, both the `stateMachineAliasArn` and `stateMachineVersionArn` parameters contain the respective values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** stopDate **   <a name="StepFunctions-Type-ExecutionListItem-stopDate"></a>
If the execution already ended, the date the execution stopped.
Type: Timestamp
Required: No

## See Also
<a name="API_ExecutionListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ExecutionListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ExecutionListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ExecutionListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
