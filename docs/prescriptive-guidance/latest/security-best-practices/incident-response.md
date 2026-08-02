---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/incident-response.html
---

# Step 10. Incorporate backup in your incident response plan
<a name="incident-response"></a>

[Security Incident Response Simulations (SIRS)](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/security-incident-response-simulations.html) are internal events that provide a structured opportunity to practice your incident response plan and procedures during a realistic scenario. It's valuable to test your backup data and operations in creative SIRS activities to test yourself against the unexpected. This helps you validate your organizational readiness and develop comfort with the rare and unexpected. Your simulations must be realistic, and they should involve cross-functional organizational teams that are required to respond to events.

Start with basic simulation exercises, and work toward a full, complex event. For example, you can build a realistic model that consists of a virtual private cloud (VPC) and associated resources that simulate inadvertent overexposure of information or a potential data breach caused by changes to policies and access control lists. To evaluate how well your incident response plan worked, document lessons learned, and identify improvements that need to be made to future response procedures.

You can use AWS Backup to set up automated instance-level backups as Amazon Machine Images (AMIs) and volume-level backups as snapshots across multiple AWS accounts. This can help your incident response team enhance their forensic processes, such as [automated forensic disk collection](https://aws.amazon.com/blogs/security/how-to-automate-forensic-disk-collection-in-aws/), by providing a restore point that could reduce the scope and impact of potential security events such as ransomware.
