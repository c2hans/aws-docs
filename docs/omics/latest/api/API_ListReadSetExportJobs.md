---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListReadSetExportJobs.html
---

# ListReadSetExportJobs
<a name="API_ListReadSetExportJobs"></a>

Retrieves a list of read set export jobs in a JSON formatted response. This API operation is used to check the status of a read set export job initiated by the `StartReadSetExportJob` API operation.

## Request Syntax
<a name="API_ListReadSetExportJobs_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/exportjobs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "createdAfter": "{{string}}",
      "createdBefore": "{{string}}",
      "status": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListReadSetExportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListReadSetExportJobs_RequestSyntax) **   <a name="omics-ListReadSetExportJobs-request-uri-maxResults"></a>
The maximum number of jobs to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListReadSetExportJobs_RequestSyntax) **   <a name="omics-ListReadSetExportJobs-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceStoreId](#API_ListReadSetExportJobs_RequestSyntax) **   <a name="omics-ListReadSetExportJobs-request-uri-sequenceStoreId"></a>
The jobs' sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_ListReadSetExportJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListReadSetExportJobs_RequestSyntax) **   <a name="omics-ListReadSetExportJobs-request-filter"></a>
A filter to apply to the list.
Type: [ExportReadSetFilter](API_ExportReadSetFilter.md) object
Required: No

## Response Syntax
<a name="API_ListReadSetExportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "exportJobs": [
      {
         "completionTime": "string",
         "creationTime": "string",
         "destination": "string",
         "id": "string",
         "sequenceStoreId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListReadSetExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exportJobs](#API_ListReadSetExportJobs_ResponseSyntax) **   <a name="omics-ListReadSetExportJobs-response-exportJobs"></a>
A list of jobs.
Type: Array of [ExportReadSetJobDetail](API_ExportReadSetJobDetail.md) objects

 ** [nextToken](#API_ListReadSetExportJobs_ResponseSyntax) **   <a name="omics-ListReadSetExportJobs-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListReadSetExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListReadSetExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListReadSetExportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListReadSetExportJobs)
