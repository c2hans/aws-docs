---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateMachineListItem.html
---

# StateMachineListItem
<a name="API_StateMachineListItem"></a>

Contains details about the state machine.

## Contents
<a name="API_StateMachineListItem_Contents"></a>

 ** creationDate **   <a name="StepFunctions-Type-StateMachineListItem-creationDate"></a>
The date the state machine is created.
Type: Timestamp
Required: Yes

 ** name **   <a name="StepFunctions-Type-StateMachineListItem-name"></a>
The name of the state machine.
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

 ** stateMachineArn **   <a name="StepFunctions-Type-StateMachineListItem-stateMachineArn"></a>
The Amazon Resource Name (ARN) that identifies the state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** type **   <a name="StepFunctions-Type-StateMachineListItem-type"></a>

Type: String
Valid Values: `STANDARD | EXPRESS`
Required: Yes

## See Also
<a name="API_StateMachineListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StateMachineListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StateMachineListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StateMachineListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
