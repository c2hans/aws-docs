---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListMaterializedViewRefreshTaskRuns.html
---

# ListMaterializedViewRefreshTaskRuns
<a name="API_ListMaterializedViewRefreshTaskRuns"></a>

List all task runs for a particular account.

## Request Syntax
<a name="API_ListMaterializedViewRefreshTaskRuns_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMaterializedViewRefreshTaskRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListMaterializedViewRefreshTaskRuns_RequestSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-request-CatalogId"></a>
The ID of the Catalog where the materialized view table resides. If none is supplied, the account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_ListMaterializedViewRefreshTaskRuns_RequestSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-request-DatabaseName"></a>
The database where the materialized view table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_ListMaterializedViewRefreshTaskRuns_RequestSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-request-MaxResults"></a>
The maximum number of materialized view refresh task runs to list in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListMaterializedViewRefreshTaskRuns_RequestSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [TableName](#API_ListMaterializedViewRefreshTaskRuns_RequestSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-request-TableName"></a>
The name of the table for which the materialized view resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_ListMaterializedViewRefreshTaskRuns_ResponseSyntax"></a>

```
{
   "MaterializedViewRefreshTaskRuns": [
      {
         "CatalogId": "string",
         "CreationTime": number,
         "CustomerId": "string",
         "DatabaseName": "string",
         "DPUSeconds": number,
         "EndTime": number,
         "ErrorMessage": "string",
         "LastUpdated": number,
         "MaterializedViewRefreshTaskRunId": "string",
         "ProcessedBytes": number,
         "RefreshType": "string",
         "Role": "string",
         "StartTime": number,
         "Status": "string",
         "TableName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMaterializedViewRefreshTaskRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaterializedViewRefreshTaskRuns](#API_ListMaterializedViewRefreshTaskRuns_ResponseSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-response-MaterializedViewRefreshTaskRuns"></a>
The results of the ListMaterializedViewRefreshTaskRuns action.
Type: Array of [MaterializedViewRefreshTaskRun](API_MaterializedViewRefreshTaskRun.md) objects

 ** [NextToken](#API_ListMaterializedViewRefreshTaskRuns_ResponseSyntax) **   <a name="Glue-ListMaterializedViewRefreshTaskRuns-response-NextToken"></a>
A continuation token, if not all task runs have yet been returned.
Type: String

## Errors
<a name="API_ListMaterializedViewRefreshTaskRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_ListMaterializedViewRefreshTaskRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListMaterializedViewRefreshTaskRuns)
