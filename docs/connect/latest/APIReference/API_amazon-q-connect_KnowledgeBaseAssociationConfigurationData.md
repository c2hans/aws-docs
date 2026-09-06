---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_KnowledgeBaseAssociationConfigurationData.html
---

# KnowledgeBaseAssociationConfigurationData
<a name="API_amazon-q-connect_KnowledgeBaseAssociationConfigurationData"></a>

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

## Contents
<a name="API_amazon-q-connect_KnowledgeBaseAssociationConfigurationData_Contents"></a>

 ** contentTagFilter **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseAssociationConfigurationData-contentTagFilter"></a>
An object that can be used to specify Tag conditions.
Type: [TagFilter](API_amazon-q-connect_TagFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maxResults **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseAssociationConfigurationData-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** overrideKnowledgeBaseSearchType **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseAssociationConfigurationData-overrideKnowledgeBaseSearchType"></a>
The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text
Type: String
Valid Values: `HYBRID | SEMANTIC`
Required: No

## See Also
<a name="API_amazon-q-connect_KnowledgeBaseAssociationConfigurationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/KnowledgeBaseAssociationConfigurationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/KnowledgeBaseAssociationConfigurationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/KnowledgeBaseAssociationConfigurationData)
