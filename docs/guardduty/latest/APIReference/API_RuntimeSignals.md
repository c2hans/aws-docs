---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RuntimeSignals.html
---

# RuntimeSignals
<a name="API_RuntimeSignals"></a>

Contains a summary of runtime signals.

## Contents
<a name="API_RuntimeSignals_Contents"></a>

 ** keyObservation **   <a name="guardduty-Type-RuntimeSignals-keyObservation"></a>
A key observation about the runtime signals.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** signalGroups **   <a name="guardduty-Type-RuntimeSignals-signalGroups"></a>
The runtime signals, grouped by finding type.
Type: Array of [SignalGroup](API_SignalGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_RuntimeSignals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RuntimeSignals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RuntimeSignals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RuntimeSignals)
