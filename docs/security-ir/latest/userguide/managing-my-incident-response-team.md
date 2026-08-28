---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/managing-my-incident-response-team.html
---

# Managing my Incident Response Team
<a name="managing-my-incident-response-team"></a>

 Your incident response teams contains stakeholders for the incident response process. You can configure up to ten stakeholders as part of your membership.

 Examples for internal stakeholders include members of your incident response team, security analysts, application owners, and your security leadership team.

 Examples for external stakeholders include individuals from independent software vendors (ISV) and managed service providers (MSP) that you want to include in an incident response process.

**Note**
 Setting up your incident response team does not automatically grant teammates access to service resources such as membership and cases. You can use AWS managed policies for AWS Security Incident Response to grant read and write access to resources. [ Click here to learn more.](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html)

 Your incident response teammates specified on a membership level will be automatically added to any case. You can add or remove individual teammates at any time after a case has been created.

 The incident response team will receive an email notification on the events listed in [ communication preferences](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_IncidentResponder.html#securityir-Type-IncidentResponder-communicationPreferences).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
