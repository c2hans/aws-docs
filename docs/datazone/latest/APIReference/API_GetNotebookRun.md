---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetNotebookRun.html
---

# GetNotebookRun
<a name="API_GetNotebookRun"></a>

Gets the details of a [notebook run](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) in Amazon SageMaker Unified Studio.

## Request Syntax
<a name="API_GetNotebookRun_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/notebook-runs/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotebookRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetNotebookRun_RequestSyntax) **   <a name="datazone-GetNotebookRun-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetNotebookRun_RequestSyntax) **   <a name="datazone-GetNotebookRun-request-uri-identifier"></a>
The identifier of the notebook run.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetNotebookRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotebookRun_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetNotebookRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cellOrder](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-cellOrder"></a>
The ordered list of cells in the notebook run.
Type: Array of [CellInformation](API_CellInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [completedAt](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-completedAt"></a>
The timestamp of when the notebook run completed.
Type: Timestamp

 ** [computeConfiguration](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-computeConfiguration"></a>
The compute configuration of the notebook run.
Type: [ComputeConfig](API_ComputeConfig.md) object

 ** [createdAt](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-createdAt"></a>
The timestamp of when the notebook run was created.
Type: Timestamp

 ** [createdBy](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-createdBy"></a>
The identifier of the user who created the notebook run.
Type: String

 ** [domainId](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentConfiguration](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-environmentConfiguration"></a>
The environment configuration of the notebook run, including image version and package settings.
Type: [EnvironmentConfig](API_EnvironmentConfig.md) object

 ** [error](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-error"></a>
The error details if the notebook run failed.
Type: [NotebookRunError](API_NotebookRunError.md) object

 ** [id](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-id"></a>
The identifier of the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [metadata](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-metadata"></a>
The metadata of the notebook run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [networkConfiguration](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-networkConfiguration"></a>
The network configuration of the notebook run.
Type: [NetworkConfig](API_NetworkConfig.md) object

 ** [notebookId](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-notebookId"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-owningProjectId"></a>
The identifier of the project that owns the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [parameters](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-parameters"></a>
The sensitive parameters of the notebook run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [scheduleId](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-scheduleId"></a>
The identifier of the schedule associated with the notebook run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [startedAt](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-startedAt"></a>
The timestamp of when the notebook run started executing.
Type: Timestamp

 ** [status](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-status"></a>
The status of the notebook run.
Type: String
Valid Values: `QUEUED | STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED`

 ** [storageConfiguration](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-storageConfiguration"></a>
The storage configuration of the notebook run, including the Amazon Simple Storage Service path and AWS KMS key ARN.
Type: [StorageConfig](API_StorageConfig.md) object

 ** [timeoutConfiguration](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-timeoutConfiguration"></a>
The timeout configuration of the notebook run.
Type: [TimeoutConfig](API_TimeoutConfig.md) object

 ** [triggerSource](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-triggerSource"></a>
The source that triggered the notebook run.
Type: [TriggerSource](API_TriggerSource.md) object

 ** [updatedAt](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-updatedAt"></a>
The timestamp of when the notebook run was last updated.
Type: Timestamp

 ** [updatedBy](#API_GetNotebookRun_ResponseSyntax) **   <a name="datazone-GetNotebookRun-response-updatedBy"></a>
The identifier of the user who last updated the notebook run.
Type: String

## Errors
<a name="API_GetNotebookRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_GetNotebookRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetNotebookRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetNotebookRun)
