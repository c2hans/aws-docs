---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/windows-environment-discovery.html
---

# Windows environment discovery
<a name="windows-environment-discovery"></a>

With today's available technologies, such as AWS Transform MGN, moving Windows Server, Linux, and other x86-based operating systems and their workloads to AWS is fairly straightforward. Getting those workloads to work properly and doing it at scale, however, presents a different set of challenges. This section is intended to identify migration considerations that can enable you to quickly, securely, and smoothly migrate your Microsoft workloads.

## Assess
<a name="assess-discovery"></a>

Although you can "brute force" smaller migrations (such as those involving 100 servers) with minimal planning and automation, you can't move 500 or more servers by using this methodology. The following considerations are major contributors to a successful large-scale migration, and you can use the [Migration Readiness Assessment (MRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/assessment-phase.html) to identify areas of consideration that you want to focus on.

### Enterprise architecture
<a name="enterprise-architecture.fcbd2b38-15ae-59ba-8013-a106db7991fa"></a>

The more technology debt there is in the environment the more difficult it is to migrate. Organizations that have healthy enterprise architecture programs strive to limit their environment to current and recent versions of software and systems (often called N and N -1 versions of major releases). This not only reduces the number of scenarios that you must account for, but it also takes advantage of the advances of newer releases. For example, Windows Server 2012, Windows Server 2008, and older versions of Windows Server are progressively much more difficult to automate in the Windows Server environment than more current versions. Licensing is also more difficult for older and unsupported versions.

### Standardization and configuration management
<a name="standardization-and-configuration-management.23e03250-a3ec-5955-974e-2f673075bd93"></a>

Standardization of the environment is another factor to consider. Organizations that have environments that are built by hand and maintained are considered to be more like pets. Each system is unique and there are far more possible configuration combinations than if they were built using standardized images, infrastructure as code (IaC), or continuous integration and continuous delivery (CI/CD) pipelines.

For example, it's a best practice to rebuild a typical web server using IaC or CI/CD when migrating, as opposed to manually migrating the individual server. It's also a best practice to store all persistent data in a datastore such as a database, file share, or repository. If systems aren't rebuilt using IaC or CI/CD, they should at least use configuration management tools (such as Puppet, Chef, or Ansible) to standardize the servers they have.

### Good data
<a name="good-data.d094101a-d4a2-5961-8983-32ce32b04db4"></a>

Good data is also a key factor for successful migrations. Accurate data regarding current servers and their metadata is essential for automation and planning. Lack of good data increases the difficulty when planning a migration. Examples of good data include an accurate inventory of servers, applications on the servers, software on the servers with versions, the number of CPUs, amount of memory, and number of disks. We recommend that you capture any data that wave planners need for planning or any data that you plan to use as part of automating the migration process.

### Automation
<a name="automation.341449d4-5d90-582e-9896-3974d7e51c9d"></a>

Automation is essential for migrations at scale. Examples of automation include installing the agent, updating software versions of utilities needed for automation such as .NET or PowerShell, loading or updating software for AWS such as the AWS Systems Manager Agent (SSM Agent), Amazon CloudWatch agent, or other backup or management software needed to run in AWS.

### Detailed planning
<a name="detailed-planning.95e9db04-91cc-547d-89e8-a35c2a64d9f1"></a>

