---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_mit_deploy_risks_freq_sm_rev_chg.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS06-BP06 Deploy frequent, small, reversible changes
<a name="ops_mit_deploy_risks_freq_sm_rev_chg"></a>

 Use frequent, small, and reversible changes to reduce the scope of a change. This results in easier troubleshooting and faster remediation with the option to roll back a change.

 **Common anti-patterns:**
+  You deploy a new version of your application quarterly.
+  You frequently make changes to your database schema.
+  You perform manual in-place updates, overwriting existing installations and configurations.

 **Benefits of establishing this best practice:** You recognize benefits from development efforts faster by deploying small changes frequently. When the changes are small it is much easier to identify if they have unintended consequences. When the changes are reversible there is less risk to implementing the change as recovery is simplified.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Deploy frequent, small, reversible changes: Use frequent, small, and reversible changes to reduce the scope of a change. This results in easier troubleshooting and faster remediation with the option to roll back a change.
