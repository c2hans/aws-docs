---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_freq_sm_rev_chg.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP09 Make frequent, small, reversible changes
<a name="ops_dev_integ_freq_sm_rev_chg"></a>

 Frequent, small, and reversible changes reduce the scope and impact of a change. This eases troubleshooting, enables faster remediation, and provides the option to roll back a change.

 **Common anti-patterns:**
+  You deploy a new version of your application quarterly.
+  You frequently make changes to your database schema.
+  You perform manual in-place updates, overwriting existing installations and configurations.

 **Benefits of establishing this best practice:** You recognize benefits from development efforts faster by deploying small changes frequently. When the changes are small, it is much easier to identify if they have unintended consequences. When the changes are reversible, there is less risk to implementing the change as recovery is simplified.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Make frequent, small, reversible changes: Frequent, small, and reversible changes reduce the scope and impact of a change. This eases troubleshooting, enables faster remediation, and provides the option to roll back a change. It also increases the rate at which you can deliver value to the business.
