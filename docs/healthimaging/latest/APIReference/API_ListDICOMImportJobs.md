---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ListDICOMImportJobs.html
---

# ListDICOMImportJobs
<a name="API_ListDICOMImportJobs"></a>

List import jobs created for a specific data store.

## Request Syntax
<a name="API_ListDICOMImportJobs_RequestSyntax"></a>

```
GET /listDICOMImportJobs/datastore/{{datastoreId}}?jobStatus={{jobStatus}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDICOMImportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_ListDICOMImportJobs_RequestSyntax) **   <a name="healthimaging-ListDICOMImportJobs-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [jobStatus](#API_ListDICOMImportJobs_RequestSyntax) **   <a name="healthimaging-ListDICOMImportJobs-request-uri-jobStatus"></a>
The filters for listing import jobs based on status.
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`

 ** [maxResults](#API_ListDICOMImportJobs_RequestSyntax) **   <a name="healthimaging-ListDICOMImportJobs-request-uri-maxResults"></a>
The max results count. The upper bound is determined by load testing.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListDICOMImportJobs_RequestSyntax) **   <a name="healthimaging-ListDICOMImportJobs-request-uri-nextToken"></a>
The pagination token used to request the list of import jobs on the next page.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Request Body
<a name="API_ListDICOMImportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDICOMImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummaries": [
      {
         "dataAccessRoleArn": "string",
         "datastoreId": "string",
         "endedAt": number,
         "jobId": "string",
         "jobName": "string",
         "jobStatus": "string",
         "message": "string",
         "submittedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDICOMImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummaries](#API_ListDICOMImportJobs_ResponseSyntax) **   <a name="healthimaging-ListDICOMImportJobs-response-jobSummaries"></a>
A list of job summaries.
Type: Array of [DICOMImportJobSummary](API_DICOMImportJobSummary.md) objects

 ** [nextToken](#API_ListDICOMImportJobs_ResponseSyntax) **   <a name="healthimaging-ListDICOMImportJobs-response-nextToken"></a>
The pagination token used to retrieve the list of import jobs on the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Errors
<a name="API_ListDICOMImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListDICOMImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/ListDICOMImportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/ListDICOMImportJobs)
