---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AgentCoreRuntimeSourceDetails.html
---

# AgentCoreRuntimeSourceDetails
<a name="API_AgentCoreRuntimeSourceDetails"></a>

The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Runtime resource.

## Contents
<a name="API_AgentCoreRuntimeSourceDetails_Contents"></a>

 ** authorizerConfiguration **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeSourceDetails-authorizerConfiguration"></a>
The authorizer configuration for a registry. Exactly one member is set.
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** protocolConfiguration **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeSourceDetails-protocolConfiguration"></a>
The protocol configuration of the AgentCore Runtime resource that the registry record was detected from.
Type: [AgentCoreRuntimeProtocolConfiguration](API_AgentCoreRuntimeProtocolConfiguration.md) object
Required: No

 ** workloadIdentityDetails **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeSourceDetails-workloadIdentityDetails"></a>
The workload identity details for the AgentCore Runtime resource. Present when the runtime has a workload identity configured.
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object
Required: No

## See Also
<a name="API_AgentCoreRuntimeSourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentCoreRuntimeSourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentCoreRuntimeSourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentCoreRuntimeSourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
