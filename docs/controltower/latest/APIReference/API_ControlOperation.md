---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ControlOperation.html
---

# ControlOperation
<a name="API_ControlOperation"></a>

An operation performed by the control.

## Contents
<a name="API_ControlOperation_Contents"></a>

 ** controlIdentifier **   <a name="controltower-Type-ControlOperation-controlIdentifier"></a>
The `controlIdentifier` of the control for the operation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** enabledControlIdentifier **   <a name="controltower-Type-ControlOperation-enabledControlIdentifier"></a>
The `controlIdentifier` of the enabled control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** endTime **   <a name="controltower-Type-ControlOperation-endTime"></a>
The time that the operation finished.
Type: Timestamp
Required: No

 ** operationIdentifier **   <a name="controltower-Type-ControlOperation-operationIdentifier"></a>
The identifier of the specified operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** operationType **   <a name="controltower-Type-ControlOperation-operationType"></a>
One of `ENABLE_CONTROL` or `DISABLE_CONTROL`.
Type: String
Valid Values: `ENABLE_CONTROL | DISABLE_CONTROL | UPDATE_ENABLED_CONTROL | RESET_ENABLED_CONTROL`
Required: No

 ** startTime **   <a name="controltower-Type-ControlOperation-startTime"></a>
The time that the operation began.
Type: Timestamp
Required: No

 ** status **   <a name="controltower-Type-ControlOperation-status"></a>
One of `IN_PROGRESS`, `SUCEEDED`, or `FAILED`.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

 ** statusMessage **   <a name="controltower-Type-ControlOperation-statusMessage"></a>
If the operation result is `FAILED`, this string contains a message explaining why the operation failed.
Type: String
Required: No

 ** targetIdentifier **   <a name="controltower-Type-ControlOperation-targetIdentifier"></a>
The target upon which the control operation is working.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_ControlOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ControlOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ControlOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ControlOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
