---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TemplatedMessageConfig.html
---

# TemplatedMessageConfig
<a name="API_TemplatedMessageConfig"></a>

Information about template message configuration.

## Contents
<a name="API_TemplatedMessageConfig_Contents"></a>

 ** KnowledgeBaseId **   <a name="connect-Type-TemplatedMessageConfig-KnowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** MessageTemplateId **   <a name="connect-Type-TemplatedMessageConfig-MessageTemplateId"></a>
The identifier of the message template Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** TemplateAttributes **   <a name="connect-Type-TemplatedMessageConfig-TemplateAttributes"></a>
Information about template attributes, that is, CustomAttributes or CustomerProfileAttributes.
Type: [TemplateAttributes](API_TemplateAttributes.md) object
Required: Yes

## See Also
<a name="API_TemplatedMessageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TemplatedMessageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TemplatedMessageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TemplatedMessageConfig)
