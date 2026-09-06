---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ExternalBedrockKnowledgeBaseConfig.html
---

# ExternalBedrockKnowledgeBaseConfig
<a name="API_amazon-q-connect_ExternalBedrockKnowledgeBaseConfig"></a>

Configuration for an external Bedrock knowledge base.

## Contents
<a name="API_amazon-q-connect_ExternalBedrockKnowledgeBaseConfig_Contents"></a>

 ** accessRoleArn **   <a name="connect-Type-amazon-q-connect_ExternalBedrockKnowledgeBaseConfig-accessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used to access the external Bedrock knowledge base.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/(?:service-role/)?[a-zA-Z0-9_+=,.@-]{1,64}`
Required: Yes

 ** bedrockKnowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_ExternalBedrockKnowledgeBaseConfig-bedrockKnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the external Bedrock knowledge base.
Type: String
Length Constraints: Minimum length of 47. Maximum length of 128.
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_amazon-q-connect_ExternalBedrockKnowledgeBaseConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ExternalBedrockKnowledgeBaseConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ExternalBedrockKnowledgeBaseConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ExternalBedrockKnowledgeBaseConfig)
