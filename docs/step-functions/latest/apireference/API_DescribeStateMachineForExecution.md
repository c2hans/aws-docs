---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineForExecution.html
---

# DescribeStateMachineForExecution
<a name="API_DescribeStateMachineForExecution"></a>

Provides information about a state machine's definition, its execution role ARN, and configuration. If a Map Run dispatched the execution, this action returns the Map Run Amazon Resource Name (ARN) in the response. The state machine returned is the state machine associated with the Map Run.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

This API action is not supported by `EXPRESS` state machines.

## Request Syntax
<a name="API_DescribeStateMachineForExecution_RequestSyntax"></a>

```
{
   "executionArn": "{{string}}",
   "includedData": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStateMachineForExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [executionArn](#API_DescribeStateMachineForExecution_RequestSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-request-executionArn"></a>
The Amazon Resource Name (ARN) of the execution you want state machine information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [includedData](#API_DescribeStateMachineForExecution_RequestSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-request-includedData"></a>
If your state machine definition is encrypted with a AWS KMS key, callers must have `kms:Decrypt` permission to decrypt the definition. Alternatively, you can call the API with `includedData = METADATA_ONLY` to get a successful response without the encrypted definition.
Type: String
Valid Values: `ALL_DATA | METADATA_ONLY`
Required: No

## Response Syntax
<a name="API_DescribeStateMachineForExecution_ResponseSyntax"></a>

```
{
   "definition": "string",
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
   "mapRunArn": "string",
   "name": "string",
   "revisionId": "string",
   "roleArn": "string",
   "stateMachineArn": "string",
   "tracingConfiguration": {
      "enabled": boolean
   },
   "updateDate": number,
   "variableReferences": {
      "string" : [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeStateMachineForExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [definition](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-definition"></a>
The Amazon States Language definition of the state machine. See [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

 ** [encryptionConfiguration](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-encryptionConfiguration"></a>
Settings to configure server-side encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [label](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-label"></a>
A user-defined or an auto-generated string that identifies a `Map` state. This field is returned only if the `executionArn` is a child workflow execution that was started by a Distributed Map state.
Type: String

 ** [loggingConfiguration](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-loggingConfiguration"></a>
The `LoggingConfiguration` data type is used to set CloudWatch Logs options.
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object

 ** [mapRunArn](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-mapRunArn"></a>
The Amazon Resource Name (ARN) of the Map Run that started the child workflow execution. This field is returned only if the `executionArn` is a child workflow execution that was started by a Distributed Map state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [name](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-name"></a>
The name of the state machine associated with the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.

 ** [revisionId](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-revisionId"></a>
The revision identifier for the state machine. The first revision ID when you create the state machine is null.
Use the state machine `revisionId` parameter to compare the revision of a state machine with the configuration of the state machine used for executions without performing a diff of the properties, such as `definition` and `roleArn`.
Type: String

 ** [roleArn](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role of the State Machine for the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [stateMachineArn](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine associated with the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [tracingConfiguration](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-tracingConfiguration"></a>
Selects whether AWS X-Ray tracing is enabled.
Type: [TracingConfiguration](API_TracingConfiguration.md) object

 ** [updateDate](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-updateDate"></a>
The date and time the state machine associated with an execution was updated. For a newly created state machine, this is the creation date.
Type: Timestamp

 ** [variableReferences](#API_DescribeStateMachineForExecution_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineForExecution-response-variableReferences"></a>
A map of **state name** to a list of variables referenced by that state. States that do not use variable references will not be shown in the response.
Type: String to array of strings map
Key Length Constraints: Minimum length of 1. Maximum length of 80.

## Errors
<a name="API_DescribeStateMachineForExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExecutionDoesNotExist **
The specified execution does not exist.
HTTP Status Code: 400

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

## See Also
<a name="API_DescribeStateMachineForExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeStateMachineForExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DescribeStateMachineForExecution)
