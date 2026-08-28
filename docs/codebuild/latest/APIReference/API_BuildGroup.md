---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildGroup.html
---

# BuildGroup
<a name="API_BuildGroup"></a>

Contains information about a batch build build group. Build groups are used to combine builds that can run in parallel, while still being able to set dependencies on other build groups.

## Contents
<a name="API_BuildGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currentBuildSummary **   <a name="CodeBuild-Type-BuildGroup-currentBuildSummary"></a>
A `BuildSummary` object that contains a summary of the current build group.
Type: [BuildSummary](API_BuildSummary.md) object
Required: No

 ** dependsOn **   <a name="CodeBuild-Type-BuildGroup-dependsOn"></a>
An array of strings that contain the identifiers of the build groups that this build group depends on.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** identifier **   <a name="CodeBuild-Type-BuildGroup-identifier"></a>
Contains the identifier of the build group.
Type: String
Required: No

 ** ignoreFailure **   <a name="CodeBuild-Type-BuildGroup-ignoreFailure"></a>
Specifies if failures in this build group can be ignored.
Type: Boolean
Required: No

 ** priorBuildSummaryList **   <a name="CodeBuild-Type-BuildGroup-priorBuildSummaryList"></a>
An array of `BuildSummary` objects that contain summaries of previous build groups.
Type: Array of [BuildSummary](API_BuildSummary.md) objects
Required: No

## See Also
<a name="API_BuildGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
