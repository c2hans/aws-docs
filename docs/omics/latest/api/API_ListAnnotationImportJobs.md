---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListAnnotationImportJobs.html
---

# ListAnnotationImportJobs
<a name="API_ListAnnotationImportJobs"></a>

**Important**
 AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html).

Retrieves a list of annotation import jobs.

## Request Syntax
<a name="API_ListAnnotationImportJobs_RequestSyntax"></a>

```
POST /import/annotations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "status": "{{string}}",
      "storeName": "{{string}}"
   },
   "ids": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListAnnotationImportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAnnotationImportJobs_RequestSyntax) **   <a name="omics-ListAnnotationImportJobs-request-uri-maxResults"></a>
The maximum number of jobs to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAnnotationImportJobs_RequestSyntax) **   <a name="omics-ListAnnotationImportJobs-request-uri-nextToken"></a>
Specifies the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10000.

## Request Body
<a name="API_ListAnnotationImportJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListAnnotationImportJobs_RequestSyntax) **   <a name="omics-ListAnnotationImportJobs-request-filter"></a>
A filter to apply to the list.
Type: [ListAnnotationImportJobsFilter](API_ListAnnotationImportJobsFilter.md) object
Required: No

 ** [ids](#API_ListAnnotationImportJobs_RequestSyntax) **   <a name="omics-ListAnnotationImportJobs-request-ids"></a>
IDs of annotation import jobs to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## Response Syntax
<a name="API_ListAnnotationImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "annotationImportJobs": [
      {
         "annotationFields": {
            "string" : "string"
         },
         "completionTime": "string",
         "creationTime": "string",
         "destinationName": "string",
         "id": "string",
         "roleArn": "string",
         "runLeftNormalization": boolean,
         "status": "string",
         "updateTime": "string",
         "versionName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnnotationImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [annotationImportJobs](#API_ListAnnotationImportJobs_ResponseSyntax) **   <a name="omics-ListAnnotationImportJobs-response-annotationImportJobs"></a>
A list of jobs.
Type: Array of [AnnotationImportJobItem](API_AnnotationImportJobItem.md) objects

 ** [nextToken](#API_ListAnnotationImportJobs_ResponseSyntax) **   <a name="omics-ListAnnotationImportJobs-response-nextToken"></a>
Specifies the pagination token from a previous request to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListAnnotationImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

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
<a name="API_ListAnnotationImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListAnnotationImportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListAnnotationImportJobs)
