---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DatasetVersionSummary.html
---

# DatasetVersionSummary
<a name="API_DatasetVersionSummary"></a>

 Summary information about a published dataset version.

## Contents
<a name="API_DatasetVersionSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-DatasetVersionSummary-createdAt"></a>
 The timestamp when this version was published.
Type: Timestamp
Required: Yes

 ** datasetVersion **   <a name="bedrockagentcorecontrol-Type-DatasetVersionSummary-datasetVersion"></a>
 The version number of this published snapshot.
Type: String
Pattern: `(DRAFT|[0-9]+)`
Required: Yes

 ** exampleCount **   <a name="bedrockagentcorecontrol-Type-DatasetVersionSummary-exampleCount"></a>
 The number of examples in this version.
Type: Long
Required: Yes

## See Also
<a name="API_DatasetVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DatasetVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DatasetVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DatasetVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
