---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.Understanding.html
---

# Understanding Domain membership
<a name="custom-sqlserver-WinAuth.Understanding"></a>

 After you create or modify your DB instance, the instance becomes a member of the domain. The AWS console indicates the status of the domain membership for the DB instance. The status of the DB instance can be one of the following:
+  **joined** – The instance is a member of the domain.
+  **joining** – The instance is in the process of becoming a member of the domain.
+  **pending-join** – The instance membership is pending.
+  **pending-maintenance-join** – AWS will attempt to make the instance a member of the domain during the next scheduled maintenance window.
+  **pending-removal** – The removal of the instance from the domain is pending.
+  **pending-maintenance-removal** – AWS will attempt to remove the instance from the domain during the next scheduled maintenance window.
+  **failed** – A configuration problem has prevented the instance from joining the domain. Check and fix your configuration before reissuing the instance modify command.
+  **removing** – The instance is being removed from the domain.

A request to become a member of a domain can fail because of a network connectivity issue or an incorrect IAM role. For example, you might create a DB instance or modify an existing instance and have the attempt fail for the DB instance to become a member of a domain. In this case, either reissue the command to create or modify the DB instance or modify the newly created instance to join the domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
