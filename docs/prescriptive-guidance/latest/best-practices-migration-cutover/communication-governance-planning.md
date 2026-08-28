---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/communication-governance-planning.html
---

# Communication and governance planning
<a name="communication-governance-planning"></a>

## Communication and governance strategy
<a name="communication-governance-strategy"></a>

What you communicate and how you communicate can be key to the success of your cutover. To achieve success, we recommend that you develop and implement a communication and governance strategy that provides clear guidance on communication tooling, defines ownership roles, and specifies communication channels for each cutover task. We also recommend that your communication strategy is documented and governed by the migration team and integrated with your migration escalation path as part of project governance.

## Communication and governance channel
<a name="communication-governance-channel"></a>

When you create a communication channel, it's important to define the target audience and decide which communication method is most effective. For example, if most people within your organization don't actively monitor emails, instant messaging might be the preferred method. We recommend that you establish a channel across all relevant stakeholders. Ideally, the channel is open before, during, and after the cutover, and your stakeholders are held accountable for the communication protocol that you set.

In some cases, it might be necessary to group communication channels (for example, creating Slack groups for business units or closely-related applications). We recommend that you assign the responsibility of managing communications and messaging to a communication lead or migration manager.

**Note**
In advance of any cutover, it's a best practice to get buy-in from the migration team, wave owners, and application owners. Be sure to inform all application stakeholders about the cutover with sufficient notice.

The following table shows an example of high-level communication protocols for various communication channels.

|
|
| **Channel** | **Method** | **Owner** | **Frequency** |
| --- |--- |--- |--- |
| Senior stakeholders (internal) | Email | Program manager or cutover manager | Major events (for example, start and end dates) or confirmed P1 issues |
| Project/Technical team | Slack or Microsoft Teams chat room | All stakeholders responsible for posting updates about their activities<br />Program manager or cutover manager | All task start and end dates and delays |
| Data center monitoring teams/L1 ops | Briefing sessions and email | Program manager or cutover manager | Engagement start (four weeks out) with updates for each completed stage |
| Customer's senior stakeholders | Briefing sessions and email | Program manager or cutover manager | Engagement start (four weeks out) with updates for each completed stage |
| End customers | Email | Program manager or application owner | Start and end of cutover |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
