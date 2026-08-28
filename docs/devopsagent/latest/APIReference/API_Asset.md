---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Asset.html
---

# Asset
<a name="API_Asset"></a>

Represents an asset in an agent space, including its identifier, type, metadata, version, and timestamps.

## Contents
<a name="API_Asset_Contents"></a>

 ** assetId **   <a name="devopsagent-Type-Asset-assetId"></a>
The unique identifier for this asset
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** assetType **   <a name="devopsagent-Type-Asset-assetType"></a>
The type of this asset
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Asset-createdAt"></a>
Timestamp when this asset was created
Type: Timestamp
Required: Yes

 ** metadata **   <a name="devopsagent-Type-Asset-metadata"></a>
The metadata for this asset
Type: JSON value
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Asset-updatedAt"></a>
Timestamp when this asset was last updated
Type: Timestamp
Required: Yes

 ** version **   <a name="devopsagent-Type-Asset-version"></a>
The version number of this asset
Type: Integer
Required: Yes

## See Also
<a name="API_Asset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Asset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Asset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Asset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
