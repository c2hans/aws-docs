---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/overview.html
---

# Overview
<a name="overview"></a>

The AWS migration approach for SAP workloads consists of four phases: assess, mobilize, migrate, and optimize. The methodology has been tailored to meet AWS customers' needs and contains specific actions with predefined inputs and outputs. The following diagram illustrates these phases, which are discussed in detail in subsequent sections.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/13dd554d-3a2a-4047-982c-002929a91c6a.png)

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

By working back from your specific requirements and by customizing the methodology, you can refine the migration strategy, business case, scope, sequencing of SAP workloads, and scheduling of the work that is required in order to successfully complete your SAP migration objectives.

We recommend using automation and infrastructure as code (IaC) for SAP deployments on AWS to enable the requisite speed and consistency to support a mass migration at scale. The latest tools and techniques are described in technical detail in the documents and blog posts listed in the [Resources](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/resources.html) section. AWS is consistently advancing and improving its services, techniques, and methodologies to offer you more benefits and options for meeting your business objectives, so we recommend that you always check the AWS website for the latest information.

As you migrate your SAP workloads, you should also work closely with your non-SAP migration teams to align the migration of applications that are integrated into SAP, and to minimize downtime and potential business disruption. Treat each cluster of coupled applications as a project with dedicated teams. You can divide each cluster of SAP applications into sequential waves, so each cluster can be delivered with a high degree of parallelism, as discussed in the next section. This approach helps you meet your migration schedule and ensures that time to value is minimal, your business case is maximized, and you can gain benefits as early as possible. The objective is to make your business more effective by increasing agility, availability, and resilience while reducing the costs of both operations and infrastructure. Moving your SAP workloads to the cloud also enables you to innovate, drive your digital S/4HANA transformation, and enable data analytics. The following diagram illustrates these business outcomes.

![Targeted business outcomes of migrating SAP to AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/3af52783-fd63-4f87-b6aa-d793198c3080.png)

For more information, find out how Engie used AWS Professional Services and AWS Partners in their SAP migration, as part of a wider [digital SAP S/4HANA transformation of their financial processes.](https://aws.amazon.com/solutions/case-studies/engie/?did=cr_card&trk=cr_card)

## Parallel migration waves
<a name="parallel-migration-waves"></a>

If you have a large and highly complex SAP application estate, AWS often proposes a migration that is split into distinct waves and coordinated with separate migration teams. The goal is to maintain the acceleration, momentum, and consistency of the migration effort while concurrently keeping each wave a manageable size from a resource and complexity perspective. The following chart illustrates a highly parallelized migration phase that is based on the geographical clustering of SAP workloads.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/00ab0570-37b9-43df-9a7d-11c5ff4a5ad2.png)

You can fine-tune this approach by factoring in your business objectives, worldwide and business division operating calendars, business cycle, the state of your current infrastructure, and the availability and capacity of your own and AWS Partner resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
