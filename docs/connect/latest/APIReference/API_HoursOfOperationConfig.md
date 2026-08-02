---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HoursOfOperationConfig.html
---

# HoursOfOperationConfig
<a name="API_HoursOfOperationConfig"></a>

Contains information about the hours of operation.

## Contents
<a name="API_HoursOfOperationConfig_Contents"></a>

 ** Day **   <a name="connect-Type-HoursOfOperationConfig-Day"></a>
The day that the hours of operation applies to.
Type: String
Valid Values: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
Required: Yes

 ** EndTime **   <a name="connect-Type-HoursOfOperationConfig-EndTime"></a>
The end time that your contact center closes.
Type: [HoursOfOperationTimeSlice](API_HoursOfOperationTimeSlice.md) object
Required: Yes

 ** StartTime **   <a name="connect-Type-HoursOfOperationConfig-StartTime"></a>
The start time that your contact center opens.
Type: [HoursOfOperationTimeSlice](API_HoursOfOperationTimeSlice.md) object
Required: Yes

## See Also
<a name="API_HoursOfOperationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HoursOfOperationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HoursOfOperationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HoursOfOperationConfig)
