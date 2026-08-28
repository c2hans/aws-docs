---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PackageVersionHistory.html
---

# PackageVersionHistory
<a name="API_PackageVersionHistory"></a>

Details about a package version.

## Contents
<a name="API_PackageVersionHistory_Contents"></a>

 ** CommitMessage **   <a name="opensearchservice-Type-PackageVersionHistory-CommitMessage"></a>
A message associated with the package version when it was uploaded.
Type: String
Length Constraints: Maximum length of 160.
Required: No

 ** CreatedAt **   <a name="opensearchservice-Type-PackageVersionHistory-CreatedAt"></a>
The date and time when the package was created.
Type: Timestamp
Required: No

 ** PackageConfiguration **   <a name="opensearchservice-Type-PackageVersionHistory-PackageConfiguration"></a>
The configuration details for a specific version of a package.
Type: [PackageConfiguration](API_PackageConfiguration.md) object
Required: No

 ** PackageVersion **   <a name="opensearchservice-Type-PackageVersionHistory-PackageVersion"></a>
The package version.
Type: String
Required: No

 ** PluginProperties **   <a name="opensearchservice-Type-PackageVersionHistory-PluginProperties"></a>
Additional information about plugin properties if the package is a `ZIP-PLUGIN` package.
Type: [PluginProperties](API_PluginProperties.md) object
Required: No

## See Also
<a name="API_PackageVersionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PackageVersionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PackageVersionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PackageVersionHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
