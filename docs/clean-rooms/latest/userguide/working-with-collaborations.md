---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-collaborations.html
---

# Collaborations and memberships in AWS Clean Rooms
<a name="working-with-collaborations"></a>

A *collaboration* is a secure logical boundary in AWS Clean Rooms in which members can perform analysis on configured tables.

Any member in AWS Clean Rooms can create a collaboration.

The collaboration creator can designate a single member to analyze configured tables and receive results. However, the collaboration creator might want to prevent the member who can run the analysis from having access to the query results. In that case, the collaboration creator can designate one [member to who can query](glossary.md#glossary-member-who-can-query) or [one member who can run queries and jobs](glossary.md#glossary-member-who-can-run-queries-jobs) and another [member who can receive results](glossary.md#glossary-member-who-can-receive-results).

In most cases, the member who can query or the member who can query and run jobs is also the [member paying for compute costs](glossary.md#glossary-member-paying-for-query-compute). However, the collaboration creator can configure a different member to be responsible for paying for the query compute costs.

For information about how to create a collaboration using the AWS SDKs, see the [*AWS Clean Rooms API Reference*](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html).

**Topics**
+ [Creating a collaboration](create-collaboration.md)
+ [Creating a membership and joining a collaboration](create-membership.md)
+ [Updating a membership](update-membership.md)
+ [Editing collaborations](edit-collaboration.md)
+ [Change requests in AWS Clean Rooms](change-requests.md)
+ [Deleting collaborations](delete-collaboration.md)
+ [Viewing collaborations](review-collab-console.md)
+ [Inviting members to a collaboration](invite-members.md)
+ [Monitoring members](monitor-status.md)
+ [Adding members to a collaboration](add-member.md)
+ [Removing members from a collaboration](remove-member.md)
+ [Leaving a collaboration](leave-collab.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
