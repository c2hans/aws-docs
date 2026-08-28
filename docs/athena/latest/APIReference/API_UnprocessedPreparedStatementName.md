---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UnprocessedPreparedStatementName.html
---

# UnprocessedPreparedStatementName
<a name="API_UnprocessedPreparedStatementName"></a>

The name of a prepared statement that could not be returned.

## Contents
<a name="API_UnprocessedPreparedStatementName_Contents"></a>

 ** ErrorCode **   <a name="athena-Type-UnprocessedPreparedStatementName-ErrorCode"></a>
The error code returned when the request for the prepared statement failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ErrorMessage **   <a name="athena-Type-UnprocessedPreparedStatementName-ErrorMessage"></a>
The error message containing the reason why the prepared statement could not be returned. The following error messages are possible:
+  `INVALID_INPUT` - The name of the prepared statement that was provided is not valid (for example, the name is too long).
+  `STATEMENT_NOT_FOUND` - A prepared statement with the name provided could not be found.
+  `UNAUTHORIZED` - The requester does not have permission to access the workgroup that contains the prepared statement.
Type: String
Required: No

 ** StatementName **   <a name="athena-Type-UnprocessedPreparedStatementName-StatementName"></a>
The name of a prepared statement that could not be returned due to an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_][a-zA-Z0-9_@:]{1,256}`
Required: No

## See Also
<a name="API_UnprocessedPreparedStatementName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UnprocessedPreparedStatementName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UnprocessedPreparedStatementName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UnprocessedPreparedStatementName)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
