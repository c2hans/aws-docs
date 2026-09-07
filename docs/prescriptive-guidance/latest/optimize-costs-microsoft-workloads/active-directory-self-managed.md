---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-self-managed.html
---

# Self-managed Active Directory on Amazon EC2
<a name="active-directory-self-managed"></a>

## Overview
<a name="active-directory-self-managed-overview"></a>

This section provides recommendations for reducing the cost of running Active Directory on Amazon Elastic Compute Cloud (Amazon EC2). The primary focus is on making sure that you can size the Active Directory domain controllers appropriately and use the flexibility of the AWS Cloud to adjust as needed for your environment. AWS can help you easily stop an instance and resize it to meet your changing needs, or downsize the instance if you scale up too fast. Choosing the right instance size and type can result in significant savings.

## Cost impact
<a name="active-directory-self-managed-cost-impact"></a>

The following table shows the difference between choosing a burstable instance family instance over a general purpose instance. This choice can save you a considerable amount of money each month. Appropriate planning and sizing of your instance can help you to manage costs.

|
|
| Instance type | Number of instances | vCPU | Memory | Cost |
| --- |--- |--- |--- |--- |
| t3a.medium | 2 | 2 | 8 | $81.76/month |
| m5a.large | 2 | 2 | 8 | $259.88/month |

