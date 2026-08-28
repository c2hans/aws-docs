---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AggregatedValue.html
---

# AggregatedValue
<a name="API_AggregatedValue"></a>

Contains aggregated asset property values (for example, average, minimum, and maximum).

## Contents
<a name="API_AggregatedValue_Contents"></a>

 ** timestamp **   <a name="iotsitewise-Type-AggregatedValue-timestamp"></a>
The date the aggregating computations occurred, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** value **   <a name="iotsitewise-Type-AggregatedValue-value"></a>
The value of the aggregates.
Type: [Aggregates](API_Aggregates.md) object
Required: Yes

 ** quality **   <a name="iotsitewise-Type-AggregatedValue-quality"></a>
The quality of the aggregated data.
Type: String
Valid Values: `GOOD | BAD | UNCERTAIN`
Required: No

## See Also
<a name="API_AggregatedValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AggregatedValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AggregatedValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AggregatedValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
