---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateNamedQuery.html
---

# UpdateNamedQuery
<a name="API_UpdateNamedQuery"></a>

Updates a [NamedQuery](API_NamedQuery.md) object. The database or workgroup cannot be updated.

## Request Syntax
<a name="API_UpdateNamedQuery_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "NamedQueryId": "{{string}}",
   "QueryString": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateNamedQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateNamedQuery_RequestSyntax) **   <a name="athena-UpdateNamedQuery-request-Description"></a>
The query description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_UpdateNamedQuery_RequestSyntax) **   <a name="athena-UpdateNamedQuery-request-Name"></a>
The name of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [NamedQueryId](#API_UpdateNamedQuery_RequestSyntax) **   <a name="athena-UpdateNamedQuery-request-NamedQueryId"></a>
The unique identifier (UUID) of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: Yes

 ** [QueryString](#API_UpdateNamedQuery_RequestSyntax) **   <a name="athena-UpdateNamedQuery-request-QueryString"></a>
The contents of the query with all query statements.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

## Response Elements
<a name="API_UpdateNamedQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateNamedQuery_Errors"></a>

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
<a name="API_UpdateNamedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdateNamedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdateNamedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
