---
source_url: https://docs.aws.amazon.com/connect-decisions/latest/adminguide/user-assignment.html
---

# User Assignment
<a name="user-assignment"></a>

User Assignment is a feature that makes it easier to balance insights between multiple users. Using User Assignment, customers can assign specific insights to users to better reflect how these tasks are shared in real life. It works as follows:
+ Whenever an exception is created, the system checks the product and site for which the exception is created against all users that have the same product OR site configured for their access control
+ If the system finds a user that matches, the Assigned To field for that exception is updated with the username. In cases where more than one user has products or sites that match with the exception, it is assigned randomly to one of them
+ Only one user can be assigned to each exception, but an exception can be reassigned to another user if needed. It can only be reassigned to a user with product or site access
+ Auto-assignment for insights occurs when the exception is first created. Previously created insights will not be reassigned automatically. Further, if a user is deleted or their access control is updated, the user assignment is not automatically updated
+ In the insights listing page, a user can filter by the Assigned To dimension to easily identify all insights assigned to them. They can also use this same filter to view unassigned insights. User Assignment is currently available only for insights

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
