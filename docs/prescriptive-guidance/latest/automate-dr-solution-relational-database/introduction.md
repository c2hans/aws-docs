---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/introduction.html
---

# Automate your DR solution for relational databases on AWS
<a name="introduction"></a>

*Jitendra Kumar, Pavithra Balasubramanian, and Oliver Francis, Amazon Web Services*

When planning a [disaster recovery (DR) strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/welcome.html) on Amazon Web Services (AWS), you can implement a DR solution for the databases in your organization. You can automate the DR solution by configuring an event-driven architecture to perform the failover of the database instances. The benefits of this approach include the following:
+ Reducing human errors caused by manual coordination
+ Providing the shortest possible recovery time objective (RTO) in some cases
+ Facilitating repeatable testing of your DR solution

Without automation, an outage in your primary AWS Region, would require resources in your organization to manually perform steps in a run-book. Those steps might include multiple processes, such as promoting Amazon Relational Database Service (Amazon RDS) read replicas in the secondary AWS Region to serve as the new primary database instance. AWS provides [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) APIs to automate these actions, which can form the building blocks of a DR solution for your organization's needs.

This guide discusses a centralized, manifest-driven DR orchestrator which can help you achieve a DR solution for AWS databases across AWS Regions within the same AWS account. The decision to perform a failover would still need human intervention and is out of scope for the automation.

The target audiences for this guide are application architects, infrastructure architects, database architects and database consultants.

## Objectives
<a name="objectives"></a>

Implementing the DR Orchestrator Framework solution can help you achieve the following outcomes:
+ **Reduce manual errors during an outage** – Manual performance of DR processes can be prone to errors. Automating actions during the phases of a DR activity reduces the manual errors and helps to ensure a smoother failover or failback.
+ **Manage DR at scale** – If your organization has a large fleet of databases, building automation for DR helps you scale your DR solution. You can automate your AWS database DR solution by using DR Orchestrator Framework. DR Orchestrator automates the steps for failover or failback of AWS databases by using a parameter file in JSON format.
