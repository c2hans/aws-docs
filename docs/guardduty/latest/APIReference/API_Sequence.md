---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Sequence.html
---

# Sequence
<a name="API_Sequence"></a>

Contains information about the GuardDuty attack sequence finding.

## Contents
<a name="API_Sequence_Contents"></a>

 ** description **   <a name="guardduty-Type-Sequence-description"></a>
Description of the attack sequence.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: Yes

 ** signals **   <a name="guardduty-Type-Sequence-signals"></a>
Contains information about the signals involved in the attack sequence.
Type: Array of [Signal](API_Signal.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** uid **   <a name="guardduty-Type-Sequence-uid"></a>
Unique identifier of the attack sequence.
Type: String
Required: Yes

 ** actors **   <a name="guardduty-Type-Sequence-actors"></a>
Contains information about the actors involved in the attack sequence.
Type: Array of [Actor](API_Actor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

 ** additionalSequenceTypes **   <a name="guardduty-Type-Sequence-additionalSequenceTypes"></a>
Additional types of sequences that may be associated with the attack sequence finding, providing further context about the nature of the detected threat.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** endpoints **   <a name="guardduty-Type-Sequence-endpoints"></a>
Contains information about the network endpoints that were used in the attack sequence.
Type: Array of [NetworkEndpoint](API_NetworkEndpoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

 ** resources **   <a name="guardduty-Type-Sequence-resources"></a>
Contains information about the resources involved in the attack sequence.
Type: Array of [ResourceV2](API_ResourceV2.md) objects
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

 ** sequenceIndicators **   <a name="guardduty-Type-Sequence-sequenceIndicators"></a>
Contains information about the indicators observed in the attack sequence.
Type: Array of [Indicator](API_Indicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: No

## See Also
<a name="API_Sequence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Sequence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Sequence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Sequence)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
