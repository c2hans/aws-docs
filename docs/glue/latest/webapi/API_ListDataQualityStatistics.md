---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListDataQualityStatistics.html
---

# ListDataQualityStatistics
<a name="API_ListDataQualityStatistics"></a>

Retrieves a list of data quality statistics.

## Request Syntax
<a name="API_ListDataQualityStatistics_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProfileId": "{{string}}",
   "StatisticId": "{{string}}",
   "TimestampFilter": {
      "RecordedAfter": {{number}},
      "RecordedBefore": {{number}}
   }
}
```

## Request Parameters
<a name="API_ListDataQualityStatistics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDataQualityStatistics_RequestSyntax) **   <a name="Glue-ListDataQualityStatistics-request-MaxResults"></a>
The maximum number of results to return in this request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListDataQualityStatistics_RequestSyntax) **   <a name="Glue-ListDataQualityStatistics-request-NextToken"></a>
A pagination token to request the next page of results.
Type: String
Required: No

 ** [ProfileId](#API_ListDataQualityStatistics_RequestSyntax) **   <a name="Glue-ListDataQualityStatistics-request-ProfileId"></a>
The Profile ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [StatisticId](#API_ListDataQualityStatistics_RequestSyntax) **   <a name="Glue-ListDataQualityStatistics-request-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [TimestampFilter](#API_ListDataQualityStatistics_RequestSyntax) **   <a name="Glue-ListDataQualityStatistics-request-TimestampFilter"></a>
A timestamp filter.
Type: [TimestampFilter](API_TimestampFilter.md) object
Required: No

## Response Syntax
<a name="API_ListDataQualityStatistics_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Statistics": [
      {
         "ColumnsReferenced": [ "string" ],
         "DoubleValue": number,
         "EvaluationLevel": "string",
         "InclusionAnnotation": {
            "LastModifiedOn": number,
            "Value": "string"
         },
         "ProfileId": "string",
         "RecordedOn": number,
         "ReferencedDatasets": [ "string" ],
         "RunIdentifier": {
            "JobRunId": "string",
            "RunId": "string"
         },
         "StatisticId": "string",
         "StatisticName": "string",
         "StatisticProperties": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListDataQualityStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataQualityStatistics_ResponseSyntax) **   <a name="Glue-ListDataQualityStatistics-response-NextToken"></a>
A pagination token to request the next page of results.
Type: String

 ** [Statistics](#API_ListDataQualityStatistics_ResponseSyntax) **   <a name="Glue-ListDataQualityStatistics-response-Statistics"></a>
A `StatisticSummaryList`.
Type: Array of [StatisticSummary](API_StatisticSummary.md) objects

## Errors
<a name="API_ListDataQualityStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListDataQualityStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListDataQualityStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListDataQualityStatistics)
