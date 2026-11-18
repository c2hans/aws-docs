---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribePeriodontalChartEvent.html
---

# MedicalScribePeriodontalChartEvent
<a name="API_MedicalScribePeriodontalChartEvent"></a>

Real-time extraction is in preview release for Amazon Connect Health and is subject to change. To request access to this feature, contact your AWS account team.

The periodontal chart as of this point in the session. Each event carries every tooth charted so far, not only the teeth that changed.

## Contents
<a name="API_MedicalScribePeriodontalChartEvent_Contents"></a>

 ** snapshotVersion **   <a name="connecthealth-Type-MedicalScribePeriodontalChartEvent-snapshotVersion"></a>
The version of this snapshot. Versions increase within a session and can skip values. Keep the snapshot with the highest version and ignore any event whose version is not higher, including after you reconnect to the session. Versions of checklist events and periodontal chart events are independent.
Type: Long
Required: Yes

 ** teeth **   <a name="connecthealth-Type-MedicalScribePeriodontalChartEvent-teeth"></a>
The teeth that have a recorded value or are marked missing, in ascending `toothNumber` order.
Type: Array of [PeriodontalTooth](API_PeriodontalTooth.md) objects
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Required: Yes

 ** reviewItems **   <a name="connecthealth-Type-MedicalScribePeriodontalChartEvent-reviewItems"></a>
Items that need the clinician's confirmation.
Type: Array of [PeriodontalReview](API_PeriodontalReview.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_MedicalScribePeriodontalChartEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribePeriodontalChartEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribePeriodontalChartEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribePeriodontalChartEvent)
