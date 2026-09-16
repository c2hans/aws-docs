---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_StartBatchJob.html
---

# StartBatchJob
<a name="API_StartBatchJob"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Starts a batch job and returns the unique identifier of this execution of the batch job. The associated application must be running in order to start the batch job.

## Request Syntax
<a name="API_StartBatchJob_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/batch-job HTTP/1.1
Content-type: application/json

{
   "authSecretsManagerArn": "{{string}}",
   "batchJobIdentifier": { ... },
   "jobParams": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartBatchJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_StartBatchJob_RequestSyntax) **   <a name="m2-StartBatchJob-request-uri-applicationId"></a>
The unique identifier of the application associated with this batch job.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_StartBatchJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authSecretsManagerArn](#API_StartBatchJob_RequestSyntax) **   <a name="m2-StartBatchJob-request-authSecretsManagerArn"></a>
The AWS Secrets Manager containing user's credentials for authentication and authorization for Start Batch Job execution operation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [batchJobIdentifier](#API_StartBatchJob_RequestSyntax) **   <a name="m2-StartBatchJob-request-batchJobIdentifier"></a>
The unique identifier of the batch job.
Type: [BatchJobIdentifier](API_BatchJobIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [jobParams](#API_StartBatchJob_RequestSyntax) **   <a name="m2-StartBatchJob-request-jobParams"></a>
The collection of batch job parameters. For details about limits for keys and values, see [Coding variables in JCL](https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 500 items.
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Key Pattern: `[A-Za-z][A-Za-z0-9]{1,31}`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_StartBatchJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionId": "string"
}
```

## Response Elements
<a name="API_StartBatchJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionId](#API_StartBatchJob_ResponseSyntax) **   <a name="m2-StartBatchJob-response-executionId"></a>
The unique identifier of this execution of the batch job.
Type: String
Pattern: `\S{1,80}`

## Errors
<a name="API_StartBatchJob_Errors"></a>

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
<a name="API_StartBatchJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/StartBatchJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/StartBatchJob)
