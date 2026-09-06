---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-directory-service-for-microsoft-ad-well-architected-analysis/reliability-pillar.html
---

# Reliability pillar
<a name="reliability-pillar"></a>

The reliability pillar focuses on workloads performing their intended functions and how they can recover quickly from failure to meet demands. The following recommendations can help you meet the reliability design principles and architectural best practices for AWS Managed Microsoft AD.

**Key focus areas**
+ Distributed system design
+ Recovery planning
+ Adapting to changing requirements

## Automatically recover from failure
<a name="automatically-recover-from-failure"></a>
+ Make sure that your IP subnet allocation accounts for expansion and availability.
+ Activate multi-Regional replication. For more information, see [Lab 4 – Enable Multi-Region with AWS Managed Microsoft AD](https://catalog.us-east-1.prod.workshops.aws/workshops/b4a4be0e-d4f9-4ff5-af82-ebfb86dbe46a/en-US/2-extending-aws-managed-microsoft-ad/multi) in the Active Directory on AWS Immersion Day Workshop.

## Test recovery procedures
<a name="test-recovery-procedures"></a>
+ Practice restoring the directory from a snapshot. For more information, see [Restoring your directory from a snapshot](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_snapshots.html#snapshot_restore) and [Creating a snapshot of your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_snapshots.html#snapshot_create) in the AWS Directory Service documentation.

## Scale horizontally to increase aggregate workload availability, and don't guess capacity
<a name="scale-horizontally"></a>
+ Automate AWS Managed Microsoft AD scaling based on utilization metrics. For more information, see [How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/) on the AWS Blog.
+ Load test before rolling changes out to production. For more information, see [How to use the Active Directory Performance Testing Tool on Windows Server 2012](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/how-to-use-the-active-directory-performance-testing-tool-on-windows-server-2012/256937) on the Microsoft Blog.

## Manage change in automation
<a name="manage-change-in-automation"></a>
+ Apply infrastructure as a code (IaC) to deploy AWS Managed Microsoft AD. For more information, see the GitHub [quickstart-microsoft-activedirectory](https://github.com/aws-quickstart/quickstart-microsoft-activedirectory)
+ Automate Microsoft Active Directory operations procedures whenever possible. For example, it's a best practice to automate the management of user objects, group objects, and Group Policy Objects (GPOs).

## Manage quotas and constraints
<a name="manage-quotas"></a>
+ Monitor and manage AWS Managed Microsoft AD quotas. For more information, watch the [View and manage quotas for AWS services using service quotas](https://www.youtube.com/watch?v=ZTwfIIf35Wc) video on the AWS YouTube channel.
+ Make sure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover.
+ Accommodate fixed service quotas and constraints through your architecture.
