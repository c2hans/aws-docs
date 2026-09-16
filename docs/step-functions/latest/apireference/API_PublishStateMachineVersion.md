---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_PublishStateMachineVersion.html
---

# PublishStateMachineVersion
<a name="API_PublishStateMachineVersion"></a>

Creates a [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) from the current revision of a state machine. Use versions to create immutable snapshots of your state machine. You can start executions from versions either directly or with an alias. To create an alias, use [CreateStateMachineAlias](API_CreateStateMachineAlias.md).

You can publish up to 1000 versions for each state machine. You must manually delete unused versions using the [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md) API action.

 `PublishStateMachineVersion` is an idempotent API. It doesn't create a duplicate state machine version if it already exists for the current revision. Step Functions bases `PublishStateMachineVersion`'s idempotency check on the `stateMachineArn`, `name`, and `revisionId` parameters. Requests with the same parameters return a successful idempotent response. If you don't specify a `revisionId`, Step Functions checks for a previously published version of the state machine's current revision.

 **Related operations:**
+  [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md)
+  [ListStateMachineVersions](API_ListStateMachineVersions.md)

## Request Syntax
<a name="API_PublishStateMachineVersion_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "revisionId": "{{string}}",
   "stateMachineArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PublishStateMachineVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_PublishStateMachineVersion_RequestSyntax) **   <a name="StepFunctions-PublishStateMachineVersion-request-description"></a>
An optional description of the state machine version.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [revisionId](#API_PublishStateMachineVersion_RequestSyntax) **   <a name="StepFunctions-PublishStateMachineVersion-request-revisionId"></a>
Only publish the state machine version if the current state machine's revision ID matches the specified ID.
Use this option to avoid publishing a version if the state machine changed since you last updated it. If the specified revision ID doesn't match the state machine's current revision ID, the API returns `ConflictException`.
To specify an initial revision ID for a state machine with no revision ID assigned, specify the string `INITIAL` for the `revisionId` parameter. For example, you can specify a `revisionID` of `INITIAL` when you create a state machine using the [CreateStateMachine](API_CreateStateMachine.md) API action.
Type: String
Required: No

 ** [stateMachineArn](#API_PublishStateMachineVersion_RequestSyntax) **   <a name="StepFunctions-PublishStateMachineVersion-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_PublishStateMachineVersion_ResponseSyntax"></a>

```
{
   "creationDate": number,
   "stateMachineVersionArn": "string"
}
```

## Response Elements
<a name="API_PublishStateMachineVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_PublishStateMachineVersion_ResponseSyntax) **   <a name="StepFunctions-PublishStateMachineVersion-response-creationDate"></a>
The date the version was created.
Type: Timestamp

 ** [stateMachineVersionArn](#API_PublishStateMachineVersion_ResponseSyntax) **   <a name="StepFunctions-PublishStateMachineVersion-response-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) (ARN) that identifies the state machine version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_PublishStateMachineVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md), [PublishStateMachineVersion](#API_PublishStateMachineVersion), or [UpdateStateMachine](API_UpdateStateMachine.md) with the `publish` parameter set to `true`.
HTTP Status Code: 409
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 402
HTTP Status Code: 400

 ** StateMachineDeleting **
The specified state machine is being deleted.
HTTP Status Code: 400

 ** StateMachineDoesNotExist **
The specified state machine does not exist.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_PublishStateMachineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/PublishStateMachineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/PublishStateMachineVersion)
