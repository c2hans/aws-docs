---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationChangeRequestSummary.html
---

# CollaborationChangeRequestSummary
<a name="API_CollaborationChangeRequestSummary"></a>

Summary information about a collaboration change request.

## Contents
<a name="API_CollaborationChangeRequestSummary_Contents"></a>

 ** changes **   <a name="API-Type-CollaborationChangeRequestSummary-changes"></a>
Summary of the changes in this change request.
Type: Array of [Change](API_Change.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** collaborationId **   <a name="API-Type-CollaborationChangeRequestSummary-collaborationId"></a>
The unique identifier for the collaboration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationChangeRequestSummary-createTime"></a>
The time when the change request was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-CollaborationChangeRequestSummary-id"></a>
The unique identifier for the change request.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** isAutoApproved **   <a name="API-Type-CollaborationChangeRequestSummary-isAutoApproved"></a>
Whether the change request was automatically approved.
Type: Boolean
Required: Yes

 ** status **   <a name="API-Type-CollaborationChangeRequestSummary-status"></a>
The current status of the change request.
Type: String
Valid Values: `PENDING | APPROVED | CANCELLED | DENIED | COMMITTED`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationChangeRequestSummary-updateTime"></a>
The time when the change request was last updated.
Type: Timestamp
Required: Yes

 ** approvals **   <a name="API-Type-CollaborationChangeRequestSummary-approvals"></a>
Summary of approval statuses from all collaboration members for this change request.
Type: String to [ApprovalStatusDetails](API_ApprovalStatusDetails.md) object map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Fixed length of 12.
Key Pattern: `\d+`
Required: No

## See Also
<a name="API_CollaborationChangeRequestSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationChangeRequestSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationChangeRequestSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationChangeRequestSummary)
