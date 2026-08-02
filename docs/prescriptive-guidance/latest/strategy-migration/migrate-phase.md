---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/migrate-phase.html
---

# Migrate phase
<a name="migrate-phase"></a>

Migrations at scale consist of the building blocks, processes, tools, resources, and methodology defined and tested during the readiness and planning phase. After using the best practices and lessons learned from the earlier phases, you can implement a *migration factory*, which is a blueprint of scaling implementation and operations, through automation and agile delivery.

## Migration factory
<a name="migration-factory"></a>

In the scale-out phase of the migration project, you will have multiple teams operating concurrently. Some will support a large volume of migrations in the rehost and minor replatform patterns. These teams are referred to as a *migration factory*. Your migration factory will increase the speed of your migration plan, with multiple sprint teams working in parallel. 20-50 percent of an enterprise application portfolio consists of repeated patterns that can be optimized by a factory approach. This is an agile delivery model, and it is important to create a release management plan. Your plan should be based on current workloads and information generated during the readiness and planning phase. It should be continually optimized for future migration waves and future migration teams. We recommend that you have a backlog of applications that support three sprints for each team. This allows you to re-prioritize applications if you have problems that affect the schedule.

Larger and more complex applications often follow the refactor/re-architect pattern. They are generally conducted in planned release cycles by the application owner. The factory teams are self-sufficient and include five to six cross-functional roles. They include operations, business analysts and owners, migration engineers, developers, and DevOps professionals. The following are examples of specifically focused migration factory teams:
+ Rehost migration teams migrate high-volume, low-complexity applications that don't require material change. These teams leverage migration automation tools. This approach is integrated into patch-and-release management processes.
+ Replatform migration teams design and migrate applications that require a change of platform or a repeatable change in application architecture.
+ Refactor/re-architect migration team(s) design and migrate complex or core business applications that have many dependencies. In most cases, development and technical operations teams support this business capability. The migration becomes a release cycle or a few release cycles within the plan for that team. Many of these can be in flight, and the Cloud Business Office (CBO) is responsible for tracking timing, risks, and issues through the completion of the migration. This team owns the application migration process.

Considerations:
+ Perform a portfolio analysis to understand common patterns across all applications to help build repeatable work for the factory teams to implement efficiently.
+ Use an AWS Partner to help with resource constraints while your team supports regular business activities. AWS and the AWS Partner community can bring specialized resources for specific topics such as databases, application development, and migration tooling.

**How-to guide**
+ [Automating large-scale server migrations with Cloud Migration Factory](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/welcome.html)
