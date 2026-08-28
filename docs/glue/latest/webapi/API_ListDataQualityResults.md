---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListDataQualityResults.html
---

# ListDataQualityResults
<a name="API_ListDataQualityResults"></a>

Returns all data quality execution results for your account.

## Request Syntax
<a name="API_ListDataQualityResults_RequestSyntax"></a>

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
      "JobName": "{{string}}",
      "JobRunId": "{{string}}",
      "StartedAfter": {{number}},
      "StartedBefore": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDataQualityResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListDataQualityResults_RequestSyntax) **   <a name="Glue-ListDataQualityResults-request-Filter"></a>
The filter criteria.
Type: [DataQualityResultFilterCriteria](API_DataQualityResultFilterCriteria.md) object
Required: No

 ** [MaxResults](#API_ListDataQualityResults_RequestSyntax) **   <a name="Glue-ListDataQualityResults-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListDataQualityResults_RequestSyntax) **   <a name="Glue-ListDataQualityResults-request-NextToken"></a>
A paginated token to offset the results.
Type: String
Required: No

## Response Syntax
<a name="API_ListDataQualityResults_ResponseSyntax"></a>

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
         "JobName": "string",
         "JobRunId": "string",
         "ResultId": "string",
         "StartedOn": number
      }
   ]
}
```

## Response Elements
<a name="API_ListDataQualityResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataQualityResults_ResponseSyntax) **   <a name="Glue-ListDataQualityResults-response-NextToken"></a>
A pagination token, if more results are available.
Type: String

 ** [Results](#API_ListDataQualityResults_ResponseSyntax) **   <a name="Glue-ListDataQualityResults-response-Results"></a>
A list of `DataQualityResultDescription` objects.
Type: Array of [DataQualityResultDescription](API_DataQualityResultDescription.md) objects

## Errors
<a name="API_ListDataQualityResults_Errors"></a>

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
<a name="API_ListDataQualityResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListDataQualityResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListDataQualityResults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
