---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/incident-management.html
---

# Incident management
<a name="incident-management"></a>

 Tags can play a vital part in all phases of incident management starting from incident logging, prioritization, investigation, communication, resolution to closure.

 Tags can detail where an incident should be logged, the team or teams that should be informed of the incident, and the defined escalation priority. It’s important to remember that tags are not encrypted, so consider what information you store in them. Also, in organizations, teams, and reporting lines, responsibilities change, so consider storing a link to a secure portal where this information can be more effectively managed. These tags don’t need to be exclusive. For instance, the application ID could be used to lookup the escalation paths in an IT service management portal. Make sure it is clear in your operational definitions that this tag is being used for multiple purposes.

 Operational requirement tags can be detailed as well, to help incident managers and operations personnel further refine their objectives in response to an incident or event.

 Relative links (to the knowledge system base URL) for [runbooks](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.runbook.en.html) and [playbooks](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.playbook.en.html) can be included as tags to assist the responding teams in identifying corresponding process, procedure and documentation.

 *Table 9 - Use operational tags to inform incident management*

|  Use Case  |  Tag Key  |  Rationale  |  Example Values  |
| --- | --- | --- | --- |
|  Incident Management  | example-inc:incident-management:escalationlog  |  The system in use by the supporting team to log incidents  | jira, servicenow, zendesk  |
|  Incident Management  | example-inc:incident-management:escalationpath  |  Path of escalation  | ops-center, dev-ops, app-team  |
|  Cost Allocation and Incident Management  | example-inc:cost-allocation:CostCenter |  Monitor costs by cost center. This is an example of a dual use tag where the cost center is being used as an application code for incident logging  | 123-\*  |
|  Backup Schedule  | example-inc:backup:schedule  |  Backup schedule of the resource  | Daily  |
|  Playbook / Incident Management  | example-inc:incident-management:playbook  |  Documented playbook  | webapp/incident/playbook  |
