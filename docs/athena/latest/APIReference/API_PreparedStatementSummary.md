---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_PreparedStatementSummary.html
---

# PreparedStatementSummary
<a name="API_PreparedStatementSummary"></a>

The name and last modified time of the prepared statement.

## Contents
<a name="API_PreparedStatementSummary_Contents"></a>

 ** LastModifiedTime **   <a name="athena-Type-PreparedStatementSummary-LastModifiedTime"></a>
The last modified time of the prepared statement.
Type: Timestamp
Required: No

 ** StatementName **   <a name="athena-Type-PreparedStatementSummary-StatementName"></a>
The name of the prepared statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_][a-zA-Z0-9_@:]{1,256}`
Required: No

## See Also
<a name="API_PreparedStatementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/PreparedStatementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/PreparedStatementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/PreparedStatementSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
