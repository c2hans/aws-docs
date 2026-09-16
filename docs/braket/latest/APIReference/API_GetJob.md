---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_GetJob.html
---

# GetJob
<a name="API_GetJob"></a>

Retrieves the specified Amazon Braket hybrid job.

## Request Syntax
<a name="API_GetJob_RequestSyntax"></a>

```
GET /job/{{jobArn}}?additionalAttributeNames={{additionalAttributeNames}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [additionalAttributeNames](#API_GetJob_RequestSyntax) **   <a name="braket-GetJob-request-uri-additionalAttributeNames"></a>
A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.
Valid Values: `QueueInfo`

 ** [jobArn](#API_GetJob_RequestSyntax) **   <a name="braket-GetJob-request-uri-jobArn"></a>
The ARN of the hybrid job to retrieve.
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:job/.*`
Required: Yes

## Request Body
<a name="API_GetJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "algorithmSpecification": {
      "containerImage": {
         "uri": "string"
      },
      "scriptModeConfig": {
         "compressionType": "string",
         "entryPoint": "string",
         "s3Uri": "string"
      }
   },
   "associations": [
      {
         "arn": "string",
         "type": "string"
      }
   ],
   "billableDuration": number,
   "checkpointConfig": {
      "localPath": "string",
      "s3Uri": "string"
   },
   "createdAt": "string",
   "deviceConfig": {
      "device": "string"
   },
   "endedAt": "string",
   "events": [
      {
         "eventType": "string",
         "message": "string",
         "timeOfEvent": "string"
      }
   ],
   "failureReason": "string",
   "hyperParameters": {
      "string" : "string"
   },
   "inputDataConfig": [
      {
         "channelName": "string",
         "contentType": "string",
         "dataSource": {
            "s3DataSource": {
               "s3Uri": "string"
            }
         }
      }
   ],
   "instanceConfig": {
      "instanceCount": number,
      "instanceType": "string",
      "volumeSizeInGb": number
   },
   "jobArn": "string",
   "jobName": "string",
   "outputDataConfig": {
      "kmsKeyId": "string",
      "s3Path": "string"
   },
   "queueInfo": {
      "message": "string",
      "position": "string",
      "queue": "string"
   },
   "roleArn": "string",
   "startedAt": "string",
   "status": "string",
   "stoppingCondition": {
      "maxRuntimeInSeconds": number
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [algorithmSpecification](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-algorithmSpecification"></a>
Definition of the Amazon Braket hybrid job created. Provides information about the container image used, and the Python scripts used for training.
Type: [AlgorithmSpecification](API_AlgorithmSpecification.md) object

 ** [associations](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-associations"></a>
The list of Amazon Braket resources associated with the hybrid job.
Type: Array of [Association](API_Association.md) objects

 ** [billableDuration](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-billableDuration"></a>
The billable time for which the Amazon Braket hybrid job used to complete.
Type: Integer

 ** [checkpointConfig](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-checkpointConfig"></a>
Information about the output locations for hybrid job checkpoint data.
Type: [JobCheckpointConfig](API_JobCheckpointConfig.md) object

 ** [createdAt](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-createdAt"></a>
The time at which the Amazon Braket hybrid job was created.
Type: Timestamp

 ** [deviceConfig](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-deviceConfig"></a>
The primary device used by the Amazon Braket hybrid job.
Type: [DeviceConfig](API_DeviceConfig.md) object

 ** [endedAt](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-endedAt"></a>
The time at which the Amazon Braket hybrid job ended.
Type: Timestamp

 ** [events](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-events"></a>
Details about the time and type of events occurred related to the Amazon Braket hybrid job.
Type: Array of [JobEventDetails](API_JobEventDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [failureReason](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-failureReason"></a>
A description of the reason why an Amazon Braket hybrid job failed, if it failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [hyperParameters](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-hyperParameters"></a>
Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the traiing job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of th hyperparameter.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 2500.
Value Pattern: `.*`

 ** [inputDataConfig](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-inputDataConfig"></a>
A list of parameters that specify the name and type of input data and where it is located.
Type: Array of [InputFileConfig](API_InputFileConfig.md) objects

 ** [instanceConfig](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-instanceConfig"></a>
The resource instances to use while running the hybrid job on Amazon Braket.
Type: [InstanceConfig](API_InstanceConfig.md) object

 ** [jobArn](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-jobArn"></a>
The ARN of the Amazon Braket hybrid job.
Type: String
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:job/.*`

 ** [jobName](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-jobName"></a>
The name of the Amazon Braket hybrid job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,50}`

 ** [outputDataConfig](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-outputDataConfig"></a>
The path to the S3 location where hybrid job artifacts are stored and the encryption key used to store them there.
Type: [JobOutputDataConfig](API_JobOutputDataConfig.md) object

 ** [queueInfo](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-queueInfo"></a>
Queue information for the requested hybrid job. Only returned if `QueueInfo` is specified in the `additionalAttributeNames"` field in the `GetJob` API request.
Type: [HybridJobQueueInfo](API_HybridJobQueueInfo.md) object

 ** [roleArn](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and other hybrid job details to the s3 buckets of a user.
Type: String
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [startedAt](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-startedAt"></a>
The time at which the Amazon Braket hybrid job was started.
Type: Timestamp

 ** [status](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-status"></a>
The status of the Amazon Braket hybrid job.
Type: String
Valid Values: `QUEUED | RUNNING | COMPLETED | FAILED | CANCELLING | CANCELLED`

 ** [stoppingCondition](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-stoppingCondition"></a>
The user-defined criteria that specifies when to stop a running hybrid job.
Type: [JobStoppingCondition](API_JobStoppingCondition.md) object

 ** [tags](#API_GetJob_ResponseSyntax) **   <a name="braket-GetJob-response-tags"></a>
The tags associated with this hybrid job.
Type: String to string map

## Errors
<a name="API_GetJob_Errors"></a>

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
<a name="API_GetJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/GetJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/GetJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/GetJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/GetJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/GetJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/GetJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/GetJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/GetJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/GetJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/GetJob)
