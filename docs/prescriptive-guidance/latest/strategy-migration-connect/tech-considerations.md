---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/tech-considerations.html
---

# Technical considerations
<a name="tech-considerations"></a>

For more information about the following technical best practices and additional recommendations, see [Best practices for Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/best-practices.html) in the Connect Customer documentation.

**Voice traffic path** – Will audio streams travel across your corporate internet link, or should you use an AWS Direct Connect connection as a dedicated link? AWS Direct Connect avoids latency-sensitive voice traffic competing with general traffic across data center internet pipes such as web browsing and email.

**Setting up your network** – A healthy end-to-end network connection is essential for a consistent and stable user experience. You should consider every component, from the agent's device, through their local network connection and virtual private network (VPN), if applicable, to Connect Customer. A network connection is only as healthy as its weakest link. To optimize your network for Connect Customer, review [Set up your network](https://docs.aws.amazon.com/connect/latest/adminguide/ccp-networking.html) in the Connect Customer documentation.

**Remote agents** – Do your agents use a VPN when they work from home? If so, consider enabling VPN split tunneling for voice traffic. This routes delay-sensitive voice traffic across the local internet instead of sending it back to the data center and routing it out to Connect Customer over the internet. If you don't use split tunneling, latency is needlessly increased (resulting in delayed audio or sluggish soft-phone actions), additional traffic load is placed on the VPN concentrator device, and your data center internet ingress and egress charges go up.

**Data migration **– For data such as call recordings and reporting statistics, consider two approaches:
+ Migrate the data to the new platform. This requires planning and feasibility assessment (for example, to check audio format compatibility), but means that you can access your legacy data from a single portal on the new platform.
+ Archive your data in place and decommission it when the minimum retention period expires. This might be more cost-effective, especially if data is stored on a purchased platform and accessed infrequently so that having two portals to browse old and new data is a practical option.

**Number porting**
+ Consider whether a non-geographic number (NGN) or toll-free number service (TFNS) provider is required. Porting toll-free, local rate, or direct-dial-in (DDI) numbers to Connect Customer allows for centralized management and billing of the end-to-end call. Consider the current charging model for your NGN/TFNS service and compare it with Connect Customer charges. Be mindful of charges for calls that are made outside operating hours. Some NGN/TFNS providers do not charge for these calls if they handle the out-of-hours check and messaging. NGN/TFNS contracts and terms vary, so collect the information carefully to perform an accurate comparison.
+ Timelines for number porting can take several weeks, so file the porting request through a ticket as early as possible. Use the ticket to finalize a cutover date and time. If there are challenges with the timeline, temporarily set a number forwarding transfer from your existing telephony queue to the new Connect Customer phone number, as detailed in cutover option below.

**Cutover approaches for porting numbers**

You can use NGN backend repointing or number porting to port phone numbers.

*NGN backend repointing* – Perform a backend repoint of the frontend NGN number to the inbound number (DDI) hosted on Connect Customer, as shown in the following diagram. This does not require any public-facing number changes and is typically managed as a service request ticket to the NGN carrier provider. Repointing can be scheduled for a specific date and time.

![NGN backend repointing](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/d40b39c7-f86e-48ed-8be2-575306f99f9f.png)

*Number porting* – This process consists of two stages:
+ Number forwarding – This optional step, illustrated in the following diagram, directs traffic from the old platform to the new platform without changing the public-facing number. You can complete this step before your scheduled number porting date. This expedites the migration of agents onto the new platform in parallel with the number porting process. It also allows for rapid rollback (which depends on a relatively simple change to call forwarding rules) without any dependencies on a carrier. However, we recommend not leaving number forwarding in place for a long period of time, because it increases call charges (you pay for inbound traffic on DDI-1, outbound forwarding, and inbound traffic on the new DDI-2) and consumes infrastructure capacity (each inbound call also consumes an outbound circuit for the forwarding path).

![Number forwarding as first step in porting call center numbers](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/216b6060-dcd9-4457-a9d4-ccde4a74626e.png)

+ Completion of number porting – On an agreed date and time, the carrier for DDI-1 ports the number to AWS, so it becomes available for Connect Customer to use, as illustrated in the following diagram. You can then assign the number to user journeys or functions, and manage it as if it were a natively sourced DDI in AWS. This simplifies billing and provides flexibility, because you can manage telephone numbers in the Connect Customer console instead of relying on a third-party carrier to process service requests.

![Completion of number porting for call center migrations](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/777abc21-38fd-4e22-9679-896a9033d56e.png)

**Transferring calls between other platforms and Amazon Connect **–** **Organizations often migrate agents to Connect Customer in groups based on line of business, job type, or other criteria. During a period of time, agent groups on other platforms are progressively migrated to Connect Customer. Depending on the number and size of the groups, the migration phase might take several months, and teams that are spread across different platforms might have to transfer calls to each other during this period.

To transfer calls between platforms, use PSTN DDI numbers. Assign these DDIs only for cross-platform transfer usage, so you can measure and report on transfers independently, and prioritize calls differently if required.

