---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetPreparedStatement.html
---

# BatchGetPreparedStatement
<a name="API_BatchGetPreparedStatement"></a>

Returns the details of a single prepared statement or a list of up to 256 prepared statements for the array of prepared statement names that you provide. Requires you to have access to the workgroup to which the prepared statements belong. If a prepared statement cannot be retrieved for the name specified, the statement is listed in `UnprocessedPreparedStatementNames`.

## Request Syntax
<a name="API_BatchGetPreparedStatement_RequestSyntax"></a>

```
{
   "PreparedStatementNames": [ "{{string}}" ],
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetPreparedStatement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PreparedStatementNames](#API_BatchGetPreparedStatement_RequestSyntax) **   <a name="athena-BatchGetPreparedStatement-request-PreparedStatementNames"></a>
A list of prepared statement names to return.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_][a-zA-Z0-9_@:]{1,256}`
Required: Yes

 ** [WorkGroup](#API_BatchGetPreparedStatement_RequestSyntax) **   <a name="athena-BatchGetPreparedStatement-request-WorkGroup"></a>
The name of the workgroup to which the prepared statements belong.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

## Response Syntax
<a name="API_BatchGetPreparedStatement_ResponseSyntax"></a>

```
{
   "PreparedStatements": [
      {
         "Description": "string",
         "LastModifiedTime": number,
         "QueryStatement": "string",
         "StatementName": "string",
         "WorkGroupName": "string"
      }
   ],
   "UnprocessedPreparedStatementNames": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "StatementName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetPreparedStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PreparedStatements](#API_BatchGetPreparedStatement_ResponseSyntax) **   <a name="athena-BatchGetPreparedStatement-response-PreparedStatements"></a>
The list of prepared statements returned.
Type: Array of [PreparedStatement](API_PreparedStatement.md) objects

 ** [UnprocessedPreparedStatementNames](#API_BatchGetPreparedStatement_ResponseSyntax) **   <a name="athena-BatchGetPreparedStatement-response-UnprocessedPreparedStatementNames"></a>
A list of one or more prepared statements that were requested but could not be returned.
Type: Array of [UnprocessedPreparedStatementName](API_UnprocessedPreparedStatementName.md) objects

## Errors
<a name="API_BatchGetPreparedStatement_Errors"></a>

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
<a name="API_BatchGetPreparedStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/BatchGetPreparedStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/BatchGetPreparedStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
