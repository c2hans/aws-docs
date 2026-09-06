---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html
---

# CreateStateMachine
<a name="API_CreateStateMachine"></a>

Creates a state machine. A state machine consists of a collection of states that can do work (`Task` states), determine to which states to transition next (`Choice` states), stop an execution with an error (`Fail` states), and so on. State machines are specified using a JSON-based, structured language. For more information, see [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) in the AWS Step Functions User Guide.

If you set the `publish` parameter of this API action to `true`, it publishes version `1` as the first revision of the state machine.

 For additional control over security, you can encrypt your data using a **customer-managed key** for Step Functions state machines. You can configure a symmetric AWS KMS key and data key reuse period when creating or updating a **State Machine**. The execution history and state machine definition will be encrypted with the key applied to the State Machine.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

**Note**
 `CreateStateMachine` is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. `CreateStateMachine`'s idempotency check is based on the state machine `name`, `definition`, `type`, `LoggingConfiguration`, `TracingConfiguration`, and `EncryptionConfiguration` The check is also based on the `publish` and `versionDescription` parameters. If a following request has a different `roleArn` or `tags`, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, `roleArn` and `tags` will not be updated, even if they are different.

## Request Syntax
<a name="API_CreateStateMachine_RequestSyntax"></a>

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
   "name": "{{string}}",
   "publish": {{boolean}},
   "roleArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "tracingConfiguration": {
      "enabled": {{boolean}}
   },
   "type": "{{string}}",
   "versionDescription": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateStateMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [definition](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-definition"></a>
The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: Yes

 ** [encryptionConfiguration](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-encryptionConfiguration"></a>
Settings to configure server-side encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [loggingConfiguration](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-loggingConfiguration"></a>
Defines what execution history events are logged and where they are logged.
By default, the `level` is set to `OFF`. For more information see [Log Levels](https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html) in the AWS Step Functions User Guide.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object
Required: No

 ** [name](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-name"></a>
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

 ** [publish](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-publish"></a>
Set to `true` to publish the first version of the state machine during creation. The default is `false`.
Type: Boolean
Required: No

 ** [roleArn](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [tags](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-tags"></a>
Tags to be added when creating a state machine.
An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*, and [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html).
Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [tracingConfiguration](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-tracingConfiguration"></a>
Selects whether AWS X-Ray tracing is enabled.
Type: [TracingConfiguration](API_TracingConfiguration.md) object
Required: No

 ** [type](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-type"></a>
Determines whether a Standard or Express state machine is created. The default is `STANDARD`. You cannot update the `type` of a state machine once it has been created.
Type: String
Valid Values: `STANDARD | EXPRESS`
Required: No

 ** [versionDescription](#API_CreateStateMachine_RequestSyntax) **   <a name="StepFunctions-CreateStateMachine-request-versionDescription"></a>
Sets description about the state machine version. You can only set the description if the `publish` parameter is set to `true`. Otherwise, if you set `versionDescription`, but `publish` to `false`, this API action throws `ValidationException`.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateStateMachine_ResponseSyntax"></a>

```
{
   "creationDate": number,
   "stateMachineArn": "string",
   "stateMachineVersionArn": "string"
}
```

## Response Elements
<a name="API_CreateStateMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_CreateStateMachine_ResponseSyntax) **   <a name="StepFunctions-CreateStateMachine-response-creationDate"></a>
The date the state machine is created.
Type: Timestamp

 ** [stateMachineArn](#API_CreateStateMachine_ResponseSyntax) **   <a name="StepFunctions-CreateStateMachine-response-stateMachineArn"></a>
The Amazon Resource Name (ARN) that identifies the created state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [stateMachineVersionArn](#API_CreateStateMachine_ResponseSyntax) **   <a name="StepFunctions-CreateStateMachine-response-stateMachineVersionArn"></a>
The Amazon Resource Name (ARN) that identifies the created state machine version. If you do not set the `publish` parameter to `true`, this field returns null value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateStateMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for [DeleteStateMachineVersion](API_DeleteStateMachineVersion.md), [PublishStateMachineVersion](API_PublishStateMachineVersion.md), or [UpdateStateMachine](API_UpdateStateMachine.md) with the `publish` parameter set to `true`.
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

 ** InvalidName **
The provided name is not valid.
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

 ** StateMachineAlreadyExists **
A state machine with the same name but a different definition or role ARN already exists.
HTTP Status Code: 400

 ** StateMachineDeleting **
The specified state machine is being deleted.
HTTP Status Code: 400

 ** StateMachineLimitExceeded **
The maximum number of state machines has been reached. Existing state machines must be deleted before a new state machine can be created.
HTTP Status Code: 400

 ** StateMachineTypeNotSupported **
State machine type is not supported.
HTTP Status Code: 400

 ** TooManyTags **
You've exceeded the number of tags allowed for a resource. See the [ Limits Topic](https://docs.aws.amazon.com/step-functions/latest/dg/limits.html) in the AWS Step Functions Developer Guide.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateStateMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/CreateStateMachine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/CreateStateMachine)
