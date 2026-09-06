---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateDelegationRequest.html
---

# CreateDelegationRequest
<a name="API_CreateDelegationRequest"></a>

 A collection of attributes that's used to create a delegation for an assessment in AWS Audit Manager.

## Contents
<a name="API_CreateDelegationRequest_Contents"></a>

 ** comment **   <a name="auditmanager-Type-CreateDelegationRequest-comment"></a>
 A comment that's related to the delegation request.
Type: String
Length Constraints: Maximum length of 350.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** controlSetId **   <a name="auditmanager-Type-CreateDelegationRequest-controlSetId"></a>
 The unique identifier for the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** roleArn **   <a name="auditmanager-Type-CreateDelegationRequest-roleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:iam:.*`
Required: No

 ** roleType **   <a name="auditmanager-Type-CreateDelegationRequest-roleType"></a>
 The type of customer persona.
In `CreateAssessment`, `roleType` can only be `PROCESS_OWNER`.
In `UpdateSettings`, `roleType` can only be `PROCESS_OWNER`.
In `BatchCreateDelegationByAssessment`, `roleType` can only be `RESOURCE_OWNER`.
Type: String
Valid Values: `PROCESS_OWNER | RESOURCE_OWNER`
Required: No

## See Also
<a name="API_CreateDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/CreateDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/CreateDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/CreateDelegationRequest)
