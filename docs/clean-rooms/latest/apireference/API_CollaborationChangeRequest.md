---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationChangeRequest.html
---

# CollaborationChangeRequest
<a name="API_CollaborationChangeRequest"></a>

Represents a request to modify a collaboration. Change requests enable structured modifications to collaborations after they have been created.

## Contents
<a name="API_CollaborationChangeRequest_Contents"></a>

 ** changes **   <a name="API-Type-CollaborationChangeRequest-changes"></a>
The list of changes specified in this change request.
Type: Array of [Change](API_Change.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** collaborationId **   <a name="API-Type-CollaborationChangeRequest-collaborationId"></a>
The unique identifier for the collaboration being modified.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationChangeRequest-createTime"></a>
The time when the change request was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-CollaborationChangeRequest-id"></a>
The unique identifier for the change request.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** isAutoApproved **   <a name="API-Type-CollaborationChangeRequest-isAutoApproved"></a>
Whether the change request was automatically approved based on the collaboration's auto-approval settings.
Type: Boolean
Required: Yes

 ** status **   <a name="API-Type-CollaborationChangeRequest-status"></a>
The current status of the change request. Valid values are `PENDING`, `APPROVED`, `DENIED`, `COMMITTED`, and `CANCELLED`.
Type: String
Valid Values: `PENDING | APPROVED | CANCELLED | DENIED | COMMITTED`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationChangeRequest-updateTime"></a>
The time when the change request was last updated.
Type: Timestamp
Required: Yes

 ** approvals **   <a name="API-Type-CollaborationChangeRequest-approvals"></a>
A list of approval details from collaboration members, including approval status and multi-party approval workflow information.
Type: String to [ApprovalStatusDetails](API_ApprovalStatusDetails.md) object map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Fixed length of 12.
Key Pattern: `\d+`
Required: No

## See Also
<a name="API_CollaborationChangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationChangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationChangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationChangeRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
