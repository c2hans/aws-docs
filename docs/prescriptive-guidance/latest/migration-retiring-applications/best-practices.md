---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Choosing to retire applications can be a complex decision, especially during a migration to the AWS Cloud. The following sections provide best practices to use in your decision-making process.
+ [Consider a migration factory approach](#best-practice-1)
+ [Identify and retire applications early in your migration](#best-practice-2)
+ [Be data-driven and use discovery tooling to avoid disruptions](#best-practice-3)
+ [Schedule a controlled stop](#best-practice-4)
+ [Reassess if the application should be migrated](#best-practice-5)
+ [Retire the application](#best-practice-6)

## Consider a migration factory approach
<a name="best-practice-1"></a>

An important part of any large-scale migration is establishing a *migration factory* after the initial pilot workloads are migrated.

A migration factory consists of teams, tools, and processes that work together to streamline migrations in a systematic way, incorporating lessons learned from previous migration waves. The migration factory applies patterns, which accelerate workload migrations and improve the final outcome.

Based on the size of the IT portfolio you need to retire, it's worth considering if there's value in implementing a migration factory approach. The methodologies and principles outlined in this guide will also complement this approach and can be embedded into its mechanisms.

Typically, twenty to fifty percent of an enterprise application portfolio consists of repeated patterns that can be optimized by using a migration factory approach. For an example of a pattern, see the [AWS Cloud Migration Factory Solution](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/), which can be implemented by a migration team to coordinate and automate migrations.

The team should begin with applications that have the lowest business criticality, before gradually moving toward more critical systems. By the time the team begins to migrate business-critical systems, they will have migrated hundreds, if not thousands, of workloads and learned many lessons.

Before the assessment phase begins, you can create a process to capture one month of dependency data for applications that are identified for retirement. A team is notified and given access to the data when it is ready. The team then gives the data a score based on the potential for an application to cause an impact. The application owners might then do a deeper analysis of the connections before next steps begin.

For more information about the migration factory methodology, see the [Guide for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/).

## Identify and retire applications early in your migration
<a name="best-practice-2"></a>

Identifying and then retiring applications early in the migration process is important and should be carried out while workloads are being migrated.

Migration projects often prioritize migrating workloads, so it's common for systems that are identified as to be retired (and not migrated) to receive focus toward the end of the project. However, there's a risk that leaving these applications until the end of the project will leave very little time to include it in the migration if the application is later deemed important.

Retiring workloads early during a migration project reduces the workload of teams that maintain them. For example, retiring servers during a migration project's early phases means that operating system teams have fewer servers to patch, upgrade, maintain, or support. Those teams are then able to focus on the migration project itself.

Finally, some of this guide's best practices are most effective when you follow them for longer periods of time. If you begin the retirement process early but later determine that an application is actually required by another service, you will be able to modify your migration plan and include it in a future migration wave.

## Be data-driven and use discovery tooling to avoid disruptions
<a name="best-practice-3"></a>

Being data-driven is critical when considering retiring applications. Architecture diagrams and institutional knowledge can easily be outdated or incomplete.  Sometimes unanticipated problems can also surface, such as another application becoming dependent on your system without formal engagement due to a break-fix scenario.

A data-driven approach provides the foundation on which you can make decisions or validate an approach. When assessing if an application can be retired, you must confirm that the workloads you are migrating aren't dependent on it. Migrating those workloads and then retiring a dependency could cause a service degradation, or worse, service interruption.

Fortunately, it's fairly straightforward to understand these dependencies by using data to monitor the network inbound and outbound connections on a server that is scheduled for retirement. Network inbound connections, such as an application connecting to your application, and outbound connections, such as a file upload to a Network File System (NFS) share, indicate a potential dependency. This dependency needs to be investigated, because if a workload that's due to be migrated to the AWS Cloud connects to the application, there's a potential for service disruption if the application is retired later. This process might require diving deep to follow the dependency chain. Following the previous example, if the application uploads a file to an NFS share, the next step will be to understand which system consumes that file and the status of that application.

You might decide to investigate those connections and assess the impact level. To do this, you can use discovery tooling to show the connections being initiated to a server that is scheduled for retirement. You might notice that most connections are from management servers and can be ignored, because they are tools that collect performance metrics or system administrator proxy instances. However, if there are applications connecting to the server that are scheduled for migration, you should dive deeper and check the potential impact of migration on that application. [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/) helps customers plan migration projects by gathering information about on-premises data centers that they are planning to retire. After you deploy the agent to your servers, Application Discovery Service records inbound and outbound network activity for each server, along with other information. By using [Amazon Athena](https://aws.amazon.com/athena/) to analyze this data, you can identify if other applications are depending on servers that are planned for retirement. [AWS Migration Competency Partners](https://aws.amazon.com/migration/partner-solutions/) can also provide deep discovery and planning tooling.

**Note**
AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html). For example, the following screen illustration shows four source IP addresses connecting to the server on port 22 (destination = 172.31.1.117).

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/images/guide-img/11b5b0ce-2bf2-40a9-9f55-c87adb6560a5/images/ec1c5cf3-0f47-4e03-be00-b0cdfc5d0556.png)

These are bastion hosts that are used by the system administrators and can be ignored. The image also shows two servers connecting to this application on port 80, which are in scope of a planned migration. At this stage, you would need to dive deeper and understand the connecting applications. This deeper analysis will allow you to assess if there will be any upstream impact after retirement.

## Schedule a controlled stop
<a name="best-practice-4"></a>

In your migration plan, be sure to schedule time for a controlled stop during the migration process. A controlled stop pauses the migration process to identify the potential for disruption if an application is retired. It simulates the application's retirement, and allows you to observe the consequences. When the controlled stop period is completed, the migration can easily resume.

The controlled stop approach varies depending on the type of application and the associated processes you are working with. Common controlled stop patterns include:
+ Implementing a host-based firewall to block all traffic, which simulates retirement
+ Pausing a virtual machine
+ Stopping a service on the host
+ Blocking all traffic by using an external firewall

The migration project and application owners need to define the duration of a controlled stop, depending on the application type. For example, if you're retiring a batch-based workload that only runs once a month or once a quarter, performing a one-week controlled stop might not be enough to determine the impact on other systems.

Continuing with the example from the previous section, another application was connecting to the server that was scheduled for retirement. An initial assessment concluded that there should not be an impact on the upstream servers. A controlled stop can now be carried out to understand the impact.

This controlled stop would be carried out by implementing a host-based firewall to block all traffic, simulating the effect of shutting down the server. If this causes service issues for applications that are scheduled to be migrated to the AWS Cloud, a firewall rule is added and all traffic resumes. After the controlled stop, the server's retirement is reconsidered due to this service degradation or interruption.

## Reassess if the application should be migrated
<a name="best-practice-5"></a>

The last two best practices we discussed help determine if it's appropriate to continue action on the systems that are scheduled for retirement. If those best practices highlight a potential upstream business impact, you should consider reassessing the application's migration pattern. By beginning the application retirement process early, you now have sufficient time to include the application in a subsequent migration wave if you encounter issues or dependencies that mean it cannot be retired.

If, after following those best practices, you are not fully confident in retiring the application, consider if it should be rehosted to the AWS Cloud. This is particularly important if your migration has a set end date, such as a data center lease expiry.

Services such as the [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) simplify the rehost migration approach. When you migrate applications to AWS, you could take a  snapshot of the Amazon Elastic Block Store (Amazon EBS) volumes and terminate the Amazon Elastic Compute Cloud (Amazon EC2) instance to reduce costs and test the retirement of the application over an extended period of time. If an impact or issue arises, you then have the confidence of being able to recreate the Amazon EBS volumes based on the snapshot to resume the Amazon EC2 instance.

**Important**
Test this recovery process before you terminate the Amazon EC2 instance.

## Retire the application
<a name="best-practice-6"></a>

After following this guide's previous five best practices, you might have determined that it's safe to retire an application. You deployed a migration factory approach, began the retirement process early, used data and discovery tools to monitor the inbound connections, performed a successful controlled stop, and assessed if the application should be retired. Retiring the application is now possible as part of your migration strategy.

At this point, you should check if the application contains data that might be useful in the future. Machine learning (ML) and analytics have given data greater value than ever before. Although you might not be developing ML algorithms now, historical data can prove beneficial in the future. You might also have regulatory or compliance requirements to store the data for a defined period of time, even if the application has been retired.

AWS offers a comprehensive set of cloud storage services for long-term retention, compliance, and digital preservation. AWS storage solutions for data archiving help provide unlimited scale, 99.999999999% durability, data reliability, and data security.

To assist your compliance efforts, AWS regularly achieves third-party validation for thousands of global compliance requirements. These are continually monitored to help you meet security and compliance standards for finance, retail, healthcare, government, and beyond.

For more information on data archiving with AWS, see [Data Archiving](https://aws.amazon.com/archive/) on the AWS website.
