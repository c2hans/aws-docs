---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_EventTriggerLimits.html
---

# EventTriggerLimits
<a name="API_connect-customer-profiles_EventTriggerLimits"></a>

Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.

## Contents
<a name="API_connect-customer-profiles_EventTriggerLimits_Contents"></a>

 ** EventExpiration **   <a name="connect-Type-connect-customer-profiles_EventTriggerLimits-EventExpiration"></a>
In milliseconds. Specifies that an event will only trigger the destination if it is processed within a certain latency period.
Type: Long
Required: No

 ** Periods **   <a name="connect-Type-connect-customer-profiles_EventTriggerLimits-Periods"></a>
A list of time periods during which the limits apply.
Type: Array of [Period](API_connect-customer-profiles_Period.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

## See Also
<a name="API_connect-customer-profiles_EventTriggerLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/EventTriggerLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/EventTriggerLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/EventTriggerLimits)
