---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/disaster-recovery-implementation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Disaster recovery implementation
<a name="disaster-recovery-implementation"></a>

 The following section explains how to implement an AWS disaster recovery solution, including grouping the application into waves, performing drills, and maintaining the solution.

## Grouping applications into waves
<a name="grouping-applications-into-waves"></a>

 Divide your applications into waves. Each wave should include applications that are designed to work together so that every wave can be tested individually without being obstructed by dependencies on resources that are allocated to future waves. By implementing disaster recovery in waves, any issues that arise will have limited impact, and the implementation project will be easier to manage.

 Make sure that the first several waves are smaller in size (10-20 servers per wave) as the implementation of these waves may take more effort and be slower due to lack of familiarity with the solutions. Once the team feels comfortable with the methodology and tools, the size of the waves can be increased according to the desired rate of progress and available resources. Large-scale disaster recovery projects usually include 100-200 servers in each wave.

## Configuration of staging area
<a name="configuration-of-staging-area"></a>

 Before the implementation of the first wave, the staging area subnets should be created for all of the waves. We recommend using dedicated subnets for the staging areas. This allows setting up the needed connectivity without interfering with any other processes. This also helps prevent existing resources from competing over private IP addresses with the resources automatically provisioned by the disaster recovery solutions.

## Using multiple AWS accounts
<a name="using-multiple-aws-accounts"></a>

 You can use multiple AWS accounts for staging areas and recovery sites (used for failover and drills). AWS accounts have API throttling, so replicating more than 300 servers to a staging area subnet in a single AWS account is not recommended. In these cases, multiple AWS accounts should be used. You can fail over servers that are using different AWS accounts for staging areas into the same recovery AWS account.

 Due to AWS API throttling and based on AWS best practices, we recommend using dedicated AWS accounts for the staging areas as any additional activity in the staging AWS accounts (especially automated tools) may compete with incoming automated disaster recovery activities and may cause API throttling.

 In general, the replication subnets (staging area) and the recovery subnets (disaster recovery site) of an application don't have to be in the same AWS account. This provides flexibility when designing the AWS account architecture for disaster recovery.

## Networking considerations
<a name="networking-considerations"></a>

 While performing a disaster recovery drill, AWS recommends that you isolate the recovery subnets to prevent potential conflicts with the source location. Isolation can be done by using route rules, network access control list (network ACL) rules, or by associating restrictive security groups when launching the applications for drills.

 If you are using Elastic Disaster Recovery, there are three points of interaction between the service components:
+  The AWS Replication Agent needs to communicate with the Elastic Disaster Recovery and Amazon S3 endpoints in your recovery AWS Region.
+  The AWS Replication Agent needs to communicate with the Elastic Disaster Recovery Replication Servers in the staging area subnet.
+  The Elastic Disaster Recovery Replication Servers need to communicate with the Elastic Disaster Recovery and Amazon S3 endpoints in your recovery AWS Region.

 It’s important to define how the applications will be divided between different AWS accounts, whether the applications will be in the organization’s main AWS account or in different AWS accounts due to organizational policies.

## Mapping application structure
<a name="mapping-application-structure"></a>

 For each wave, the following components need to be analyzed:
+  **Networks** – The networks that the components are located in need to be analyzed and documented. This includes the classless inter-domain routing (CIDR) of each network, a map of the components of the networks, the IP addresses of each component in each network, and the security group configuration that each failed over server should be using.
+  **Server configuration** – Every server that participates in a wave needs its central processing unit (CPU) and random-access memory (RAM) information recorded to validate that the [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) instances that Elastic Disaster Recovery launches during drills and recovery will have enough resources to work. Elastic Disaster Recovery selects a right-sized EC2 instance type based on your source server’s operating system, CPU, and RAM. However, it is recommended that you verify the selection logic.

 Using the results of the mapping described previously, you can build the disaster recovery site environment that will be used to recover your servers and other application components in case of a disaster or drill.

## General process for each wave
<a name="general-process-for-each-wave"></a>

 AWS suggests sprints of one to two weeks for each wave. The recommended process for each wave is as follows:

1.  **Define replication settings –** Your replication settings include configuring your staging area subnets and security groups (both based on the networking analysis described earlier), and additional settings that determine how data will be replicated from your source servers to AWS. You can make changes to these settings at any time, for individual servers or a group of servers.

