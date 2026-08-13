---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricFilterNumberCondition.html
---

# MetricFilterNumberCondition
<a name="API_MetricFilterNumberCondition"></a>

A numeric comparison condition for metric filters.

## Contents
<a name="API_MetricFilterNumberCondition_Contents"></a>

 ** Comparison **   <a name="connect-Type-MetricFilterNumberCondition-Comparison"></a>
The comparison operator. Valid values: `LESSER` (less than) \| `LESSER_OR_EQUAL` (less than or equal to) \| `GREATER` (greater than) \| `GREATER_OR_EQUAL` (greater than or equal to).
Type: String
Valid Values: `LESSER | LESSER_OR_EQUAL | GREATER | GREATER_OR_EQUAL`
Required: Yes

 ** Values **   <a name="connect-Type-MetricFilterNumberCondition-Values"></a>
The numeric values to compare against.
Type: Array of doubles
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_MetricFilterNumberCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricFilterNumberCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricFilterNumberCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricFilterNumberCondition)
