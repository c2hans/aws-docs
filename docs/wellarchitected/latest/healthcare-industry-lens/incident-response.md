---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/incident-response.html
---

# Incident response
<a name="incident-response"></a>

| HCL\_SEC9. What is your disaster recovery for critical systems? |
| --- |
|   |

 **Mitigate and respond to potential incidents by creating policies, procedures, and playbooks**

 Healthcare, and heath data, are valuable targets for malicious actors. Create policies, procedures, and playbooks designed to respond to and mitigate the potential impact of a security event or natural disaster. This includes exercises that practice the response to a simulated incident using the defined policies, procedures, and playbooks to prepare your organization.

 As malicious actors continue to target healthcare and health data owners with attacks such as ransomware, implement a data availability strategy to help reduce the potential impact. This can include backups that are stored in a separate AWS account with authorization controls in place to prevent modifying the backup (such as setting the backup as read only) or a [pilot light disaster recovery environment](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html). Create specific policies, procedures, and playbooks for ransomware to prepare your organization.

 The [incident response section of the security pillar in the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/incident-response.html) contains further details on preparing for and responding to security incidents in the cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
