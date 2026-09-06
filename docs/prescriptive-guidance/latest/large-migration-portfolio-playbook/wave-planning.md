---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/wave-planning.html
---

# Task 5: Defining the wave planning process
<a name="wave-planning"></a>

Wave planning is a key milestone in a large migration. In a wave plan, you group similar applications together, accounting for infrastructure and application dependencies (such as a shared database), the priority of the applications, similarity of application architecture, and business functionality. You then review the wave plan with the application and infrastructure teams to confirm their availability during the specified migration and cutover window.

Based on real-life deployments for various AWS customers, the following are some of the best practices for wave planning:
+ Plan migration waves at least 4–5 waves in advance. This helps ensure that there are always enough servers for the migration workstream.
+ Fail fast. You should start with a few, low-complexity applications and apply your learnings to later waves.
+ In early waves (waves 1–5), select fewer servers (less than 10), low-complexity applications, and applications in lower environments, such as development or test environments. Gradually introduce more complexity and more servers into the waves as you progress.
+ Wave planning is an ongoing process, not a one-off task. Do not try to plan all waves at once.
+ If you are using a portfolio discovery tool and it has a complexity scoring feature, use it in wave planning. Migrate the applications with the lowest complexity first.

This task consists of the following steps:
+ [Step 1: Define the move group process](#wave-planning-1)
+ [Step 2: Define the wave planning selection criteria](#wave-planning-2)
+ [Step 3: Finalize the wave planning process](#wave-planning-3)

## Step 1: Define the move group process
<a name="wave-planning-1"></a>

In this step, you identify any application-to-server dependencies and define the rules that will be used to determine which servers should be moved together, as a move group. A *move group* is a block of servers or applications that should be **moved** together in a **group**. This is the building block of a migration wave, where each wave consists of one or more move groups, depending on the number of servers in each move group.

### Identify the application dependencies
<a name="identify-the-application-dependencies.9b953bed-55e4-561a-abe4-69943224f1c5"></a>

The following are key considerations when grouping interdependent applications in a move group:
+ Consider infrastructure dependencies, such as:
  + An application might have multiple databases, and those databases could be shared by other applications.
  + An application might be dependent on another application.
  + A server might host databases for multiple applications.
+ Consider business and operational dependencies, such as:
  + Due to a business impact or operational schedule (such as backup or patching), an application can only be migrated during a certain window.
  + An application owner is available only for one migration cutover window, so all of the owner's applications must be in the same move group.

You identified infrastructure dependencies in the application workshop process or when you defined the target state. You can identify infrastructure dependencies through automated or manual processes. To automate identification of infrastructure dependencies, you can use a discovery tool, such as Flexera One Cloud Migration and Modernization or TDS TransitionManager. For a manual process, validate CMDB information with the application and infrastructure teams.

You identified business and operational dependencies in the application workshop process.

As a starting point for building your own wave planning runbook, we recommend that you use the attached *Runbook template for wave planning* (Microsoft Word format). Document the dependencies for your migration as follows:

1. Open your wave planning runbook.

1. In the *Application dependencies* section, record the dependency. Identify the type (infrastructure, business, or operational), the dependency, and a brief description of the dependency.

1. Save the wave planning runbook.

1. Maintain the dependencies in the wave planning runbook. As you progress, you might identify new dependencies.

The following table shows example dependencies.

|
|
| Type | Dependency | Description |
| --- |--- |--- |
| Infrastructure | Database | A database is shared with other applications |
| Infrastructure | File store | The application uses a central file store that can be decoupled, or all associated applications should migrate together |
| Infrastructure | Application | The application depends on one or more other applications to function, such as extract, transform, and load (ETL) jobs |
| Business | Business outage | Specific and approved outage windows for the application |
| Operational | Patch window | Scheduled operational tasks, such as patching, that can impact migration cutover |

### Define the move group rules
<a name="define-the-move-group-rules.307a9665-94d2-51c5-8e73-9ddca1b7c2cf"></a>

After you record the dependencies in your wave planning runbook, you must build move group rules based on those dependencies. These rules govern how servers are grouped together into move groups. Use the following steps to build your rules:

1. Review the dependencies you defined in the previous section.

1. Choose the dependencies that affect whether applications must be moved together, in a move group. Not all dependencies require applications to be migrated together. For example, an infrastructure dependency on Microsoft Active Directory should not be considered when defining move groups because it is a common dependency for all applications. You should build a domain controller in the cloud before migrating any applications.

1. Convert the dependencies that require the applications to be moved together to a move group rule.

If an application matches any of the rules, then all of the associated servers must be placed in the same move group so that they are migrated together.

Document the move group rules for your migration as follows:

1. Open your wave planning runbook.

1. In the *Move group rules* section, record the move group rules in order of priority.

1. Save the wave planning runbook.

1. Maintain the rules in the wave planning runbook. As you progress, you might identify new rules.

The following table shows example move group rules.

|
|
| Rule | Move group rule |
| --- |--- |
| 1 | Applications with a shared database must migrate together. |
| 2 | Applications that have the same application owner must migrate together. |
| 3 | Applications with the same patch window must migrate together. |

## Step 2: Define the wave planning selection criteria
<a name="wave-planning-2"></a>

After you have established move groups, you need to gather similar move groups together in order to form migration waves. In this step, you define the criteria that you use to select one or more move groups for each wave.

Understanding the size of each move group is critical to successful wave planning. The goal is to size each wave so that the migration remains agile and maintains a healthy pipeline of servers. Waves that are too large can be difficult to adapt to change in the migration plan, and waves that are too small might not provide sufficient servers to achieve the desired migration velocity.

We recommend that you consider the following criteria when sizing waves:
+ **Small first waves** – Initial waves should be smaller, with less than 10 servers, and then you can gradually increase the number of servers in each wave. This allows you to fail fast and build on lessons learned. For example, migrate an application with 3 servers before migrating an application with 20 servers.
+ **Resources** – Identify how many servers the migration team can migrate in a single wave. A standard measure is that a migration team of four architects can migrate up to 50 servers in a week for rehost patterns. Combine move groups to form migration waves that don't exceed the capacity of the migration team.
+ **Agility** – Waves must be adaptive to any changes in the migration plan. In the event that you must reschedule a server, you should be able to reschedule the entire move group of affected servers.
+ **Storage size** – Migrate smaller applications first. For example, migrate a 100 GB application before a 2 TB application.
+ **Application environment**– Migrate applications in lower environments, such as development or test environments, before applications in production environments.
+ **Application complexity** – Migrate less-complex applications with fewer external dependencies first.
+ **Criticality of the application** – Migrate non-critical applications before mission-critical applications.
+ **User base** – Migrate applications that have small user bases first. For example, migrate an application that has 10 users before an application that has 10,000 users.
+ **Network bandwidth** – The size of the wave should not exceed the network bandwidth. For more information, see your migration principles, which you defined according to the instructions in the [Foundation playbook for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/).

Document the selection criteria for wave planning as follows:

1. Open your wave planning runbook.

1. In the *Wave planning selection criteria* section, record the criteria you want to use for your migration.

1. Save the wave planning runbook.

1. Maintain the criteria in the wave planning runbook. As you progress, you might need to adjust the criteria or add new criteria.

The following table shows example wave planning selection criteria.

|
|
| Criteria | Description |
| --- |--- |
| Identify the least complex applications | Identify applications with higher complexity scores in the move groups. |
| Lower environment first | Non-critical applications within lower environments, such as development or test environments, must migrate first. Critical applications within production environments, such as those that generate revenue, must migrate last. |
| Fail fast | Form initial waves with less than 10 servers. |
| Migration team strength | Identify how many servers each migration team can cut over. |
| Combine similar move groups | Combine move groups based on commonalities. For example, the move groups might share the same application owner, source data center, or target AWS account. |
| Wave size | Waves should not exceed 50 servers in total. |

### Step exit criteria
<a name="step-exit-criteria.cd26136c-905e-5825-bc10-bf1dc4d76dec"></a>
+ You have identified the wave planning criteria for your use case and documented it in your wave planning runbook.

## Step 3: Finalize the wave planning process
<a name="wave-planning-3"></a>

Now that you have defined how to create move groups and established the criteria you used to combine move groups into migration waves, you must define the process for planning waves.  In this step, you update your wave planning runbook to record the complete wave planning process, and you confirm that you have a dashboard tool the team can use to record wave information.

In this step, we recommend that you use the attached *Dashboard template for wave planning and migration*. This template is designed to assist portfolio teams and serves as a starting point for collating data, helping to analyze application portfolios, identifying application-to-server dependencies, and eventually planning migration waves. You can modify this template as needed for your environment.

Document the wave planning process as follows:

1. Open the *Dashboard template for wave planning and migration*.

1. Modify the dashboard as needed for your use case. For example, you might add a worksheet for extracting server inventory, add a new pivot table or chart, or import source information by using the `VLOOKUP` function.

1. Save the dashboard template.

1. Open your wave planning runbook.

1. In the *Stage 2: Perform wave planning* section, modify the standard process provided to meet the needs of your use case.

1. Save the wave planning runbook.

1. Share your wave planning runbook with the team for review.

1. Maintain the process in the wave planning runbook. This process acts as a standard operating procedure for planning waves for your large migration.

## Task exit criteria
<a name="wave-planning-exit-criteria"></a>
+ You have documented the following in your wave planning runbook:
  + Application dependencies
  + Application move group rules, listed in order of priority
  + Wave planning selection criteria
  + Wave planning process
