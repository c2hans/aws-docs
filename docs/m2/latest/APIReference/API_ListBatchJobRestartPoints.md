---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobRestartPoints.html
---

# ListBatchJobRestartPoints
<a name="API_ListBatchJobRestartPoints"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Lists all the job steps for a JCL file to restart a batch job. This is only applicable for Micro Focus engine with versions 8.0.6 and above.

## Request Syntax
<a name="API_ListBatchJobRestartPoints_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/batch-job-executions/{{executionId}}/steps?authSecretsManagerArn={{authSecretsManagerArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBatchJobRestartPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListBatchJobRestartPoints_RequestSyntax) **   <a name="m2-ListBatchJobRestartPoints-request-uri-applicationId"></a>
The unique identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

 ** [authSecretsManagerArn](#API_ListBatchJobRestartPoints_RequestSyntax) **   <a name="m2-ListBatchJobRestartPoints-request-uri-authSecretsManagerArn"></a>
The AWS Secrets Manager containing user's credentials for authentication and authorization for List Batch Job Restart Points operation.
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [executionId](#API_ListBatchJobRestartPoints_RequestSyntax) **   <a name="m2-ListBatchJobRestartPoints-request-uri-executionId"></a>
The unique identifier of the batch job execution.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_ListBatchJobRestartPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBatchJobRestartPoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchJobSteps": [
      {
         "procStepName": "string",
         "procStepNumber": number,
         "stepCheckpoint": number,
         "stepCheckpointStatus": "string",
         "stepCheckpointTime": number,
         "stepCondCode": "string",
         "stepName": "string",
         "stepNumber": number,
         "stepRestartable": boolean
      }
   ]
}
```

## Response Elements
<a name="API_ListBatchJobRestartPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchJobSteps](#API_ListBatchJobRestartPoints_ResponseSyntax) **   <a name="m2-ListBatchJobRestartPoints-response-batchJobSteps"></a>
Returns all the batch job steps and related information for a batch job that previously ran.
Type: Array of [JobStep](API_JobStep.md) objects

## Errors
<a name="API_ListBatchJobRestartPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** ConflictException **
The parameters provided in the request conflict with existing resources.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_ListBatchJobRestartPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/ListBatchJobRestartPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/ListBatchJobRestartPoints)
