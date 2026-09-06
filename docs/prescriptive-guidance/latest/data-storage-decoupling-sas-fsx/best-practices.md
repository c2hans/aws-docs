---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/best-practices.html
---

# Best practices
<a name="best-practices"></a>

We recommend the following best practices when you design your decoupled data architecture:
+ **Plan your data migration** – Develop a detailed plan on how to migrate data from a single production environment to a multi-environment setup early on in the design process. This can help you identify bottlenecks, reduce risks, and properly allocate the time and resources that are required for the migration.
+ **Keep the design simple and modular** – The example scenario in this guide is based on a multi-account architecture that uses three different AWS accounts. It's typically not necessary to use more than one AWS account per environment. We recommend that you place all infrastructure for the same environment in the same AWS account. Then, you can use the automation capabilities of AWS CDK to operationalize restore processes.
+ **Design your archicture to be secure and compliant** – We recommend that you design your architecture to meet the compliance and operational best practices required by your organization. For example, you can design your architecture to meet 21 CFR Part 11 electronic signature requirements.
+ **Minimize cost** – Throughput is a significant factor in the cost of a data migration. This is because SAS strongly recommends high I/O throughput from SAS servers to any file servers. We recommend that you review and assess these requirements for your unique use case.
+ **Simplify future operations and build resilience** – We recommend that you use FSx for Windows File Server to simplify your operations and build resilience. This is possible because FSx for Windows File Server offers the following benefits:
  + No patching, agents, or antivirus software required
  + No manual fail-over involved
  + Self-service recovery of deleted or corrupted data files for end users
  + Easier to share data across other potential data analysis applications and systems
  + Simplifies the management of servers (servers hold the application but data resides elsewhere)
