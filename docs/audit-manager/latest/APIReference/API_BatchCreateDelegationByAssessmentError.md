---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchCreateDelegationByAssessmentError.html
---

# BatchCreateDelegationByAssessmentError
<a name="API_BatchCreateDelegationByAssessmentError"></a>

 An error entity for the `BatchCreateDelegationByAssessment` API. This is used to provide more meaningful errors than a simple string message.

## Contents
<a name="API_BatchCreateDelegationByAssessmentError_Contents"></a>

 ** createDelegationRequest **   <a name="auditmanager-Type-BatchCreateDelegationByAssessmentError-createDelegationRequest"></a>
 The API request to batch create delegations in AWS Audit Manager.
Type: [CreateDelegationRequest](API_CreateDelegationRequest.md) object
Required: No

 ** errorCode **   <a name="auditmanager-Type-BatchCreateDelegationByAssessmentError-errorCode"></a>
 The error code that the `BatchCreateDelegationByAssessment` API returned.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[0-9]{3}`
Required: No

 ** errorMessage **   <a name="auditmanager-Type-BatchCreateDelegationByAssessmentError-errorMessage"></a>
 The error message that the `BatchCreateDelegationByAssessment` API returned.
Type: String
Length Constraints: Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: No

## See Also
<a name="API_BatchCreateDelegationByAssessmentError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/BatchCreateDelegationByAssessmentError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/BatchCreateDelegationByAssessmentError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/BatchCreateDelegationByAssessmentError)
