---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ManualEvidence.html
---

# ManualEvidence
<a name="API_ManualEvidence"></a>

 Evidence that's manually added to a control in AWS Audit Manager. `manualEvidence` can be one of the following: `evidenceFileName`, `s3ResourcePath`, or `textResponse`.

## Contents
<a name="API_ManualEvidence_Contents"></a>

 ** evidenceFileName **   <a name="auditmanager-Type-ManualEvidence-evidenceFileName"></a>
The name of the file that's uploaded as manual evidence. This name is populated using the `evidenceFileName` value from the [https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl.html](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl.html) API response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\/]*`
Required: No

 ** s3ResourcePath **   <a name="auditmanager-Type-ManualEvidence-s3ResourcePath"></a>
The S3 URL of the object that's imported as manual evidence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(S|s)3:\/\/[a-zA-Z0-9\-\.\(\)\'\*\_\!\=\+\@\:\s\,\?\/]+$`
Required: No

 ** textResponse **   <a name="auditmanager-Type-ManualEvidence-textResponse"></a>
The plain text response that's entered and saved as manual evidence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

## See Also
<a name="API_ManualEvidence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ManualEvidence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ManualEvidence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ManualEvidence)
