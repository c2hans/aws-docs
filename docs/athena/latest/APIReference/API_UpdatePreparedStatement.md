---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdatePreparedStatement.html
---

# UpdatePreparedStatement
<a name="API_UpdatePreparedStatement"></a>

Updates a prepared statement.

## Request Syntax
<a name="API_UpdatePreparedStatement_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "QueryStatement": "{{string}}",
   "StatementName": "{{string}}",
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePreparedStatement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdatePreparedStatement_RequestSyntax) **   <a name="athena-UpdatePreparedStatement-request-Description"></a>
The description of the prepared statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [QueryStatement](#API_UpdatePreparedStatement_RequestSyntax) **   <a name="athena-UpdatePreparedStatement-request-QueryStatement"></a>
The query string for the prepared statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** [StatementName](#API_UpdatePreparedStatement_RequestSyntax) **   <a name="athena-UpdatePreparedStatement-request-StatementName"></a>
The name of the prepared statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_][a-zA-Z0-9_@:]{1,256}`
Required: Yes

 ** [WorkGroup](#API_UpdatePreparedStatement_RequestSyntax) **   <a name="athena-UpdatePreparedStatement-request-WorkGroup"></a>
The workgroup for the prepared statement.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

## Response Elements
<a name="API_UpdatePreparedStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePreparedStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePreparedStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdatePreparedStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdatePreparedStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
