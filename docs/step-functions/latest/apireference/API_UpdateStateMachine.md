---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html
---

# UpdateStateMachine
<a name="API_UpdateStateMachine"></a>

Updates an existing state machine by modifying its `definition`, `roleArn`, `loggingConfiguration`, or `EncryptionConfiguration`. Running executions will continue to use the previous `definition` and `roleArn`. You must include at least one of `definition` or `roleArn` or you will receive a `MissingRequiredParameter` error.

A qualified state machine ARN refers to a *Distributed Map state* defined within a state machine. For example, the qualified state machine ARN `arn:partition:states:region:account-id:stateMachine:stateMachineName/mapStateLabel` refers to a *Distributed Map state* with a label `mapStateLabel` in the state machine named `stateMachineName`.

A qualified state machine ARN can either refer to a *Distributed Map state* defined within a state machine, a version ARN, or an alias ARN.

The following are some examples of qualified and unqualified state machine ARNs:
+ The following qualified state machine ARN refers to a *Distributed Map state* with a label `mapStateLabel` in a state machine named `myStateMachine`.

   `arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel`
**Note**
If you provide a qualified state machine ARN that refers to a *Distributed Map state*, the request fails with `ValidationException`.
+ The following qualified state machine ARN refers to an alias named `PROD`.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD>`
**Note**
If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.
+ The following unqualified state machine ARN refers to a state machine named `myStateMachine`.

   `arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>`

After you update your state machine, you can set the `publish` parameter to `true` in the same action to publish a new [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html). This way, you can opt-in to strict versioning of your state machine.

**Note**
Step Functions assigns monotonically increasing integers for state machine versions, starting at version number 1.

**Note**
All `StartExecution` calls within a few seconds use the updated `definition` and `roleArn`. Executions started immediately after you call `UpdateStateMachine` may use the previous state machine `definition` and `roleArn`.

## Request Syntax
<a name="API_UpdateStateMachine_RequestSyntax"></a>

```
{
   "definition": "{{string}}",
   "encryptionConfiguration": {
      "kmsDataKeyReusePeriodSeconds": {{number}},
      "kmsKeyId": "{{string}}",
      "type": "{{string}}"
   },
   "loggingConfiguration": {
      "destinations": [
         {
            "cloudWatchLogsLogGroup": {
               "logGroupArn": "{{string}}"
            }
         }
      ],
      "includeExecutionData": {{boolean}},
      "level": "{{string}}"
   },
   "publish": {{boolean}},
   "roleArn": "{{string}}",
   "stateMachineArn": "{{string}}",
   "tracingConfiguration": {
      "enabled": {{boolean}}
   },
   "versionDescription": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateStateMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [definition](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-definition"></a>
The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

 ** [encryptionConfiguration](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-encryptionConfiguration"></a>
Settings to configure server-side encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [loggingConfiguration](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-loggingConfiguration"></a>
Use the `LoggingConfiguration` data type to set CloudWatch Logs options.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** [publish](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-publish"></a>
Specifies whether the state machine version is published. The default is `false`. To publish a version after updating the state machine, set `publish` to `true`.
Type: Boolean
Required: No

 ** [roleArn](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role of the state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [stateMachineArn](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [tracingConfiguration](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-tracingConfiguration"></a>
Selects whether AWS X-Ray tracing is enabled.
Type: [TracingConfiguration](API_TracingConfiguration.md) object
Required: No

 ** [versionDescription](#API_UpdateStateMachine_RequestSyntax) **   <a name="StepFunctions-UpdateStateMachine-request-versionDescription"></a>
An optional description of the state machine version to publish.
You can only specify the `versionDescription` parameter if you've set `publish` to `true`.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateStateMachine_ResponseSyntax"></a>

```
{
   "revisionId": "string",
   "stateMachineVersionArn": "string",
   "updateDate": number
}
```

## Response Elements
<a name="API_UpdateStateMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [revisionId](#API_UpdateStateMachine_ResponseSyntax) **   <a name="StepFunctions-UpdateStateMachine-response-revisionId"></a>
The revision identifier for the updated state machine.
Type: String

 ** [stateMachineVersionArn](#API_UpdateStateMachine_ResponseSyntax) **   <a name="StepFunctions-UpdateStateMachine-response-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) of the published state machine version.
If the `publish` parameter isn't set to `true`, this field returns null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [updateDate](#API_UpdateStateMachine_ResponseSyntax) **   <a name="StepFunctions-UpdateStateMachine-response-updateDate"></a>
The date and time the state machine was updated.
Type: Timestamp

## Errors
<a name="API_UpdateStateMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md), [PublishStateMachineVersion](API_PublishStateMachineVersion.md), or [UpdateStateMachine](#API_UpdateStateMachine) with the `publish` parameter set to `true`.
HTTP Status Code: 409
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidDefinition **
The provided Amazon States Language definition is not valid.
HTTP Status Code: 400

 ** InvalidEncryptionConfiguration **
Received when `encryptionConfiguration` is specified but various conditions exist which make the configuration invalid. For example, if `type` is set to `CUSTOMER_MANAGED_KMS_KEY`, but `kmsKeyId` is null, or `kmsDataKeyReusePeriodSeconds` is not between 60 and 900, or the AWS KMS key is not symmetric or inactive.
HTTP Status Code: 400

 ** InvalidLoggingConfiguration **
Configuration is not valid.
HTTP Status Code: 400

 ** InvalidTracingConfiguration **
Your `tracingConfiguration` key does not match, or `enabled` has not been set to `true` or `false`.
HTTP Status Code: 400

 ** KmsAccessDeniedException **
Either your AWS KMS key policy or API caller does not have the required permissions.
HTTP Status Code: 400

 ** KmsThrottlingException **
Received when AWS KMS returns `ThrottlingException` for a AWS KMS call that Step Functions makes on behalf of the caller.
HTTP Status Code: 400

 ** MissingRequiredParameter **
Request is missing a required parameter. This error occurs if both `definition` and `roleArn` are not specified.
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
<a name="API_UpdateStateMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/UpdateStateMachine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/UpdateStateMachine)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
