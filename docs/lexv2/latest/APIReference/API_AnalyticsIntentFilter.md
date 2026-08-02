---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentFilter.html
---

# AnalyticsIntentFilter
<a name="API_AnalyticsIntentFilter"></a>

Contains fields describing a condition by which to filter the intents. The expression may be understood as `name` `operator` `values`. For example:
+  `IntentName CO Book` – The intent name contains the string "Book."
+  `BotVersion EQ 2` – The bot version is equal to two.

The operators that each filter supports are listed below:
+  `BotAlias` – `EQ`.
+  `BotVersion` – `EQ`.
+  `LocaleId` – `EQ`.
+  `Modality` – `EQ`.
+  `Channel` – `EQ`.
+  `SessionId` – `EQ`.
+  `OriginatingRequestId` – `EQ`.
+  `IntentName` – `EQ`, `CO`.
+  `IntentEndState` – `EQ`, `CO`.

## Contents
<a name="API_AnalyticsIntentFilter_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsIntentFilter-name"></a>
The category by which to filter the intents. The descriptions for each option are as follows:
+  `BotAlias` – The name of the bot alias.
+  `BotVersion` – The version of the bot.
+  `LocaleId` – The locale of the bot.
+  `Modality` – The modality of the session with the bot (audio, DTMF, or text).
+  `Channel` – The channel that the bot is integrated with.
+  `SessionId` – The identifier of the session with the bot.
+  `OriginatingRequestId` – The identifier of the first request in a session.
+  `IntentName` – The name of the intent.
+  `IntentEndState` – The final state of the intent.
Type: String
Valid Values: `BotAliasId | BotVersion | LocaleId | Modality | Channel | SessionId | OriginatingRequestId | IntentName | IntentEndState`
Required: Yes

 ** operator **   <a name="lexv2-Type-AnalyticsIntentFilter-operator"></a>
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
+  `SessionId` – `EQ`.
+  `OriginatingRequestId` – `EQ`.
+  `IntentName` – `EQ`, `CO`.
+  `IntentEndState` – `EQ`, `CO`.
Type: String
Valid Values: `EQ | GT | LT`
Required: Yes

 ** values **   <a name="lexv2-Type-AnalyticsIntentFilter-values"></a>
An array containing the values of the category by which to apply the operator to filter the results. You can provide multiple values if the operator is `EQ` or `CO`. If you provide multiple values, you filter for results that equal/contain any of the values. For example, if the `name`, `operator`, and `values` fields are `Modality`, `EQ`, and `[Speech, Text]`, the operation filters for results where the modality was either `Speech` or `Text`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_AnalyticsIntentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsIntentFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsIntentFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsIntentFilter)
