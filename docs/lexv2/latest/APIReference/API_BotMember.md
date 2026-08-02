---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotMember.html
---

# BotMember
<a name="API_BotMember"></a>

A bot that is a member of a network of bots.

## Contents
<a name="API_BotMember_Contents"></a>

 ** botMemberAliasId **   <a name="lexv2-Type-BotMember-botMemberAliasId"></a>
The alias ID of a bot that is a member of this network of bots.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: Yes

 ** botMemberAliasName **   <a name="lexv2-Type-BotMember-botMemberAliasName"></a>
The alias name of a bot that is a member of this network of bots.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\bAmazonLexTestAlias\b|[0-9a-zA-Z][_-]?)+$`
Required: Yes

 ** botMemberId **   <a name="lexv2-Type-BotMember-botMemberId"></a>
The unique ID of a bot that is a member of this network of bots.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** botMemberName **   <a name="lexv2-Type-BotMember-botMemberName"></a>
The unique name of a bot that is a member of this network of bots.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** botMemberVersion **   <a name="lexv2-Type-BotMember-botMemberVersion"></a>
The version of a bot that is a member of this network of bots.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

## See Also
<a name="API_BotMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotMember)
