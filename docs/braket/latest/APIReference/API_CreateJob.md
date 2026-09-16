---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateJob.html
---

# CreateJob
<a name="API_CreateJob"></a>

Creates an Amazon Braket hybrid job.

## Request Syntax
<a name="API_CreateJob_RequestSyntax"></a>

```
POST /job HTTP/1.1
Content-type: application/json

{
   "algorithmSpecification": {
      "containerImage": {
         "uri": "{{string}}"
      },
      "scriptModeConfig": {
         "compressionType": "{{string}}",
         "entryPoint": "{{string}}",
         "s3Uri": "{{string}}"
      }
   },
   "associations": [
      {
         "arn": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "checkpointConfig": {
      "localPath": "{{string}}",
      "s3Uri": "{{string}}"
   },
   "clientToken": "{{string}}",
   "deviceConfig": {
      "device": "{{string}}"
   },
   "hyperParameters": {
      "{{string}}" : "{{string}}"
   },
   "inputDataConfig": [
      {
         "channelName": "{{string}}",
         "contentType": "{{string}}",
         "dataSource": {
            "s3DataSource": {
               "s3Uri": "{{string}}"
            }
         }
      }
   ],
   "instanceConfig": {
      "instanceCount": {{number}},
      "instanceType": "{{string}}",
      "volumeSizeInGb": {{number}}
   },
   "jobName": "{{string}}",
   "outputDataConfig": {
      "kmsKeyId": "{{string}}",
      "s3Path": "{{string}}"
   },
   "roleArn": "{{string}}",
   "stoppingCondition": {
      "maxRuntimeInSeconds": {{number}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [algorithmSpecification](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-algorithmSpecification"></a>
Definition of the Amazon Braket job to be created. Specifies the container image the job uses and information about the Python scripts used for entry and training.
Type: [AlgorithmSpecification](API_AlgorithmSpecification.md) object
Required: Yes

 ** [associations](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-associations"></a>
The list of Amazon Braket resources associated with the hybrid job.
Type: Array of [Association](API_Association.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [checkpointConfig](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-checkpointConfig"></a>
Information about the output locations for hybrid job checkpoint data.
Type: [JobCheckpointConfig](API_JobCheckpointConfig.md) object
Required: No

 ** [clientToken](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-clientToken"></a>
The client token associated with this request that guarantees that the request is idempotent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [deviceConfig](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-deviceConfig"></a>
The quantum processing unit (QPU) or simulator used to create an Amazon Braket hybrid job.
Type: [DeviceConfig](API_DeviceConfig.md) object
Required: Yes

 ** [hyperParameters](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-hyperParameters"></a>
Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the training job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of the hyperparameter.
Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Value Length Constraints: Minimum length of 1. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** [inputDataConfig](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-inputDataConfig"></a>
A list of parameters that specify the name and type of input data and where it is located.
Type: Array of [InputFileConfig](API_InputFileConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [instanceConfig](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-instanceConfig"></a>
Configuration of the resource instances to use while running the hybrid job on Amazon Braket.
Type: [InstanceConfig](API_InstanceConfig.md) object
Required: Yes

 ** [jobName](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-jobName"></a>
The name of the Amazon Braket hybrid job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,50}`
Required: Yes

 ** [outputDataConfig](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-outputDataConfig"></a>
The path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.
Type: [JobOutputDataConfig](API_JobOutputDataConfig.md) object
Required: Yes

 ** [roleArn](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and hybrid job details to the users' s3 buckets.
Type: String
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [stoppingCondition](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-stoppingCondition"></a>
 The user-defined criteria that specifies when a hybrid job stops running.
Type: [JobStoppingCondition](API_JobStoppingCondition.md) object
Required: No

 ** [tags](#API_CreateJob_RequestSyntax) **   <a name="braket-CreateJob-request-tags"></a>
Tags to be added to the hybrid job you're creating.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateJob_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateJob_ResponseSyntax) **   <a name="braket-CreateJob-response-jobArn"></a>
The ARN of the Amazon Braket hybrid job created.
Type: String
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:job/.*`

## Errors
<a name="API_CreateJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
An error occurred due to a conflict.
HTTP Status Code: 409

 ** DeviceOfflineException **
The specified device is currently offline.
HTTP Status Code: 424

 ** DeviceRetiredException **
The specified device has been retired.
HTTP Status Code: 410

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request failed because a service quota is exceeded.
HTTP Status Code: 402

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
<a name="API_CreateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/CreateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/CreateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/CreateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/CreateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/CreateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/CreateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/CreateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/CreateJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/CreateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/CreateJob)
