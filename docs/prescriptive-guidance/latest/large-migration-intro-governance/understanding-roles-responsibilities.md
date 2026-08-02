---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-intro-governance/understanding-roles-responsibilities.html
---

# Understanding roles and responsibilities
<a name="understanding-roles-responsibilities"></a>

Many organizations are not prepared for the people, process, and technology changes that occur over the duration of a large migration project. The Cloud Operating Model helps you adapt throughout the migration process and iterates as the organization matures. You can take a Cloud Operating Model workshop to help you visualize the journey ahead. This workshop can help you address questions like *Can I use the same resources to support on-premises and cloud infrastructure, or do I need a new support organization?* and *Can I handle support requests through a ticket system? *These are a sample of the key questions that organizations need to address to prepare the organization for the large migration.

This section contains the following topics:
+ [Fostering alignment within workstreams](#workstream-alignment)
+ [Roles and responsibilities for large migration projects](#roles-responsibilities)
+ [Project management team responsibilities](#pm-responsibilities)

## Fostering alignment within workstreams
<a name="workstream-alignment"></a>

With many workstreams operating simultaneously and dependent on one another to complete the migration, it's imperative that the workstreams are aligned. The following are the keys to success when aligning your workstreams:
+ Competing work priorities can impact the success of the migration. Ensure all workstreams are working to the same goals and understand the importance of their contribution to the project.
+ It is important to define the roles and responsibilities for all migration team members, including consultants and other third-party vendors, within your RACI matrix. For more information, see [Roles and responsibilities for large migration projects](#roles-responsibilities).
+ Set up communication on a regular daily and weekly cadence that helps the workstreams align their tasks. For more information, see [Communication planning for large migrations](communication-planning.md).

|
|
| Note In the event of an organization merger or divestiture, the large migration team needs to align wave planning activities with other concurrent activities, such as directory migrations, network changes, and single sign-on capabilities. |
| --- |

## Roles and responsibilities for large migration projects
<a name="roles-responsibilities"></a>

In large migrations, it is critical for all migration team members to understand their roles and responsibilities during the migration process. Especially if you have the support of an external provider, such as AWS Professional Services, you must clearly understand which party is responsible for each task. In this case, there is a shared responsibility model for the migration. The AWS teams are responsible for infrastructure readiness and troubleshooting, and your organization is responsible for application-level testing and troubleshooting during the cutover.

There is additional complexity if a company is being acquired by or divested from its parent company or if the on-premises environment is controlled by the parent entity while a subsidiary is migrating to the AWS Cloud.

We recommend that you build a responsible, accountable, consulted, informed (RACI) matrix for each [migration strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html). This matrix defines which teams are responsible, accountable, consulted, or informed for each task. For more information about how to create a RACI matrix and for templates, see [Creating RACI matrices](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/team-org.html#raci) in the *Foundation playbook for AWS large migrations*.

For example, you would build a RACI matrix for the rehost migration strategy. The rehost migration strategy typically consists of the following phases. After the initial waves are defined, the mapped servers follow these phases, and you capture the detailed activities in the RACI matrix:

1. **Pre-migration** – Obtain formal commitment from the application owners and other stakeholders for the applications in the wave and for their tasks and responsibilities to meet the wave schedule.

1. **Build** – For the in-scope servers, you confirm that you meet the technical prerequisites for [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) (AWS MGN). You install the replication agents on the servers to build the staging areas for those servers. You copy any post-cutover scripts Application Migration Service servers so that you can run them after the cutover.

1. **Validate** – Validate the replication progress and request a local admin user on the source servers. This local admin user is for a break-glass scenario to access the servers if they lose domain trust after the migration. If you're using CMF, perform a dry run of the migration wave.

1. **Test** – Test the target infrastructure. If you are using CMF, launching the Amazon Elastic Compute Cloud (Amazon EC2) instances in test mode. This helps ensure that the [machine conversion](https://docs.aws.amazon.com/mgn/latest/ug/AWS-Related-FAQ.html#What-Conversion-Server-Do) process is successful and the instances pass the [instance status checks](https://aws.amazon.com/blogs/aws/ec2-instance-status-checks/).

1. **Cutover** – The source servers are shut down, and the target servers are launched in AWS. If you are using CMF, launch the EC2 instances in cutover mode. This phase causes an outage window for the applications that are being cutover, so you should schedule this phase accordingly to minimize the business impact.

1. **Cutover validation** – After the EC2 instances are initialized on AWS, the application owners test the applications on the target servers and confirm they are ready to go live. This phase occurs immediately after cutover and during the cutover window.

1. **Handover and signoff** –** **After applications have successfully migrated and meet the criteria for handoff, the migration team transfers responsibility to the cloud operations (Cloud Ops) team or a managed service provider. At this time, the wave is considered complete.

After you define the tasks, you need to understand the lead time for each. When you understand how long each task takes, you can incorporate that information into the T-minus schedule. For more information about the T-minus schedule, see [Application owner communications](communication-delivery-layers.md#app-owner-communications).

Finally, it is important to ensure coordination between the different teams. This helps address emerging issues and obstacles for the migration. All teams must work towards the same, single goal, and their individual schedules must align with the wave plans to complete the migration on time.

## Project management team responsibilities
<a name="pm-responsibilities"></a>

Your project management team should do the following to foster alignment and drive workstream ownership:
+ Define roles and responsibilities early to clearly specify ownership for all tasks.
+ Develop a regular communication cadence to help ensure that all team members are actively participating in key meetings.
+ Use the escalation process when a participant is not meeting their commitments.
