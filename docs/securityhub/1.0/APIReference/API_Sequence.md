---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Sequence.html
---

# Sequence
<a name="API_Sequence"></a>

 Contains information about an Amazon GuardDuty Extended Threat Detection attack sequence finding. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_Sequence_Contents"></a>

 ** Actors **   <a name="securityhub-Type-Sequence-Actors"></a>
 Provides information about the actors involved in the attack sequence.
Type: Array of [Actor](API_Actor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Endpoints **   <a name="securityhub-Type-Sequence-Endpoints"></a>
 Contains information about the network endpoints that were used in the attack sequence.
Type: Array of [NetworkEndpoint](API_NetworkEndpoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** SequenceIndicators **   <a name="securityhub-Type-Sequence-SequenceIndicators"></a>
 Contains information about the indicators observed in the attack sequence. The values for [SignalIndicators](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Signal.html) are a subset of the values for `SequenceIndicators`, but the values for these fields don't always match 1:1.
Type: Array of [Indicator](API_Indicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Signals **   <a name="securityhub-Type-Sequence-Signals"></a>
 Contains information about the signals involved in the attack sequence.
Type: Array of [Signal](API_Signal.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Uid **   <a name="securityhub-Type-Sequence-Uid"></a>
 Unique identifier of the attack sequence.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Sequence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Sequence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Sequence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Sequence)
