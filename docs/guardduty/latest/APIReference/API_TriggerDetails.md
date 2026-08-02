---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_TriggerDetails.html
---

# TriggerDetails
<a name="API_TriggerDetails"></a>

Represents the reason the scan was triggered.

## Contents
<a name="API_TriggerDetails_Contents"></a>

 ** description **   <a name="guardduty-Type-TriggerDetails-description"></a>
The description of the scan trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** guardDutyFindingId **   <a name="guardduty-Type-TriggerDetails-guardDutyFindingId"></a>
The ID of the GuardDuty finding that triggered the malware scan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** triggerType **   <a name="guardduty-Type-TriggerDetails-triggerType"></a>
Specifies the trigger type that started the malware scan.
Type: String
Valid Values: `BACKUP | GUARDDUTY`
Required: No

## See Also
<a name="API_TriggerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/TriggerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/TriggerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/TriggerDetails)
