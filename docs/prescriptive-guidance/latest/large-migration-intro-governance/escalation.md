---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/escalation.html
---

# Escalation plan
<a name="escalation"></a>

One key challenge for nearly all migrations is securing commitment from the application owners and technical support resources to support the wave plan. Therefore, in addition to having a well-defined communication plan, it is even more important to define an escalation plan. For each wave, starting with the T-28 commit meeting through the T-0 cutover date, you need to ensure that you facilitate commitment on a weekly basis. If any issues arise or an application owner cannot commit to the cutover date, you initiate the escalation plan.

When establishing the escalation plan, you need to define the type of issue, the circumstances in which you should escalate the issue (known as the *trigger*), and define the tiers of escalation. We recommend no more than three tiers. For each tier, you should identify the *audience*, or *response owner*, and the amount of time that the audience has to respond.

|
|
| \# | Issue | Trigger | Tier 1 | Tier 2 | Tier 3 |
| --- |--- |--- |--- |--- |--- |
| *Audience* | *Escalate after* | *Audience* | *Escalate after* | *Audience* |
| 1 | Firewall ports need to be open to migrate workloads to AWS | Firewall isn't open by T-28 commit meeting | Network team, migration lead | 24 hours | Network team manager | 24 hours | Executive team, lead of impacted business unit |

It is important that you share the escalation plan during the project kickoff. By defining and sharing this plan before the migration starts, you can provide a clear process to the team in advance, which helps prevent delay, frustration, or surprises. We also recommend that you share the escalation plan again during the T-28 commit and T-14 checkpoint meetings to reinforce commitment from the application owners.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
