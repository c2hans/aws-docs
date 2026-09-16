---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListMetadataTransferJobs.html
---

# ListMetadataTransferJobs
<a name="API_ListMetadataTransferJobs"></a>

Lists the metadata transfer jobs.

## Request Syntax
<a name="API_ListMetadataTransferJobs_RequestSyntax"></a>

```
POST /metadata-transfer-jobs-list HTTP/1.1
Content-type: application/json

{
   "destinationType": "{{string}}",
   "filters": [
      { ... }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMetadataTransferJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMetadataTransferJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationType](#API_ListMetadataTransferJobs_RequestSyntax) **   <a name="tm-ListMetadataTransferJobs-request-destinationType"></a>
The metadata transfer job's destination type.
Type: String
Valid Values: `s3 | iotsitewise | iottwinmaker`
Required: Yes

 ** [filters](#API_ListMetadataTransferJobs_RequestSyntax) **   <a name="tm-ListMetadataTransferJobs-request-filters"></a>
An object that filters metadata transfer jobs.
Type: Array of [ListMetadataTransferJobsFilter](API_ListMetadataTransferJobsFilter.md) objects
Required: No

 ** [maxResults](#API_ListMetadataTransferJobs_RequestSyntax) **   <a name="tm-ListMetadataTransferJobs-request-maxResults"></a>
The maximum number of results to return at one time.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListMetadataTransferJobs_RequestSyntax) **   <a name="tm-ListMetadataTransferJobs-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

 ** [sourceType](#API_ListMetadataTransferJobs_RequestSyntax) **   <a name="tm-ListMetadataTransferJobs-request-sourceType"></a>
The metadata transfer job's source type.
Type: String
Valid Values: `s3 | iotsitewise | iottwinmaker`
Required: Yes

## Response Syntax
<a name="API_ListMetadataTransferJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metadataTransferJobSummaries": [
      {
         "arn": "string",
         "creationDateTime": number,
         "metadataTransferJobId": "string",
         "progress": {
            "failedCount": number,
            "skippedCount": number,
            "succeededCount": number,
            "totalCount": number
         },
         "status": {
            "error": {
               "code": "string",
               "message": "string"
            },
            "queuedPosition": number,
            "state": "string"
         },
         "updateDateTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMetadataTransferJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metadataTransferJobSummaries](#API_ListMetadataTransferJobs_ResponseSyntax) **   <a name="tm-ListMetadataTransferJobs-response-metadataTransferJobSummaries"></a>
The metadata transfer job summaries.
Type: Array of [MetadataTransferJobSummary](API_MetadataTransferJobSummary.md) objects

 ** [nextToken](#API_ListMetadataTransferJobs_ResponseSyntax) **   <a name="tm-ListMetadataTransferJobs-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

## Errors
<a name="API_ListMetadataTransferJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListMetadataTransferJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListMetadataTransferJobs)
