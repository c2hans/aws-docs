---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssetFileSummary.html
---

# AssetFileSummary
<a name="API_AssetFileSummary"></a>

Summary of a file within an asset, including its path, version, and timestamps.

## Contents
<a name="API_AssetFileSummary_Contents"></a>

 ** createdAt **   <a name="devopsagent-Type-AssetFileSummary-createdAt"></a>
Timestamp when this file was created
Type: Timestamp
Required: Yes

 ** path **   <a name="devopsagent-Type-AssetFileSummary-path"></a>
The path of this file within the asset
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9_./ ()-]+`
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-AssetFileSummary-updatedAt"></a>
Timestamp when this file was last updated
Type: Timestamp
Required: Yes

 ** version **   <a name="devopsagent-Type-AssetFileSummary-version"></a>
The asset version this file belongs to
Type: Integer
Required: Yes

 ** metadata **   <a name="devopsagent-Type-AssetFileSummary-metadata"></a>
The metadata for this file
Type: JSON value
Required: No

## See Also
<a name="API_AssetFileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AssetFileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AssetFileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AssetFileSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
