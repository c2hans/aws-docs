---
source_url: https://docs.aws.amazon.com/EDI/latest/eco-support-guide/eco-scope.html
---

# Scope of changes performed by EDI Cloud Operations
<a name="eco-scope"></a>

ECO deploys or updates AWS resources only in the following situations through a predefined access model:
+ To deploy and update tools and resources required by ECO to service EDI.
+ As part of EDI monitoring in response to events and alarms.
+ To remediate security issues as part of responses to violations in EDI such as making noncompliant resources conform to security best practices.
+ During remediation and restoration as part of an incident response.
+ During deployment, application patching, and updates for major and minor releases of EDI.
+ When conﬁguring the following ECO features:
  + Alarm manager
  + Resource tagger
  + Resource scheduler
  + Backup plans

ECO doesn't deploy or update resources outside the preceding situations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Energy Data Insights on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query EDI` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
