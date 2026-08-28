---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CurrentRevision.html
---

# CurrentRevision
<a name="API_CurrentRevision"></a>

Represents information about a current revision.

## Contents
<a name="API_CurrentRevision_Contents"></a>

 ** changeIdentifier **   <a name="CodePipeline-Type-CurrentRevision-changeIdentifier"></a>
The change identifier for the current revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** revision **   <a name="CodePipeline-Type-CurrentRevision-revision"></a>
The revision ID of the current version of an artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: Yes

 ** created **   <a name="CodePipeline-Type-CurrentRevision-created"></a>
The date and time when the most recent revision of the artifact was created, in timestamp format.
Type: Timestamp
Required: No

 ** revisionSummary **   <a name="CodePipeline-Type-CurrentRevision-revisionSummary"></a>
The summary of the most recent revision of the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_CurrentRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/CurrentRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/CurrentRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/CurrentRevision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
