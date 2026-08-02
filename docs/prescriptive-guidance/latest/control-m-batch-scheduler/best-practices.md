---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/best-practices.html
---

# Best practices
<a name="best-practices"></a>

During the initial planning and integration stages, we recommend the following best practices:
+ Before integration, thoroughly understand the workload and processes that need to be migrated or automated. This helps in identifying the most critical jobs for migration and in planning their scheduling and automation using Control-M.
+ When migrating mainframe workloads to AWS, plan for their automation with Control-M from the start. Consider how jobs and workflows will be scheduled, managed, and monitored in the cloud environment.
+ We recommend using centralized connection profiles because this approach reduces the number of objects to manage and simplifies elastic deployment of Control-M Agents.
+ When possible, perform mainframe migration incrementally to reduce complexity and risk. By doing incremental migration, migration teams can provide faster feedback regarding the migration progress. Businesses can use that feedback to optimize internal processes to accelerate the pace of migration.
+ To avoid unnecessary work, consider using the provided templates for job type and connection profile for initial stages.
