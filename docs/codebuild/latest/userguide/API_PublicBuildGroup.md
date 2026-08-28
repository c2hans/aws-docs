---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/API_PublicBuildGroup.html
---

# PublicBuildGroup
<a name="API_PublicBuildGroup"></a>

**Note**
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicBuildGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 **currentBuildSummary**   <a name="CodeBuild-Type-PublicBuildGroup-currentBuildSummary"></a>
Type: [PublicBuildSummary](API_PublicBuildSummary.md) object
Required: No

 **dependsOn**   <a name="CodeBuild-Type-PublicBuildGroup-dependsOn"></a>
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 **identifier**   <a name="CodeBuild-Type-PublicBuildGroup-identifier"></a>
Type: String
Required: No

 **ignoreFailure**   <a name="CodeBuild-Type-PublicBuildGroup-ignoreFailure"></a>
Type: Boolean
Required: No

 **priorBuildSummaryList**   <a name="CodeBuild-Type-PublicBuildGroup-priorBuildSummaryList"></a>
Type: Array of [PublicBuildSummary](API_PublicBuildSummary.md) objects
Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
