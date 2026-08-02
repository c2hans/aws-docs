---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AgentSpace.html
---

# AgentSpace
<a name="API_AgentSpace"></a>

Represents a complete AgentSpace with all its properties, timestamps, encryption settings, and unique identifier.

## Contents
<a name="API_AgentSpace_Contents"></a>

 ** agentSpaceId **   <a name="devopsagent-Type-AgentSpace-agentSpaceId"></a>
Unique identifier for an agent space (allows alphanumeric characters and hyphens; 1-64 characters)
Type: String
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-AgentSpace-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="devopsagent-Type-AgentSpace-name"></a>
The name of the AgentSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-AgentSpace-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="devopsagent-Type-AgentSpace-description"></a>
The description of the AgentSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

 ** kmsKeyArn **   <a name="devopsagent-Type-AgentSpace-kmsKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.
Type: String
Length Constraints: Minimum length of 20.
Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** locale **   <a name="devopsagent-Type-AgentSpace-locale"></a>
The locale for the AgentSpace, which determines the language used in agent responses.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Pattern: `[a-zA-Z]{2,3}(-[a-zA-Z0-9]{2,8})*`
Required: No

## See Also
<a name="API_AgentSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AgentSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AgentSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AgentSpace)
