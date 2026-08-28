---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_WeightedRoute.html
---

# WeightedRoute
<a name="API_WeightedRoute"></a>

A weighted route that splits traffic between multiple gateway targets.

## Contents
<a name="API_WeightedRoute_Contents"></a>

 ** trafficSplit **   <a name="bedrockagentcorecontrol-Type-WeightedRoute-trafficSplit"></a>
The traffic split entries defining how traffic is distributed between targets.
Type: Array of [TargetTrafficSplitEntry](API_TargetTrafficSplitEntry.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

## See Also
<a name="API_WeightedRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/WeightedRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/WeightedRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/WeightedRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
