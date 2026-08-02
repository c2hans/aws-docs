---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AssistantData.html
---

# AssistantData
<a name="API_amazon-q-connect_AssistantData"></a>

The assistant data.

## Contents
<a name="API_amazon-q-connect_AssistantData_Contents"></a>

 ** assistantArn **   <a name="connect-Type-amazon-q-connect_AssistantData-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantId **   <a name="connect-Type-amazon-q-connect_AssistantData-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_AssistantData-name"></a>
The name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_AssistantData-status"></a>
The status of the assistant.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_AssistantData-type"></a>
The type of assistant.
Type: String
Valid Values: `AGENT`
Required: Yes

 ** aiAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AssistantData-aiAgentConfiguration"></a>
The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that is set on the Amazon Q in Connect Assistant.
Type: String to [AIAgentConfigurationData](API_amazon-q-connect_AIAgentConfigurationData.md) object map
Valid Keys: `MANUAL_SEARCH | ANSWER_RECOMMENDATION | SELF_SERVICE | EMAIL_RESPONSE | EMAIL_OVERVIEW | EMAIL_GENERATIVE_ANSWER | ORCHESTRATION | NOTE_TAKING | CASE_SUMMARIZATION`
Required: No

 ** capabilityConfiguration **   <a name="connect-Type-amazon-q-connect_AssistantData-capabilityConfiguration"></a>
The configuration information for the Amazon Q in Connect assistant capability.
Type: [AssistantCapabilityConfiguration](API_amazon-q-connect_AssistantCapabilityConfiguration.md) object
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_AssistantData-description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** integrationConfiguration **   <a name="connect-Type-amazon-q-connect_AssistantData-integrationConfiguration"></a>
The configuration information for the Amazon Q in Connect assistant integration.
Type: [AssistantIntegrationConfiguration](API_amazon-q-connect_AssistantIntegrationConfiguration.md) object
Required: No

 ** orchestratorConfigurationList **   <a name="connect-Type-amazon-q-connect_AssistantData-orchestratorConfigurationList"></a>
The list of orchestrator configurations for the assistant.
Type: Array of [OrchestratorConfigurationEntry](API_amazon-q-connect_OrchestratorConfigurationEntry.md) objects
Required: No

 ** serverSideEncryptionConfiguration **   <a name="connect-Type-amazon-q-connect_AssistantData-serverSideEncryptionConfiguration"></a>
The configuration information for the customer managed key used for encryption.
This KMS key must have a policy that allows `kms:CreateGrant`, `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey*` permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow `kms:Decrypt`, `kms:GenerateDataKey*`, and `kms:DescribeKey` permissions to the `connect.amazonaws.com` service principal.
For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html).
Type: [ServerSideEncryptionConfiguration](API_amazon-q-connect_ServerSideEncryptionConfiguration.md) object
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_AssistantData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_AssistantData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AssistantData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AssistantData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AssistantData)
