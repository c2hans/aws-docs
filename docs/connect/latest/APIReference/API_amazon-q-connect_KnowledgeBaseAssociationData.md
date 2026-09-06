---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_KnowledgeBaseAssociationData.html
---

# KnowledgeBaseAssociationData
<a name="API_amazon-q-connect_KnowledgeBaseAssociationData"></a>

Association information about the knowledge base.

## Contents
<a name="API_amazon-q-connect_KnowledgeBaseAssociationData_Contents"></a>

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseAssociationData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: No

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseAssociationData-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_amazon-q-connect_KnowledgeBaseAssociationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/KnowledgeBaseAssociationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/KnowledgeBaseAssociationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/KnowledgeBaseAssociationData)
