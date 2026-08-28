---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/getting-started.html
---

# Getting started
<a name="getting-started"></a>

 **Time to deploy:** Approximately 30 minutes per account.

We recommend adopting the solution in phases rather than enabling automatic remediation everywhere at once. With a phased approach, you build confidence in each remediation against your own environment before the solution acts on findings without human review.

## Use a non-production environment first
<a name="test-environment"></a>

Before you enable fully automated remediation in production, validate the controls you intend to automate in a non-production account and Region. Reproduce the finding on a disposable resource, run the remediation, and confirm the outcome. This gives you a safe place to experiment with new controls and filters without affecting production workloads.

## Walk, then run
<a name="walk-run-model"></a>

1.  **Observe.** Deploy the solution and review the findings that arrive in the Web UI. On a fresh deployment, automatic remediation is off by default, so no remediations run automatically at this stage. If instead you are upgrading from an earlier ASR version, any controls you had configured for automatic remediation remain enabled after the upgrade — so remediations may run automatically. In that case, review the **Controls** page (or the Remediation Configuration table) to confirm which controls are enabled before proceeding. Use this phase to confirm that findings from your member accounts and Regions are aggregating to the admin account and appearing in the solution.

1.  **Remediate on demand.** Run remediations manually from the Web UI, or from the AWS Security Hub CSPM custom action, on individual findings. Review the remediation result and the affected resource before moving on. Where a remediation supports rollback, you can restore the resource to its pre-remediation state from the Web UI. With on-demand remediation, you validate a control’s behavior on real resources without committing to automatic action.

1.  **Automate selectively.** When you are confident in a control’s behavior, enable fully automated remediation for that control. Enable one control at a time. Use filters to limit the accounts, organizational units, and resource tags the solution acts on. For the steps, see [Manage automated remediation](manage-automated-remediation.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
