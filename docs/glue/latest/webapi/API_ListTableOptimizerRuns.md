---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListTableOptimizerRuns.html
---

# ListTableOptimizerRuns
<a name="API_ListTableOptimizerRuns"></a>

Lists the history of previous optimizer runs for a specific table.

## Request Syntax
<a name="API_ListTableOptimizerRuns_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TableName": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTableOptimizerRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListTableOptimizerRuns_RequestSyntax) **   <a name="Glue-ListTableOptimizerRuns-request-CatalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_ListTableOptimizerRuns_RequestSyntax) **   <a name="Glue-ListTableOptimizerRuns-request-DatabaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [MaxResults](#API_ListTableOptimizerRuns_RequestSyntax) **   <a name="Glue-ListTableOptimizerRuns-request-MaxResults"></a>
The maximum number of optimizer runs to return on each call.
Type: Integer
Required: No

 ** [NextToken](#API_ListTableOptimizerRuns_RequestSyntax) **   <a name="Glue-ListTableOptimizerRuns-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [TableName](#API_ListTableOptimizerRuns_RequestSyntax) **   <a name="Glue-ListTableOptimizerRuns-request-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Type](#API_ListTableOptimizerRuns_RequestSyntax) **   <a name="Glue-ListTableOptimizerRuns-request-Type"></a>
The type of table optimizer.
Type: String
Valid Values: `compaction | retention | orphan_file_deletion`
Required: Yes

## Response Syntax
<a name="API_ListTableOptimizerRuns_ResponseSyntax"></a>

```
{
   "CatalogId": "string",
   "DatabaseName": "string",
   "NextToken": "string",
   "TableName": "string",
   "TableOptimizerRuns": [
      {
         "compactionMetrics": {
            "IcebergMetrics": {
               "DpuHours": number,
               "JobDurationInHour": number,
               "NumberOfBytesCompacted": number,
               "NumberOfDpus": number,
               "NumberOfFilesCompacted": number
            }
         },
         "compactionStrategy": "string",
         "endTimestamp": number,
         "error": "string",
         "eventType": "string",
         "metrics": {
            "JobDurationInHour": "string",
            "NumberOfBytesCompacted": "string",
            "NumberOfDpus": "string",
            "NumberOfFilesCompacted": "string"
         },
         "orphanFileDeletionMetrics": {
            "IcebergMetrics": {
               "DpuHours": number,
               "JobDurationInHour": number,
               "NumberOfDpus": number,
               "NumberOfOrphanFilesDeleted": number
            }
         },
         "retentionMetrics": {
            "IcebergMetrics": {
               "DpuHours": number,
               "JobDurationInHour": number,
               "NumberOfDataFilesDeleted": number,
               "NumberOfDpus": number,
               "NumberOfManifestFilesDeleted": number,
               "NumberOfManifestListsDeleted": number
            }
         },
         "startTimestamp": number
      }
   ]
}
```

## Response Elements
<a name="API_ListTableOptimizerRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogId](#API_ListTableOptimizerRuns_ResponseSyntax) **   <a name="Glue-ListTableOptimizerRuns-response-CatalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [DatabaseName](#API_ListTableOptimizerRuns_ResponseSyntax) **   <a name="Glue-ListTableOptimizerRuns-response-DatabaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [NextToken](#API_ListTableOptimizerRuns_ResponseSyntax) **   <a name="Glue-ListTableOptimizerRuns-response-NextToken"></a>
A continuation token for paginating the returned list of optimizer runs, returned if the current segment of the list is not the last.
Type: String

 ** [TableName](#API_ListTableOptimizerRuns_ResponseSyntax) **   <a name="Glue-ListTableOptimizerRuns-response-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [TableOptimizerRuns](#API_ListTableOptimizerRuns_ResponseSyntax) **   <a name="Glue-ListTableOptimizerRuns-response-TableOptimizerRuns"></a>
A list of the optimizer runs associated with a table.
Type: Array of [TableOptimizerRun](API_TableOptimizerRun.md) objects

## Errors
<a name="API_ListTableOptimizerRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListTableOptimizerRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListTableOptimizerRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListTableOptimizerRuns)
