---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachine.html
---

# DeleteStateMachine
<a name="API_DeleteStateMachine"></a>

Deletes a state machine. This is an asynchronous operation. It sets the state machine's status to `DELETING` and begins the deletion process. A state machine is deleted only when all its executions are completed. On the next state transition, the state machine's executions are terminated.

A qualified state machine ARN can either refer to a *Distributed Map state* defined within a state machine, a version ARN, or an alias ARN.

The following are some examples of qualified and unqualified state machine ARNs:
+ The following qualified state machine ARN refers to a *Distributed Map state* with a label `mapStateLabel` in a state machine named `myStateMachine`.

   `arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel`
**Note**
If you provide a qualified state machine ARN that refers to a *Distributed Map state*, the request fails with `ValidationException`.
+ The following unqualified state machine ARN refers to a state machine named `myStateMachine`.

   `arn:partition:states:region:account-id:stateMachine:myStateMachine`

This API action also deletes all [versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) and [aliases](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) associated with a state machine.

**Note**
For `EXPRESS` state machines, the deletion happens eventually (usually in less than a minute). Running executions may emit logs after `DeleteStateMachine` API is called.

## Request Syntax
<a name="API_DeleteStateMachine_RequestSyntax"></a>

```
{
   "stateMachineArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteStateMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [stateMachineArn](#API_DeleteStateMachine_RequestSyntax) **   <a name="StepFunctions-DeleteStateMachine-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_DeleteStateMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteStateMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteStateMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DeleteStateMachine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DeleteStateMachine)
