---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineVersion.html
---

# DeleteStateMachineVersion
<a name="API_DeleteStateMachineVersion"></a>

Deletes a state machine [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html). After you delete a version, you can't call [StartExecution](API_StartExecution.md) using that version's ARN or use the version with a state machine [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html).

**Note**
Deleting a state machine version won't terminate its in-progress executions.

**Note**
You can't delete a state machine version currently referenced by one or more aliases. Before you delete a version, you must either delete the aliases or update them to point to another state machine version.

 **Related operations:**
+  [PublishStateMachineVersion](API_PublishStateMachineVersion.md)
+  [ListStateMachineVersions](API_ListStateMachineVersions.md)

## Request Syntax
<a name="API_DeleteStateMachineVersion_RequestSyntax"></a>

```
{
   "stateMachineVersionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteStateMachineVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [stateMachineVersionArn](#API_DeleteStateMachineVersion_RequestSyntax) **   <a name="StepFunctions-DeleteStateMachineVersion-request-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) of the state machine version to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## Response Elements
<a name="API_DeleteStateMachineVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteStateMachineVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for [DeleteStateMachineVersion](#API_DeleteStateMachineVersion), [PublishStateMachineVersion](API_PublishStateMachineVersion.md), or [UpdateStateMachine](API_UpdateStateMachine.md) with the `publish` parameter set to `true`.
HTTP Status Code: 409
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteStateMachineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DeleteStateMachineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DeleteStateMachineVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
