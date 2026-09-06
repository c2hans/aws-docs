---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentReportsDestination.html
---

# AssessmentReportsDestination
<a name="API_AssessmentReportsDestination"></a>

 The location where AWS Audit Manager saves assessment reports for the given assessment.

## Contents
<a name="API_AssessmentReportsDestination_Contents"></a>

 ** destination **   <a name="auditmanager-Type-AssessmentReportsDestination-destination"></a>
 The destination bucket where Audit Manager stores assessment reports.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(S|s)3:\/\/[a-zA-Z0-9\-\.\(\)\'\*\_\!\=\+\@\:\s\,\?\/]+$`
Required: No

 ** destinationType **   <a name="auditmanager-Type-AssessmentReportsDestination-destinationType"></a>
 The destination type, such as Amazon S3.
Type: String
Valid Values: `S3`
Required: No

## See Also
<a name="API_AssessmentReportsDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentReportsDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentReportsDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentReportsDestination)
