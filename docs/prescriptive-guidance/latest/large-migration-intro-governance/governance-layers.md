---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/governance-layers.html
---

# Governance structure and cadence
<a name="governance-layers"></a>

Before the formal project kickoff, work with your project sponsor and stakeholders to establish mechanisms to communicate delivery progress for both the executive and non-executive stakeholders. Sharing the defined mechanism should be part of the project kickoff and should visually depict the communication cadence, objectives, and participants within each governance layer. The governance structure helps participants understand how the project will be managed, who the leaders are, how leaders will oversee the project, how decisions will be made, how and when issues will be escalated, and how progress will be measured.

The following diagram shows a top-down approach in the governance layers. The top three layers are the management layers, which are responsible for establishing the large migration strategy, program governance, and the workstream approach. The bottom three layers are the delivery layers, which are responsible for governing the communication gates and regular meetings, such as infrastructure and operations meetings, and migration business hours.

![Governance layers in order of management to delivery, as described in the following table.](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/images/guide-img/0ce37e8e-2c4b-4da7-ad35-503caa83d254/images/60c489a7-021e-4549-a71f-24ab4d29fefe.png)

The following table describes the objectives and typical participants for each governance layer.

|
|
| Governance layer | Objective | Participants |
| --- |--- |--- |
| Strategic governance | Develop business and strategic plans, review contractual commitments, address escalated issues, and check overall performance. | Executive sponsor or executive steering committee<br />Leads for partners or consultants<br />Migration delivery leadership |
| Program governance | Report and review the status of all workstreams, determine the need for resources or subject matter experts, and allocate time for migration team reporting. | Workstream owners<br />Leads for partners or consultants<br />Migration lead<br />Scrum masters |
| Workstream approach | Support and review the status of planned and completed activities, and review blocked items for the PMO, foundation workstream, migration workstream, and Cloud Ops team. | Workstream leads<br />Scrum master<br />Team members<br />Owners defined in the RACI matrix<br />Managers for partners or consultants<br />Project manager<br />Migration lead |
| Application owner commit meetings | Confirm commitment to the wave that is scheduled to start | Application owners<br />Leads for partners or consultants<br />Migration lead<br />Communication lead<br />Custom migration lead |
| Infrastructure and operations | Review the progress of the migration, review active issues, and decide whether escalation is required. Collaborate across workstreams and plan resources for the next sprint. | RACI-defined members<br />Migration lead<br />Lead architect<br />Consultants for the migration, applications, SQL, or other special workloads |
| Migration business hours | Provide application owners with an open meeting to seek support or guidance. | Leads for partners or consultants<br />Application owners<br />Migration lead<br />Engagement manager |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
