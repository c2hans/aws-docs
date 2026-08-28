---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_priorities_governance_reqs.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS01-BP03 Evaluate governance requirements
<a name="ops_priorities_governance_reqs"></a>

 Ensure that you are aware of guidelines or obligations defined by your organization that may mandate or emphasize specific focus. Evaluate internal factors, such as organization policy, standards, and requirements. Validate that you have mechanisms to identify changes to governance. If no governance requirements are identified, ensure that you have applied due diligence to this determination.

 **Common anti-patterns:**
+  You are being audited and are asked to provide proof of compliance with internal governance. You have no idea if you are compliant because you have never evaluated what your compliance requirements are.
+  You have suffered a compromise resulting in financial loss. You discover that the insurance that would have covered the financial loss was contingent on your implementation of specific security controls that are not in place and required by your governance.
+  Your administrative account has been compromised resulting in the defacement of your company web site and damaged to customer trust. Your internal governance requires the use of Multifactor Authentication (MFA) to secure administrative accounts. You did not secure your administrative account with MFA and subject to disciplinary action.

 **Benefits of establishing this best practice:** Evaluating and understanding the governance requirements that your organization applies to your workload will inform how you prioritize your efforts to deliver business value.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Understand governance requirements: Evaluate internal governance factors, such as program or organizational policy, program policies, issue or system specific policies, standards, procedures, baselines, and guidelines. Validate that you have mechanisms to identify changes to governance. If no governance requirements are identified, ensure that you have applied due diligence to this determination.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cloud Compliance](https://aws.amazon.com/compliance/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
