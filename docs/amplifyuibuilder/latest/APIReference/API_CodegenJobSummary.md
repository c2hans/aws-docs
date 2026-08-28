---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJobSummary.html
---

# CodegenJobSummary
<a name="API_CodegenJobSummary"></a>

A summary of the basic information about the code generation job.

## Contents
<a name="API_CodegenJobSummary_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-CodegenJobSummary-appId"></a>
The unique ID of the Amplify app associated with the code generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `d[a-z0-9]+`
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-CodegenJobSummary-environmentName"></a>
The name of the backend environment associated with the code generation job.
Type: String
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-CodegenJobSummary-id"></a>
The unique ID for the code generation job summary.
Type: String
Required: Yes

 ** createdAt **   <a name="amplifyuibuilder-Type-CodegenJobSummary-createdAt"></a>
The time that the code generation job summary was created.
Type: Timestamp
Required: No

 ** modifiedAt **   <a name="amplifyuibuilder-Type-CodegenJobSummary-modifiedAt"></a>
The time that the code generation job summary was modified.
Type: Timestamp
Required: No

## See Also
<a name="API_CodegenJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CodegenJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CodegenJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CodegenJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
