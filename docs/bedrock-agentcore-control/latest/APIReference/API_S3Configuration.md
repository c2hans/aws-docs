---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

The Amazon S3 configuration for a gateway. This structure defines how the gateway accesses files in Amazon S3.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** bucketOwnerAccountId **   <a name="bedrockagentcorecontrol-Type-S3Configuration-bucketOwnerAccountId"></a>
The account ID of the Amazon S3 bucket owner. This ID is used for cross-account access to the bucket.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** uri **   <a name="bedrockagentcorecontrol-Type-S3Configuration-uri"></a>
The URI of the Amazon S3 object. This URI specifies the location of the object in Amazon S3.
Type: String
Pattern: `s3://.{1,2043}`
Required: No

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/S3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
