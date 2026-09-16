---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListVectorEnrichmentJobs.html
---

# ListVectorEnrichmentJobs
<a name="API_geospatial_ListVectorEnrichmentJobs"></a>

Retrieves a list of vector enrichment jobs.

## Request Syntax
<a name="API_geospatial_ListVectorEnrichmentJobs_RequestSyntax"></a>

```
POST /list-vector-enrichment-jobs HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## URI Request Parameters
<a name="API_geospatial_ListVectorEnrichmentJobs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geospatial_ListVectorEnrichmentJobs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_geospatial_ListVectorEnrichmentJobs_RequestSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_geospatial_ListVectorEnrichmentJobs_RequestSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-request-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** [SortBy](#API_geospatial_ListVectorEnrichmentJobs_RequestSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-request-SortBy"></a>
The parameter by which to sort the results.
Type: String
Required: No

 ** [SortOrder](#API_geospatial_ListVectorEnrichmentJobs_RequestSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-request-SortOrder"></a>
An optional value that specifies whether you want the results sorted in `Ascending` or `Descending` order.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** [StatusEquals](#API_geospatial_ListVectorEnrichmentJobs_RequestSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-request-StatusEquals"></a>
A filter that retrieves only jobs with a specific status.
Type: String
Required: No

## Response Syntax
<a name="API_geospatial_ListVectorEnrichmentJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "VectorEnrichmentJobSummaries": [
      {
         "Arn": "string",
         "CreationTime": "string",
         "DurationInSeconds": number,
         "Name": "string",
         "Status": "string",
         "Tags": {
            "string" : "string"
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_geospatial_ListVectorEnrichmentJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_geospatial_ListVectorEnrichmentJobs_ResponseSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-response-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [VectorEnrichmentJobSummaries](#API_geospatial_ListVectorEnrichmentJobs_ResponseSyntax) **   <a name="sagemaker-geospatial_ListVectorEnrichmentJobs-response-VectorEnrichmentJobSummaries"></a>
Contains summary information about the Vector Enrichment jobs.
Type: Array of [ListVectorEnrichmentJobOutputConfig](API_geospatial_ListVectorEnrichmentJobOutputConfig.md) objects

## Errors
<a name="API_geospatial_ListVectorEnrichmentJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
 ** ResourceId **

HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
 ** ResourceId **
Identifier of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** ResourceId **

HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** ResourceId **

HTTP Status Code: 400

## See Also
<a name="API_geospatial_ListVectorEnrichmentJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ListVectorEnrichmentJobs)
