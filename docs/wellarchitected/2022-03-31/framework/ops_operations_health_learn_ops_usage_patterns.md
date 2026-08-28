---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_operations_health_learn_ops_usage_patterns.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP05 Learn the expected patterns of activity for operations
<a name="ops_operations_health_learn_ops_usage_patterns"></a>

 Establish patterns of operations activities to identify anomalous activity so that you can respond appropriately if necessary.

 **Common anti-patterns:**
+  Your deployment failure rate has increased substantially recently. You address each of the failures independently. You do not realize that the failures correspond to deployments by a new employee who is unfamiliar with the deployment management system.

 **Benefits of establishing this best practice:** By learning patterns of behavior, you can recognize unexpected behavior and take action if necessary.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Learn expected patterns of activity for operations: Establish patterns of operations activity to determine when behavior is outside of the expected values so that you can respond appropriately if required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
