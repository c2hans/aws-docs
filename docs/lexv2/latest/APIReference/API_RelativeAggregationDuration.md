---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_RelativeAggregationDuration.html
---

# RelativeAggregationDuration
<a name="API_RelativeAggregationDuration"></a>

Specifies the time window that utterance statistics are returned for. The time window is always relative to the last time that the that utterances were aggregated. For example, if the `ListAggregatedUtterances` operation is called at 1600, the time window is set to 1 hour, and the last refresh time was 1530, only utterances made between 1430 and 1530 are returned.

You can choose the time window that statistics should be returned for.
+  **Hours** - You can request utterance statistics for 1, 3, 6, 12, or 24 hour time windows. Statistics are refreshed every half hour for 1 hour time windows, and hourly for the other time windows.
+  **Days** - You can request utterance statistics for 3 days. Statistics are refreshed every 6 hours.
+  **Weeks** - You can see statistics for one or two weeks. Statistics are refreshed every 12 hours for one week time windows, and once per day for two week time windows.

## Contents
<a name="API_RelativeAggregationDuration_Contents"></a>

 ** timeDimension **   <a name="lexv2-Type-RelativeAggregationDuration-timeDimension"></a>
The type of time period that the `timeValue` field represents.
Type: String
Valid Values: `Hours | Days | Weeks`
Required: Yes

 ** timeValue **   <a name="lexv2-Type-RelativeAggregationDuration-timeValue"></a>
The period of the time window to gather statistics for. The valid value depends on the setting of the `timeDimension` field.
+  `Hours` - 1/3/6/12/24
+  `Days` - 3
+  `Weeks` - 1/2
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: Yes

## See Also
<a name="API_RelativeAggregationDuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/RelativeAggregationDuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/RelativeAggregationDuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/RelativeAggregationDuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
