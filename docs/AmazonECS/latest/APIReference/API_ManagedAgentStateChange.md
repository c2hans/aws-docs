---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedAgentStateChange.html
---

# ManagedAgentStateChange
<a name="API_ManagedAgentStateChange"></a>

An object representing a change in state for a managed agent.

## Contents
<a name="API_ManagedAgentStateChange_Contents"></a>

 ** containerName **   <a name="ECS-Type-ManagedAgentStateChange-containerName"></a>
The name of the container that's associated with the managed agent.
Type: String
Required: Yes

 ** managedAgentName **   <a name="ECS-Type-ManagedAgentStateChange-managedAgentName"></a>
The name of the managed agent.
Type: String
Valid Values: `ExecuteCommandAgent`
Required: Yes

 ** status **   <a name="ECS-Type-ManagedAgentStateChange-status"></a>
The status of the managed agent.
Type: String
Required: Yes

 ** reason **   <a name="ECS-Type-ManagedAgentStateChange-reason"></a>
The reason for the status of the managed agent.
Type: String
Required: No

## See Also
<a name="API_ManagedAgentStateChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedAgentStateChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedAgentStateChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedAgentStateChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
