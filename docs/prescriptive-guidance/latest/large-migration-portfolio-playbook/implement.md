---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/implement.html
---

# Stage 2: Implementing a large migration
<a name="implement"></a>

In stage 1, *initializing a large migration*, you defined the portfolio assessment and wave planning processes and documented them in runbooks. In stage 2, *implementing a large migration*, you complete these processes and repeat them for each sprint until the migration is complete.

The portfolio team completes the following portfolio assessment and wave planning tasks in stage 2:
+ [Task 1: Prioritizing the applications](implement-prioritization.md)
+ [Task 2: Performing the application deep dive](implement-deep-dive.md)
+ [Task 3: Performing wave planning and metadata collection](implement-wave-planning.md)

**Note**
Portfolio assessment and wave planning is not a one-off task. It is a continuous task that supports the migration. You repeat all the tasks in this stage many times until the migration is complete.

The portfolio assessment and wave planning process typically requires 1–2 weeks for each wave. The portfolio workstream typically plans 4–5 waves in advance to maintain a healthy pipeline of servers for the migration workstream. The portfolio workstream begins planning waves at the end of the initialization stage (stage 1), and the implementation stage (stage 2) begins when the migration workstream begins migrating the first wave of applications. For an example of a wave schedule, see [Stage 2: Implement a large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/stage2.html) in the *Guide for AWS large migrations*.

## Tracking progress
<a name="tracking-progress"></a>

As you begin preparing waves for migration, we recommend that you track the status of each application through the portfolio assessment process. You can use the attached *Progress tracking template for portfolio assessment* (Microsoft Excel format). This template allows you to track the following for each application: complexity score, target wave, application owner, target completion dates for the primary tasks (application prioritization, deep dive, wave planning, and data collection), and the overall readiness of the application for migration. The guidance in this playbook includes instructions for when to update the progress tracking sheet.
