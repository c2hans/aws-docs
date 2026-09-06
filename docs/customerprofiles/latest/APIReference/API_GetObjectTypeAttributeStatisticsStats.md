---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetObjectTypeAttributeStatisticsStats.html
---

# GetObjectTypeAttributeStatisticsStats
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatisticsStats"></a>

Statistical measurements for object type attributes including basic statistics and percentiles.

## Contents
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatisticsStats_Contents"></a>

 ** Average **   <a name="connect-Type-connect-customer-profiles_GetObjectTypeAttributeStatisticsStats-Average"></a>
The arithmetic mean of the attribute values.
Type: Double
Required: Yes

 ** Maximum **   <a name="connect-Type-connect-customer-profiles_GetObjectTypeAttributeStatisticsStats-Maximum"></a>
The maximum value found in the attribute dataset.
Type: Double
Required: Yes

 ** Minimum **   <a name="connect-Type-connect-customer-profiles_GetObjectTypeAttributeStatisticsStats-Minimum"></a>
The minimum value found in the attribute dataset.
Type: Double
Required: Yes

 ** Percentiles **   <a name="connect-Type-connect-customer-profiles_GetObjectTypeAttributeStatisticsStats-Percentiles"></a>
Percentile distribution statistics for the attribute values.
Type: [GetObjectTypeAttributeStatisticsPercentiles](API_connect-customer-profiles_GetObjectTypeAttributeStatisticsPercentiles.md) object
Required: Yes

 ** StandardDeviation **   <a name="connect-Type-connect-customer-profiles_GetObjectTypeAttributeStatisticsStats-StandardDeviation"></a>
The standard deviation of the attribute values, measuring their spread around the mean.
Type: Double
Required: Yes

## See Also
<a name="API_connect-customer-profiles_GetObjectTypeAttributeStatisticsStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetObjectTypeAttributeStatisticsStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetObjectTypeAttributeStatisticsStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetObjectTypeAttributeStatisticsStats)
