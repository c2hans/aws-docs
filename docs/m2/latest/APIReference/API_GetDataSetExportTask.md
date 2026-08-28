---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetExportTask.html
---

# GetDataSetExportTask
<a name="API_GetDataSetExportTask"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Gets the status of a data set import task initiated with the [CreateDataSetExportTask](API_CreateDataSetExportTask.md) operation.

## Request Syntax
<a name="API_GetDataSetExportTask_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/dataset-export-tasks/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataSetExportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetDataSetExportTask_RequestSyntax) **   <a name="m2-GetDataSetExportTask-request-uri-applicationId"></a>
The application identifier.
Pattern: `\S{1,80}`
Required: Yes

 ** [taskId](#API_GetDataSetExportTask_RequestSyntax) **   <a name="m2-GetDataSetExportTask-request-uri-taskId"></a>
The task identifier returned by the [CreateDataSetExportTask](API_CreateDataSetExportTask.md) operation.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_GetDataSetExportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataSetExportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kmsKeyArn": "string",
   "status": "string",
   "statusReason": "string",
   "summary": {
      "failed": number,
      "inProgress": number,
      "pending": number,
      "succeeded": number,
      "total": number
   },
   "taskId": "string"
}
```

## Response Elements
<a name="API_GetDataSetExportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyArn](#API_GetDataSetExportTask_ResponseSyntax) **   <a name="m2-GetDataSetExportTask-response-kmsKeyArn"></a>
The identifier of a customer managed key used for exported data set encryption.
Type: String

 ** [status](#API_GetDataSetExportTask_ResponseSyntax) **   <a name="m2-GetDataSetExportTask-response-status"></a>
The status of the task.
Type: String
Valid Values: `Creating | Running | Completed | Failed`

 ** [statusReason](#API_GetDataSetExportTask_ResponseSyntax) **   <a name="m2-GetDataSetExportTask-response-statusReason"></a>
If dataset export failed, the failure reason will show here.
Type: String

 ** [summary](#API_GetDataSetExportTask_ResponseSyntax) **   <a name="m2-GetDataSetExportTask-response-summary"></a>
A summary of the status of the task.
Type: [DataSetExportSummary](API_DataSetExportSummary.md) object

 ** [taskId](#API_GetDataSetExportTask_ResponseSyntax) **   <a name="m2-GetDataSetExportTask-response-taskId"></a>
The task identifier.
Type: String
Pattern: `\S{1,80}`

## Errors
<a name="API_GetDataSetExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

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
<a name="API_GetDataSetExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetDataSetExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetDataSetExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
