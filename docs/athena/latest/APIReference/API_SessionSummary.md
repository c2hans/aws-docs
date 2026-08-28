---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_SessionSummary.html
---

# SessionSummary
<a name="API_SessionSummary"></a>

Contains summary information about a session.

## Contents
<a name="API_SessionSummary_Contents"></a>

 ** Description **   <a name="athena-Type-SessionSummary-Description"></a>
The session description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** EngineVersion **   <a name="athena-Type-SessionSummary-EngineVersion"></a>
The engine version used by the session (for example, `PySpark engine version 3`).
Type: [EngineVersion](API_EngineVersion.md) object
Required: No

 ** NotebookVersion **   <a name="athena-Type-SessionSummary-NotebookVersion"></a>
The notebook version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SessionId **   <a name="athena-Type-SessionSummary-SessionId"></a>
The session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Status **   <a name="athena-Type-SessionSummary-Status"></a>
Contains information about the session status.
Type: [SessionStatus](API_SessionStatus.md) object
Required: No

## See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/SessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/SessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/SessionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
