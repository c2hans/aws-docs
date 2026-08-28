---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StopMaterializedViewRefreshTaskRun.html
---

# StopMaterializedViewRefreshTaskRun
<a name="API_StopMaterializedViewRefreshTaskRun"></a>

Stops a materialized view refresh task run for a specified materialized view table.

## Request Syntax
<a name="API_StopMaterializedViewRefreshTaskRun_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_StopMaterializedViewRefreshTaskRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_StopMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StopMaterializedViewRefreshTaskRun-request-CatalogId"></a>
The ID of the Catalog where the materialized view table resides. If none is supplied, the account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_StopMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StopMaterializedViewRefreshTaskRun-request-DatabaseName"></a>
The database where the materialized view table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_StopMaterializedViewRefreshTaskRun_RequestSyntax) **   <a name="Glue-StopMaterializedViewRefreshTaskRun-request-TableName"></a>
The name of the table to stop the materialized view refresh task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Elements
<a name="API_StopMaterializedViewRefreshTaskRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopMaterializedViewRefreshTaskRun_Errors"></a>

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

 ** MaterializedViewRefreshTaskNotRunningException **
Exception thrown when stopping a task that is not in running state.
HTTP Status Code: 400

 ** MaterializedViewRefreshTaskStoppingException **
Exception thrown when a task is already in stopping state.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StopMaterializedViewRefreshTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StopMaterializedViewRefreshTaskRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
