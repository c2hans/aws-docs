---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/preparing-organization.html
---

# Preparing the organization for a large migration
<a name="preparing-organization"></a>

For a large migration, your organization needs to scale up operational processes that directly or indirectly affect your ability to deliver the project on time and within budget. The following are key areas that you need to consider when preparing your organization:
+ [Tagging strategy](#tagging)
+ [Cloud operating model](#cloud-operating-model)
+ [Backup and administration](#backup)
+ [Hypercare period](#hypercare)
+ [Security](#security)
+ [Feeding the migration pipeline](#migration-pipeline)
+ [Global infrastructure support models](#support-models)
+ [Migration cutover](#cutover)

## Tagging strategy
<a name="tagging"></a>

Before starting a large migration, define and implement a *tagging strategy*. This is a best practice that helps you assign metadata to your AWS resources. For example, you can use tags to establish charge-back models, establish SLA requirements, or define backup needs. Commonly, the tags for each application must be determined directly by finance, operations, or the application owner. We recommend you define the tagging strategy before starting the migration and then collecting the information for each application as part of the wave planning process. This information can be difficult to collect if your organization doesn't have a well-curated configuration management database (CMDB), which is common. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) (AWS General Reference).

## Cloud operating model
<a name="cloud-operating-model"></a>

When you move your workloads to the cloud, you need a build a cloud operating model to support those services. Commonly, this means adding staff, such as a Cloud Ops team, to manage the cloud infrastructure and environment. In addition, you need to consider extending or replacing your on-premises support capabilities. Your cloud operating model should be designed to implement cloud-native best practices, such as the pillars of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/).

Another element of setting up the cloud operating model is defining standard operating procedures, or *runbooks*, for common, repeatable tasks in the cloud. This ensures that your staff is performing tasks in the same way, with the desired configurations, and according to best practices. Setting up runbooks before starting the migration is critical to a successful transition to the cloud.

Some managed service providers (MSPs) support new cloud operations models or offer services to establish an in-house model or a hybrid approach that uses both the MSP and in-house resources. Make sure that you define your policies, create your runbooks, and establish a sufficient knowledge-transfer process early in the large migration project.

## Backup and administration
<a name="backup"></a>

As workloads transition from the on-premises operating model to the cloud operating model, the Cloud Ops team needs to be prepared to support a defined backup and disaster recover (DR) strategy based on the requirements of each workload. It also must have the resources necessary to provide database administration (DBA) and application support capabilities. During the mobilize phase of the migration, we recommend that you establish an [operations workstream](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/operations.html) that is responsible for facilitating these outcomes. Application discovery should provide excellent insights to define these requirements and determine what kind of application support your application owners and teams need.

## Hypercare period
<a name="hypercare"></a>

After you have completed the cutover, the migrated applications and servers enter the hypercare period. In the hypercare period, the migration team manages and monitors the migrated applications in the cloud in order to address any issues. Typically, this period is 1–4 days in length. At the end of the hypercare period, the migration team transfers responsibility for the applications to the cloud operations (Cloud Ops) team. At this time, the wave is considered complete.

Define a process for handing off the workloads to the Cloud Ops team when the hypercare period is complete. In addition, as described in [Communication planning for a large migration](communication-planning.md), make sure that you have set up a communication process to notify application owners and other stakeholders when applications are entering or existing the hypercare period.

The following image shows an example of a hypercare process and the teams involved. Communications are built into this process to facilitate tasks and transfer ownership. After cutover, the application owner validates the migration was successful. They then notify the migration team and also communicate any concerns or issues that arise during the hypercare period directly to the migration team. When the hypercare period is complete, the migration team reviews the handoff checklist with the Cloud Ops team. The Cloud Ops team emails the application owners and other stakeholders to notify them that the hypercare period is complete. Application owners can then use the organization's service desk system to request ongoing support for the application.

![Workflow diagram of tasks and task owners during the cutover, hypercare, and ongoing support periods.](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/images/guide-img/0ce37e8e-2c4b-4da7-ad35-503caa83d254/images/a6ad3981-f4c2-4dae-b08c-257db6916ee9.png)

## Security
<a name="security"></a>

During the mobilize phase, the [security, risk, and compliance (SRC) workstream](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/security-risk-and-compliance.html) helps make sure that you have established a secure foundation in the AWS Cloud. This workstream can participate in or lead the [AWS Well-Architected Labs Security workshop](https://wellarchitectedlabs.com/security/) to make sure that you are implementing best practices. A key output of this workstream is helping the migration team understand the cybersecurity monitoring requirements and tools for the cloud environment and migrated workloads. Similar to the Cloud Ops team, it is common to create the cybersecurity team. This team supports the cloud transformation by providing the security processes, tools, and support resources. During the mobilize phase, the security workstream should define the required tools that must be installed on workloads and the AWS environment and identify any audits of the environment that must be completed before moving workloads. Delays in the audit process can impact your schedule. In addition, understand if the cybersecurity team is instituting any new processes, such as new single sign-on (SSO) capabilities, that might impact the readiness of some of the applications to be migrated. Coordinate the wave plans and security workstream schedule to ensure alignment with the sequence of activities.

## Feeding the migration pipeline
<a name="migration-pipeline"></a>

In the [migration factory](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/workflow.html), wave planning and migration occur at the same time and operate continuously. This allows for experience-based acceleration. The portfolio team feeds the migration pipeline by planning waves, and the migration team completes the pipeline by performing the migration and cutting over workloads. The portfolio team prepares five waves at the end of the initialization stage, and the implementation stage begins when the migration team begins migrating one or more of the prepared waves.

For each wave, the portfolio workstream runs 1–2 weeks, and the migration workstream typically runs 3–4 weeks. The portfolio workstream is five waves ahead of the migration workstream, so there is always a buffer between the portfolio and migration workstreams. Throughout the implementation stage, both the portfolio team and the migration team continue to process waves, and the buffer prevents the migration workstream from running out of servers to migrate. The following is an example of a wave schedule.

![Wave plan showing portfolio team preparing waves for the migration team.](http://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/images/guide-img/0ce37e8e-2c4b-4da7-ad35-503caa83d254/images/a9af9dc5-c35b-49ba-99b2-e068fa4dda3e.png)

The portfolio team prioritizes applications and then assigns them to waves in logical move groups. When planning waves, the portfolio team considers migration complexity, application similarities, and application and infrastructure dependencies. This helps make sure that the applications and their dependencies are migrated in their entirety. For more information about wave planning, see the [Portfolio playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/welcome.html). For project governance, you manage and track information about the waves and sprints, including the applications, servers, and application owners. You might use a dashboard on a Confluence site, a list in Microsoft Excel, or a combination of tools.

## Global infrastructure support models
<a name="support-models"></a>

As described in the [Understanding roles and responsibilities for a large migration](understanding-roles-responsibilities.md) chapter, you clearly define the tasks and task owners for the migration project. However, what this process will not identify is the key support processes that need to be in place before workloads are migrated to AWS. Support requirements might differ by region. If you have different support teams across multiple AWS Regions, you will need to determine who owns the responsibilities for each Region.

Additionally, other third parties might be responsible for backing up or supporting applications in the on-premises infrastructure, on behalf of the application owner. For these applications, make sure that your portfolio workstream captures this information during the discovery process, and make sure the Cloud Ops team is prepared to assume these responsibilities or has plans to arrange support through another means. If you don't identify these support models early, it is difficult to maintain a consistent pipeline of servers and applications within each wave, and the migration schedule can be impacted for an entire region.

## Migration cutover
<a name="cutover"></a>

Migration *cutover* is a finite window in which the source applications or servers are **cut** from on-premises infrastructure **over** to the AWS Cloud and go live. This is sometimes called a *migration party* because it involves so many participants and stakeholders. The migration lead starts the migration cutover call. The call ownership is then transferred to the project manager. After the Amazon Elastic Compute Cloud (Amazon EC2) instances are launched in AWS Application Migration Service, the infrastructure and application teams lead the call during the cutover validation phase. If your team is performing repetitive cutover tasks, we recommend you use [Cloud Migration Factory](https://aws.amazon.com/solutions/implementations/aws-cloudendure-migration-factory-solution/?did=sl_card&trk=sl_card) to cut over all servers in the migration wave.

For a typical template of activities that can be used to set expectations and drive migration cutover, see the *migration playbook templates* in the [Migration playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/welcome.html#about-components).
