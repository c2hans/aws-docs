---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListVariantImportJobs.html
---

# ListVariantImportJobs
<a name="API_ListVariantImportJobs"></a>

**Important**
 AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html).

Retrieves a list of variant import jobs.

## Request Syntax
<a name="API_ListVariantImportJobs_RequestSyntax"></a>

```
POST /import/variants?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
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
<a name="API_ListVariantImportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListVariantImportJobs_RequestSyntax) **   <a name="omics-ListVariantImportJobs-request-uri-maxResults"></a>
The maximum number of import jobs to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListVariantImportJobs_RequestSyntax) **   <a name="omics-ListVariantImportJobs-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10000.

## Request Body
<a name="API_ListVariantImportJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListVariantImportJobs_RequestSyntax) **   <a name="omics-ListVariantImportJobs-request-filter"></a>
A filter to apply to the list.
Type: [ListVariantImportJobsFilter](API_ListVariantImportJobsFilter.md) object
Required: No

 ** [ids](#API_ListVariantImportJobs_RequestSyntax) **   <a name="omics-ListVariantImportJobs-request-ids"></a>
A list of job IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## Response Syntax
<a name="API_ListVariantImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "variantImportJobs": [
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
         "updateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVariantImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVariantImportJobs_ResponseSyntax) **   <a name="omics-ListVariantImportJobs-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String

 ** [variantImportJobs](#API_ListVariantImportJobs_ResponseSyntax) **   <a name="omics-ListVariantImportJobs-response-variantImportJobs"></a>
A list of jobs.
Type: Array of [VariantImportJobItem](API_VariantImportJobItem.md) objects

## Errors
<a name="API_ListVariantImportJobs_Errors"></a>

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
<a name="API_ListVariantImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListVariantImportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListVariantImportJobs)
