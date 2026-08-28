---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/team-org.html
---

# Team organization and composition
<a name="team-org"></a>

This section includes the following topics:
+ [Best practices for team organization and composition](#bp-team-org)
+ [Creating RACI matrices](#raci)
+ [Cloud Enablement Engine (CEE)](#cee)

## Best practices for team organization and composition
<a name="bp-team-org"></a>

Team composition in a large migration varies by organization and changes over the course of the project. The following are best practices that are common for all large migration projects:
+ **Identify a single-threaded technical leader at the project level and avoid silos** – Large migration projects often have multiple workstreams and teams, each team has different tasks and expected outcomes. A single-threaded leader at the project level is important because this leader makes sure all workstreams work together and stay connected. This helps prevent silos and boundaries. For example, the portfolio workstream needs to continuously send the migration metadata to the migration workstream to support the migration activities. Without a complete understanding of the required migration metadata, the output of the portfolio workstream might not work as an input for the migration workstream. A single-threaded leader helps coordinate the inputs and outputs of each workstream to help the migration run efficiently.
+ **Align all workstream-level outcomes with the project-level business outcomes**– Project-level business outcomes should be communicated to all workstream leaders before the migration starts. Each workstream leader must understand the role of their workstream and design their processes to support the project-level business outcomes. For example, if a project-level business outcome is exiting a data center in the next 12 months and speed is the most important factor, the workstream leaders should do the following:
  + All workstreams should prioritize rehost migrations, reduce the number of manual tasks, and add automation to improve the velocity.
  + The portfolio workstream should define standardized patterns and limit customizable patterns to reduce the amount of time required to design the target environment.
+ **Design workstreams based on project scope and stage – **Every migration project is different, and one size does not fit all. We recommend having four core workstreams for all large migration projects: migration workstream, portfolio workstream, project governance workstream, and foundation workstream. You might decide to create additional, supporting workstreams depending on your use case. For more information about workstreams, see [Workstreams in a large migration](workstreams.md). For example, if you have not yet designed the security guardrails in the mobilize phase, you need to create a security and compliance workstream that can define the security and compliance requirements before you start migrating. For more information about building the security guardrails in the mobilize phase, see [Security, risk and compliance](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/security-risk-compliance.html) in *Mobilize your organization to accelerate large-scale migrations*.
+ **Get the application team involved before the migration** – A large migration is never just an IT infrastructure project – it changes the operating model for your business. Involving the application team early and embedding the application owners into your large migration workstreams is critical to the success of large migration project. For example, during portfolio assessment, schedule your meetings early with application owners so that they can participate in the deep dive and help design their application's target state on AWS.
+ **Determine the team size based on workstreams and business outcomes** – Your expected business outcomes and migration strategies drive the size of each team, which is composed of smaller units called *pods*. In each workstream, you define teams for each migration strategy and then separate those teams into pods. For example, if rehost is your primary migration strategy, then you should have a rehost migration team that is composed of pods that contain 3­–5 people. When operating at peak velocity, a pod of 4­–5 people on a migration team can typically rehost up to 50 servers per week. This is approximately 200 servers per month or 2,500 servers per year. If your target is to rehost 100 servers per week, you should create two pods of 4–­5 people within the rehost migration team. If you are targeting less than 50 servers per week, you can reduce the size of the migration pod to 3 people. Replatform migrations usually cost more than rehost, and the same size pod can migrate up to 20 servers per week. The portfolio workstream is usually half the size of the migration workstream. You create additional teams and pods in each workstream to support each migration strategy. These recommendations assume that your migration resources are skilled and do not require significant training. The following table is an example of how you would divide the migration and portfolio workstreams into teams and pods for the rehost and replatform migration strategies. The following example assumes that you need to migrate 120 servers per week (100 rehost \+ 20 replatform) or 6,000 servers per year. This example is the maximum velocity. We recommend that you plan for additional resources in order to help prevent delays.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/team-org.html)
+ **Build a governance model in the early stage** – A large migration typically involves many people, including people from your own company, third-party software vendors, system integrators, or external consultants. Your project might include representatives from AWS, such as your account team, support engineers, or experts from AWS Professional Services. Your delivery model varies depending on your project scope and who you work with to deliver the project. For example, your project might include AWS or a system integrator, or you might include both. It is important to build a governance model early and create a RACI matrix that clearly defines the roles and responsibilities. As a recommendation, we also recommend creating a Cloud Enablement Engine (CEE), also known as *Cloud Center of Excellence*, in your organization and including representation from all parties. The key purpose of the CEE is to transform the organization from an on-premises operating model to a cloud-operating model. This centralized team is critical to the success of a large migration because it manages relationships, makes key decisions, and handles escalations throughout the project. The CEE is discussed in more detail later in this guide.

## Creating RACI matrices
<a name="raci"></a>

A large migration project typically involves a lot of people, so building a governance model is important to manage the project. One of the key components of a governance model is a RACI matrix, which is used to define the roles and responsibilities for all parties involved in the large migration. The name *RACI matrix* is derived from the four responsibility types defined in the matrix:
+ **Responsible (R)** – This role is responsible for performing the work to complete the task.
+ **Accountable (A)** – This role is held accountable for making sure the task is completed. This role is also responsible for ensuring the prerequisites are met and delegating the task to those who are responsible.
+ **Consulted (C)** – This role should be consulted for opinions or expertise on the task. Depending on the task, this responsibility type might not be required.
+ **Informed (I)** – This role should be kept up to date on the progress of the task and notified when the task is completed.

Because of the complexity of a large migration, we do not recommend using a single RACI matrix to document every task in the large migration. A multi-layer RACI matrix is a much more accessible approach. You start by building a high-level RACI matrix, and then you add more details to each section to build a detailed matrix. Building a detailed RACI matrix is not a one-off approach. You need to build new matrices or add more details to the existing ones as you progress through the portfolio and discover more migration strategies and patterns.

You can use the attached *RACI template* (Microsoft Excel format) as a starting point for building your own high-level and detailed RACI matrices. This template includes two examples of detailed RACI matrices, one for a rehost migration and another for a replatform migration. The tasks in these examples are included for sample purposes only, and you should customize these examples based on your use case.

### Build a high-level RACI matrix
<a name="build-a-high-level-raci-matrix.41286038-01ec-5d51-bf83-5ce8a3505075"></a>

Before you start building a high-level RACI matrix, you need to have the following information ready:
+ **Who are the high-level parties involved in this migration? **Identify any partners or consultants that will be involved in this project, such as AWS Professional services or system integrators. Consider whether any part of your current IT infrastructure is managed by an external partner. The following are examples of high-level parties:
  + Your organization
  + AWS Professional Services
  + System integrators
+ **What are the workstreams in your migration?** For more information, see [Workstreams in a large migration](workstreams.md). At a minimum, you should have the four core workstreams, and you can add support workstreams as needed for your project.
+ **What are the high-level tasks in your migration? **Create a list of the high-level tasks in your migration. The following are examples of high-level tasks:
  + Build an AWS landing zone
  + Perform portfolio assessment and collect migration metadata
  + Perform a rehost, replatform, or relocate migration
  + Perform application testing and cutover
  + Perform project management and governance tasks

Do the following to build your high-level RACI matrix:

1. Open the attached *RACI template* (Microsoft Excel format).

1. On the **High-level RACI** tab, in the first row, enter your organization name and any partners that you identified.

1. In the first column, enter the high-level tasks and workstreams that you identified.

1. In the matrix, determine which parties are responsible for each task as follows:
   + If a party is **responsible** for completing the task, enter an **R**.
   + If a party is **accountable** for completing the task, enter an **A**.
   + If a party should be **consulted** about the task, enter a **C**.
   + If a party should be **informed** about the task, enter an **I**.

The following table is an example of a high-level RACI matrix.

|
|
| Task | Your organization | Partner A | Partner B | Partner C |
| --- |--- |--- |--- |--- |
| Build an AWS landing zone | R/C | A | I | I |
| Perform portfolio assessment and wave planning | R/C | A | I | I |
| Perform rehost migration activities | C | C | R/A | I |
| Perform replatform migration activities | C | C | I | R/A |
| Project management and governance | R/C | A | I | I |
| Application changes and testing | C | R/A | C | C |
| Cloud operations | I | C | R/A | I |

### Build the detailed RACI matrices
<a name="build-the-detailed-raci-matrices.921b925d-ac0e-5df9-8160-b3fecc6d47c5"></a>

After creating the high-level RACI matrix, the next step is to create a detailed RACI for each high-level task and further refine the tasks, parties, and ownership. Before you start building detailed matrices, you need to have the following information ready:
+ **What are the detailed tasks in your migration? **After you have prepared the runbooks and task lists for your large migration project, the processes and details in these runbooks form the detailed layer of your RACI matrix. For example, for a rehost migration, detailed tasks might include installing a replication agent, verifying replication, and launching test instances for boot-up testing. If you haven't done so already, follow the instructions in the following playbooks to create these documents:
  + [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/)
  + [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/)
+ **What smaller teams make up each workstream and each high-level party?** For example, teams in your organization might include an application team, infrastructure team, operations team, networking team, or a project management office.

Do the following to build a detailed RACI matrix:

1. Open your high-level RACI matrix.

1. Create a copy of the **Detailed RACI (template)** spreadsheet.

1. Name the copied spreadsheet for a high-level task that you identified in *Build a high-level RACI matrix*.

1. In the first row, enter the names of the teams involved in this high-level task.

1. In the first column, enter the detailed tasks that you identified for this high-level task. You can group the detailed tasks into logical sequential groups, which helps readers navigate the matrix.

1. In the matrix, determine which teams are responsible for each task as follows:
   + If a team is **responsible** for completing the task, enter an **R**.
   + If a team is **accountable** for the task, enter an **A**.
   + If a team should be **consulted** about the task, enter a **C**.
   + If a team should be **informed** about the task, enter an **I**.

1. For each detailed task, confirm that only one team is responsible and only one team is accountable. If multiple teams are responsible or accountable, this can indicate that the task is not clearly defined or doesn't have clear ownership.

1. Share the detailed RACI matrix with the identified teams and confirm that all teams are familiar with their roles and responsibilities.

1. Repeat this process for each high-level task that you identified in Build a high-level RACI matrix.

For examples of detailed RACI matrices, see the **Rehost RACI** and **Replatform RACI** spreadsheets in the attached *RACI template*.

## Cloud Enablement Engine (CEE)
<a name="cee"></a>

### Best practices for using a CEE
<a name="best-practices-for-using-a-cee.0cbe2209-a125-5cd5-b21a-0591aad57d94"></a>

The purpose of a CEE is transforming an IT organization from an on-premises operating model to a cloud-operating model, and it is responsible for guiding the organization through the organizational and cultural changes. As a best practice, it is recommended that you establish a CEE for your large migration. The well-defined foundational processes and guard rails of a CEE can help you achieve the scale and velocity required for large migrations. For information about setting up a CEE, see [Cloud Enablement Engine: A Practical Guide](https://d1.awsstatic.com/whitepapers/cloud-enablement-engine-practical-guide.pdf). The following are additional recommendations and best practices for establishing a CEE for a large migration project:
+ The CEE team should be comprised of cross-functional leaders with the following qualities:
  + Have deep institutional knowledge
  + Have strong, long-standing internal relationships
  + Have a vested interest in the progress and success in the large migration
  + Are curious and want to learn
  + Are primarily or solely focused on the migration
+ The CEE team should be a mix of people who have worked together previously and newcomers who can provide fresh insights.
+ The CEE team should have strong executive support and alignment on the migration objectives.
+ Make sure the goals of the CEE team are specific to the large migration.
+ Conduct regular, open meetings that provide opportunities for questions and answers, demonstrate cloud services and architectures, and share updates on successful migrations and other wins.
+ The CEE team should be empowered to make critical decisions about the large migration project.

### Typical CEE roles and responsibilities for large migrations
<a name="typical-cee-roles-and-responsibilities-for-large-migrations.48646c7f-c2f0-5a53-a884-d96ff54385b9"></a>

The following table provides roles in a large-migration CEE team, and it describes the typical tasks and responsibilities for each role. The actual composition of your team and their responsibilities can vary based your use case, scope, and business objective.

|
|
| Roles | Tasks and responsibilities |
| --- |--- |
| Executive sponsor | + Managing escalations<br />+ Aligning the organization tightly around the objectives and criticality of the migration.<br />+ Serving as the voice of authority |
| Enterprise architect or project-level technical lead | + Identifying and documenting the reference architecture for known workload types<br />+ Designing and building migration processes for the entire project, across all workstreams<br />+ Serving as the single-threaded technical leader who makes sure all workstreams are collaborating and working to deliver the same business-level objectives<br />+ Strong institutional knowledge of major applications and common architectures |
| Project management office lead | + Managing timelines, onboarding, training, documentation, reporting, communication, and resource governance<br />+ Managing resourcing and training<br />+ Managing migration-related town halls |
| Migration lead | + Designing migration processes and tools<br />+ Designing migration strategies and automation<br />+ Overseeing migration cutovers and achieving the target velocity |
| Portfolio lead | + Designing portfolio assessment and wave planning processes and tools<br />+ Designing portfolio discovery and data collection processes<br />+ Overseeing the continuous supply of migration metadata and wave plans to the migration workstream |
| Cloud operations lead | + Designing the operating model for running workloads on AWS<br />+ Designing strategies for monitoring, incident response, tagging, business continuity, and disaster recovery strategies |
| Application team leader | + Managing the relationship with individual application owners<br />+ Managing migration planning and cutovers for their applications<br />+ Managing application changes, testing, and approvals |
| Network and infrastructure lead | + Designing the AWS landing zone for target accounts<br />+ Designing network connectivity and infrastructure<br />+ Designing and deploying security groups<br />+ Managing infrastructure and networking changes to support the large migration |
| Licensing lead | + Identifying all commercial off-the-shelf (COTS) and enterprise applications and working with the migration team and application team to plan migration strategies around licensing |
| Security and compliance lead | + Designing authentication and authorization for the large migration, including Active Directory, single sign-on, and IAM policies<br />+ Designing network security, including on-premises firewalls, and managing vulnerabilities<br />+ Designing compliance requirements for in-scope workloads |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
