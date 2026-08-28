---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-roles.html
---

# Create IAM roles for cross-service interaction
<a name="gsg-iam-permissions-roles"></a>

In order for Amazon GameLift Servers FleetIQ to work with your Amazon EC2 instances and Auto Scaling groups, you must allow the services to interact with each other. This is done by creating IAM roles in your AWS account and assigning a set of limited permissions. Each role also specifies which services can assume the role.

Set up the following roles:
+ [Create a role for Amazon GameLift Servers FleetIQ](gsg-iam-permissions-roles-gamelift.md) to update your Amazon EC2 resources.
+ [Create a role for Amazon EC2](gsg-iam-permissions-roles-ec2.md) resources to communicate with Amazon GameLift Servers FleetIQ.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
