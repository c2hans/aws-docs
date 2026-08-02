---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/what-to-create-playbooks-for.html
---

# What to create playbooks for
<a name="what-to-create-playbooks-for"></a>

 Playbooks should be created for incident scenarios such as:
+  **Expected incidents** – Playbooks should be created for incidents you anticipate. This includes threats like denial of service (DoS), ransomware, and credential compromise.
+ ** Known security findings or alerts** – Playbooks should be created for your known security findings and alerts, such as GuardDuty findings. You might receive a GuardDuty finding and think, “Now what?” To prevent mishandling of a GuardDuty finding or ignoring the finding, create a playbook for each potential GuardDuty finding. Some remediation details and guidance can be found in the [GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html). It’s worth noting that GuardDuty is not enabled by default and does incur a cost. More details on GuardDuty can be found in Appendix A: Cloud capability definitions - [Visibility and alerting](visibility-and-alerting.md).
