---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_dev_integ_freq_sm_rev_chg.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP09 Make frequent, small, reversible changes
<a name="ops_dev_integ_freq_sm_rev_chg"></a>

 Frequent, small, and reversible changes reduce the scope and impact of a change. This eases troubleshooting, helps with faster remediation, and provides the option to roll back a change.

 **Common anti-patterns:**
+  You deploy a new version of your application quarterly.
+  You frequently make changes to your database schema.
+  You perform manual in-place updates, overwriting existing installations and configurations.

 **Benefits of establishing this best practice:** You recognize benefits from development efforts faster by deploying small changes frequently. When the changes are small, it is much easier to identify if they have unintended consequences. When the changes are reversible, there is less risk to implementing the change as recovery is simplified.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Make frequent, small, reversible changes: Frequent, small, and reversible changes reduce the scope and impact of a change. This eases troubleshooting, helps with faster remediation, and provides the option to roll back a change. It also increases the rate at which you can deliver value to the business.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
