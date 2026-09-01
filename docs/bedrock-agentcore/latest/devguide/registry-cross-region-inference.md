---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-cross-region-inference.html
---

# Cross-region inference in AWS Agent Registry
<a name="registry-cross-region-inference"></a>

As part of enabling semantic search, AWS Agent Registry automatically selects the optimal Region to process the embedding model inference request, maximizing available compute resources and model availability.

For AWS Agent Registry, inference requests might be securely routed to available compute resources across all commercial AWS Regions. Although your data remains stored only in the primary Region, input prompts and output results might be processed in any commercial AWS Region. All data is transmitted encrypted across the secure Amazon network.

If you have data residency or compliance requirements, assess whether cross-region inference fits your compliance framework, because requests might be processed in any commercial AWS Region.

**Note**
There is no additional cost for using cross-region inference. Amazon CloudWatch and AWS CloudTrail logs won’t specify the AWS Region in which inference occurs.

## Supported Regions
<a name="registry-cross-region-inference-supported-regions"></a>

The following Regions support AWS Agent Registry with cross-region inference:

 **United States**
+ US East - N. Virginia (us-east-1)
+ US West - Oregon (us-west-2)

 **Europe**
+ Europe - Ireland (eu-west-1)

 **Asia Pacific**
+ Asia Pacific - Tokyo (ap-northeast-1)
+ Asia Pacific - Sydney (ap-southeast-2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
