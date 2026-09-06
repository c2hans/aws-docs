---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentMetadata.html
---

# AssessmentMetadata
<a name="API_AssessmentMetadata"></a>

 The metadata that's associated with the specified assessment.

## Contents
<a name="API_AssessmentMetadata_Contents"></a>

 ** assessmentReportsDestination **   <a name="auditmanager-Type-AssessmentMetadata-assessmentReportsDestination"></a>
 The destination that evidence reports are stored in for the assessment.
Type: [AssessmentReportsDestination](API_AssessmentReportsDestination.md) object
Required: No

 ** complianceType **   <a name="auditmanager-Type-AssessmentMetadata-complianceType"></a>
 The name of the compliance standard that's related to the assessment, such as PCI-DSS.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** creationTime **   <a name="auditmanager-Type-AssessmentMetadata-creationTime"></a>
 Specifies when the assessment was created.
Type: Timestamp
Required: No

 ** delegations **   <a name="auditmanager-Type-AssessmentMetadata-delegations"></a>
 The delegations that are associated with the assessment.
Type: Array of [Delegation](API_Delegation.md) objects
Required: No

 ** description **   <a name="auditmanager-Type-AssessmentMetadata-description"></a>
 The description of the assessment.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentMetadata-id"></a>
 The unique identifier for the assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-AssessmentMetadata-lastUpdated"></a>
 The time of the most recent update.
Type: Timestamp
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentMetadata-name"></a>
 The name of the assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** roles **   <a name="auditmanager-Type-AssessmentMetadata-roles"></a>
 The roles that are associated with the assessment.
Type: Array of [Role](API_Role.md) objects
Required: No

 ** scope **   <a name="auditmanager-Type-AssessmentMetadata-scope"></a>
 The wrapper of AWS accounts and services that are in scope for the assessment.
Type: [Scope](API_Scope.md) object
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentMetadata-status"></a>
 The overall status of the assessment.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_AssessmentMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentMetadata)
