---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ApprovalStatusDetails.html
---

# ApprovalStatusDetails
<a name="API_ApprovalStatusDetails"></a>

Contains detailed information about the approval state of a given member in the collaboration for a given collaboration change request.

## Contents
<a name="API_ApprovalStatusDetails_Contents"></a>

 ** status **   <a name="API-Type-ApprovalStatusDetails-status"></a>
The approval status of a member's vote on the change request. Valid values are PENDING (if they haven't voted), APPROVED, or DENIED.
Type: String
Valid Values: `APPROVED | DENIED | PENDING`
Required: Yes

## See Also
<a name="API_ApprovalStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ApprovalStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ApprovalStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ApprovalStatusDetails)
