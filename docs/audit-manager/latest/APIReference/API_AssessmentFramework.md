---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentFramework.html
---

# AssessmentFramework
<a name="API_AssessmentFramework"></a>

 The file used to structure and automate AWS Audit Manager assessments for a given compliance standard.

## Contents
<a name="API_AssessmentFramework_Contents"></a>

 ** arn **   <a name="auditmanager-Type-AssessmentFramework-arn"></a>
 The Amazon Resource Name (ARN) of the framework.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:auditmanager:.*`
Required: No

 ** controlSets **   <a name="auditmanager-Type-AssessmentFramework-controlSets"></a>
 The control sets that are associated with the framework.
Type: Array of [AssessmentControlSet](API_AssessmentControlSet.md) objects
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentFramework-id"></a>
 The unique identifier for the framework.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** metadata **   <a name="auditmanager-Type-AssessmentFramework-metadata"></a>
 The metadata of a framework, such as the name, ID, or description.
Type: [FrameworkMetadata](API_FrameworkMetadata.md) object
Required: No

## See Also
<a name="API_AssessmentFramework_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentFramework)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentFramework)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentFramework)
