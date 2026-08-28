---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_GetQuantumTask.html
---

# GetQuantumTask
<a name="API_GetQuantumTask"></a>

Retrieves the specified quantum task.

## Request Syntax
<a name="API_GetQuantumTask_RequestSyntax"></a>

```
GET /quantum-task/{{quantumTaskArn}}?additionalAttributeNames={{additionalAttributeNames}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQuantumTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [additionalAttributeNames](#API_GetQuantumTask_RequestSyntax) **   <a name="braket-GetQuantumTask-request-uri-additionalAttributeNames"></a>
A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.
Valid Values: `QueueInfo`

 ** [quantumTaskArn](#API_GetQuantumTask_RequestSyntax) **   <a name="braket-GetQuantumTask-request-uri-quantumTaskArn"></a>
The ARN of the quantum task to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetQuantumTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQuantumTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionMetadata": {
      "actionType": "string",
      "executableCount": number,
      "programCount": number
   },
   "associations": [
      {
         "arn": "string",
         "type": "string"
      }
   ],
   "createdAt": "string",
   "deviceArn": "string",
   "deviceParameters": "string",
   "endedAt": "string",
   "experimentalCapabilities": { ... },
   "failureReason": "string",
   "jobArn": "string",
   "numSuccessfulShots": number,
   "outputS3Bucket": "string",
   "outputS3Directory": "string",
   "quantumTaskArn": "string",
   "queueInfo": {
      "message": "string",
      "position": "string",
      "queue": "string",
      "queuePriority": "string"
   },
   "shots": number,
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetQuantumTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionMetadata](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-actionMetadata"></a>
Metadata about the action performed by the quantum task, including information about the type of action and program counts.
Type: [ActionMetadata](API_ActionMetadata.md) object

 ** [associations](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-associations"></a>
The list of Amazon Braket resources associated with the quantum task.
Type: Array of [Association](API_Association.md) objects

 ** [createdAt](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-createdAt"></a>
The time at which the quantum task was created.
Type: Timestamp

 ** [deviceArn](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-deviceArn"></a>
The ARN of the device the quantum task was run on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [deviceParameters](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-deviceParameters"></a>
The parameters for the device on which the quantum task ran.
Type: String

 ** [endedAt](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-endedAt"></a>
The time at which the quantum task ended.
Type: Timestamp

 ** [experimentalCapabilities](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-experimentalCapabilities"></a>
Enabled experimental capabilities for the quantum task, if any.
Type: [ExperimentalCapabilities](API_ExperimentalCapabilities.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [failureReason](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-failureReason"></a>
The reason that a quantum task failed.
Type: String

 ** [jobArn](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-jobArn"></a>
The ARN of the Amazon Braket job associated with the quantum task.
Type: String
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:job/.*`

 ** [numSuccessfulShots](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-numSuccessfulShots"></a>
The number of successful shots for the quantum task. This is available after a successfully completed quantum task.
Type: Long

 ** [outputS3Bucket](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-outputS3Bucket"></a>
The S3 bucket where quantum task results are stored.
Type: String

 ** [outputS3Directory](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-outputS3Directory"></a>
The folder in the S3 bucket where quantum task results are stored.
Type: String

 ** [quantumTaskArn](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-quantumTaskArn"></a>
The ARN of the quantum task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [queueInfo](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-queueInfo"></a>
Queue information for the requested quantum task. Only returned if `QueueInfo` is specified in the `additionalAttributeNames"` field in the `GetQuantumTask` API request.
Type: [QuantumTaskQueueInfo](API_QuantumTaskQueueInfo.md) object

 ** [shots](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-shots"></a>
The number of shots used in the quantum task.
Type: Long

 ** [status](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-status"></a>
The status of the quantum task.
Type: String
Valid Values: `CREATED | QUEUED | RUNNING | COMPLETED | FAILED | CANCELLING | CANCELLED`

 ** [tags](#API_GetQuantumTask_ResponseSyntax) **   <a name="braket-GetQuantumTask-response-tags"></a>
The tags that belong to this quantum task.
Type: String to string map

## Errors
<a name="API_GetQuantumTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetQuantumTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/GetQuantumTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/GetQuantumTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
