---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/portfolio-analysis-migration-planning.html
---

# Portfolio analysis and migration planning
<a name="portfolio-analysis-migration-planning"></a>

This stage focuses on iterating the portfolio-level view, closing data gaps, and obtaining more data to produce high-confidence migration wave plans for the entire portfolio.

The stakeholders of this stage are typically a mix of the previous two stages. They include CxOs and senior leaders, migration and platform teams, and IT and Enterprise architects. The key is to augment the portfolio-level data fidelity through iteration and refinement.

**Tip**
For details and guidance, see the relevant section in the [Application portfolio assessment guide for AWS Cloud migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/portfolio-analysis-migration-planning.html).

## High-level objectives and actions
<a name="analysis-objectives"></a>
+ Establish a baseline for the application portfolio and associated infrastructure – Iterate portfolio-level data, building up from the [discovery acceleration and initial planning](portfolio-discovery-initial-planning.md) stage, to close gaps and produce a high-level view of the entire application portfolio. At this stage, it is key to refine application-to-infrastructure mapping, usage data, and application metadata attributes. These attributes include ownership, criticality, and the primary function of each application.
+ Obtain and analyze dependency data (typically by using specialized discovery tooling) – To validate applications and aid the creation of migration wave plans, high-confidence application-dependency data is key at this stage. Dependency data includes communication data, such as volume and frequency of communication between systems, and nontechnical dependencies, such as operational considerations. These dependencies dictate which applications must move at the same time and which applications can operate from different locations.
+ Identify and validate compliance and regulatory requirements – Identify and validate frameworks, rules, evidence, and documentation requirements.
+ Convert assumptions into facts – How much has been assumed in previous stages? It is key in this stage to reduce the number of assumptions to a minimum.
+ Establish a baseline for the migration portfolio-rationalization models – Iterate models from previous stages (for example, application prioritization criteria and the 6 Rs decision tree). Validate the models by applying them to the entire application portfolio.
+ Document measurable business outcomes – To align migration waves to business objectives, identify business outcomes and associated key primary indicators (KPI) for each migration wave.
+ Evolve the directional business case – Replace benchmarks with actual utilization and cost data, and refine migration costs in line with the updated wave plan. Broaden the coverage to include the full expected value from each expected business outcome, such as cost reduction, IT productivity improvement, increased resilience, and greater agility.
+ Document and communicate key dates – Document and communicate compelling events (such as data center exit dates, contracts and licensing agreement renewals), application release cycles, migration dates to avoid, technology refresh cycles, and people availability.
+ Analyze cost and risk for wave planning – How much parallel change can be supported or tolerated? Analyze people requirements, risks identification and mitigation, criticality, and impact.
+ Identify skills requirements – What is the projected level of readiness to support the different workload types in the cloud? Does the migration wave plan align to the projected readiness? Can the support teams meet the wave plan requirements?
+ Document internal processes – Document information about current processes impacting cloud migration, such as change management, service management, architectural review boards, risk assessments, and approval workflows.
+ Create a migration wave plan – To create a wave plan, combine all the elements previously discussed in this list. Apply prioritization criteria to the portfolio, and analyze dependencies to create waves of applications. Incorporate platform and migration readiness into the migration wave plan. How long does it take to implement AWS infrastructure and services? What is required for security and operational readiness? What is the impact to the wave duration? How long does it take to implement migration tooling? How long does it take to replicate data, considering network and systems usage? What is the cutover window? How long does it take to roll back?
+ Update workstreams – Establish a process to feed portfolio and detailed application assessment data into Migration and Landing Zone workstreams. Ensure these workstreams clearly outline their data requirements.

## Outcomes
<a name="analysis-outcomes"></a>
+ High-fidelity application and infrastructure inventory
+ High-level migration strategy for each application
+ Detailed business case
+ High-confidence migration wave plan

## Best practices
<a name="analysis-best-practices"></a>
+ Ensure that applications are evenly distributed in the migration wave plan. Consider criticality and complexity to avoid pockets of complexity that could create blockers or delay migrations.
+ Prioritize noncritical, simple applications in the first two waves.
+ Focus on combining prioritization, dependencies, and business drivers to iterate the wave plan.
+ Consider cloud infrastructure, security, and operational readiness (including skills) when creating the wave plan.
+ Construct wave plans so that the length of a migration wave, typically ranging 4-8 weeks, outlines the application journey. Each wave should cover the following:
  + Detailed assessment
  + Migration readiness
  + Infrastructure build and test
  + Data transfer
  + Cutover of the applications in the wave
  + Wave closure (for example, lessons learned, post-migration issues resolution)

Define and use a default wave structure to apply a migration [factory model ](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/)that includes detailed assessment, design, implementation, test, cutover, and validation.
