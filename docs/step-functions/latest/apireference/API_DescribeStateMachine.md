---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html
---

# DescribeStateMachine
<a name="API_DescribeStateMachine"></a>

Provides information about a state machine's definition, its IAM role Amazon Resource Name (ARN), and configuration.

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

This API action returns the details for a state machine version if the `stateMachineArn` you specify is a state machine version ARN.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

## Request Syntax
<a name="API_DescribeStateMachine_RequestSyntax"></a>

```
{
   "includedData": "{{string}}",
   "stateMachineArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStateMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includedData](#API_DescribeStateMachine_RequestSyntax) **   <a name="StepFunctions-DescribeStateMachine-request-includedData"></a>
If your state machine definition is encrypted with a AWS KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call the API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.
 When calling a labelled ARN for an encrypted state machine, the `includedData = METADATA_ONLY` parameter will not apply because Step Functions needs to decrypt the entire state machine definition to get the Distributed Map state’s definition. In this case, the API caller needs to have `kms:Decrypt` permission.
Type: String
Valid Values: `ALL_DATA | METADATA_ONLY`
Required: No

 ** [stateMachineArn](#API_DescribeStateMachine_RequestSyntax) **   <a name="StepFunctions-DescribeStateMachine-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine for which you want the information.
If you specify a state machine version ARN, this API returns details about that version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_DescribeStateMachine_ResponseSyntax"></a>

```
{
   "creationDate": number,
   "definition": "string",
   "description": "string",
   "encryptionConfiguration": {
      "kmsDataKeyReusePeriodSeconds": number,
      "kmsKeyId": "string",
      "type": "string"
   },
   "label": "string",
   "loggingConfiguration": {
      "destinations": [
         {
            "cloudWatchLogsLogGroup": {
               "logGroupArn": "string"
            }
         }
      ],
      "includeExecutionData": boolean,
      "level": "string"
   },
   "name": "string",
   "revisionId": "string",
   "roleArn": "string",
   "stateMachineArn": "string",
   "status": "string",
   "tracingConfiguration": {
      "enabled": boolean
   },
   "type": "string",
   "variableReferences": {
      "string" : [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeStateMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-creationDate"></a>
The date the state machine is created.
For a state machine version, `creationDate` is the date the version was created.
Type: Timestamp

 ** [definition](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-definition"></a>
The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html).
If called with `includedData = METADATA_ONLY`, the returned definition will be `{}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

 ** [description](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-description"></a>
The description of the state machine version.
Type: String
Length Constraints: Maximum length of 256.

 ** [encryptionConfiguration](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-encryptionConfiguration"></a>
Settings to configure server-side encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [label](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-label"></a>
A user-defined or an auto-generated string that identifies a `Map` state. This parameter is present only if the `stateMachineArn` specified in input is a qualified state machine ARN.
Type: String

 ** [loggingConfiguration](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-loggingConfiguration"></a>
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object

 ** [name](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-name"></a>
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

 ** [revisionId](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-revisionId"></a>
The revision identifier for the state machine.
Use the `revisionId` parameter to compare between versions of a state machine configuration used for executions without performing a diff of the properties, such as `definition` and `roleArn`.
Type: String

 ** [roleArn](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. (The IAM role maintains security by granting Step Functions access to AWS resources.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [stateMachineArn](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-stateMachineArn"></a>
The Amazon Resource Name (ARN) that identifies the state machine.
If you specified a state machine version ARN in your request, the API returns the version ARN. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, `stateMachineARN:1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [status](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-status"></a>
The current status of the state machine.
Type: String
Valid Values: `ACTIVE | DELETING`

 ** [tracingConfiguration](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-tracingConfiguration"></a>
Selects whether AWS X-Ray tracing is enabled.
Type: [TracingConfiguration](API_TracingConfiguration.md) object

 ** [type](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-type"></a>
The `type` of the state machine (`STANDARD` or `EXPRESS`).
Type: String
Valid Values: `STANDARD | EXPRESS`

 ** [variableReferences](#API_DescribeStateMachine_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachine-response-variableReferences"></a>
A map of **state name** to a list of variables referenced by that state. States that do not use variable references will not be shown in the response.
Type: String to array of strings map
Key Length Constraints: Minimum length of 1. Maximum length of 80.

## Errors
<a name="API_DescribeStateMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** KmsAccessDeniedException **
Either your AWS KMS key policy or API caller does not have the required permissions.
HTTP Status Code: 400

 ** KmsInvalidStateException **
The AWS KMS key is not in valid state, for example: Disabled or Deleted.
 ** kmsKeyState **
Current status of the AWS KMS; key. For example: `DISABLED`, `PENDING_DELETION`, `PENDING_IMPORT`, `UNAVAILABLE`, `CREATING`.
HTTP Status Code: 400

 ** KmsThrottlingException **
Received when AWS KMS returns `ThrottlingException` for a AWS KMS call that Step Functions makes on behalf of the caller.
HTTP Status Code: 400

 ** StateMachineDoesNotExist **
The specified state machine does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStateMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeStateMachine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DescribeStateMachine)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
