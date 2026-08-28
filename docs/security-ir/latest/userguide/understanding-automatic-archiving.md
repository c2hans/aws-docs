---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/understanding-automatic-archiving.html
---

# Understanding Automatic Archiving with Proactive Response
<a name="understanding-automatic-archiving"></a>

When you enable proactive response and alert triaging, AWS Security Incident Response automatically monitors and triages security findings from Amazon GuardDuty and Security Hub CSPM. As part of this auto-triage workflow, findings are automatically archived based on the following criteria:

**Automatic archiving behavior:**
+ **Benign findings:** When the auto-triage process determines that a finding is benign (not a true security threat), AWS Security Incident Response automatically archives the finding in Amazon GuardDuty and creates suppression rules to prevent similar findings from generating alerts in the future.
+ **Suppression rules:** The service creates suppression and auto-archive rules in both Amazon GuardDuty and Security Hub CSPM for findings that match your environment's known-good patterns, such as expected IP addresses, IAM entities, and normal operational behaviors.
+ **Reduced alert volume:** Organizations using SIEM technology see significantly reduced Amazon GuardDuty finding volumes over time as the service learns your environment and automatically archives benign findings. This improves efficiency for both the AWS Security Incident Response service and your SIEM.

**Viewing archived findings:**

You can review automatically archived findings and the suppression rules created by AWS Security Incident Response:

1. Navigate to the Amazon GuardDuty console

1. Choose **Findings**

1. Select **Archived** from the findings filter

1. Review the suppression rules by selecting the down arrow next to each rule

**Important considerations:**
+ Archived findings are retained in Amazon GuardDuty for 90 days and can be viewed at any time during that period
+ You can modify or delete suppression rules at any time through the Amazon GuardDuty console
+ The auto-triage process continuously adapts to your environment, improving accuracy over time and reducing false positives

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
