---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_TimePeriod.html
---

# TimePeriod
<a name="API_TimePeriod"></a>

Sets the start date and end date for retrieving a cost estimate. The start date is inclusive, but the end date is exclusive. For example, if `start` is `2017-01-01` and `end` is `2017-05-01`, then the cost and usage data is retrieved from `2017-01-01` up to and including `2017-04-30` but not including `2017-05-01`.

## Contents
<a name="API_TimePeriod_Contents"></a>

 ** end **   <a name="Lightsail-Type-TimePeriod-end"></a>
The end of the time period. The end date is exclusive. For example, if `end` is `2017-05-01`, Lightsail for Research retrieves cost and usage data from the start date up to, but not including, `2017-05-01`.
Type: Timestamp
Required: No

 ** start **   <a name="Lightsail-Type-TimePeriod-start"></a>
The beginning of the time period. The start date is inclusive. For example, if `start` is `2017-01-01`, Lightsail for Research retrieves cost and usage data starting at `2017-01-01` up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.
Type: Timestamp
Required: No

## See Also
<a name="API_TimePeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/TimePeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/TimePeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/TimePeriod)
