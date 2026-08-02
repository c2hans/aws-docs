---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartMaterializedViewRefreshTaskRun.html
---

# StartMaterializedViewRefreshTaskRun
<a name="API_StartMaterializedViewRefreshTaskRun"></a>

Starts a materialized view refresh task run, for a specified materialized view table.

## Request Syntax
<a name="API_StartMaterializedViewRefreshTaskRun_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "FullRefresh": {{boolean}},
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMaterializedViewRefreshTaskRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_StartMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StartMaterializedViewRefreshTaskRun-request-CatalogId"></a>
The ID of the Catalog where the materialized view table resides. If none is supplied, the account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_StartMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StartMaterializedViewRefreshTaskRun-request-DatabaseName"></a>
The database where the materialized view table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [FullRefresh](#API_StartMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StartMaterializedViewRefreshTaskRun-request-FullRefresh"></a>
Specifies whether this is a full refresh of the task run.
Type: Boolean
Required: No

 ** [TableName](#API_StartMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StartMaterializedViewRefreshTaskRun-request-TableName"></a>
The name of the table to generate run the materialized view refresh task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_StartMaterializedViewRefreshTaskRun_ResponseSyntax"></a>

```
{
   "MaterializedViewRefreshTaskRunId": "string"
}
```

## Response Elements
<a name="API_StartMaterializedViewRefreshTaskRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaterializedViewRefreshTaskRunId](#API_StartMaterializedViewRefreshTaskRun_ResponseSyntax) **   <a name="Glue-StartMaterializedViewRefreshTaskRun-response-MaterializedViewRefreshTaskRunId"></a>
The identifier for the materialized view refresh task run.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_StartMaterializedViewRefreshTaskRun_Errors"></a>

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

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** MaterializedViewRefreshTaskRunningException **
Exception thrown when a task is already in running state.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartMaterializedViewRefreshTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartMaterializedViewRefreshTaskRun)
