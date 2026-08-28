---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetImportFileTask.html
---

# GetImportFileTask
<a name="API_GetImportFileTask"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves the details about a specific import task.

## Request Syntax
<a name="API_GetImportFileTask_RequestSyntax"></a>

```
GET /get-import-file-task/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImportFileTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-request-uri-id"></a>
 The ID of the import file task. This ID is returned in the response of [StartImportFileTask](API_StartImportFileTask.md).
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetImportFileTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImportFileTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completionTime": number,
   "id": "string",
   "importName": "string",
   "inputS3Bucket": "string",
   "inputS3Key": "string",
   "numberOfRecordsFailed": number,
   "numberOfRecordsSuccess": number,
   "startTime": number,
   "status": "string",
   "statusReportS3Bucket": "string",
   "statusReportS3Key": "string"
}
```

## Response Elements
<a name="API_GetImportFileTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completionTime](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-completionTime"></a>
 The time that the import task completed.
Type: Timestamp

 ** [id](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-id"></a>
 The import file task `id` returned in the response of [StartImportFileTask](API_StartImportFileTask.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [importName](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-importName"></a>
 The name of the import task given in [StartImportFileTask](API_StartImportFileTask.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [inputS3Bucket](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-inputS3Bucket"></a>
 The S3 bucket where import file is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`

 ** [inputS3Key](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-inputS3Key"></a>
 The Amazon S3 key name of the import file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [numberOfRecordsFailed](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-numberOfRecordsFailed"></a>
 The number of records that failed to be imported.
Type: Integer

 ** [numberOfRecordsSuccess](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-numberOfRecordsSuccess"></a>
 The number of records successfully imported.
Type: Integer

 ** [startTime](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-startTime"></a>
 Start time of the import task.
Type: Timestamp

 ** [status](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-status"></a>
 Status of import file task.
Type: String
Valid Values: `ImportInProgress | ImportFailed | ImportPartialSuccess | ImportSuccess | DeleteInProgress | DeleteFailed | DeletePartialSuccess | DeleteSuccess`

 ** [statusReportS3Bucket](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-statusReportS3Bucket"></a>
 The S3 bucket name for status report of import task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`

 ** [statusReportS3Key](#API_GetImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-GetImportFileTask-response-statusReportS3Key"></a>
 The Amazon S3 key name for status report of import task. The report contains details about whether each record imported successfully or why it did not.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_GetImportFileTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_GetImportFileTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetImportFileTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetImportFileTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
