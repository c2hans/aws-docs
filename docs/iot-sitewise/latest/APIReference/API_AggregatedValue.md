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
