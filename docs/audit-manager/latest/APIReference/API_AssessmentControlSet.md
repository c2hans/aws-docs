---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentControlSet.html
---

# AssessmentControlSet
<a name="API_AssessmentControlSet"></a>

 Represents a set of controls in an Audit Manager assessment.

## Contents
<a name="API_AssessmentControlSet_Contents"></a>

 ** controls **   <a name="auditmanager-Type-AssessmentControlSet-controls"></a>
 The list of controls that's contained with the control set.
Type: Array of [AssessmentControl](API_AssessmentControl.md) objects
Required: No

 ** delegations **   <a name="auditmanager-Type-AssessmentControlSet-delegations"></a>
 The delegations that are associated with the control set.
Type: Array of [Delegation](API_Delegation.md) objects
Required: No

 ** description **   <a name="auditmanager-Type-AssessmentControlSet-description"></a>
 The description for the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentControlSet-id"></a>
 The identifier of the control set in the assessment. This is the control set name in a plain string format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** manualEvidenceCount **   <a name="auditmanager-Type-AssessmentControlSet-manualEvidenceCount"></a>
 The total number of evidence objects that are uploaded manually to the control set.
Type: Integer
Required: No

 ** roles **   <a name="auditmanager-Type-AssessmentControlSet-roles"></a>
 The roles that are associated with the control set.
Type: Array of [Role](API_Role.md) objects
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentControlSet-status"></a>
 The current status of the control set.
Type: String
Valid Values: `ACTIVE | UNDER_REVIEW | REVIEWED`
Required: No

 ** systemEvidenceCount **   <a name="auditmanager-Type-AssessmentControlSet-systemEvidenceCount"></a>
 The total number of evidence objects that are retrieved automatically for the control set.
Type: Integer
Required: No

## See Also
<a name="API_AssessmentControlSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentControlSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentControlSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentControlSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
