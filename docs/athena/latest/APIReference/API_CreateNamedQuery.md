---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateNamedQuery.html
---

# CreateNamedQuery
<a name="API_CreateNamedQuery"></a>

Creates a named query in the specified workgroup. Requires that you have access to the workgroup.

## Request Syntax
<a name="API_CreateNamedQuery_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Database": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "QueryString": "{{string}}",
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateNamedQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateNamedQuery_RequestSyntax) **   <a name="athena-CreateNamedQuery-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another `CreateNamedQuery` request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the `QueryString`, an error is returned.
This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [Database](#API_CreateNamedQuery_RequestSyntax) **   <a name="athena-CreateNamedQuery-request-Database"></a>
The database to which the query belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Description](#API_CreateNamedQuery_RequestSyntax) **   <a name="athena-CreateNamedQuery-request-Description"></a>
The query description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Name](#API_CreateNamedQuery_RequestSyntax) **   <a name="athena-CreateNamedQuery-request-Name"></a>
The query name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [QueryString](#API_CreateNamedQuery_RequestSyntax) **   <a name="athena-CreateNamedQuery-request-QueryString"></a>
The contents of the query with all query statements.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** [WorkGroup](#API_CreateNamedQuery_RequestSyntax) **   <a name="athena-CreateNamedQuery-request-WorkGroup"></a>
The name of the workgroup in which the named query is being created.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## Response Syntax
<a name="API_CreateNamedQuery_ResponseSyntax"></a>

```
{
   "NamedQueryId": "string"
}
```

## Response Elements
<a name="API_CreateNamedQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NamedQueryId](#API_CreateNamedQuery_ResponseSyntax) **   <a name="athena-CreateNamedQuery-response-NamedQueryId"></a>
The unique ID of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`

## Errors
<a name="API_CreateNamedQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateNamedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateNamedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CreateNamedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
