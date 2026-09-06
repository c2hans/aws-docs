---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Settings.html
---

# Settings
<a name="API_Settings"></a>

 The settings object that holds all supported Audit Manager settings.

## Contents
<a name="API_Settings_Contents"></a>

 ** defaultAssessmentReportsDestination **   <a name="auditmanager-Type-Settings-defaultAssessmentReportsDestination"></a>
The default S3 destination bucket for storing assessment reports.
Type: [AssessmentReportsDestination](API_AssessmentReportsDestination.md) object
Required: No

 ** defaultExportDestination **   <a name="auditmanager-Type-Settings-defaultExportDestination"></a>
The default S3 destination bucket for storing evidence finder exports.
Type: [DefaultExportDestination](API_DefaultExportDestination.md) object
Required: No

 ** defaultProcessOwners **   <a name="auditmanager-Type-Settings-defaultProcessOwners"></a>
 The designated default audit owners.
Type: Array of [Role](API_Role.md) objects
Required: No

 ** deregistrationPolicy **   <a name="auditmanager-Type-Settings-deregistrationPolicy"></a>
The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.
Type: [DeregistrationPolicy](API_DeregistrationPolicy.md) object
Required: No

 ** evidenceFinderEnablement **   <a name="auditmanager-Type-Settings-evidenceFinderEnablement"></a>
The current evidence finder status and event data store details.
Type: [EvidenceFinderEnablement](API_EvidenceFinderEnablement.md) object
Required: No

 ** isAwsOrgEnabled **   <a name="auditmanager-Type-Settings-isAwsOrgEnabled"></a>
 Specifies whether AWS Organizations is enabled.
Type: Boolean
Required: No

 ** kmsKey **   <a name="auditmanager-Type-Settings-kmsKey"></a>
 The AWS KMS key details.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Pattern: `^arn:.*:kms:.*|DEFAULT`
Required: No

 ** snsTopic **   <a name="auditmanager-Type-Settings-snsTopic"></a>
 The designated Amazon Simple Notification Service (Amazon SNS) topic.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9-_\(\)\[\]]+$`
Required: No

## See Also
<a name="API_Settings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Settings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Settings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Settings)
