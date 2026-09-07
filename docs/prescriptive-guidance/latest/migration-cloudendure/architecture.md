---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/architecture.html
---

# Architecture
<a name="architecture"></a>

CloudEndure Migration simplifies, expedites, and automates large-scale migrations to AWS. Continuous data replication takes place in the background, without application disruption or performance impact, which ensures that data is synchronized in real time and minimizes cutover windows. When you initiate migration cutover, CloudEndure runs a highly automated machine conversion and orchestration process, which reduces the potential for human error. After migration, even the most complex applications and databases run natively on AWS, without compatibility issues and with minimal IT skills necessary.  The following diagram illustrates the migration process.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/0c0a76d2-d326-4b6d-9e19-cd5f2a0e19da.png)

Benefits of using CloudEndure Migration include:
+ **Easy migration**  – You can run complex, large-scale migration projects rapidly, regardless of the application type, while significantly reducing risk.
+ **Increased uptime** – You can maintain normal business operations throughout the replication process. CloudEndure Migration copies source machines  continuously, without taking snapshots or writing any data to disks. This means that there is minimal performance impact and no need to reboot machines. Continuous replication also makes it easy to conduct non-disruptive tests and shortens cutover windows.
+ **Reduced costs** – CloudEndure Migration is a single tool for migrating any application or database from any source infrastructure on supported operating systems to AWS. You can migrate legacy applications, third-party applications, and line-of-business applications. There is no need to invest in specialized cloud development, operating system or application-specific skills, or significant IT resources, which results in greatly reduced operational costs.

Migrating your workloads by using CloudEndure Migration involves four phases of activities:

1. Preparing your environment. Includes setting up your CloudEndure account, creating AWS credentials, and configuring your network.

1. Migrating your workload. Includes installing CloudEndure Agents and replicating your source environment in the AWS staging area.

1. Testing the migration. Includes verifying the target machine settings and validating that the target machines are operating correctly.

1. Cutting over to AWS. CloudEndure Migration automatically converts your machines to run natively on AWS.

These phases are illustrated in the following diagram and described in detail in the following sections.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/d54335cc-e4f5-4d9e-b1eb-9e1fc44bfad6.png)
