---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Amazon Q Business ServiceNow Online connector
<a name="servicenow-limitations"></a>

The ServiceNow Online connector has the following known limitations:
+ There is no REST API to wake up your ServiceNow instance. To activate it when it's in hibernation mode, log in to the your ServiceNow instance.
+  Because Amazon Q Business uses email address as unique identifiers, each user must have a unique email address.
+ We don't support ServiceNow access controls.
+ We don't support ServiceNow user criteria.
+ Only the following ServiceNow roles are supported for incidents:
  + ITIL: This role provides broad access to incident management functionality.
  + Custom roles: You can create custom roles with specific incident access permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
