---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionFilter.html
---

# AnalyticsSessionFilter
<a name="API_AnalyticsSessionFilter"></a>

Contains fields describing a condition by which to filter the sessions. The expression may be understood as `name` `operator` `values`. For example:
+  `LocaleId EQ en` – The locale is "en".
+  `Duration GT 200` – The duration is greater than 200 seconds.

The operators that each filter supports are listed below:
+  `BotAlias` – `EQ`.
+  `BotVersion` – `EQ`.
+  `LocaleId` – `EQ`.
+  `Modality` – `EQ`.
+  `Channel` – `EQ`.
+  `Duration` – `EQ`, `GT`, `LT`.
+  `conversationEndState` – `EQ`, `CO`.
+  `SessionId` – `EQ`.
+  `OriginatingRequestId` – `EQ`.
+  `IntentPath` – `EQ`.

## Contents
<a name="API_AnalyticsSessionFilter_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsSessionFilter-name"></a>
The category by which to filter the sessions. The descriptions for each option are as follows:
+  `BotAlias` – The name of the bot alias.
+  `BotVersion` – The version of the bot.
+  `LocaleId` – The locale of the bot.
+  `Modality` – The modality of the session with the bot (audio, DTMF, or text).
+  `Channel` – The channel that the bot is integrated with.
+  `Duration` – The duration of the session.
+  `conversationEndState` – The final state of the session.
+  `SessionId` – The identifier of the session with the bot.
+  `OriginatingRequestId` – The identifier of the first request in a session.
+  `IntentPath` – The order of intents taken in a session.
Type: String
Valid Values: `BotAliasId | BotVersion | LocaleId | Modality | Channel | Duration | ConversationEndState | SessionId | OriginatingRequestId | IntentPath`
Required: Yes

 ** operator **   <a name="lexv2-Type-AnalyticsSessionFilter-operator"></a>
The operation by which to filter the category. The following operations are possible:
+  `CO` – Contains
+  `EQ` – Equals
+  `GT` – Greater than
+  `LT` – Less than
The operators that each filter supports are listed below:
+  `BotAlias` – `EQ`.
+  `BotVersion` – `EQ`.
+  `LocaleId` – `EQ`.
+  `Modality` – `EQ`.
+  `Channel` – `EQ`.
+  `Duration` – `EQ`, `GT`, `LT`.
+  `conversationEndState` – `EQ`, `CO`.
+  `SessionId` – `EQ`.
+  `OriginatingRequestId` – `EQ`.
+  `IntentPath` – `EQ`.
Type: String
Valid Values: `EQ | GT | LT`
Required: Yes

 ** values **   <a name="lexv2-Type-AnalyticsSessionFilter-values"></a>
An array containing the values of the category by which to apply the operator to filter the results. You can provide multiple values if the operator is `EQ` or `CO`. If you provide multiple values, you filter for results that equal/contain any of the values. For example, if the `name`, `operator`, and `values` fields are `Modality`, `EQ`, and `[Speech, Text]`, the operation filters for results where the modality was either `Speech` or `Text`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_AnalyticsSessionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsSessionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsSessionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsSessionFilter)
