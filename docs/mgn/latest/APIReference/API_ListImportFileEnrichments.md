---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListImportFileEnrichments.html
---

# ListImportFileEnrichments
<a name="API_ListImportFileEnrichments"></a>

Lists import file enrichment jobs with optional filtering by job IDs.

## Request Syntax
<a name="API_ListImportFileEnrichments_RequestSyntax"></a>

```
POST /network-migration/ListImportFileEnrichments HTTP/1.1
Content-type: application/json

{
   "filters": {
      "jobIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImportFileEnrichments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImportFileEnrichments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImportFileEnrichments_RequestSyntax) **   <a name="mgn-ListImportFileEnrichments-request-filters"></a>
Filters to apply when listing import file enrichment jobs.
Type: [ListImportFileEnrichmentsFilters](API_ListImportFileEnrichmentsFilters.md) object
Required: No

 ** [maxResults](#API_ListImportFileEnrichments_RequestSyntax) **   <a name="mgn-ListImportFileEnrichments-request-maxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListImportFileEnrichments_RequestSyntax) **   <a name="mgn-ListImportFileEnrichments-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListImportFileEnrichments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "checksum": {
            "encryptionAlgorithm": "string",
            "hash": "string"
         },
         "createdAt": number,
         "endedAt": number,
         "jobID": "string",
         "s3BucketTarget": {
            "s3Bucket": "string",
            "s3BucketOwner": "string",
            "s3Key": "string"
         },
         "status": "string",
         "statusDetails": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListImportFileEnrichments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListImportFileEnrichments_ResponseSyntax) **   <a name="mgn-ListImportFileEnrichments-response-items"></a>
A list of import file enrichment jobs.
Type: Array of [ImportFileEnrichment](API_ImportFileEnrichment.md) objects

 ** [nextToken](#API_ListImportFileEnrichments_ResponseSyntax) **   <a name="mgn-ListImportFileEnrichments-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListImportFileEnrichments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ListImportFileEnrichments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListImportFileEnrichments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListImportFileEnrichments)
