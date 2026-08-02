---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ConditionBasedSignalFetchConfig.html
---

# ConditionBasedSignalFetchConfig
<a name="API_ConditionBasedSignalFetchConfig"></a>

Specifies the condition under which a signal fetch occurs.

## Contents
<a name="API_ConditionBasedSignalFetchConfig_Contents"></a>

 ** conditionExpression **   <a name="iotfleetwise-Type-ConditionBasedSignalFetchConfig-conditionExpression"></a>
The condition that must be satisfied to trigger a signal fetch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: Yes

 ** triggerMode **   <a name="iotfleetwise-Type-ConditionBasedSignalFetchConfig-triggerMode"></a>
Indicates the mode in which the signal fetch is triggered.
Type: String
Valid Values: `ALWAYS | RISING_EDGE`
Required: Yes

## See Also
<a name="API_ConditionBasedSignalFetchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ConditionBasedSignalFetchConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ConditionBasedSignalFetchConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ConditionBasedSignalFetchConfig)
