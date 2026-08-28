---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ExportedEnvironmentVariable.html
---

# ExportedEnvironmentVariable
<a name="API_ExportedEnvironmentVariable"></a>

Contains information about an exported environment variable.

Exported environment variables are used in conjunction with CodePipeline to export environment variables from the current build stage to subsequent stages in the pipeline. For more information, see [Working with variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html) in the *CodePipeline User Guide*.

**Note**
 During a build, the value of a variable is available starting with the `install` phase. It can be updated between the start of the `install` phase and the end of the `post_build` phase. After the `post_build` phase ends, the value of exported variables cannot change.

## Contents
<a name="API_ExportedEnvironmentVariable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="CodeBuild-Type-ExportedEnvironmentVariable-name"></a>
The name of the exported environment variable.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** value **   <a name="CodeBuild-Type-ExportedEnvironmentVariable-value"></a>
The value assigned to the exported environment variable.
Type: String
Required: No

## See Also
<a name="API_ExportedEnvironmentVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ExportedEnvironmentVariable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ExportedEnvironmentVariable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ExportedEnvironmentVariable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
