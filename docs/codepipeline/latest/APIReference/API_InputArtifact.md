---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_InputArtifact.html
---

# InputArtifact
<a name="API_InputArtifact"></a>

Represents information about an artifact to be worked on, such as a test or build artifact.

## Contents
<a name="API_InputArtifact_Contents"></a>

 ** name **   <a name="CodePipeline-Type-InputArtifact-name"></a>
The name of the artifact to be worked on (for example, "My App").
Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp\_Windows.zip
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

## See Also
<a name="API_InputArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/InputArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/InputArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/InputArtifact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
