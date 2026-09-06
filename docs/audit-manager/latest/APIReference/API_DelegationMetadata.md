---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DelegationMetadata.html
---

# DelegationMetadata
<a name="API_DelegationMetadata"></a>

 The metadata that's associated with the delegation.

## Contents
<a name="API_DelegationMetadata_Contents"></a>

 ** assessmentId **   <a name="auditmanager-Type-DelegationMetadata-assessmentId"></a>
 The unique identifier for the assessment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** assessmentName **   <a name="auditmanager-Type-DelegationMetadata-assessmentName"></a>
 The name of the associated assessment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** controlSetName **   <a name="auditmanager-Type-DelegationMetadata-controlSetName"></a>
 Specifies the name of the control set that was delegated for review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** creationTime **   <a name="auditmanager-Type-DelegationMetadata-creationTime"></a>
 Specifies when the delegation was created.
Type: Timestamp
Required: No

 ** id **   <a name="auditmanager-Type-DelegationMetadata-id"></a>
 The unique identifier for the delegation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** roleArn **   <a name="auditmanager-Type-DelegationMetadata-roleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:iam:.*`
Required: No

 ** status **   <a name="auditmanager-Type-DelegationMetadata-status"></a>
 The current status of the delegation.
Type: String
Valid Values: `IN_PROGRESS | UNDER_REVIEW | COMPLETE`
Required: No

## See Also
<a name="API_DelegationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/DelegationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/DelegationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/DelegationMetadata)
