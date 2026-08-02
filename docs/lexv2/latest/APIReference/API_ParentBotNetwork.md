---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ParentBotNetwork.html
---

# ParentBotNetwork
<a name="API_ParentBotNetwork"></a>

A network of bots.

## Contents
<a name="API_ParentBotNetwork_Contents"></a>

 ** botId **   <a name="lexv2-Type-ParentBotNetwork-botId"></a>
The identifier of the network of bots assigned by Amazon Lex.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** botVersion **   <a name="lexv2-Type-ParentBotNetwork-botVersion"></a>
The version of the network of bots.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

## See Also
<a name="API_ParentBotNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ParentBotNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ParentBotNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ParentBotNetwork)
