---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListDataQualityResultsV2.html
---

# ListDataQualityResultsV2
<a name="API_ListDataQualityResultsV2"></a>

Returns a paginated list of data quality execution results for your account, filtered by the specified criteria. Use the `NextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListDataQualityResultsV2_RequestSyntax"></a>

```
{
   "Filter": {
      "DataSource": {
         "DataQualityGlueTable": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "CatalogId": "{{string}}",
            "ConnectionName": "{{string}}",
            "DatabaseName": "{{string}}",
            "PreProcessingQuery": "{{string}}",
            "TableName": "{{string}}"
         },
         "GlueTable": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "CatalogId": "{{string}}",
            "ConnectionName": "{{string}}",
            "DatabaseName": "{{string}}",
            "TableName": "{{string}}"
         }
      },
      "Dimensions": {
         "{{string}}" : "{{string}}"
      },
      "EvaluationContext": "{{string}}",
      "PublishedAfter": {{number}},
      "PublishedBefore": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDataQualityResultsV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListDataQualityResultsV2_RequestSyntax) **   <a name="Glue-ListDataQualityResultsV2-request-Filter"></a>
The filter criteria.
Type: [DataQualityResultsV2FilterCriteria](API_DataQualityResultsV2FilterCriteria.md) object
Required: No

 ** [MaxResults](#API_ListDataQualityResultsV2_RequestSyntax) **   <a name="Glue-ListDataQualityResultsV2-request-MaxResults"></a>
The maximum number of results to return. If you don't specify a value, the operation uses the default number of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListDataQualityResultsV2_RequestSyntax) **   <a name="Glue-ListDataQualityResultsV2-request-NextToken"></a>
A pagination token to retrieve the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListDataQualityResultsV2_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Results": [
      {
         "DataSource": {
            "DataQualityGlueTable": {
               "AdditionalOptions": {
                  "string" : "string"
               },
               "CatalogId": "string",
               "ConnectionName": "string",
               "DatabaseName": "string",
               "PreProcessingQuery": "string",
               "TableName": "string"
            },
            "GlueTable": {
               "AdditionalOptions": {
                  "string" : "string"
               },
               "CatalogId": "string",
               "ConnectionName": "string",
               "DatabaseName": "string",
               "TableName": "string"
            }
         },
         "Descriptors": {
            "string" : "string"
         },
         "Dimensions": {
            "string" : "string"
         },
         "EvaluationContext": "string",
         "ResultId": "string",
         "ResultPublishedOn": number
      }
   ]
}
```

## Response Elements
<a name="API_ListDataQualityResultsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataQualityResultsV2_ResponseSyntax) **   <a name="Glue-ListDataQualityResultsV2-response-NextToken"></a>
A pagination token, if more results are available.
Type: String

 ** [Results](#API_ListDataQualityResultsV2_ResponseSyntax) **   <a name="Glue-ListDataQualityResultsV2-response-Results"></a>
A list of `DataQualityResultsV2Description` objects.
Type: Array of [DataQualityResultsV2Description](API_DataQualityResultsV2Description.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_ListDataQualityResultsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListDataQualityResultsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListDataQualityResultsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListDataQualityResultsV2)
