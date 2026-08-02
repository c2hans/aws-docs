---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/process-perspective.html
---

# Process perspective
<a name="process-perspective"></a>

Processes bring consistency but they also evolve and are susceptible to change because each project is unique. As you run the process repeatedly, you will identify gaps and room for improvements that can add up to huge benefits as you fail, learn, adopt, and iterate. These changes can lead to new ideas or innovations that the project and the business can take advantage of in the future, which provides a catalyst for growth that brings quality and team confidence.

Processes in migrations can be complex as they cross technologies and boundaries that might not have been linked previously. This perspective provides processes and guidance on specific requirements for large migrations.

## Preparing for your large migration
<a name="preparing-large-migration"></a>

The following sections outline the core principles that are required to ensure that you start your migration journey with a clear direction and buy-in from the stakeholders that will be critical to its success.

In this section:
+ Define business drivers and communicate timeline, scope, and strategy
+ Define a clear escalation path to help remove the blockers
+ Minimize unnecessary change
+ Document an end-to-end process early
+ Document standard migration patterns and artifacts
+ Establish a single source of truth for migration metadata and status

### Define business drivers and communicate timeline, scope, and strategy
<a name="define-business-drivers-and-communicate-timeline--scope--and-strategy.47d52d48-65f4-5af8-8713-cc682e2a93ed"></a>

