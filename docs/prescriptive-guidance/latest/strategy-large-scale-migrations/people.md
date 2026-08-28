---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/people.html
---

# People perspective
<a name="people"></a>

This section focuses on the following key areas of the people perspective:
+ [Executive support](#executive-support) - Identifying a single-threaded leader who's empowered to make decisions
+ [Team collaboration and ownership](#team-collab-ownership) - Collaborating among various teams
+ [Training](#training) - Proactively training teams on the various tooling

## Executive support
<a name="executive-support"></a>

In this section:
+ Identify a single-threaded leader
+ Align the senior leadership team

### Identify a single-threaded leader
<a name="identify-a-single-threaded-leader.6f721890-5f4f-5ab3-a507-e984678348cf"></a>

When starting a large migration, it's important to identify a single-threaded technical leader who is 100 percent dedicated to the project and accountable. That leader is empowered to make decisions, help avoid silos, and streamline work-streams by maintaining consistent priorities.

A large migration global customer was able to scale from one server each week at the outset of the program to more than 80 servers each week at the start of the second month. The CIO's full support as a single-threaded leader was critical to the rapid scale up of servers being migrated. The CIO attended weekly migration cutover calls with the migration team to ensure real-time escalation and resolution of issues, which accelerated the migration velocity.

### Align the senior leadership team
<a name="align-the-senior-leadership-team.9654f44b-fea1-5b26-8043-959b6a76668b"></a>

It's important to create alignment between the various teams regarding the success criteria of the migration. While migration planning and implementation can be accomplished by a small, dedicated team, challenges arise when defining the strategy and performing peripheral activities. These potential obstacles might require actions or escalations from different areas of the IT organization, including the following:
+ Business
+ Applications
+ Networking
+ Security
+ Infrastructure
+ Third-party vendors

Direct action from application owners, leadership, alignment, and a clear escalation to the single-threaded leader become important.

## Team collaboration and ownership
<a name="team-collab-ownership"></a>

In this section:
+ Create a cross-functional team cloud-enablement team
+ Define requirements for teams and individuals outside the core migration team in advance
+ Validate that there are no licensing issues when migrating workloads

### Create a cross-functional cloud-enablement team
<a name="create-a-cross-functional-cloud-enablement-team.43de006e-89cd-5eca-a95e-b7b33f210ca6"></a>

A critical first step in a large migration project is to enable the organization to work in the cloud.  To accomplish this, we recommend building a [Cloud Enablement Engine](https://d1.awsstatic.com/whitepapers/cloud-enablement-engine-practical-guide.pdf) (CEE). The CEE is an empowered and accountable team focused on  organization's operational readiness for migrations to AWS. The CEE should be a cross-functional team that includes representation from infrastructure, applications, operations, and security. The team is charged with the following responsibilities:
+ Developing policies
+ Defining and implementing tools, processes and the architectures that will establish the organizations cloud operations model
+ Continuing to facilitate stakeholder alignment across all the areas that they represent

One healthcare customer didn't start with a CEE. However, through initial pilot migrations, the gap was identified. Leading up to the final migration cutover date, with stringent deadlines in place, the team implemented a *migration war room.* In the migration war room, stakeholders from infrastructure, security, applications, and business could assist in resolving issues.

### Define requirements for teams and individuals outside the core migration team in advance
<a name="define-requirements-for-teams-and-individuals-outside-the-core-migration-team-in-advance.87acb99e-0e9f-5377-9db1-e7f9d00d21f3"></a>

Identify teams and individuals that are outside the core program, and define their involvement during the migration planning phases. To facilitate the momentum of the migration during the later stages, pay specific attention to the application teams' involvement. Their knowledge of the application, ability to diagnose issues, and requirement to sign off on the cutover will be required.

While the migration will be led by a core team, the application teams will likely be involved in validating the migration plan and testing during cutover. Customers often approach the cloud migration as an infrastructure project, instead of as an application migration. This can lead to issues during the migration.

We recommend considering the application team's required involvement when selecting a migration strategy. For example, a rehost strategy requires less application-team involvement compared with a replatform or refactor strategy in which more of the application landscape is being changed. If application owner availability is limited, consider using rehost or replatform as opposed to the refactor, relocate, or repurchase strategies.

### Validate that there are no licensing issues when migrating workloads
<a name="validate-that-there-are-no-licensing-issues-when-migrating-workloads.5ee90256-c36c-5ffb-8eae-f6d3d60d20d5"></a>

Licensing might change when you migrate corporate off–the-shelf products to the cloud. Your license agreements might be focused on your on-premises estate. For example, a license might be by CPU or linked to a specific MAC address. Alternatively, license agreements might not include the right to host in a public cloud environment. However, renegotiating licensing with vendors can include long lead times and presents a hard blocker for the migration.

We recommend collaborating with your sourcing or vendor management teams as soon as the scope of the migration is defined. Licensing might also influence your target architecture and migration patterns.

## Training
<a name="training"></a>

After the migration strategy is defined, invest time in understanding what training might be required for the migration and for your target operating model. During the migration, you will likely use tooling, such as AWS Database Migration Service (AWS DMS), that is new to your organization. Proactively training teams reduces the delays experienced during the migration phases.

We recommend seeking active knowledge transfer methods that provide an opportunity to experiment with the tooling in a hands-on fashion. As an example, AWS Professional Services provided several Cloud Migration Factory training sessions for three systems integrator (SI) AWS Partners responsible for a large migration. This ensured that the team had basic familiarity as it moved into the migration phase. It also helped identify subject matter experts (SMEs) who could serve as first-line escalation within each SI AWS Partner team.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
