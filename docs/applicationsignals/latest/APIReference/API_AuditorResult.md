---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditorResult.html
---

# AuditorResult
<a name="API_AuditorResult"></a>

A structure that contains the result of an automated audit analysis, including the auditor name, description of findings, additional data, and severity level.

## Contents
<a name="API_AuditorResult_Contents"></a>

 ** Auditor **   <a name="applicationsignals-Type-AuditorResult-Auditor"></a>
The name of the auditor algorithm that generated this result.
Type: String
Required: No

 ** Data **   <a name="applicationsignals-Type-AuditorResult-Data"></a>
This is a string-to-string map. It contains additional data about the result of an automated audit analysis.
Type: String to string map
Required: No

 ** Description **   <a name="applicationsignals-Type-AuditorResult-Description"></a>
A detailed description of the audit finding, explaining what was observed and potential implications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: No

 ** Severity **   <a name="applicationsignals-Type-AuditorResult-Severity"></a>
The severity level of this audit finding, indicating the importance and potential impact of the issue.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | NONE`
Required: No

## See Also
<a name="API_AuditorResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/AuditorResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/AuditorResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/AuditorResult)
