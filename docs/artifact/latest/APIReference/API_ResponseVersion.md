---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ResponseVersion.html
---

# ResponseVersion
<a name="API_ResponseVersion"></a>

A versioned snapshot of a response edit.

## Contents
<a name="API_ResponseVersion_Contents"></a>

 ** responseText **   <a name="artifact-Type-ResponseVersion-responseText"></a>
The response text for this version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: Yes

 ** timestamp **   <a name="artifact-Type-ResponseVersion-timestamp"></a>
ISO 8601 timestamp of when this edit was made.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ResponseVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ResponseVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ResponseVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ResponseVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