When approaching a large migration to AWS, you will quickly discover that there are numerous ways to migrate your servers. For example, you could do the following:
+ Rehost workloads using [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html).
+ Containerize your application and host it on [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or the [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) managed container service.
+ Redesign your workload into a fully serverless application.

To determine the correct migration path, it's important to work backwards from your business drivers. If your ultimate goal is to increase business agility, you might favor the second two patterns, which involve more levels of transformation. If your goal is to vacate a data center by the end of the year, you might choose to rehost workloads because of the velocity that rehosting provides.

A large migration typically involves a wide range of stakeholders, including the following:
+ Application owners
+ Network teams
+ Database administrators
+ Executive sponsors

It is key to identify the business drivers of the migration and include that list in a document, such as a project charter that members of the migration program can access. Furthermore, create key performance indicators (KPIs) that closely align with your target business outcomes.

For example, one customer wanted to migrate 2,000 servers within 12 months to achieve their target business outcome of vacating their data center. However, their security teams were not aligned toward this goal. The result was several months of technical debates on whether to miss the data center closure date but modernize applications further or to rehost initially to enable the timely data center closure and then modernize applications on AWS.

### Define a clear escalation path to help remove the blockers
<a name="define-a-clear-escalation-path-to-help-remove-the-blockers.1c9c9111-ced3-5512-a8fd-891f6fb70f34"></a>

Large cloud migration programs typically involve a wide range of stakeholders. After all, you're potentially changing applications that have been hosted on premises for several decades. It's common for each of the stakeholders to have conflicting priorities.

While all the priorities might drive value, the program will likely have a limited amount of budget and a defined target outcome. Managing the various stakeholders and focusing on the target business outcomes can be challenging. This challenge is compounded when you multiply it by the hundreds or thousands of applications that are in scope of the migration. Further, the stakeholders likely report into different leadership teams, which have other priorities. With this in mind, alongside clearly documenting the target business outcomes, it's important to define a clear escalation matrix to help remove blockers. This can save a significant amount of time and help align the various teams toward a common goal.

One example that demonstrates this is a financial services company whose goal was to vacate their primary data center within 12 months. There wasn't a clear mandate or escalation path, which resulted in the stakeholders crafting their desired migration paths, regardless of time and budget constraints. Following an escalation to the CIO, a clear mandate was set and a mechanism was provided for requesting required decisions.

### Minimize unnecessary change
<a name="minimize-unnecessary-change.0a9d2515-3e33-5876-acfa-a977a1c22dc3"></a>

Change is good but more changes mean more risks. When the business case for the large migration is approved, there is most likely a target business outcome driving this initiative, such as vacating a data center by a specific date. While it's common for technologists to want to re-write everything to take full advantage of AWS services, this might not be your business goal.

One customer was focused on a two-year migration of the company's entire web-scale infrastructure to AWS. They created a two-week rule as a mechanism to prevent application teams from spending months rewriting their applications. By using the two-week rule, the customer was able to sustain a long-term migration with a consistent cadence when hundreds of applications had to be moved over a multiple-year period. For more information, see the blog post [The Two-Week Rule: Refactor Your Applications for the Cloud in 10 Days](https://aws.amazon.com/blogs/enterprise-strategy/the-two-week-rule-refactor-your-applications-for-the-cloud-in-10-days/).

We recommend minimizing any change that doesn't align with the business outcome. Instead, build mechanisms to manage these additional changes in future projects.

### Document an end-to-end process early
<a name="document-an-end-to-end-process-early.d152a7b4-5f40-59f7-bf9c-b54d58eeb5af"></a>

Document the complete migration process and assignment of ownership in the early stages of a large migration program. This documentation is important in educating all stakeholders about how the migration will run and their roles and responsibilities. The documentation will also help you to understand where issues might occur and to provide updates and iterations of the process as you progress through the migrations.

During the development of the migration project, ensure that any existing processes are understood and that integration points and dependencies documented clearly. Include places where engagement with external process owners will be required, including change requests, service requests, vendor support, and network and firewall support. After the process is understood, we recommend documenting ownership in a responsible, accountable, consulted, informed (RACI) matrix to track the different activities. To finalize the process, establish a countdown plan by identifying the timelines involved in each step of the migration. The countdown plan generally works backwards from the workload migration cutover date and time.

This documentation approach worked well for a multinational home appliance corporation that migrated to AWS successfully in less than a year and exited four data centers. They had six different organizational teams and multiple third parties involved, which introduced management overhead resulting in back-and-forth decisions and delays in implementation. The AWS Professional Services team, together with the customer and their third parties, identified key processes for the migration activities and documented them with respective owners. The resulting RACI matrix was shared and agreed upon by all involved teams. Using the RACI matrix and an escalation matrix, the customer alleviated the blockers and issues that were creating delays. They were then able to exit the data centers ahead of schedule.

In another example of using RACI and escalation matrices, an insurance firm was able to exit the data center in less than 4 months. The customer understood and implemented a shared responsibility model, and a detailed RACI matrix was followed to track the progress of each process and activity throughout the migration. As a result, the customer was able to migrate over 350 servers in the first 12 weeks of implementation.

### Document standard migration patterns and artifacts
<a name="document-standard-migration-patterns-and-artifacts.23433c2e-d040-5270-84e8-a20c1612886a"></a>

Think of this as creating cookie cutters for the implementation. Reusable references, documentation, runbooks, and patterns are the key to scale. These journal the experience, learning, pitfalls, issues, and solutions that future migration projects can reuse and avoid, significantly accelerating the migration. The patterns and artifacts are  also an investment that will help improve the process and guide future projects.

For example, one customer was performing a year-long migration where applications were being migrated by three different SI AWS Partners. In the early stages, each AWS Partner was using their own standards, runbooks, and artifacts. This placed numerous stresses on the customer teams, because the same information could be presented to them in different ways. After these early pains, the customer established central ownership of all documentation and artifacts to be used in the migration, with a process for submitting recommended changes. These assets include the following:
+ A standard migration process and checklists
+ Network diagram style and format standards
+ Application architectural and security standards based on business criticality

In addition, changes to any of these documents and standards were sent out to all teams on a weekly cadence, and each partner was required to confirm receipt and adherence to any changes. This greatly improved communication and consistency for the migration project, and when a separate large migration effort in another business unit started, that team was able to adopt the existing process and documents, greatly accelerating their success.

### Establish a single source of truth for migration metadata and status
<a name="establish-a-single-source-of-truth-for-migration-metadata-and-status.2e598680-0d1d-5a34-a4a4-1df36cdcc5f4"></a>

When it comes to planning a large migration, establishing a source of truth is important to keep the various teams aligned and enable data-driven decisions. When you start this journey, you might find numerous data sources that you can use, such as the configuration management database (CMDB), application performance monitoring tooling, inventory lists, and so on.

Alternatively, you might find that there are few data sources and you must create mechanisms to capture the data needed. For example, you might need to use discovery tooling to uncover technical information, and to survey IT leaders to obtain business information.

It's important to aggregate the various data sources into a single dataset that you can use for the migration. You can then use the single source of truth for tracking the migration during the implementation. For example, you can track which servers have been migrated.

A financial services customer that wanted to migrate all workloads to AWS focused on planning the migration with the dataset that had been provided. This dataset had key gaps, such as business criticality and dependency information, so the program started a discovery exercise.

In another example, a company in the same industry moved into migration wave implementation based on an out-of-date understanding of their server infrastructure inventory. They quickly started to see migration numbers decrease because the data was incorrect. In this case, application owners were not understood, which meant that they could not find testers in time. Additionally, the data were not aligned to the decommissioning that their applications teams had completed, so servers were running without being used for a business purpose.

## Running your large migration
<a name="running-large-migration"></a>

After you have established your business outcomes and communicated the strategy to the stakeholders, you can move to planning how you carve up the scope of the large migration into sustainable migration events or waves. The following examples provide key guidance for making the wave plan.

In this section:
+ Plan migration waves ahead of time to ensure a steady flow
+ Keep wave implementation and wave planning as separate processes and teams
+ Start small for great outcomes
+ Minimize the number of cutover windows
+ Fail fast, apply experience, and iterate
+ Don't forget the retrospective

### Plan migration waves ahead of time to ensure a steady flow
<a name="plan-migration-waves-ahead-of-time-to-ensure-a-steady-flow.a3404293-646b-54ae-9d89-4e6303dae732"></a>

Planning your migration is one of the most important phases of the program. It goes with the saying "if you fail to plan, you plan to fail." Planning migration waves ahead of time allows the project to flow swiftly as the team becomes more proactive to the migration situation. It helps the project scale more easily, and it improves decision making and forecasting as project demands increase and become complex. Planning ahead also improves the team's ability to adapt to changes**. **

For example, a large financial services customer was working on a data center exit program. Initially, the customer planned the migration waves in a sequential fashion, completing one wave before beginning to plan the next. This approach resulted in less time to prepare. When the stakeholders were informed that their applications were being migrated to AWS, they still had several steps to perform before starting the migration. This added significant delays to the program. After the customer realized this, they implemented a holistic and future-focused migration planning stream where migration waves were planned several months in advance. This provided enough notice for the application teams to perform their pre-migration activities such as notifying AWS Partners, licensing analysis, and so forth. They could then remove those tasks from the program's critical path.

### Keep wave implementation and wave planning as separate processes and teams
<a name="keep-wave-implementation-and-wave-planning-as-separate-processes-and-teams.6152b5ad-367d-561a-a646-9410ee57a514"></a>

When wave planning and wave implementation teams are separate, the two processes can work in parallel. With communication and coordination, this avoids slowing down the migration because not enough servers or applications are ready to achieve the expected velocity. For example, the migration team might need to migrate 30 servers a week, but only 10 servers are ready in the current wave. This challenge is often caused by the following:
+ The migration implementation team was not involved in the wave planning, and the data collected in the wave planning phase are not complete. The migration implementation team must collect more server data before starting the wave.
+ Migration implementation is scheduled to start right after wave planning, with no buffer between.

It is critical to plan waves ahead of time, and to create a buffer between preparation and the start of the wave implementation. It is also important to make sure that the wave planning team and the migration team work together to collect the right data and avoid rework.

### Start small for great outcomes
<a name="start-small-for-great-outcomes.f94e6ef3-602c-587e-8b32-b6d598f4dff6"></a>

Plan to start small and increase migration velocity with each subsequent wave. The initial wave should be a single, small application, fewer than 10 servers. Add additional applications and servers in subsequent waves, building up to your full migration velocity. Prioritizing less complex or risky applications, and ramping velocity on a schedule, gives the team time to adjust to working together and to learn the process. In addition, the team can identify and implement process improvements with each wave, which can substantially improve the velocity of later waves.

One customer was migrating more than 1,300 servers in a year. By starting with a pilot migration and a few smaller waves, the migration team was able to identify multiple ways to improve later migrations. For example, they identified new data center network segments earlier. They worked with their firewall team early in the process to put in place firewall rules that allowed communication with migration tooling. This helped prevent unnecessary delays in future waves. In addition, the team was able to develop scripts to help automate more of their discovery and cutover processes with each wave. Starting small helped the team focus on early process improvements, and greatly increased their confidence.

### Minimize the number of cutover windows
<a name="minimize-the-number-of-cutover-windows.ad538e45-68c1-55aa-aedf-e45264cad707"></a>

Mass migrations require a disciplined approach to driving scale. Being too flexible in some areas is an anti-pattern for large migrations. By limiting the number of weekly cutover windows, time spent on cutover activities has higher value.

For example, if the cutover window is too flexible, you could end up with 20 cutovers with five servers each. Instead, you could have two cutovers with 50 servers each. Because the time and effort for each cutover are similar, having fewer, larger cutovers reduces the operational burden of scheduling, and limits unnecessary delays.

A large technology company was trying to migrate out of a few leased data centers before contract expiration. Missing the expiration would result in expensive, short-term renewal terms. Earlier in the migration, application teams were allowed to dictate migration schedule up to the last minute, including opting out of migration for any reason just days ahead of cutover. This led to numerous delays in the early stages of the project. Often, the customer had to negotiate with other application teams at the last minute to fill in. The customer eventually increased their planning discipline, but this early mistake led to constant stress for the migration team. Delays to the overall schedule resulted in some applications not making it out of the data centers in time.

### Fail fast, apply experience, and iterate
<a name="fail-fast--apply-experience--and-iterate.08980bf2-ba90-5d7d-b756-3145b0a4a4b7"></a>

Every migration has pitfalls initially. Failing early helps the team learn, understand the bottlenecks, and apply the lessons learned to larger waves. It is expected that the first couple of waves in a migration will be slow for the following reasons:
+ Team members are adjusting to each other and the process.
+ Large migrations usually involve many different tools and people.
+ It takes time to integrate, test, fail, learn, and continuously improve the end-to-end process.

Issues are common and expected during the first couple of waves. It is important to understand and communicate this to the entire organization, because some teams may not like to try new things and fail. Failure can discourage the team and become a blocker for future migrations. Making sure everyone understands that initial issues are part of the job and encouraging everyone to try and fail is key to a successful migration.

One company planned to migrate more than 10,000 servers in 24–36 months. To achieve that goal, they needed to migrate nearly 300 servers a month. However, that does not mean they migrated 300 servers from day one. The first couple waves were learning waves so that the team could understand how things worked and who had permissions to do what. They also identified integrations that would improve the process, such as integrating with CMDB and CyberArk. They used the learning waves to fail, improve, and fail again, refining the process and automation. After 6 months, they were able to migrate more than 120 servers each week.

### Don't forget the retrospective
<a name="don-t-forget-the-retrospective.d622432f-acee-5cb4-bc77-a7fc293e300d"></a>

This is an important part of an agile process. It's where the team communicates, adjusts, learns, agrees, and moves forward. A retrospective at the most basic level is looking back, discussing what happened, determining what went well and what needs to improve. Improvements can then be built based on those discussions. Retrospectives wrap some formality or process around the idea of lessons-learned. Retrospectives are important because to achieve the scale and velocity for large migrations to succeed, the processes, tools, and teams must constantly evolve and improve. Retrospectives can play a significant part in that.

Traditional lessons-learned sessions do not happen until the end of a program, so often these lessons do not get reviewed at the start of the next migration wave. With large migrations, lessons learned should be applied to the next wave and should be a key part of the wave planning process.

For one customer, weekly retrospectives were held to discuss and document lessons learned from the cutovers. In these sessions, they uncovered areas where there was scope for streamlining from a process standpoint or automation. This resulted in implementation of a countdown schedule with specific activities, owners, and automation scripts to minimize manual tasks, including validation of third-party tools and Amazon CloudWatch agent installation, during cutover.

At another large tech company, regular retrospectives were held with the team to identify problems with previous migration waves. This resulted in process, script, and automation improvements that drove the average migration time down by 40 percent over the course of the program.

## Additional considerations
<a name="process-perspective-add-considerations"></a>

Many areas must be factored into a large migration program. The following sections provide thoughts on other items that must be considered.

In this section:
+ Clean up as you go
+ Implement multiple phases for any additional transformation

### Clean up as you go
<a name="clean-up-as-you-go.d1c788a5-7f01-5d1e-b2cf-bd4def78e9ad"></a>

A migration isn't considered successful if it costs 10 times what you expected, and the project is not complete until the resources used for migration are shut down and cleaned up. This cleanup should be part of the post-migration activity. It ensures that you will not leave unused resources and services in your environment that will add to the costs. Post-migration cleanup is also a good security practice for preventing threats and vulnerabilities that expose your environment.

Two key outcomes of moving to the AWS Cloud are the cost savings and the security. Leaving unused resources can defeat the business purpose of moving to cloud. The most common resources that are not cleaned up include the following:
+ Test data
+ Test databases
+ Test accounts, including firewall rules, security groups, and network access control list (network ACL) IP addresses
+ Ports provisioned for testing
+ Amazon Elastic Block Store (Amazon EBS) volumes
+ Snapshots
+ Replication (such as stopping the data replication from on-premises to AWS)
+ Files that consume space (such as temporary database backups used to migrate)
+ Instances that host the migration tools

In one example of bad cleanup practices, SI AWS Partners were not removing replication agents after a successful migration. An AWS audit discovered that replication servers and EBS volumes that had already been migrated were costing $20,000 (USD) each month. To mitigate the issue, AWS Professional Services created an automated audit process that notified SI AWS Partners when stale servers were still being replicated. The SI AWS Partners could then take action on unused and stale instances.

For future migrations, a process was adopted to define a post-migration hypercare period of 48 hours to ensure smooth platform adoption. The customer's infrastructure team then submitted a decommission request for on-premises servers. It was advised that upon approval of the decommission request, servers of the respective wave would be removed from the service console.

### Implement multiple phases for any additional transformation
<a name="implement-multiple-phases-for-any-additional-transformation.1309f241-0274-595b-bbe3-56c877b891b9"></a>

When carrying out a large migration, it's important to remain focused on your core goal, such as data center closure or infrastructure transformation. In smaller migrations, scope creep might have a minimal impact. However, a few days of additional effort multiplied by potentially thousands of servers can add a significant amount of time to the program. Furthermore, the additional changes might also require updates to documentation, process, and training for support teams.

To overcome potential scope creep, you can implement a multiple-phase approach to your migration. For example, if your goal was to vacate a data center, phase 1 may include only rehosting the workload to AWS as fast as possible. After a workload is rehosted, phase 2 can implement transformational activities without risking the target business outcome.

For example, one customer planned to exit their data center in 12 months. However, their migration encompassed other transformation activities, such as rolling out new application performance monitoring tooling and upgrading operating systems. More than 1,000 servers were in scope of the migration, so these activities added a significant delay to the migration. Furthermore, this approach required training in the use of the new tooling. The customer later decided to implement a multiple-phase approach with an initial focus on rehost. This increased their migration velocity and reduced the risk of not meeting the data center closure date.
