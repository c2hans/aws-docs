---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/onboarding-preparation.html
---

# Prepare for onboarding
<a name="onboarding-preparation"></a>

 AWS Security Incident Response recommends using a proof-of-concept (POC) approach when implementing AWS Security Incident Response. Before deployment, complete the following preparation steps with your internal teams and AWS account team.
+ **Identify key stakeholders**: Map out the incident response decision-makers in your organization. Their involvement in policy updates and process changes is essential for a successful rollout.
+ **Validate finding sources**: Confirm that all security finding sources are properly configured and deployed. GuardDuty and Security Hub CSPM are critical inputs for the service's auto-triage technology.
+ **Determine account scope**: Decide whether AWS Security Incident Response will cover your entire AWS organization or specific organizational units (OUs). Defining this scope early makes implementation and scaling more straightforward.
+ **Establish escalation protocols**: Update your existing escalation procedures to include AWS Security Incident Response. Communicate the updated protocols to all stakeholders and response personnel.
+ **Collect points of contact and critical information**: Collecting customer information early ensures a smooth onboarding experience and enables timely outreach from the AWS Security Incident Response Engineering team when needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
