---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeOutputStream.html
---

# MedicalScribeOutputStream

The output stream of a listening session. It carries transcript events, periodontal chart events, checklist events, and errors.

## Contents
<a name="API_MedicalScribeOutputStream_Contents"></a>

 ** checklistEvent **   <a name="connecthealth-Type-MedicalScribeOutputStream-checklistEvent"></a>
Real-time extraction is in preview release for Amazon Connect Health and is subject to change. To request access to this feature, contact your AWS account team.
A snapshot of the session's checklist. Amazon Connect Health sends this event only when real-time extraction is enabled for the account and the session uses a supported note template.
Type: [MedicalScribeChecklistEvent](API_MedicalScribeChecklistEvent.md) object
Required: No

 ** internalFailureException **   <a name="connecthealth-Type-MedicalScribeOutputStream-internalFailureException"></a>

Type: Exception
HTTP Status Code: 500
Required: No

 ** periodontalChartEvent **   <a name="connecthealth-Type-MedicalScribeOutputStream-periodontalChartEvent"></a>
Real-time extraction is in preview release for Amazon Connect Health and is subject to change. To request access to this feature, contact your AWS account team.
A snapshot of the periodontal chart. Amazon Connect Health sends this event only when real-time extraction is enabled for the account and periodontal charting is dictated during the session.
Type: [MedicalScribePeriodontalChartEvent](API_MedicalScribePeriodontalChartEvent.md) object
Required: No

 ** transcriptEvent **   <a name="connecthealth-Type-MedicalScribeOutputStream-transcriptEvent"></a>

Type: [MedicalScribeTranscriptEvent](API_MedicalScribeTranscriptEvent.md) object
Required: No

 ** validationException **   <a name="connecthealth-Type-MedicalScribeOutputStream-validationException"></a>

Type: Exception
HTTP Status Code: 400
Required: No

## See Also
<a name="API_MedicalScribeOutputStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeOutputStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeOutputStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeOutputStream)
