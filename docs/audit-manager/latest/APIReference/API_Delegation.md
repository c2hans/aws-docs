---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Delegation.html
---

# Delegation
<a name="API_Delegation"></a>

 The assignment of a control set to a delegate for review.

## Contents
<a name="API_Delegation_Contents"></a>

 ** assessmentId **   <a name="auditmanager-Type-Delegation-assessmentId"></a>
 The identifier for the assessment that's associated with the delegation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** assessmentName **   <a name="auditmanager-Type-Delegation-assessmentName"></a>
 The name of the assessment that's associated with the delegation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** comment **   <a name="auditmanager-Type-Delegation-comment"></a>
 The comment that's related to the delegation.
Type: String
Length Constraints: Maximum length of 350.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** controlSetId **   <a name="auditmanager-Type-Delegation-controlSetId"></a>
 The identifier for the control set that's associated with the delegation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** createdBy **   <a name="auditmanager-Type-Delegation-createdBy"></a>
 The user or role that created the delegation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\s-_()\[\]]+$`
Required: No

 ** creationTime **   <a name="auditmanager-Type-Delegation-creationTime"></a>
 Specifies when the delegation was created.
Type: Timestamp
Required: No

 ** id **   <a name="auditmanager-Type-Delegation-id"></a>
 The unique identifier for the delegation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-Delegation-lastUpdated"></a>
 Specifies when the delegation was last updated.
Type: Timestamp
Required: No

 ** roleArn **   <a name="auditmanager-Type-Delegation-roleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:iam:.*`
Required: No

 ** roleType **   <a name="auditmanager-Type-Delegation-roleType"></a>
 The type of customer persona.
In `CreateAssessment`, `roleType` can only be `PROCESS_OWNER`.
In `UpdateSettings`, `roleType` can only be `PROCESS_OWNER`.
In `BatchCreateDelegationByAssessment`, `roleType` can only be `RESOURCE_OWNER`.
Type: String
Valid Values: `PROCESS_OWNER | RESOURCE_OWNER`
Required: No

 ** status **   <a name="auditmanager-Type-Delegation-status"></a>
 The status of the delegation.
Type: String
Valid Values: `IN_PROGRESS | UNDER_REVIEW | COMPLETE`
Required: No

## See Also
<a name="API_Delegation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Delegation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Delegation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Delegation)
