---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AssistantAssociationInputData.html
---

# AssistantAssociationInputData
<a name="API_amazon-q-connect_AssistantAssociationInputData"></a>

The data that is input into Amazon Q in Connect as a result of the assistant association.

## Contents
<a name="API_amazon-q-connect_AssistantAssociationInputData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** externalBedrockKnowledgeBaseConfig **   <a name="connect-Type-amazon-q-connect_AssistantAssociationInputData-externalBedrockKnowledgeBaseConfig"></a>
The configuration for an external Bedrock knowledge base association.
Type: [ExternalBedrockKnowledgeBaseConfig](API_amazon-q-connect_ExternalBedrockKnowledgeBaseConfig.md) object
Required: No

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_AssistantAssociationInputData-knowledgeBaseId"></a>
The identifier of the knowledge base. This should not be a QUICK\_RESPONSES type knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_amazon-q-connect_AssistantAssociationInputData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AssistantAssociationInputData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AssistantAssociationInputData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AssistantAssociationInputData)
