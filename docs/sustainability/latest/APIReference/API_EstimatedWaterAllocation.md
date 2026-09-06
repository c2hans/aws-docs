---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_EstimatedWaterAllocation.html
---

# EstimatedWaterAllocation
<a name="API_EstimatedWaterAllocation"></a>

Contains estimated water allocation data for a specific time period and dimension grouping.

## Contents
<a name="API_EstimatedWaterAllocation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllocationValues **   <a name="sustainability-Type-EstimatedWaterAllocation-AllocationValues"></a>
The allocation values for the requested water allocation types.
Type: String to [WaterAllocation](API_WaterAllocation.md) object map
Valid Keys: `TOTAL_WATER_WITHDRAWALS`
Required: Yes

 ** DimensionsValues **   <a name="sustainability-Type-EstimatedWaterAllocation-DimensionsValues"></a>
The dimensions used to group water allocation values.
Type: String to string map
Valid Keys: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** ModelVersion **   <a name="sustainability-Type-EstimatedWaterAllocation-ModelVersion"></a>
The semantic version-formatted string that indicates the methodology version used to calculate the water allocation values.
 The AWS Sustainability service reflects the most recent model version for every month. You will not see two entries for the same month with different `ModelVersion` values.
Type: String
Pattern: `v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?`
Required: Yes

 ** TimePeriod **   <a name="sustainability-Type-EstimatedWaterAllocation-TimePeriod"></a>
The reporting period for water allocation values.
Type: [TimePeriod](API_TimePeriod.md) object
Required: Yes

## See Also
<a name="API_EstimatedWaterAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/EstimatedWaterAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/EstimatedWaterAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/EstimatedWaterAllocation)