Consider whether call attached data has to be exchanged between platforms during transfers. For example, if a caller has passed security checks on one platform, their security status should be exchanged during the call transfer to prevent them from having to go through security again with an agent on Connect Customer. There are two approaches to consider:
+ **Transfers without call attached data** - Structure migration group phasing to reduce the operational need for transfers where call attached data would be necessary. For example, migrate teams that frequently transfer calls to each other together, after a caller has exchanged a significant amount of data, which would otherwise need to be recaptured. If a caller interacts only minimally with IVRs or agents before being transferred across platforms, it might be unnecessary to exchange call attached data. You should also consider expediting migration timelines to minimize the period when cross-platform transfers would be performed. This means accepting a temporary inconvenience in exchange for not having to build technical debt and manage a cross-platform data exchange solution that will no longer be required after migrations are complete.
+ **Transfers with call attached data** - This approach is relevant for teams that will be spread across platforms for a significant period of time and need to have call attached data exchanged during transfers to maintain operational performance. Use a technique called *rolling dialed number identification service (DNIS)*. For an example of how you can get started with rolling DNIS, see the GitHub repository [Transfers from Legacy Platform into Connect Customer](https://github.com/aws-samples/Transfers_from_Legacy_Platform_into_Amazon_Connect).

**Separate AWS accounts **– Set up different AWS accounts for your Connect Customer development, testing, and production instances. This approach separates those activities and limits the impact of changes to a single account. It also provides billing boundaries so that the appropriate business unit can pay for development, testing, and production work.

You can create new accounts with specific policies, rules, and principles, based on predefined templates. This means that any build or configuration in that account will have to comply with the specifications defined by the organization. You can use [AWS Organizations](https://aws.amazon.com/organizations/) to centrally manage and govern accounts.

**Logging and alerting** – Enable Amazon CloudWatch Logs to track usage thresholds and errors in contact flows. You can view usage and errors by using CloudWatch dashboards. You can also proactively send alerts through email or SMS text messages. By gaining visibility into low-level system behavior, you can identify and resolve issues quickly before they become bigger problems. An example of a proactive alerting solution for Connect Customer is described in the blog post [Monitor and trigger alerts using Amazon CloudWatch for Connect Customer](https://aws.amazon.com/blogs/contact-center/monitor-and-trigger-alerts-using-amazon-cloudwatch-for-amazon-connect/).

**Single sign-on (SSO)** – Use SSO to enable users to log in to Connect Customer by using their corporate credentials (for example, through Active Directory) instead of requiring a separate username and password. This provides the optimum user experience because it doesn't require an additional login step or another set of credentials. It also avoids the need to centrally manage separate login credentials for password resets and other operations. Connect Customer supports a number of identity management integration patterns. For more information, see [Plan your identity management in Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/connect-identity-management.html) in the Connect Customer documentation.

**Workstation devices** – Verify that end-user (for example, agent and supervisor) machines meet the minimum CPU and memory requirements noted in the [Agent headset and workstation requirements for the CCP](https://docs.aws.amazon.com/connect/latest/adminguide/ccp-agent-hardware.html) section of the Connect Customer documentation. If you're planning to use these workstations for tasks outside contact center work, they should meet higher requirements. Use the Connect Customer [Endpoint Test Utility](https://docs.aws.amazon.com/connect/latest/adminguide/check-connectivity-tool.html) to check device and network compatibility. We recommend that you run this utility on a variety of agent workstations at different locations, including agents who are working from home or from distinct network-island locations, to ensure compatibility across your organization.

**Virtual desktop infrastructure (VDI) environments **– Consider [network ](https://docs.aws.amazon.com/connect/latest/adminguide/using-ccp-vdi.html)and [deployment ](https://docs.aws.amazon.com/connect/latest/adminguide/scenario-deployment-approaches.html)optimizations for virtual desktop users.

**Headsets **– Use wired USB-powered headsets to ensure a consistent audio experience. Discourage the use of bluetooth or wireless headsets, which can add latency and reduce audio quality.

**Wired network connectio**ns – Devices should use wired (Ethernet) connections to ensure a stable, high-quality audio experience. Verify that devices have wired ports. If a dongle is required, it must be budgeted and procured before migration.

**Microphone and speaker** **settings **– If your organization uses multi-purpose devices, confirm that shared use of microphones and speakers is allowed (turn off exclusive mode). For guidance, see [One-way audio from customers?](https://docs.aws.amazon.com/connect/latest/adminguide/one-way-audio-from-customers.html) in the Connect Customer documentation. This guidance applies to both speakers and microphones.

**Dedicated devices **(ideal) – If possible, users should be given devices for exclusive contact center use. You can then optimize these devices for the contact center experience, and use different devices for other duties.

**Legacy habits** – Watch out for legacy user behavior that might affect new processes. For example:
+ Do agent devices predominantly connect over Wi-Fi today? If so, requiring wired connections will be a cultural shift for agents and might lead to poor compliance and call experience. An end-user education campaign might be required to drive this culture shift.
+ Do agents use other collaboration applications (such as Microsoft Teams or Zoom) on their devices? This can lead to conflicting demands for speaker and microphone devices on the device, such as when Connect Customer tries to deliver an incoming call while the agent is on another call. It can also lead to agents missing customer calls because they are busy making internal calls. We recommend removing other collaboration applications, where practical, to avoid call clashes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
