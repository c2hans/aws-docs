---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Association.html
---

# Association
<a name="API_Association"></a>

Represents a service association within an AgentSpace, defining how the agent interacts with external services.

## Contents
<a name="API_Association_Contents"></a>

 ** agentSpaceId **   <a name="devopsagent-Type-Association-agentSpaceId"></a>
The unique identifier of the AgentSpace
Type: String
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

 ** associationId **   <a name="devopsagent-Type-Association-associationId"></a>
The unique identifier of the given association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** configuration **   <a name="devopsagent-Type-Association-configuration"></a>
The configuration that directs how AgentSpace interacts with the given service.
Type: [ServiceConfiguration](API_ServiceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Association-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** serviceId **   <a name="devopsagent-Type-Association-serviceId"></a>
The identifier for associated service
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Association-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp
Required: Yes

 ** capabilities **   <a name="devopsagent-Type-Association-capabilities"></a>
Enabled capabilities for this association.
Type: String to [CapabilityConfiguration](API_CapabilityConfiguration.md) object map
Valid Keys: `RELEASE_READINESS_REVIEW | RELEASE_READINESS_REVIEW_AUTOMATED_TESTING`
Required: No

 ** status **   <a name="devopsagent-Type-Association-status"></a>
Validation status
Type: String
Valid Values: `valid | invalid | pending-confirmation`
Required: No

## See Also
<a name="API_Association_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Association)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Association)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Association)
