---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsPathFilter.html
---

# AnalyticsPathFilter
<a name="API_AnalyticsPathFilter"></a>

Contains fields describing a condition by which to filter the paths. The expression may be understood as `name` `operator` `values`. For example:
+  `LocaleId EQ en` – The locale is "en".
+  `BotVersion EQ 2` – The bot version is equal to two.

The operators that each filter supports are listed below:
+  `BotAlias` – `EQ`.
+  `BotVersion` – `EQ`.
+  `LocaleId` – `EQ`.
+  `Modality` – `EQ`.
+  `Channel` – `EQ`.

## Contents
<a name="API_AnalyticsPathFilter_Contents"></a>

 ** name **   <a name="lexv2-Type-AnalyticsPathFilter-name"></a>
The category by which to filter the intent paths. The descriptions for each option are as follows:
+  `BotAlias` – The name of the bot alias.
+  `BotVersion` – The version of the bot.
+  `LocaleId` – The locale of the bot.
+  `Modality` – The modality of the session with the bot (audio, DTMF, or text).
+  `Channel` – The channel that the bot is integrated with.
Type: String
Valid Values: `BotAliasId | BotVersion | LocaleId | Modality | Channel`
Required: Yes

 ** operator **   <a name="lexv2-Type-AnalyticsPathFilter-operator"></a>
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
Type: String
Valid Values: `EQ | GT | LT`
Required: Yes

 ** values **   <a name="lexv2-Type-AnalyticsPathFilter-values"></a>
An array containing the values of the category by which to apply the operator to filter the results. You can provide multiple values if the operator is `EQ` or `CO`. If you provide multiple values, you filter for results that equal/contain any of the values. For example, if the `name`, `operator`, and `values` fields are `Modality`, `EQ`, and `[Speech, Text]`, the operation filters for results where the modality was either `Speech` or `Text`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_AnalyticsPathFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsPathFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsPathFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsPathFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
