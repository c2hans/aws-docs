---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_JobPostLaunchActionsLaunchStatus.html
---

# JobPostLaunchActionsLaunchStatus
<a name="API_JobPostLaunchActionsLaunchStatus"></a>

Launch Status of the Job Post Launch Actions.

## Contents
<a name="API_JobPostLaunchActionsLaunchStatus_Contents"></a>

 ** executionID **   <a name="mgn-Type-JobPostLaunchActionsLaunchStatus-executionID"></a>
AWS Systems Manager Document's execution ID of the Job Post Launch Actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** executionStatus **   <a name="mgn-Type-JobPostLaunchActionsLaunchStatus-executionStatus"></a>
AWS Systems Manager Document's execution status.
Type: String
Valid Values: `IN_PROGRESS | SUCCESS | FAILED`
Required: No

 ** failureReason **   <a name="mgn-Type-JobPostLaunchActionsLaunchStatus-failureReason"></a>
AWS Systems Manager Document's failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ssmDocument **   <a name="mgn-Type-JobPostLaunchActionsLaunchStatus-ssmDocument"></a>
AWS Systems Manager's Document of the Job Post Launch Actions.
Type: [SsmDocument](API_SsmDocument.md) object
Required: No

 ** ssmDocumentType **   <a name="mgn-Type-JobPostLaunchActionsLaunchStatus-ssmDocumentType"></a>
AWS Systems Manager Document type.
Type: String
Valid Values: `AUTOMATION | COMMAND`
Required: No

## See Also
<a name="API_JobPostLaunchActionsLaunchStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/JobPostLaunchActionsLaunchStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/JobPostLaunchActionsLaunchStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/JobPostLaunchActionsLaunchStatus)
