---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetNamedQuery.html
---

# BatchGetNamedQuery
<a name="API_BatchGetNamedQuery"></a>

Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Requires you to have access to the workgroup in which the queries were saved. Use [ListNamedQueriesInput](API_ListNamedQueriesInput.md) to get the list of named query IDs in the specified workgroup. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under [UnprocessedNamedQueryId](API_UnprocessedNamedQueryId.md). Named queries differ from executed queries. Use [BatchGetQueryExecutionInput](API_BatchGetQueryExecutionInput.md) to get details about each unique query execution, and [ListQueryExecutionsInput](API_ListQueryExecutionsInput.md) to get a list of query execution IDs.

## Request Syntax
<a name="API_BatchGetNamedQuery_RequestSyntax"></a>

```
{
   "NamedQueryIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetNamedQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NamedQueryIds](#API_BatchGetNamedQuery_RequestSyntax) **   <a name="athena-BatchGetNamedQuery-request-NamedQueryIds"></a>
An array of query IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_BatchGetNamedQuery_ResponseSyntax"></a>

```
{
   "NamedQueries": [
      {
         "Database": "string",
         "Description": "string",
         "Name": "string",
         "NamedQueryId": "string",
         "QueryString": "string",
         "WorkGroup": "string"
      }
   ],
   "UnprocessedNamedQueryIds": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "NamedQueryId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetNamedQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NamedQueries](#API_BatchGetNamedQuery_ResponseSyntax) **   <a name="athena-BatchGetNamedQuery-response-NamedQueries"></a>
Information about the named query IDs submitted.
Type: Array of [NamedQuery](API_NamedQuery.md) objects

 ** [UnprocessedNamedQueryIds](#API_BatchGetNamedQuery_ResponseSyntax) **   <a name="athena-BatchGetNamedQuery-response-UnprocessedNamedQueryIds"></a>
Information about provided query IDs.
Type: Array of [UnprocessedNamedQueryId](API_UnprocessedNamedQueryId.md) objects

## Errors
<a name="API_BatchGetNamedQuery_Errors"></a>

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
<a name="API_BatchGetNamedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/BatchGetNamedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/BatchGetNamedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
