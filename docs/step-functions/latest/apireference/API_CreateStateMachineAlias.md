---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachineAlias.html
---

# CreateStateMachineAlias
<a name="API_CreateStateMachineAlias"></a>

Creates an [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) for a state machine that points to one or two [versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) of the same state machine. You can set your application to call [StartExecution](API_StartExecution.md) with an alias and update the version the alias uses without changing the client's code.

You can also map an alias to split [StartExecution](API_StartExecution.md) requests between two versions of a state machine. To do this, add a second `RoutingConfig` object in the `routingConfiguration` parameter. You must also specify the percentage of execution run requests each version should receive in both `RoutingConfig` objects. Step Functions randomly chooses which version runs a given execution based on the percentage you specify.

To create an alias that points to a single version, specify a single `RoutingConfig` object with a `weight` set to 100.

You can create up to 100 aliases for each state machine. You must delete unused aliases using the [DeleteStateMachineAlias](API_DeleteStateMachineAlias.md) API action.

 `CreateStateMachineAlias` is an idempotent API. Step Functions bases the idempotency check on the `stateMachineArn`, `description`, `name`, and `routingConfiguration` parameters. Requests that contain the same values for these parameters return a successful idempotent response without creating a duplicate resource.

 **Related operations:**
+  [DescribeStateMachineAlias](API_DescribeStateMachineAlias.md)
+  [ListStateMachineAliases](API_ListStateMachineAliases.md)
+  [UpdateStateMachineAlias](API_UpdateStateMachineAlias.md)
+  [DeleteStateMachineAlias](API_DeleteStateMachineAlias.md)

## Request Syntax
<a name="API_CreateStateMachineAlias_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "routingConfiguration": [
      {
         "stateMachineVersionArn": "{{string}}",
         "weight": {{number}}
      }
   ]
}
```

## Request Parameters
<a name="API_CreateStateMachineAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-CreateStateMachineAlias-request-description"></a>
A description for the state machine alias.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [name](#API_CreateStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-CreateStateMachineAlias-request-name"></a>
The name of the state machine alias.
To avoid conflict with version ARNs, don't use an integer in the name of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `^(?=.*[a-zA-Z_\-\.])[a-zA-Z0-9_\-\.]+$`
Required: Yes

 ** [routingConfiguration](#API_CreateStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-CreateStateMachineAlias-request-routingConfiguration"></a>
The routing configuration of a state machine alias. The routing configuration shifts execution traffic between two state machine versions. `routingConfiguration` contains an array of `RoutingConfig` objects that specify up to two state machine versions. Step Functions then randomly choses which version to run an execution with based on the weight assigned to each `RoutingConfig`.
Type: Array of [RoutingConfigurationListItem](API_RoutingConfigurationListItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## Response Syntax
<a name="API_CreateStateMachineAlias_ResponseSyntax"></a>

```
{
   "creationDate": number,
   "stateMachineAliasArn": "string"
}
```

## Response Elements
<a name="API_CreateStateMachineAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_CreateStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-CreateStateMachineAlias-response-creationDate"></a>
The date the state machine alias was created.
Type: Timestamp

 ** [stateMachineAliasArn](#API_CreateStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-CreateStateMachineAlias-response-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) that identifies the created state machine alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateStateMachineAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md), [PublishStateMachineVersion](API_PublishStateMachineVersion.md), or [UpdateStateMachine](API_UpdateStateMachine.md) with the `publish` parameter set to `true`.
HTTP Status Code: 409
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidName **
The provided name is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 402
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
<a name="API_CreateStateMachineAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/CreateStateMachineAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/CreateStateMachineAlias)