Developing and managing a detailed plan is also essential for migrations at scale. You must have a well-defined plan in place to migrate 50 servers a week for many weeks. An effective plan includes the following:
+ Use **wave planning** to organize servers into waves according to your dependencies and priorities.
+ Use** weekly planning **(leading up to cutover) to communicate with application teams and identify network, DNS, firewall, and other details that must be addressed during cutover.
+ Use detailed,** hour-to-hour planning **(around actual cutover) to describe the cutover maintenance window.
+ Use** go/no-go criteria** to describe under what circumstances an application will either be considered cut over to AWS or must be failed back to the source location.
+ Use** cleanup activities** as follow-up activities that must be completed. These activities can happen outside the cutover maintenance window or after the completion of [hypercare](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-governance-playbook/managing-large-migration.html#hypercare-period). Clean-up activities include verifying backups and various agents, removing the MGN agent from a server, or removing the source server and associated resources.

## Mobilize
<a name="mobilize-discovery"></a>

During the mobilize phase, it's important to discover as many of your organization's complexities and variations as possible so that they can be accounted for during migration planning. Ideally, you can avoid dealing with such complexities and variations during the cutover maintenance window and prevent any failbacks.

### Challenges of migrations at scale
<a name="challenges-of-migrations-at-scale.ceb0824f-f74e-5b76-a44c-3fef0de007d5"></a>

Migration failures occur when an application or applications have been cutover to their new environments and performance or functional requirements can't be met within the migration maintenance window. This forces the application or applications to fail back to their original location. In addition, all other applications that are dependent on that application or applications also need to fail back. Failed migrations tend to impact not only the current wave but future waves as applications must be rescheduled.

### Latency-sensitive dependencies
<a name="latency-sensitive-dependencies.811bb354-7391-5cc9-928b-88d84b0f7561"></a>

A major reason for failed migrations is latency-sensitive dependencies. Failing to identify dependencies that are latency sensitive can introduce performance issues that result in unacceptable response times or transaction times.

For example, typically an application moves its database and application servers to the cloud at the same time because they communicate with each other frequently and need the sub-millisecond response time they have when both are in the same data center. Moving only the database to the cloud is likely to introduce many seconds of latency into those transactions, resulting in significant performance impact to the application. This also applies to applications that are heavily dependent on one another and must be in the same data center to perform adequately.

Understanding and addressing application dependencies is therefore of primary importance when planning migrations. Applications and services that are dependent on one another must be identified so that they can be migrated together.

### IT shared services
<a name="it-shared-services.efc4b14b-3db5-50b5-a1f7-f1ca149fa64a"></a>

After a workload is in the cloud, it needs a variety of services to function and be maintained properly and securely. This includes a landing zone, network and security perimeter, authentication, patching, security scanners, IT service management tools, backups, bastion hosts, and other resources. Without these services, workloads might not operate properly and will be forced to fail back to their original location.

### Configuration updates
<a name="configuration-updates.82095022-4b1b-5295-b0cb-92e4cd5a5a45"></a>

In most cases, you must make several configuration changes for a workload to function properly after that workload is moved to the cloud. These configuration changes are often associated with the following dependencies of the workload:
+ Firewall rules
+ Allow lists
+ DNS records
+ Connection strings

If you don't make the proper configuration updates, then the workload, its users, and its dependent systems may fail to communicate with each other. Resolving these issues within the outage window could be possible, but changes at this time can be time consuming or require change records that can't be satisfied in time.

### Application functional testing
<a name="application-functional-testing.cbfccff7-8c65-5915-a195-50c24dc7e7ef"></a>

Another challenge for migrations at scale is the need for application functional testing. This is of particular importance since many organizations rely on application teams to identify latency-sensitive dependencies, IT shared services, or needed configuration updates. Ideally, an application team provides a written or automated test plan that they can run during the cutover maintenance window to validate that their application is fully functional with acceptable performance. To keep the cutover maintenance window to a minimum, the test should be able to be completed within 30 minutes.

### Tools for application dependency discovery
<a name="tools-for-application-dependency-discovery.c05a7670-4ef8-5f05-a230-44ed004813ad"></a>

Determining dependencies between applications is critical for successful migrations—both for detecting latency-sensitive dependencies and connectivity configuration items. There are several tools available in the marketplace for discovering dependencies, such as [AWS Transform discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html) (agent-based tool) and [Cloudamize](https://cloudamize.com/en/) (agent-based tool).

When you choose a tool for application dependency discovery, consider the following:
+ **Duration** – We recommended that you run discovery tools long enough to capture application-specific events such as known peaks, month end, and other events. The recommended minimum is 30 days.
+ **Active (agent based)** – Active dependency discovery tools are often embedded in the kernel of the operating system and capture all transactions. However, this is typically the most expensive and time-consuming method.
+ **Passive** (**agentless**) – Passive dependency discovery tools are much cheaper and faster to implement but risk missing some lesser used connections.
+ **Institutional knowledge** – Although application discovery tools provide more detailed and accurate information, most organizations rely on their application teams and their institutional knowledge to discover application dependencies. Application teams are often knowledgeable about latency-sensitive dependencies, but it's not uncommon for them to miss some details such as connectivity configuration settings, firewall rules, or allow list requirements from a partner. You can use institutional knowledge to enhance your application dependency discovery, but we recommend that you also consider and mitigate the risks involved. For example, there is a risk of missing connectivity configuration items or latency-sensitive dependencies if you only depend on the knowledge of your application teams. This could result in outages or failed migrations. To mitigate this risk, we recommend that you conduct detailed application functional testing.
