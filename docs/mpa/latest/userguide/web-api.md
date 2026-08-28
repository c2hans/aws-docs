---
source_url: https://docs.aws.amazon.com/mpa/latest/userguide/web-api.html
---

# Multi-party approval portal APIs
<a name="web-api"></a>

The APIs listed in this section are called by the Multi-party approval portal on behalf of approvers. These APIs cannot be called directly and are not captured in the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/reference.html). However, these APIs are logged in AWS CloudTrail events and log entries.
+ `GetApprovalTeamForApprover`: Returns details for an approval team.
+ `GetInvitationForApprover`: Returns details for an approval team invitation.
+ `GetSessionForApprover`: Returns a list of sessions.
+ `ListApprovalTeamsForApprover`: Returns a list of approval teams.
+ `ListInvitationsForApprover`: Returns a list of approval team invitations.
+ `ListSessionsForApprover`: Returns a list of sessions.
+ `UpdateInvitationForApprover`: Sends a response to an approval team invitation.
+ `UpdateSessionForApprover`: Sends a response in a session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
