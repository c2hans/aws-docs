---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DevOpsAgentConfiguration.html
---

# DevOpsAgentConfiguration
<a name="API_DevOpsAgentConfiguration"></a>

The AWS DevOps Agent (DevOps Agent) integration configuration that you supply when creating or updating a service. Connecting a service to a DevOps Agent Agent Space lets DevOps Agent investigate the service's resilience test runs and attach its analysis to the results. Include this block with an Agent Space Amazon Resource Name (ARN) to connect or reconnect the service to an Agent Space. Include it without an Agent Space ARN to disconnect the service. Omit it to leave the existing linkage unchanged.

## Contents
<a name="API_DevOpsAgentConfiguration_Contents"></a>

 ** agentSpaceArn **   <a name="ngresiliencehub-Type-DevOpsAgentConfiguration-agentSpaceArn"></a>
The ARN of the DevOps Agent Agent Space to link to this service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:aidevops:[a-z0-9-]+:[0-9]{12}:agentspace/[a-zA-Z0-9-]{1,64}`
Required: No

## See Also
<a name="API_DevOpsAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DevOpsAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DevOpsAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DevOpsAgentConfiguration)
