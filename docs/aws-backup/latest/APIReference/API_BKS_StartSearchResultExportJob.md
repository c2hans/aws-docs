---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_StartSearchResultExportJob.html
---

# StartSearchResultExportJob
<a name="API_BKS_StartSearchResultExportJob"></a>

This operations starts a job to export the results of search job to a designated S3 bucket.

## Request Syntax
<a name="API_BKS_StartSearchResultExportJob_RequestSyntax"></a>

```
PUT /export-search-jobs HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ExportSpecification": { ... },
   "RoleArn": "{{string}}",
   "SearchJobIdentifier": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_BKS_StartSearchResultExportJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BKS_StartSearchResultExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_BKS_StartSearchResultExportJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-request-ClientToken"></a>
Include this parameter to allow multiple identical calls for idempotency.
A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.
Type: String
Required: No

 ** [ExportSpecification](#API_BKS_StartSearchResultExportJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-request-ExportSpecification"></a>
This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.
Type: [ExportSpecification](API_BKS_ExportSpecification.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [RoleArn](#API_BKS_StartSearchResultExportJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-request-RoleArn"></a>
This parameter specifies the role ARN used to start the search results export jobs.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov):iam::[a-z0-9-]+:role/(.+)`
Required: No

 ** [SearchJobIdentifier](#API_BKS_StartSearchResultExportJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-request-SearchJobIdentifier"></a>
The unique string that specifies the search job.
Type: String
Required: Yes

 ** [Tags](#API_BKS_StartSearchResultExportJob_RequestSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-request-Tags"></a>
Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: \+ - = . \_ : /.
Type: String to string map
Required: No

## Response Syntax
<a name="API_BKS_StartSearchResultExportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExportJobArn": "string",
   "ExportJobIdentifier": "string"
}
```

## Response Elements
<a name="API_BKS_StartSearchResultExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportJobArn](#API_BKS_StartSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-response-ExportJobArn"></a>
This is the unique ARN (Amazon Resource Name) that belongs to the new export job.
Type: String

 ** [ExportJobIdentifier](#API_BKS_StartSearchResultExportJob_ResponseSyntax) **   <a name="Backup-BKS_StartSearchResultExportJob-response-ExportJobIdentifier"></a>
This is the unique identifier that specifies the new export job.
Type: String

## Errors
<a name="API_BKS_StartSearchResultExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.
A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** message **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
Identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request denied due to exceeding the quota limits permitted.
 ** message **
This request was not successful due to a service quota exceeding limits.
 ** quotaCode **
This is the code specific to the quota type.
 ** resourceId **
Identifier of the resource.
 ** resourceType **
Type of resource.
 ** serviceCode **
This is the code unique to the originating service with the quota.
HTTP Status Code: 402

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
<a name="API_BKS_StartSearchResultExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/StartSearchResultExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/StartSearchResultExportJob)
