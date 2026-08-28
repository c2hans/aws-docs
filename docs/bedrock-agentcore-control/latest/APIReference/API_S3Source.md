---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_S3Source.html
---

# S3Source
<a name="API_S3Source"></a>

 Amazon S3 location of a JSONL file containing dataset examples.

## Contents
<a name="API_S3Source_Contents"></a>

 ** s3Uri **   <a name="bedrockagentcorecontrol-Type-S3Source-s3Uri"></a>
 Amazon S3 URI of the JSONL file (for example, `s3://my-bucket/path/to/examples.jsonl`).
Type: String
Pattern: `s3://[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]/.{1,1024}`
Required: Yes

## See Also
<a name="API_S3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/S3Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/S3Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/S3Source)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
