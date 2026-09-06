---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AutomationRulesFindingFieldsUpdate.html
---

# AutomationRulesFindingFieldsUpdate
<a name="API_AutomationRulesFindingFieldsUpdate"></a>

 Identifies the finding fields that the automation rule action updates when a finding matches the defined criteria.

## Contents
<a name="API_AutomationRulesFindingFieldsUpdate_Contents"></a>

 ** Confidence **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-Confidence"></a>
 The rule action updates the `Confidence` field of a finding.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Criticality **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-Criticality"></a>
 The rule action updates the `Criticality` field of a finding.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Note **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-Note"></a>
The updated note.
Type: [NoteUpdate](API_NoteUpdate.md) object
Required: No

 ** RelatedFindings **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-RelatedFindings"></a>
 The rule action updates the `RelatedFindings` field of a finding.
Type: Array of [RelatedFinding](API_RelatedFinding.md) objects
Required: No

 ** Severity **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-Severity"></a>
Updates to the severity information for a finding.
Type: [SeverityUpdate](API_SeverityUpdate.md) object
Required: No

 ** Types **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-Types"></a>
 The rule action updates the `Types` field of a finding.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** UserDefinedFields **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-UserDefinedFields"></a>
 The rule action updates the `UserDefinedFields` field of a finding.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** VerificationState **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-VerificationState"></a>
 The rule action updates the `VerificationState` field of a finding.
Type: String
Valid Values: `UNKNOWN | TRUE_POSITIVE | FALSE_POSITIVE | BENIGN_POSITIVE`
Required: No

 ** Workflow **   <a name="securityhub-Type-AutomationRulesFindingFieldsUpdate-Workflow"></a>
Used to update information about the investigation into the finding.
Type: [WorkflowUpdate](API_WorkflowUpdate.md) object
Required: No

## See Also
<a name="API_AutomationRulesFindingFieldsUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AutomationRulesFindingFieldsUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AutomationRulesFindingFieldsUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AutomationRulesFindingFieldsUpdate)