1.  **Agent installation –** Install the AWS Replication Agent on all the servers and confirm that replication has started successfully.

1.  **Launch settings configuration –** After replication has started successfully for all the servers in the wave, configure launch settings for each server to define how your drill and recovery instances will be launched on AWS. These settings include configuring the subnet within which instances will be launched, Amazon EC2 instance types, and license transfers.

1.  **Testing –** Every time a server or a group of servers has reached Continuous Data Protection (indicated in the console as “Ready for recovery” and “Healthy” data replication status), run a sanity launch for the group to make sure that each drill instance has launched and booted successfully in AWS (the server has reached 2/2 status check in the Amazon EC2 Console).

    It’s important that all the drill launches (tests conducted during implementation as well as periodic drills) are launched into isolated subnets to make sure they don’t interfere with the source applications.

    Note that for every staging area subnet that you set up, the first wave may uncover configuration issues and the effort required to correct these issues should be considered when planning the wave.

1.  **Clean up –** By default, Elastic Disaster Recovery removes any resources created during drills, either when requested by the user or when a new drill instance is launched.

## First disaster recovery drill
<a name="first-disaster-recovery-drill"></a>

 After the implementation of all the waves is finished, run a formal disaster recovery drill to validate the drill section of the disaster recovery plan and to make sure nothing was missed during implementation. Finding and correcting issues during a full disaster recovery drill is more expensive and labor intensive than fixing issues during the implementation phase. Therefore, it’s important to run the first comprehensive disaster recovery drill only after the implementation is finished — including test launches of all servers.

 AWS recommends that you isolate the recovery subnets before performing any drill (including the first one), to avoid potential conflicts with the source environment.

 Isolating launched applications is a drill methodology that enables you to continue operating the production site uninterrupted during drills, to lower risks in case the drill does not go as expected.

 A successful first disaster recovery drill is the beginning of the maintenance phase.

## Maintenance
<a name="maintenance"></a>

 A disaster recovery solution requires regular maintenance after implementation in order to ensure that it will work as expected during a disaster.

 The two main parts of maintaining a disaster recovery solution are monitoring and periodic drills that should be performed as frequently as possible while taking the business goals and limitations into account.

## Monitoring
<a name="monitoring"></a>

 There are multiple methods for monitoring your disaster recovery solution:

