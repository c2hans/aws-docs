---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UnprocessedNamedQueryId.html
---

# UnprocessedNamedQueryId
<a name="API_UnprocessedNamedQueryId"></a>

Information about a named query ID that could not be processed.

## Contents
<a name="API_UnprocessedNamedQueryId_Contents"></a>

 ** ErrorCode **   <a name="athena-Type-UnprocessedNamedQueryId-ErrorCode"></a>
The error code returned when the processing request for the named query failed, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ErrorMessage **   <a name="athena-Type-UnprocessedNamedQueryId-ErrorMessage"></a>
The error message returned when the processing request for the named query failed, if applicable.
Type: String
Required: No

 ** NamedQueryId **   <a name="athena-Type-UnprocessedNamedQueryId-NamedQueryId"></a>
The unique identifier of the named query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: No

## See Also
<a name="API_UnprocessedNamedQueryId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UnprocessedNamedQueryId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UnprocessedNamedQueryId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UnprocessedNamedQueryId)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
