---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListDataQualityRulesetEvaluationRuns.html
---

# ListDataQualityRulesetEvaluationRuns
<a name="API_ListDataQualityRulesetEvaluationRuns"></a>

Lists all the runs meeting the filter criteria, where a ruleset is evaluated against a data source.

## Request Syntax
<a name="API_ListDataQualityRulesetEvaluationRuns_RequestSyntax"></a>

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
      "StartedAfter": {{number}},
      "StartedBefore": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDataQualityRulesetEvaluationRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListDataQualityRulesetEvaluationRuns_RequestSyntax) **   <a name="Glue-ListDataQualityRulesetEvaluationRuns-request-Filter"></a>
The filter criteria.
Type: [DataQualityRulesetEvaluationRunFilter](API_DataQualityRulesetEvaluationRunFilter.md) object
Required: No

 ** [MaxResults](#API_ListDataQualityRulesetEvaluationRuns_RequestSyntax) **   <a name="Glue-ListDataQualityRulesetEvaluationRuns-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListDataQualityRulesetEvaluationRuns_RequestSyntax) **   <a name="Glue-ListDataQualityRulesetEvaluationRuns-request-NextToken"></a>
A paginated token to offset the results.
Type: String
Required: No

## Response Syntax
<a name="API_ListDataQualityRulesetEvaluationRuns_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Runs": [
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
         "RunId": "string",
         "StartedOn": number,
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDataQualityRulesetEvaluationRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataQualityRulesetEvaluationRuns_ResponseSyntax) **   <a name="Glue-ListDataQualityRulesetEvaluationRuns-response-NextToken"></a>
A pagination token, if more results are available.
Type: String

 ** [Runs](#API_ListDataQualityRulesetEvaluationRuns_ResponseSyntax) **   <a name="Glue-ListDataQualityRulesetEvaluationRuns-response-Runs"></a>
A list of `DataQualityRulesetEvaluationRunDescription` objects representing data quality ruleset runs.
Type: Array of [DataQualityRulesetEvaluationRunDescription](API_DataQualityRulesetEvaluationRunDescription.md) objects

## Errors
<a name="API_ListDataQualityRulesetEvaluationRuns_Errors"></a>

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
<a name="API_ListDataQualityRulesetEvaluationRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListDataQualityRulesetEvaluationRuns)
