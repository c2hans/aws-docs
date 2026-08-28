---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/operations-conclusion.html
---

# Conclusion
<a name="operations-conclusion"></a>

 Each operations phase has unique goals, techniques, methodologies, and strategies. Table 4 summarizes these phases and some of the techniques and methodologies covered in this section.

* Table 4 – Operations phases: Goals, techniques, and methodologies*

|  Phase  |  Goal  |  Techniques and methodologies  |
| --- | --- | --- |
|  Detection  |  Identify a potential security event.  |  +   Security controls for detection  <br />+   Behavior and rule-based detection  <br />+   People-based detection    |
|  Analysis  |  Determine if the security event is an incident and assess the scope of the incident.  |  +   Validate and scope alert  <br />+   Query logs  <br />+   Threat intelligence  <br />+   Automation    |
|  Containment  |  Minimize and limit the impact of the security event.  |  +   Source containment  <br />+   Technique and access containment  <br />+   Destination containment    |
|  Eradication  |  Remove unauthorized resources or artifacts related to the security event.  |  +   Compromised or unauthorized credential rotation or deletion  <br />+   Unauthorized resource deletion  <br />+   Malware removal  <br />+   Security scans    |
|  Recovery  |  Restore systems to a known good state and monitor these systems to ensure the threat does not return.  |  +   System restoration from backups  <br />+   Systems rebuilt from scratch  <br />+   Compromised files replaced with clean versions    |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
