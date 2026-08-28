---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GitPullRequestFilter.html
---

# GitPullRequestFilter
<a name="API_GitPullRequestFilter"></a>

The event criteria for the pull request trigger configuration, such as the lists of branches or file paths to include and exclude.

The following are valid values for the events for this filter:
+ CLOSED
+ OPEN
+ UPDATED

## Contents
<a name="API_GitPullRequestFilter_Contents"></a>

 ** branches **   <a name="CodePipeline-Type-GitPullRequestFilter-branches"></a>
The field that specifies to filter on branches for the pull request trigger configuration.
Type: [GitBranchFilterCriteria](API_GitBranchFilterCriteria.md) object
Required: No

 ** events **   <a name="CodePipeline-Type-GitPullRequestFilter-events"></a>
The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPEN | UPDATED | CLOSED`
Required: No

 ** filePaths **   <a name="CodePipeline-Type-GitPullRequestFilter-filePaths"></a>
The field that specifies to filter on file paths for the pull request trigger configuration.
Type: [GitFilePathFilterCriteria](API_GitFilePathFilterCriteria.md) object
Required: No

## See Also
<a name="API_GitPullRequestFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GitPullRequestFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GitPullRequestFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GitPullRequestFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
