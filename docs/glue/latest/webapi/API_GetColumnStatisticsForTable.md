---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetColumnStatisticsForTable.html
---

# GetColumnStatisticsForTable
<a name="API_GetColumnStatisticsForTable"></a>

Retrieves table statistics of columns.

The Identity and Access Management (IAM) permission required for this operation is `GetTable`.

## Request Syntax
<a name="API_GetColumnStatisticsForTable_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ColumnNames": [ "{{string}}" ],
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetColumnStatisticsForTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetColumnStatisticsForTable_RequestSyntax) **   <a name="Glue-GetColumnStatisticsForTable-request-CatalogId"></a>
The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ColumnNames](#API_GetColumnStatisticsForTable_RequestSyntax) **   <a name="Glue-GetColumnStatisticsForTable-request-ColumnNames"></a>
A list of the column names.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetColumnStatisticsForTable_RequestSyntax) **   <a name="Glue-GetColumnStatisticsForTable-request-DatabaseName"></a>
The name of the catalog database where the partitions reside.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_GetColumnStatisticsForTable_RequestSyntax) **   <a name="Glue-GetColumnStatisticsForTable-request-TableName"></a>
The name of the partitions' table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetColumnStatisticsForTable_ResponseSyntax"></a>

```
{
   "ColumnStatisticsList": [
      {
         "AnalyzedTime": number,
         "ColumnName": "string",
         "ColumnType": "string",
         "StatisticsData": {
            "BinaryColumnStatisticsData": {
               "AverageLength": number,
               "MaximumLength": number,
               "NumberOfNulls": number
            },
            "BooleanColumnStatisticsData": {
               "NumberOfFalses": number,
               "NumberOfNulls": number,
               "NumberOfTrues": number
            },
            "DateColumnStatisticsData": {
               "MaximumValue": number,
               "MinimumValue": number,
               "NumberOfDistinctValues": number,
               "NumberOfNulls": number
            },
            "DecimalColumnStatisticsData": {
               "MaximumValue": {
                  "Scale": number,
                  "UnscaledValue": blob
               },
               "MinimumValue": {
                  "Scale": number,
                  "UnscaledValue": blob
               },
               "NumberOfDistinctValues": number,
               "NumberOfNulls": number
            },
            "DoubleColumnStatisticsData": {
               "MaximumValue": number,
               "MinimumValue": number,
               "NumberOfDistinctValues": number,
               "NumberOfNulls": number
            },
            "LongColumnStatisticsData": {
               "MaximumValue": number,
               "MinimumValue": number,
               "NumberOfDistinctValues": number,
               "NumberOfNulls": number
            },
            "StringColumnStatisticsData": {
               "AverageLength": number,
               "MaximumLength": number,
               "NumberOfDistinctValues": number,
               "NumberOfNulls": number
            },
            "Type": "string"
         }
      }
   ],
   "Errors": [
      {
         "ColumnName": "string",
         "Error": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetColumnStatisticsForTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ColumnStatisticsList](#API_GetColumnStatisticsForTable_ResponseSyntax) **   <a name="Glue-GetColumnStatisticsForTable-response-ColumnStatisticsList"></a>
List of ColumnStatistics.
Type: Array of [ColumnStatistics](API_ColumnStatistics.md) objects

 ** [Errors](#API_GetColumnStatisticsForTable_ResponseSyntax) **   <a name="Glue-GetColumnStatisticsForTable-response-Errors"></a>
List of ColumnStatistics that failed to be retrieved.
Type: Array of [ColumnError](API_ColumnError.md) objects

## Errors
<a name="API_GetColumnStatisticsForTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetColumnStatisticsForTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetColumnStatisticsForTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetColumnStatisticsForTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
