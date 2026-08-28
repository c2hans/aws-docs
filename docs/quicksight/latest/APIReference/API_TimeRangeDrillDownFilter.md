---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TimeRangeDrillDownFilter.html
---

# TimeRangeDrillDownFilter
<a name="API_TimeRangeDrillDownFilter"></a>

The time range drill down filter.

## Contents
<a name="API_TimeRangeDrillDownFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Column **   <a name="QS-Type-TimeRangeDrillDownFilter-Column"></a>
The column that the filter is applied to.
Type: [ColumnIdentifier](API_ColumnIdentifier.md) object
Required: Yes

 ** RangeMaximum **   <a name="QS-Type-TimeRangeDrillDownFilter-RangeMaximum"></a>
The maximum value for the filter value range.
Type: Timestamp
Required: Yes

 ** RangeMinimum **   <a name="QS-Type-TimeRangeDrillDownFilter-RangeMinimum"></a>
The minimum value for the filter value range.
Type: Timestamp
Required: Yes

 ** TimeGranularity **   <a name="QS-Type-TimeRangeDrillDownFilter-TimeGranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: Yes

## See Also
<a name="API_TimeRangeDrillDownFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TimeRangeDrillDownFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TimeRangeDrillDownFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TimeRangeDrillDownFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