For more information about costs, see the AWS Pricing Calculator [estimate](https://calculator.aws/#/estimate?id=46db184a3e7cad0a089d0cc5b1f7435576192cbc).

A savings of $178.12 per month ends up being over $2,000 in savings per year for your domain controllers. Keep in mind that is for a small footprint of just two domain controllers in one account. At scale with multiple accounts and additional domain controllers, such savings can add up to a significant cost reduction.

## Cost optimization recommendations
<a name="active-directory-self-managed-recommendations"></a>

Microsoft provides [capacity planning recommendations](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/capacity-planning-for-active-directory-domain-services) for when you're deploying your Active Directory environment. We recommend that you take the following main components into consideration when you plan or scale your Active Directory environment:
+ Memory
+ Network
+ Storage
+ Processor

While keeping these main components in mind, you can work through selecting an instance type that makes sense for your Active Directory environment on AWS. This section covers a few example Active Directory to AWS deployment scenarios. These scenarios make it clear that it's not necessary to replicate your on-premises environment in AWS, if you don't plan to handle the same number of users and computers as you do in your on-premises environment.

The following table highlights important components regarding vCPU, memory, and disk for your AWS footprint.

|
|
| Component | Estimates |
| --- |--- |
| Storage/database size | 40–60 KB for each user |
| RAM | Database size<br />Base operating system recommendations<br />Third-party applications |
| Network | 1 GB |
| CPU | 1,000 concurrent users for each core |

### Hybrid deployment scenario
<a name="hybrid-deployment-scenario.259d8f57-4020-5f35-8b72-4a7d84d3a8f1"></a>

The following diagram shows an example architecture for a hybrid deployment of Active Directory.

![Architecture for hybrid deployment of Active Directory](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/107146a1-157e-4295-8bb2-d4c5457285ae.png)

As the diagram shows, you typically have an on-premises footprint and then expand this into the AWS Cloud. In the initial phases of a migration, you typically won't have all your users and servers deployed in AWS. That's why it's important to initially deploy a smaller sized footprint to save money on the migration efforts.

If you're going to maintain an on-premises footprint with servers and users authenticating on premises, then you won't need the same footprint for domain controllers in AWS. By following Active Directory best practices, you can implement proper [Active Directory sites and services](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/multisite/configure/step-2-configure-the-multisite-infrastructure) to authenticate users and computers to your on-premises footprint, while only authenticating your AWS footprint to the domain controllers in AWS. This enables you to avoid oversizing your Active Directory footprint on AWS by limiting the use to just AWS resources and not all of your on-premises infrastructure. For guidance designing a hybrid setup, see [Proper placement of domain controllers and site considerations](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/site-definition-considerations) in the Microsoft documentation.

### Optimize for an AWS migration by right sizing
<a name="optimize-for-an-9999999999999999aws--migration-by-right-sizing.0766f35d-4e70-5575-9fae-ea61ba23a825"></a>

If you're deploying a new instance of Active Directory for your users or plan to fully migrate to AWS for your Active Directory infrastructure, we recommend that you plan the sizing against Microsoft's recommendations for vCPU, memory, and disk space for the instances choice in the preceding table.

If this is a new footprint, you can start small and take advantage of the ability to easily [change instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) to resize your environment as it grows on AWS. The [Windows on Amazon EC2](windows-ec2.md) section of this guide shows you how to monitor and review your CPU and memory utilization on AWS. That way, you know when to increase size of your EC2 instance.

If you're fully migrating your on-premises Active Directory environment to AWS, you can implement the same sizing plans to ensure proper performance. Before duplicating what you have on premises in AWS, we recommend that you complete a thorough review of your Active Directory environment. This can help you prevent overprovisioning. Be sure to use Performance Monitor to collect information about the amount of traffic and utilization for your existing domain controllers. This can give you an understanding of the overall usage so that you can right size and ultimately reduce your costs.

### Optimize Active Directory on AWS
<a name="optimize-active-directory-on-9999999999999999aws-.0e69580d-b0ea-58cf-9af8-700e81efecd5"></a>

If you're running Active Directory on AWS, it's important to also continuously monitor utilization and change instance sizes as needed to reduce your spending. You can use AWS Compute Optimizer to get information about the resources that you're running in AWS. For information about using Compute Optimizer to right size your Windows workloads, see the [Windows on Amazon EC2](windows-ec2.md) section of this guide. For a more comprehensive deep dive, you can use Performance Monitor to monitor the utilization of your Active Directory domain controllers, assess performance, and then resize accordingly.

You can also use CloudWatch to monitor the performance of domain controllers. To optimize your domain controllers (scaling up or down), you can use the metrics available in CloudWatch to help you make the right decisions. You can use the CloudWatch agent to configure custom Performance Monitor metrics to be sent for data collection. For instructions, see [How can I use the CloudWatch agent to view metrics for Performance Monitor on a Windows server?](https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows) in the AWS Knowledge Center.

After you deploy the CloudWatch agent, you can configure the following metrics within the agent configuration file under `metrics_collected`:

|
|
| Metric category | Metric name |
| --- |--- |
| Database to instances (NTDSA) | Database cache % hit |
| I/O database reads average latency |  |
| I/O database reads/sec |  |
| I/O log writes average latency |  |
| DirectoryServices (NTDS) | LDAP bind time |
| DRA pending replication operations |  |
| DRA pending replication synchronizations |  |
| DNS | Recursive queries/sec |
| Recursive query failure/sec |  |
| TCP query received/sec |  |
| Total query received/sec |  |
| Total response sent/sec |  |
| UDP query received/sec |  |
| LogicalDisk | Avg. disk queue length |
| % free space |  |
| Memory | % committed bytes in use |
| Long-term average standby cache lifetime(s) |  |
| Network interface | Bytes sent/sec |
| Bytes Received/sec |  |
| Current bandwidth |  |
| NTDS | ATQ estimated queue delay |
| ATQ request latency |  |
| DS directory reads/sec |  |
| DS directory searches/sec |  |
| DS directory writes/sec |  |
| LDAP client sessions |  |
| LDAP searches/sec |  |
| LDAP successful binds/sec |  |
| Processor | % processor time |
| Security system-wide statistics | Kerberos authentications |
| NTLM authentications |  |

## Additional resources
<a name="active-directory-self-managed-resources"></a>
+ [Active Directory Domain Services on AWS: Partner Solution Deployment Guide](https://aws-quickstart.github.io/quickstart-microsoft-activedirectory/) (AWS documentation)
+ [Capacity planning for Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/capacity-planning-for-active-directory-domain-services) (Microsoft documentation)
+ [Design considerations for running Active Directory on EC2 instances](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/design-considerations-for-running-active-directory-on-ec2-instances.html) (AWS Whitepapers)