## Built-in monitoring capabilities
<a name="built-in-monitoring-capabilities"></a>

 Some services, such as Elastic Disaster Recovery, have several basic monitoring features. For example, after you add source servers to Elastic Disaster Recovery, you can monitor and interact with them from the [Source Servers](https://docs.aws.amazon.com/drs/latest/userguide/source-servers.html) page. The Source Servers page is the default view in the Elastic Disaster Recovery Console. On the Source Servers page, you can view all of your source servers, monitor their recovery readiness and data replication state, view the last recovery result, view any pending actions, and sort your servers by a variety of categories. These built-in monitoring capabilities provide a general impression of the health of your disaster recovery solution.

## Using AWS services for AWS Elastic Disaster Recovery monitoring
<a name="using-aws-services-for-aws-elastic-disaster-recovery-monitoring"></a>

 Ongoing monitoring for replication metrics, including receiving alerts and status updates, should be a high priority for limiting downtime and maintaining your disaster readiness.

 One of the ways you can monitor Elastic Disaster Recovery is by configuring an [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboard to monitor the AWS resources you use for disaster recovery. Amazon CloudWatch is a monitoring and observability service that provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, and optimize resource utilization. Creating a CloudWatch dashboard can give you a single operational overview of your Elastic Disaster Recovery operations.

 You can use built-in CloudWatch widgets to populate your disaster recovery dashboard, including metrics to visualize bandwidth consumption, network throughput, security, and server replication metrics. For example, you can use CloudWatch to:
+  Monitor source server replication metrics such as lag duration and backlog. This can help you identify and remediate replication issues, so that your RPO remains as expected.
+  Monitor Replication Server metrics such as CPU utilization, input/output (I/O) characteristics, and network throughput. These metrics can help you determine whether to optimize Replication Server EC2 instance sizes or [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) disk types.
+  Monitor drill and recovery launch metrics, such as the amount of time since the last drill or recovery instance was launched. This helps validate that you are performing drills with the frequency defined by your disaster runbooks.

![This image shows an example CloudWatch dashboard for Elastic Disaster Recovery monitoring.](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/images/examplecloudwatchdashboardforelasticdisasterrecoverymonitoring.png)

 You can also use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to create rules for Elastic Disaster Recovery events you want to monitor, and configure notification alerts using [Amazon Simple Notification Service](https://aws.amazon.com/sns) (Amazon SNS). For example, you can configure Amazon SNS notifications for an EventBridge rule to notify you in the event that replication has stalled for any source servers. Doing so can help your teams quickly identify and address replication issues that could affect RPO and RTO if you need to recover these servers.

 For a detailed walkthrough of how to create a CloudWatch dashboard for Elastic Disaster Recovery monitoring and how to use EventBridge and Amazon SNS to receive alerts, refer to [Disaster recovery monitoring of AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/storage/disaster-recovery-monitoring-of-aws-elastic-disaster-recovery/).

## Implementing monitoring using the APIs of AWS services
<a name="implementing-monitoring-using-the-apis-of-aws-services"></a>

 For the best customization and granularity of monitoring, you can use the APIs of the AWS services you are using for disaster recovery (for example, [Elastic Disaster Recovery APIs](https://docs.aws.amazon.com/drs/latest/APIReference/Welcome.html)). Using these APIs, most notably the DescribeSourceServers API that returns all the data about replicating servers, you can build your own monitoring solution to track any data that the Elastic Disaster Recovery service contains. Using APIs for monitoring is meant for advanced user customizations because it enables you to choose the exact data you want to monitor and define triggers and alerts for your specific needs.

## Drills
<a name="drills"></a>

 Performing periodic drills is the only way to gain confidence that a disaster recovery solution will provide business continuity within the desired RTO and RPO for each application and that the disaster run books are accurate. The more frequently drills are performed, the higher the level of confidence. However, every drill has costs associated with it, including workforce costs and the cost of launched resources on AWS. Therefore, every organization needs to decide for itself the frequency of drills for each application. Industry best practice is to conduct a disaster recovery drill no less than once per year and for the more business-critical applications, no less than once per quarter.

## Performing drills
<a name="performing-drills"></a>

 AWS disaster recovery-related services facilitate frequent drills because they provide a simple mechanism for testing the recovery of your source environment at scale, without performance impact on your source applications.

## How Elastic Disaster Recovery drills work
<a name="how-elastic-disaster-recovery-drills-work"></a>

 During normal business operation, Elastic Disaster Recovery continuously replicates data on your source servers to a low-cost staging area in your AWS account. When you launch source servers for drills or recovery, Elastic Disaster Recovery automates source server conversion, so your recovered applications run natively on AWS. Drills are non-disruptive and do not impact your source servers or ongoing data replication. The instances you launch during Elastic Disaster Recovery drills will operate in the same way on AWS as the instances you launch for recovery on AWS.

 When you launch drill instances for disaster recovery drills, you are launching a copy of your servers in your recovery AWS Region from a point in time that you select. You can perform secure drills in isolated subnets configured in your Elastic Disaster Recovery [launch settings](https://docs.aws.amazon.com/drs/latest/userguide/launch-settings.html), which define the settings and configuration of your launched drill instances. Your launch settings and EC2 launch template enable you to isolate your drill instances by using a separate subnet or different security groups to avoid network conflicts. You can also launch drill instances in a [separate AWS account](https://docs.aws.amazon.com/drs/latest/userguide/multi-account.html) to further isolate your drill and production environments. Elastic Disaster Recovery automates provisioning the resources needed to launch your instances on AWS.

 You can use Elastic Disaster Recovery to run a virtually unlimited number of drills, as often as you choose. There are [no additional fees for drills](https://aws.amazon.com/disaster-recovery/pricing/), beyond payment for the provisioned resources generated. You can minimize costs by performing some disaster recovery drills using smaller Amazon EC2 instances, instead of fully provisioning resources at scale.

 Familiarity with drill and recovery processes enables your organization to verify that you can respond quickly if you must recover applications on AWS. You can facilitate disaster recovery drills at scale by automating drill and recovery processes.
