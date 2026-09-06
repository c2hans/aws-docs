---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_EstimatedCarbonEmissions.html
---

# EstimatedCarbonEmissions
<a name="API_EstimatedCarbonEmissions"></a>

Contains estimated carbon emissions data for a specific time period and dimension grouping.

## Contents
<a name="API_EstimatedCarbonEmissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DimensionsValues **   <a name="sustainability-Type-EstimatedCarbonEmissions-DimensionsValues"></a>
The dimensions used to group emissions values.
Type: String to string map
Valid Keys: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** EmissionsValues **   <a name="sustainability-Type-EstimatedCarbonEmissions-EmissionsValues"></a>
The emissions values for the requested emissions types.
Type: String to [Emissions](API_Emissions.md) object map
Valid Keys: `TOTAL_LBM_CARBON_EMISSIONS | TOTAL_MBM_CARBON_EMISSIONS | TOTAL_SCOPE_1_CARBON_EMISSIONS | TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS | TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS | TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS | TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS`
Required: Yes

 ** ModelVersion **   <a name="sustainability-Type-EstimatedCarbonEmissions-ModelVersion"></a>
The semantic version-formatted string that indicates the methodology version used to calculate the emission values.
 The AWS Sustainability service reflects the most recent model version for every month. You will not see two entries for the same month with different `ModelVersion` values. To track the evolution of the methodology and compare emission values from previous versions, we recommend creating a [Data Export](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html).
Type: String
Pattern: `v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?`
Required: Yes

 ** TimePeriod **   <a name="sustainability-Type-EstimatedCarbonEmissions-TimePeriod"></a>
The reporting period for emission values.
Type: [TimePeriod](API_TimePeriod.md) object
Required: Yes

## See Also
<a name="API_EstimatedCarbonEmissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/EstimatedCarbonEmissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/EstimatedCarbonEmissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/EstimatedCarbonEmissions)
