---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_incident_response_playbooks.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC10-BP04 Develop and test security incident response playbooks
<a name="sec_incident_response_playbooks"></a>

 A key part of preparing your incident response processes is developing playbooks. Incident response playbooks provide a series of prescriptive guidance and steps to follow when a security event occurs. Having clear structure and steps simplifies the response and reduces the likelihood for human error.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Playbooks should be created for incident scenarios such as:
+  **Expected incidents**: Playbooks should be created for incidents you anticipate. This includes threats like denial of service (DoS), ransomware, and credential compromise.
+  **Known security findings or alerts**: Playbooks should be created for your known security findings and alerts, such as GuardDuty findings. You might receive a GuardDuty finding and think, "Now what?" To prevent the mishandling or ignoring of a GuardDuty finding, create a playbook for each potential GuardDuty finding. Some remediation details and guidance can be found in the [GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html). It’s worth noting that GuardDuty is not enabled by default and does incur a cost. For more detail on GuardDuty, see [Appendix A: Cloud capability definitions - Visibility and alerting](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/visibility-and-alerting.html).

 Playbooks should contain technical steps for a security analyst to complete in order to adequately investigate and respond to a potential security incident.

### Implementation steps
<a name="implementation-steps"></a>

 Items to include in a playbook include:
+  **Playbook overview**: What risk or incident scenario does this playbook address? What is the goal of the playbook?
+  **Prerequisites**: What logs, detection mechanisms, and automated tools are required for this incident scenario? What is the expected notification?
+  **Communication and escalation information**: Who is involved and what is their contact information? What are each of the stakeholders’ responsibilities?
+  **Response steps**: Across phases of incident response, what tactical steps should be taken? What queries should an analyst run? What code should be run to achieve the desired outcome?
  +  **Detect**: How will the incident be detected?
  +  **Analyze**: How will the scope of impact be determined?
  +  **Contain**: How will the incident be isolated to limit scope?
  +  **Eradicate**: How will the threat be removed from the environment?
  +  **Recover**: How will the affected system or resource be brought back into production?
+  **Expected outcomes**: After queries and code are run, what is the expected result of the playbook?

## Resources
<a name="resources"></a>

 **Related Well-Architected best practices:**
+  [SEC10-BP02 - Develop incident management plans](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_incident_response_develop_management_plans.html)

 **Related documents:**
+  [Framework for Incident Response Playbooks](https://github.com/aws-samples/aws-customer-playbook-framework)
+  [Develop your own Incident Response Playbooks](https://github.com/aws-samples/aws-incident-response-playbooks-workshop)
+  [Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks)
+  [Building an AWS incident response runbook using Jupyter playbooks and CloudTrail Lake](https://catalog.workshops.aws/incident-response-jupyter/en-US)
