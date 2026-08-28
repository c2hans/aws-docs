---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ComputeNode.html
---

# ComputeNode
<a name="API_ComputeNode"></a>

A single compute node in a pipeline DAG. Each compute node references a task and can declare dependencies on other nodes.

## Contents
<a name="API_ComputeNode_Contents"></a>

 ** computeNodeName **   <a name="iotsitewise-Type-ComputeNode-computeNodeName"></a>
The unique name for this compute node within the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** taskName **   <a name="iotsitewise-Type-ComputeNode-taskName"></a>
The name of the task to execute for this compute node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** dependsOn **   <a name="iotsitewise-Type-ComputeNode-dependsOn"></a>
A list of compute node names that must complete successfully before this node can start.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** environmentVariables **   <a name="iotsitewise-Type-ComputeNode-environmentVariables"></a>
Environment variables specific to this compute node. These override pipeline-level environment variables with the same key.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `(?!(?i)AWS_)[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ComputeNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ComputeNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ComputeNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ComputeNode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
