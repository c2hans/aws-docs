---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentMetadataItem.html
---

# AssessmentMetadataItem
<a name="API_AssessmentMetadataItem"></a>

 A metadata object that's associated with an assessment in AWS Audit Manager.

## Contents
<a name="API_AssessmentMetadataItem_Contents"></a>

 ** complianceType **   <a name="auditmanager-Type-AssessmentMetadataItem-complianceType"></a>
 The name of the compliance standard that's related to the assessment, such as PCI-DSS.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** creationTime **   <a name="auditmanager-Type-AssessmentMetadataItem-creationTime"></a>
 Specifies when the assessment was created.
Type: Timestamp
Required: No

 ** delegations **   <a name="auditmanager-Type-AssessmentMetadataItem-delegations"></a>
 The delegations that are associated with the assessment.
Type: Array of [Delegation](API_Delegation.md) objects
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentMetadataItem-id"></a>
 The unique identifier for the assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-AssessmentMetadataItem-lastUpdated"></a>
 The time of the most recent update.
Type: Timestamp
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentMetadataItem-name"></a>
 The name of the assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** roles **   <a name="auditmanager-Type-AssessmentMetadataItem-roles"></a>
 The roles that are associated with the assessment.
Type: Array of [Role](API_Role.md) objects
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentMetadataItem-status"></a>
 The current status of the assessment.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_AssessmentMetadataItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentMetadataItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentMetadataItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentMetadataItem)
