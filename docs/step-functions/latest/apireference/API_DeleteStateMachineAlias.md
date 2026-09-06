---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineAlias.html
---

# DeleteStateMachineAlias
<a name="API_DeleteStateMachineAlias"></a>

Deletes a state machine [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html).

After you delete a state machine alias, you can't use it to start executions. When you delete a state machine alias, Step Functions doesn't delete the state machine versions that alias references.

 **Related operations:**
+  [CreateStateMachineAlias](API_CreateStateMachineAlias.md)
+  [DescribeStateMachineAlias](API_DescribeStateMachineAlias.md)
+  [ListStateMachineAliases](API_ListStateMachineAliases.md)
+  [UpdateStateMachineAlias](API_UpdateStateMachineAlias.md)

## Request Syntax
<a name="API_DeleteStateMachineAlias_RequestSyntax"></a>

```
{
   "stateMachineAliasArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteStateMachineAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [stateMachineAliasArn](#API_DeleteStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-DeleteStateMachineAlias-request-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) of the state machine alias to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Elements
<a name="API_DeleteStateMachineAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteStateMachineAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md), [PublishStateMachineVersion](API_PublishStateMachineVersion.md), or [UpdateStateMachine](API_UpdateStateMachine.md) with the `publish` parameter set to `true`.
HTTP Status Code: 409
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteStateMachineAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DeleteStateMachineAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DeleteStateMachineAlias)
