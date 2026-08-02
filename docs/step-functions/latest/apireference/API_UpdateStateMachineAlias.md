---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachineAlias.html
---

# UpdateStateMachineAlias
<a name="API_UpdateStateMachineAlias"></a>

Updates the configuration of an existing state machine [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) by modifying its `description` or `routingConfiguration`.

You must specify at least one of the `description` or `routingConfiguration` parameters to update a state machine alias.

**Note**
 `UpdateStateMachineAlias` is an idempotent API. Step Functions bases the idempotency check on the `stateMachineAliasArn`, `description`, and `routingConfiguration` parameters. Requests with the same parameters return an idempotent response.

**Note**
This operation is eventually consistent. All [StartExecution](API_StartExecution.md) requests made within a few seconds use the latest alias configuration. Executions started immediately after calling `UpdateStateMachineAlias` may use the previous routing configuration.

 **Related operations:**
+  [CreateStateMachineAlias](API_CreateStateMachineAlias.md)
+  [DescribeStateMachineAlias](API_DescribeStateMachineAlias.md)
+  [ListStateMachineAliases](API_ListStateMachineAliases.md)
+  [DeleteStateMachineAlias](API_DeleteStateMachineAlias.md)

## Request Syntax
<a name="API_UpdateStateMachineAlias_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "routingConfiguration": [
      {
         "stateMachineVersionArn": "{{string}}",
         "weight": {{number}}
      }
   ],
   "stateMachineAliasArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateStateMachineAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachineAlias-request-description"></a>
A description of the state machine alias.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [routingConfiguration](#API_UpdateStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachineAlias-request-routingConfiguration"></a>
The routing configuration of the state machine alias.
An array of `RoutingConfig` objects that specifies up to two state machine versions that the alias starts executions for.
Type: Array of [RoutingConfigurationListItem](API_RoutingConfigurationListItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [stateMachineAliasArn](#API_UpdateStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachineAlias-request-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) of the state machine alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_UpdateStateMachineAlias_ResponseSyntax"></a>

```
{
   "updateDate": number
}
```

## Response Elements
<a name="API_UpdateStateMachineAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [updateDate](#API_UpdateStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-UpdateStateMachineAlias-response-updateDate"></a>
The date and time the state machine alias was updated.
Type: Timestamp

## Errors
<a name="API_UpdateStateMachineAlias_Errors"></a>

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

 ** StateMachineDeleting **
The specified state machine is being deleted.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStateMachineAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/UpdateStateMachineAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/UpdateStateMachineAlias)
