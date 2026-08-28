---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssetContent.html
---

# AssetContent
<a name="API_AssetContent"></a>

Content for an asset: a single file, a zip bundle, or a source URL to import from

## Contents
<a name="API_AssetContent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** file **   <a name="devopsagent-Type-AssetContent-file"></a>
A single file with path and content
Type: [AssetFileContent](API_AssetFileContent.md) object
Required: No

 ** sourceUrl **   <a name="devopsagent-Type-AssetContent-sourceUrl"></a>
A source URL to import asset content from
Type: [AssetSourceUrlContent](API_AssetSourceUrlContent.md) object
Required: No

 ** zip **   <a name="devopsagent-Type-AssetContent-zip"></a>
A zip file containing multiple files
Type: [AssetZipContent](API_AssetZipContent.md) object
Required: No

## See Also
<a name="API_AssetContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AssetContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AssetContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AssetContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
