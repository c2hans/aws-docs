---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_GetSearchResultExportJob.html
---

# GetSearchResultExportJob
<a name="API_BKS_GetSearchResultExportJob"></a>

This operation retrieves the metadata of an export job.

An export job is an operation that transmits the results of a search job to a specified S3 bucket in a .csv file.

An export job allows you to retain results of a search beyond the search job's scheduled retention of 7 days.

## Request Syntax
<a name="API_BKS_GetSearchResultExportJob_RequestSyntax"></a>

```
GET /export-search-jobs/{{ExportJobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BKS_GetSearchResultExportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExportJobIdentifier](#API_BKS_GetSearchResultExportJob_RequestSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-request-uri-ExportJobIdentifier"></a>
This is the unique string that identifies a specific export job.
Required for this operation.
Required: Yes

## Request Body
<a name="API_BKS_GetSearchResultExportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BKS_GetSearchResultExportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CompletionTime": number,
   "CreationTime": number,
   "ExportJobArn": "string",
   "ExportJobIdentifier": "string",
   "ExportSpecification": { ... },
   "SearchJobArn": "string",
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_BKS_GetSearchResultExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletionTime](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-CompletionTime"></a>
The date and time that an export job completed, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [CreationTime](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-CreationTime"></a>
The date and time that an export job was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [ExportJobArn](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-ExportJobArn"></a>
The unique Amazon Resource Name (ARN) that uniquely identifies the export job.
Type: String

 ** [ExportJobIdentifier](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-ExportJobIdentifier"></a>
This is the unique string that identifies the specified export job.
Type: String

 ** [ExportSpecification](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-ExportSpecification"></a>
The export specification consists of the destination S3 bucket to which the search results were exported, along with the destination prefix.
Type: [ExportSpecification](API_BKS_ExportSpecification.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [SearchJobArn](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-SearchJobArn"></a>
The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.
Type: String

 ** [Status](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-Status"></a>
This is the current status of the export job.
Type: String
Valid Values: `RUNNING | FAILED | COMPLETED`

 ** [StatusMessage](#API_BKS_GetSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_GetSearchResultExportJob-response-StatusMessage"></a>
A status message is a string that is returned for search job with a status of `FAILED`, along with steps to remedy and retry the operation.
Type: String

## Errors
<a name="API_BKS_GetSearchResultExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** message **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Retry the call after number of seconds.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource was not found for this request.
Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.
 ** message **
Request references a resource which does not exist.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Request was unsuccessful due to request throttling.
 ** quotaCode **
This is the code unique to the originating service with the quota.
 ** retryAfterSeconds **
Retry the call after number of seconds.
 ** serviceCode **
This is the code unique to the originating service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
 ** message **
The input fails to satisfy the constraints specified by an Amazon service.
HTTP Status Code: 400

## See Also
<a name="API_BKS_GetSearchResultExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/GetSearchResultExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/GetSearchResultExportJob)
