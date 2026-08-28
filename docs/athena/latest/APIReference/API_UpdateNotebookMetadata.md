---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateNotebookMetadata.html
---

# UpdateNotebookMetadata
<a name="API_UpdateNotebookMetadata"></a>

Updates the metadata for a notebook.

## Request Syntax
<a name="API_UpdateNotebookMetadata_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}",
   "NotebookId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateNotebookMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateNotebookMetadata_RequestSyntax) **   <a name="athena-UpdateNotebookMetadata-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).
This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [Name](#API_UpdateNotebookMetadata_RequestSyntax) **   <a name="athena-UpdateNotebookMetadata-request-Name"></a>
The name to update the notebook to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!.*[/:\\])[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]+`
Required: Yes

 ** [NotebookId](#API_UpdateNotebookMetadata_RequestSyntax) **   <a name="athena-UpdateNotebookMetadata-request-NotebookId"></a>
The ID of the notebook to update the metadata for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Elements
<a name="API_UpdateNotebookMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateNotebookMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request was throttled.
 ** Reason **
The reason for the query throttling, for example, when it exceeds the concurrent query limit.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNotebookMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdateNotebookMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdateNotebookMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
