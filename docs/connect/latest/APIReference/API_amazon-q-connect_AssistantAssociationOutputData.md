---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_AssistantAssociationOutputData.html
---

# AssistantAssociationOutputData
<a name="API_amazon-q-connect_AssistantAssociationOutputData"></a>

The data that is output as a result of the assistant association.

## Contents
<a name="API_amazon-q-connect_AssistantAssociationOutputData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** externalBedrockKnowledgeBaseConfig **   <a name="connect-Type-amazon-q-connect_AssistantAssociationOutputData-externalBedrockKnowledgeBaseConfig"></a>
The configuration for an external Bedrock knowledge base association in the output data.
Type: [ExternalBedrockKnowledgeBaseConfig](API_amazon-q-connect_ExternalBedrockKnowledgeBaseConfig.md) object
Required: No

 ** knowledgeBaseAssociation **   <a name="connect-Type-amazon-q-connect_AssistantAssociationOutputData-knowledgeBaseAssociation"></a>
The knowledge base where output data is sent.
Type: [KnowledgeBaseAssociationData](API_amazon-q-connect_KnowledgeBaseAssociationData.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_AssistantAssociationOutputData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AssistantAssociationOutputData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AssistantAssociationOutputData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AssistantAssociationOutputData)
