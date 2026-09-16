---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StartNotebookRun.html
---

# StartNotebookRun
<a name="API_StartNotebookRun"></a>

Starts a notebook run in Amazon SageMaker Unified Studio. A notebook run represents the execution of an [Amazon SageMaker notebook](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) within a project. You can configure compute, network, timeout, and environment settings for the run.

## Request Syntax
<a name="API_StartNotebookRun_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/notebook-runs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "computeConfiguration": {
      "environmentVersion": "{{string}}",
      "instanceType": "{{string}}"
   },
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "networkConfiguration": {
      "networkAccessType": "{{string}}",
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ],
      "vpcId": "{{string}}"
   },
   "notebookIdentifier": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "parameters": {
      "{{string}}" : "{{string}}"
   },
   "scheduleIdentifier": "{{string}}",
   "timeoutConfiguration": {
      "runTimeoutInMinutes": {{number}}
   },
   "triggerSource": {
      "name": "{{string}}",
      "type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartNotebookRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_StartNotebookRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [computeConfiguration](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-computeConfiguration"></a>
The compute configuration for the notebook run, including instance type and environment version.
Type: [ComputeConfig](API_ComputeConfig.md) object
Required: No

 ** [metadata](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-metadata"></a>
The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [networkConfiguration](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-networkConfiguration"></a>
The network configuration for the notebook run, including network access type and optional VPC settings.
Type: [NetworkConfig](API_NetworkConfig.md) object
Required: No

 ** [notebookIdentifier](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-notebookIdentifier"></a>
The identifier of the notebook to run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [owningProjectIdentifier](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-owningProjectIdentifier"></a>
The identifier of the project that owns the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [parameters](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-parameters"></a>
The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [scheduleIdentifier](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-scheduleIdentifier"></a>
The identifier of the schedule associated with the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [timeoutConfiguration](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-timeoutConfiguration"></a>
The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).
Type: [TimeoutConfig](API_TimeoutConfig.md) object
Required: No

 ** [triggerSource](#API_StartNotebookRun_RequestSyntax) **   <a name="datazone-StartNotebookRun-request-triggerSource"></a>
The source that triggered the notebook run.
Type: [TriggerSource](API_TriggerSource.md) object
Required: No

## Response Syntax
<a name="API_StartNotebookRun_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "cellOrder": [
      {
      }
   ],
   "completedAt": number,
   "computeConfiguration": {
      "environmentVersion": "string",
      "instanceType": "string"
   },
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "environmentConfiguration": {
      "imageVersion": "string",
      "packageConfig": {
         "packageManager": "string",
         "packageSpecification": "string"
      }
   },
   "error": {
      "message": "string"
   },
   "id": "string",
   "metadata": {
      "string" : "string"
   },
   "networkConfiguration": {
      "networkAccessType": "string",
      "securityGroupIds": [ "string" ],
      "subnetIds": [ "string" ],
      "vpcId": "string"
   },
   "notebookId": "string",
   "owningProjectId": "string",
   "parameters": {
      "string" : "string"
   },
   "scheduleId": "string",
   "startedAt": number,
   "status": "string",
   "storageConfiguration": {
      "kmsKeyArn": "string",
      "projectS3Path": "string"
   },
   "timeoutConfiguration": {
      "runTimeoutInMinutes": number
   },
   "triggerSource": {
      "name": "string",
      "type": "string"
   },
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_StartNotebookRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [cellOrder](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-cellOrder"></a>
The ordered list of cells in the notebook run.
Type: Array of [CellInformation](API_CellInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [completedAt](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-completedAt"></a>
The timestamp of when the notebook run completed.
Type: Timestamp

 ** [computeConfiguration](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-computeConfiguration"></a>
The compute configuration of the notebook run.
Type: [ComputeConfig](API_ComputeConfig.md) object

 ** [createdAt](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-createdAt"></a>
The timestamp of when the notebook run was created.
Type: Timestamp

 ** [createdBy](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-createdBy"></a>
The identifier of the user who created the notebook run.
Type: String

 ** [domainId](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentConfiguration](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-environmentConfiguration"></a>
The environment configuration of the notebook run, including image version and package settings.
Type: [EnvironmentConfig](API_EnvironmentConfig.md) object

 ** [error](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-error"></a>
The error details if the notebook run failed.
Type: [NotebookRunError](API_NotebookRunError.md) object

 ** [id](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-id"></a>
The identifier of the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [metadata](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-metadata"></a>
The metadata of the notebook run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [networkConfiguration](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-networkConfiguration"></a>
The network configuration of the notebook run.
Type: [NetworkConfig](API_NetworkConfig.md) object

 ** [notebookId](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-notebookId"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-owningProjectId"></a>
The identifier of the project that owns the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [parameters](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-parameters"></a>
The sensitive parameters of the notebook run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [scheduleId](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-scheduleId"></a>
The identifier of the schedule associated with the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [startedAt](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-startedAt"></a>
The timestamp of when the notebook run started executing.
Type: Timestamp

 ** [status](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-status"></a>
The status of the notebook run.
Type: String
Valid Values: `QUEUED | STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED`

 ** [storageConfiguration](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-storageConfiguration"></a>
The storage configuration of the notebook run, including the Amazon Simple Storage Service path and AWS KMS key ARN.
Type: [StorageConfig](API_StorageConfig.md) object

 ** [timeoutConfiguration](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-timeoutConfiguration"></a>
The timeout configuration of the notebook run.
Type: [TimeoutConfig](API_TimeoutConfig.md) object

 ** [triggerSource](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-triggerSource"></a>
The source that triggered the notebook run.
Type: [TriggerSource](API_TriggerSource.md) object

 ** [updatedAt](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-updatedAt"></a>
The timestamp of when the notebook run was last updated.
Type: Timestamp

 ** [updatedBy](#API_StartNotebookRun_ResponseSyntax) **   <a name="datazone-StartNotebookRun-response-updatedBy"></a>
The identifier of the user who last updated the notebook run.
Type: String

## Errors
<a name="API_StartNotebookRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartNotebookRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/StartNotebookRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StartNotebookRun)
