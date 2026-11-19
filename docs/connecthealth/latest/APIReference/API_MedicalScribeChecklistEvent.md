---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeChecklistEvent.html
---

# MedicalScribeChecklistEvent

Real-time extraction is in preview release for Amazon Connect Health and is subject to change. To request access to this feature, contact your AWS account team.

The session's checklist as of this point in the session. Each event carries every item with its current status, not only the items that changed.

## Contents
<a name="API_MedicalScribeChecklistEvent_Contents"></a>

 ** checklists **   <a name="connecthealth-Type-MedicalScribeChecklistEvent-checklists"></a>
The checklists for the session. The list is empty when no checklist is active.
Type: Array of [Checklist](API_Checklist.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** snapshotVersion **   <a name="connecthealth-Type-MedicalScribeChecklistEvent-snapshotVersion"></a>
The version of this snapshot. Versions increase within a session and can skip values. Keep the snapshot with the highest version and ignore any event whose version is not higher, including after you reconnect to the session. Versions of checklist events and periodontal chart events are independent.
Type: Long
Required: Yes

## See Also
<a name="API_MedicalScribeChecklistEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeChecklistEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeChecklistEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeChecklistEvent)
