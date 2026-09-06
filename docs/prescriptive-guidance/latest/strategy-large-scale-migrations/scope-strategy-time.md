---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/scope-strategy-time.html
---

# Scope, strategy, and timeline
<a name="scope-strategy-time"></a>

Three key elements make up the building blocks of all programs and their relevance in large migrations: scope, strategy, and the timeline.

![image.png](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/images/guide-img/5d21bc8a-8f8a-4dd9-a6cb-7df7164767ad/images/d587b6c2-8d64-4dd5-883f-b9e9d63cb4c7.png)

To set the stage for your migration journey, these elements must be aligned and understood from the start of a migration program. Any changes to one of these elements will affect the others. Realignment must be factored into every change, no matter how basic or sensible the change might seem.

## Scope – What are you migrating?
<a name="scope"></a>

It's common for the total scope of the program to be undefined, even when you're half way through the migration. This is because various factors might not be unpacked until the later stages. For example, halfway through your migration, you might uncover a pocket of shadow IT that was not recorded in your configuration management database (CMDB). Alternatively, the planning might have focused on a server view without considering the supporting network and security services that are required for those applications to run (such as VPN connections to AWS Partners, and certificate authorities to sign certificates). We recommend investing some time in defining the scope, working backwards from your target business outcome. You might end up using discovery tooling to uncover assets, a best practice that will be discussed later in this guide.

The scope will change, because large migrations come with unknowns. These unknowns could be in the form of systems that have become part of the archeology of the environment with little to no understanding of their relevance, or production incidents that cause delays and shifts to the plans you have made. The key is to be flexible and have contingency plans in place to keep the program moving forward.

## Strategy – Why do you want to migrate?
<a name="strategy"></a>

You might be planning to migrate to AWS for one or more of the following reasons:
+ Your application teams want to implement new CI/CD pipelines, deploy the latest application stacks, or modernize legacy platforms that are out of support.
+ Your infrastructure team must get out of an aging data center quickly before the lease expires and the provider turns the power off.
+ The board has decided that you need to move to the cloud as a strategic direction, allowing for a fast pace of change in the business's future.

Whatever the reason, all these reasons and more will be on the minds of your business and IT organizations. It's key to understand what your drivers are, to communicate them, and to prioritize them. Each additional driver potentially adds time, costs, scope, and risks to your already-large migration. Being fully aware of the impact that the strategy has on the timeline and scope is key.

After you define your migration strategy, one of the main keys to success is alignment of requirements across the various stakeholders and teams. Performing the migration requires different teams across the organization, including Infrastructure, Security, Application, and Operations. These teams will have individual priorities and other projects that might have already commenced. If these teams are working toward different timelines and priorities, it's more challenging to agree on and implement a migration plan. The migration team and key stakeholders must ensure that all involved teams work toward a single goal and align their priorities with a single timeline of migrations.

We recommend exploring how the desired business outcomes can be aligned across the various teams. For example, migrating to AWS and using AWS Key Management Service (AWS KMS) to encrypt storage at rest might satisfy both the migration and security goals.

Frequently, businesses want to modernize applications, which can result in infrastructure upgrades, while the infrastructure team wants to be frugal and minimize infrastructure changes. The mindset for large migrations should be as basic as possible. The teams involved must avoid trying to do everything at once.

To achieve this, set the right expectations early in the project. The key message should be "Migrate first, then modernize." This approach not only enables organizations to reduce technical debt and operate at scale eventually, it opens avenues for different modernization approaches by using the scalability and agility that the AWS Cloud can provide. Thinking long term will help infrastructure teams to streamline infrastructure deployment and management. As a result the business can have faster feature release cycles.

## Timeline – When do you need to complete the migration?
<a name="timeline"></a>

Depending on your business case, you must ensure you are not taking on more than is possible to achieve in the time allocated. If your driver for migrating is based on a fixed date of completion, you must choose the strategy that meets that timeline requirement. Most large migrations are based on these time-based constraints, so the migration strategies must have defined, fixed timelines and outcomes, with little room for extensions or overrun.

In these time-sensitive types of migrations, we recommend the "Migrate first, then modernize" approach. This helps set expectations and encourages the teams to ensure that their individual project plans and budgets are aligned with the overall migration goal. It's important to find out any disagreements as early as possible in the project, fail fast and address the disagreements at the Steering Committee level, and engage the right stakeholders to ensure that alignment is in place.

Conversely, if your main goal of migration is to gain the benefits of application modernization, this must be called out early in the program. Many programs start with an initial goal based on a fixed deadline, and they don't plan for the requirements from stakeholders who want to resolve outstanding issues and problems. In some cases, these issues have been present for years in the source systems, but now they become artificial blockers to migration.

Modernization activities during a migration can affect the functionality of business applications. Even what is perceived to be a small upgrade, such as an operating system version change, can have a major effect on the program timelines. These should not be considered trivial.
