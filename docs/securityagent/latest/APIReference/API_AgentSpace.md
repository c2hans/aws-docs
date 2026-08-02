---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_AgentSpace.html
---

# AgentSpace
<a name="API_AgentSpace"></a>

Represents an agent space, which is a dedicated workspace for securing a specific application. An agent space contains the configuration, resources, and settings needed for security testing.

## Contents
<a name="API_AgentSpace_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-AgentSpace-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** name **   <a name="securityagent-Type-AgentSpace-name"></a>
The name of the agent space.
Type: String
Required: Yes

 ** awsResources **   <a name="securityagent-Type-AgentSpace-awsResources"></a>
The AWS resources associated with the agent space.
Type: [AWSResources](API_AWSResources.md) object
Required: No

 ** codeReviewSettings **   <a name="securityagent-Type-AgentSpace-codeReviewSettings"></a>
The code review settings for the agent space.
Type: [CodeReviewSettings](API_CodeReviewSettings.md) object
Required: No

 ** createdAt **   <a name="securityagent-Type-AgentSpace-createdAt"></a>
The date and time the agent space was created, in UTC format.
Type: Timestamp
Required: No

 ** description **   <a name="securityagent-Type-AgentSpace-description"></a>
A description of the agent space.
Type: String
Required: No

 ** kmsKeyId **   <a name="securityagent-Type-AgentSpace-kmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt data in the agent space.
Type: String
Required: No

 ** targetDomainIds **   <a name="securityagent-Type-AgentSpace-targetDomainIds"></a>
The list of target domain identifiers associated with the agent space.
Type: Array of strings
Required: No

 ** updatedAt **   <a name="securityagent-Type-AgentSpace-updatedAt"></a>
The date and time the agent space was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_AgentSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/AgentSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/AgentSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/AgentSpace)
