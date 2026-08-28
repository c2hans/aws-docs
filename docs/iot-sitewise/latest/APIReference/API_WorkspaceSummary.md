---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_WorkspaceSummary.html
---

# WorkspaceSummary
<a name="API_WorkspaceSummary"></a>

Contains summary information about a workspace, including its name, ARN, status, and creation and update timestamps.

## Contents
<a name="API_WorkspaceSummary_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-WorkspaceSummary-arn"></a>
The ARN of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** createdAt **   <a name="iotsitewise-Type-WorkspaceSummary-createdAt"></a>
The date the workspace was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** name **   <a name="iotsitewise-Type-WorkspaceSummary-name"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** status **   <a name="iotsitewise-Type-WorkspaceSummary-status"></a>
The status of the workspace.
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object
Required: Yes

 ** updatedAt **   <a name="iotsitewise-Type-WorkspaceSummary-updatedAt"></a>
The date the workspace was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

## See Also
<a name="API_WorkspaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/WorkspaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/WorkspaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/WorkspaceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
