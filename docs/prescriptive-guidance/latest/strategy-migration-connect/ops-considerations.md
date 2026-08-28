---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/ops-considerations.html
---

# Operational considerations
<a name="ops-considerations"></a>

The best practices in this section focus on smoothing operations and keeping end-users happy with the new contact center platform and processes so they can provide constructive feedback. If end-users feel ignored or under-valued during the project, they will be reluctant to move to the new platform. If end-users are unhappy, the migration will be considered a failure regardless of how well the technology performs.

**Shifting to soft phones **– Will this be the first time agents use a soft phone, which provides the phone interface on the screen, because they currently control calls through a physical desk phone? If so, it might be difficult for agents to transition from pressing buttons on a desk phone to using a soft phone keypad on a PC.
+ Make sure that adjustment time is included in the training schedule. Expect a learning curve after the new contact center goes live.
+ Accessibility might be a concern for agents who are used to desk phones, which are tactile devices. Consult agents who have accessibility concerns and include their feedback in design specifications for the soft phone color scheme and keypad button sizes.

**Desk phone alternative **– Agents can have calls delivered to a desk phone, as explained in the Amazon Connect Customer [setup instructions](https://docs.aws.amazon.com/connect/latest/adminguide/configure-agents.html), as an alternative to a soft phone. This alternative handset must have a publicly reachable phone number, which is then configured in the agent profile. For example, this can be useful when a remote internet connection cannot support high-quality audio on the soft phone audio. In this case, the audio is sent across the traditional (PSTN) phone network.

**Device inventory** – Ensure that end-users have the right equipment on the day the new contact center goes live:
+ Desk phones are no longer needed, so they can be decommissioned to free up desk space.
+ Devices (such as laptops) might need Ethernet dongles to support hardwired Ethernet connections. Issue these to users before the go-live date to avoid last-minute demands that will affect your local IT parts team.
+ Devices might have to provide faster CPU and more memory to run soft phone and business applications in parallel. Perform real-life testing (during UAT) with end-users by using the soft phone *alongside *their usual applications, to see if devices remain performant.

**Support model** (raising support tickets, levels 1-3 technical support desk ownership) – Work with your AWS account team, such as your technical account manager (TAM), to verify that you're on the most suitable [AWS support plan](https://aws.amazon.com/premiumsupport/plans/). Make sure that everyone knows their role in the support model―from receiving incident reports from end-users to raising incident bridges for business-critical issues. Simulate an issue by raising a test incident to the level 1 support desk and tracking it through support model processes. This will help you find gaps in the support model, so you can avoid issues after you go live.

**Back office** – Consider how tasks will flow between front-office agents and back-office teams. For example, the process for transferring calls and escalating customer cases might change. Include task workflows and routing in your test scripts.

**Billing **– AWS billing costs will increase and legacy platform costs will decrease immediately after the new contact center goes live. Contact center charges will be subsumed into AWS billing after migration. Notify your finance and accounting teams of this change so that costs from AWS accounts that host Connect Customer instances can be mapped to the appropriate business unit. This is likely the same business unit that's responsible for legacy platform charges.

**Access permissions** – You can provide granular permissions to your contact center users by creating [security profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in Connect Customer. This feature enables you to create advanced user access models based on the principle of least privilege to perform a role. On legacy platforms, permissions are typically granted too broadly. In contrast, in Connect Customer, you can give users access to very specific resources and activities. For example, you can grant employees permission to edit users but not create or delete them, or to view user journey contact flows but not change them. Granular permissions are a powerful way to improve user engagement and optimize how responsibilities are distributed across roles and (such as agents, operators, supervisors, and developers) and teams. In addition to using security profiles, you can use Connect Customer with AWS Identity and Access Management (IAM) features and polices. For more information, see [How Connect Customer works with IAM](https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_service-with-iam.html) in the Connect Customer documentation.

**Service quotas** – Service quotas are default settings that protect you from unexpected load and consumption charges. For example, service quotas can limit you to 10 concurrent calls or 5 phone numbers per instance. We recommend that you view your service quotas and request increases to support your expected usage. For more information, see [Connect Customer service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html).

**Agility through DevOps** – Use a DevOps deployment pipeline to accelerate your release schedules and deliver new features more frequently. Business owners might have to reset expectations on how quickly they can release software, because the technology is more agile. Using deployment pipelines enables you to release smaller code bundles more frequently, so your releases are less risky and reach your customers faster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
