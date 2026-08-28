---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeOutputStream.html
---

# MedicalScribeOutputStream
<a name="API_MedicalScribeOutputStream"></a>

Output stream from Medical Scribe containing transcript events and errors

## Contents
<a name="API_MedicalScribeOutputStream_Contents"></a>

 ** internalFailureException **   <a name="connecthealth-Type-MedicalScribeOutputStream-internalFailureException"></a>

Type: Exception
HTTP Status Code: 500
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
