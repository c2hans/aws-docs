---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DataSourceConfiguration.html
---

# DataSourceConfiguration
<a name="API_DataSourceConfiguration"></a>

Contains details about the configuration of the knowledge store used for the `AMAZON.QnAIntent`. You must have already created the knowledge store and indexed the documents within it.

## Contents
<a name="API_DataSourceConfiguration_Contents"></a>

 ** bedrockKnowledgeStoreConfiguration **   <a name="lexv2-Type-DataSourceConfiguration-bedrockKnowledgeStoreConfiguration"></a>
Contains details about the configuration of the Amazon Bedrock knowledge base used for the `AMAZON.QnAIntent`. To set up a knowledge base, follow the steps at [Building a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html).
Type: [BedrockKnowledgeStoreConfiguration](API_BedrockKnowledgeStoreConfiguration.md) object
Required: No

 ** kendraConfiguration **   <a name="lexv2-Type-DataSourceConfiguration-kendraConfiguration"></a>
Contains details about the configuration of the Amazon Kendra index used for the `AMAZON.QnAIntent`. To create a Amazon Kendra index, follow the steps at [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html).
Type: [QnAKendraConfiguration](API_QnAKendraConfiguration.md) object
Required: No

 ** opensearchConfiguration **   <a name="lexv2-Type-DataSourceConfiguration-opensearchConfiguration"></a>
Contains details about the configuration of the Amazon OpenSearch Service database used for the `AMAZON.QnAIntent`. To create a domain, follow the steps at [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).
Type: [OpensearchConfiguration](API_OpensearchConfiguration.md) object
Required: No

## See Also
<a name="API_DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DataSourceConfiguration)
