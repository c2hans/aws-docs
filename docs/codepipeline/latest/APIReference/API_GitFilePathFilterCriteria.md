---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GitFilePathFilterCriteria.html
---

# GitFilePathFilterCriteria
<a name="API_GitFilePathFilterCriteria"></a>

The Git repository file paths specified as filter criteria to start the pipeline.

## Contents
<a name="API_GitFilePathFilterCriteria_Contents"></a>

 ** excludes **   <a name="CodePipeline-Type-GitFilePathFilterCriteria-excludes"></a>
The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** includes **   <a name="CodePipeline-Type-GitFilePathFilterCriteria-includes"></a>
The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

## See Also
<a name="API_GitFilePathFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitFilePathFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitFilePathFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitFilePathFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
