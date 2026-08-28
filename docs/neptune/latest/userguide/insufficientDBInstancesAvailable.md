---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/insufficientDBInstancesAvailable.html
---

# Insufficient DB instances available
<a name="insufficientDBInstancesAvailable"></a>

 The `InsufficientDBInstanceCapacity` error can be returned when you try to create, start, or modify a DB instance. It can also be returned when you try to restore a DB instance from a DB snapshot. When this error is returned, a common cause is that the specific DB instance class isn't available in the requested Availability Zone. You can try one of the following to solve the problem:
+  Retry the request with a different DB instance class.
+  Retry the request with a different Availability Zone.
+  Retry the request without specifying an explicit Availability Zone.

 For information about troubleshooting instance capacity issues for Amazon EC2, see [ Insufficient instance capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html#troubleshooting-launch-capacity) in the Amazon EC2 User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
