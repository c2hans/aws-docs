---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ConditionBasedCollectionScheme.html
---

# ConditionBasedCollectionScheme
<a name="API_ConditionBasedCollectionScheme"></a>

Information about a collection scheme that uses a simple logical expression to recognize what data to collect.

## Contents
<a name="API_ConditionBasedCollectionScheme_Contents"></a>

 ** expression **   <a name="iotfleetwise-Type-ConditionBasedCollectionScheme-expression"></a>
The logical expression used to recognize what data to collect. For example, `$variable.`Vehicle.OutsideAirTemperature` >= 105.0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** conditionLanguageVersion **   <a name="iotfleetwise-Type-ConditionBasedCollectionScheme-conditionLanguageVersion"></a>
Specifies the version of the conditional expression language.
Type: Integer
Valid Range: Fixed value of 1.
Required: No

 ** minimumTriggerIntervalMs **   <a name="iotfleetwise-Type-ConditionBasedCollectionScheme-minimumTriggerIntervalMs"></a>
The minimum duration of time between two triggering events to collect data, in milliseconds.
If a signal changes often, you might want to collect data at a slower rate.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** triggerMode **   <a name="iotfleetwise-Type-ConditionBasedCollectionScheme-triggerMode"></a>
Whether to collect data for all triggering events (`ALWAYS`). Specify (`RISING_EDGE`), or specify only when the condition first evaluates to false. For example, triggering on "AirbagDeployed"; Users aren't interested on triggering when the airbag is already exploded; they only care about the change from not deployed => deployed.
Type: String
Valid Values: `ALWAYS | RISING_EDGE`
Required: No

## See Also
<a name="API_ConditionBasedCollectionScheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ConditionBasedCollectionScheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ConditionBasedCollectionScheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ConditionBasedCollectionScheme)
