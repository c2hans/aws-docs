---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/portfolio-discovery-initial-planning.html
---

# Discovery acceleration and initial planning
<a name="portfolio-discovery-initial-planning"></a>

This stage of portfolio assessment occurs early in the cloud journey. It's typically performed close to an executive decision to move an existent portfolio of applications to the cloud or during exploratory phases. The discovery acceleration and initial planning stage focuses on the following:
+ Understanding business drivers
+ Identifying existent sources of data
+ Evaluating the need for automated discovery tooling
+ Establishing base models for application prioritization and migration strategy selection

These activities lead to the following:
+ A preliminary analysis of the portfolio
+ Identification of initial migration candidates
+ The creation of a directional business case for migration
+ An outline of initial plans.

The key is to understand who the stakeholders of this stage are and what data requirements they have for moving forward. Stakeholders range from board members and CxOs, to business unit leads, senior managers, and application owners.

**Tip**
** **For details and guidance, see the relevant section in the [Application portfolio assessment guide for AWS Cloud migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/portfolio-discovery-initial-planning.html).

## High-level objectives and actions
<a name="discovery-objectives"></a>
+ Determine stakeholders – Who is impacted by the migration? Who are the decision-makers? Who benefits from this migration? Who is responsible for performing the migration?
+ Identify business drivers – What business outcomes and goals are being pursued as a result of migration (for example, business transformation, cost reduction, agility)? This information will be a key determinant of migration strategy and prioritization.
+ Identify existing sources of data – Identify and document existing sources of data, such as people, tooling, documentation. Assign a level of trust to each source. For example, programmatic or automated sources are more trusted than institutional knowledge or documents. Over time, lower-trust data sources will be replaced with higher-trust data sources.
+ Build an initial inventory of applications and infrastructure – Identify application names, primary function, criticality, IT environments, high-level compliance and regulatory requirements, and known dependencies. Which IT assets are associated to the applications? Identify product names and versions, historic performance data, known issues, and risks.
+ Identify data gaps and discovery needs – Analyze data gaps and evaluate the need to procure automated discovery tooling. Discovery tool investment decisions should be backed by a need to increase overall confidence in data for accurate analysis. To maintain an up-to-date view of the application portfolio, we recommend specialized tooling for workload discovery.
+ Deploy discovery tooling – Procure, install, and configure discovery tooling, if applicable, and create a roll-out plan to targeted systems. Two weeks of programmatic data collection to all targeted systems provide enough data to achieve the outcomes of this stage. However, to refine the outputs, ongoing data collection is required in later stages.
+ Collect Total Cost of Ownership (TCO) data – Use collected data to produce and update TCO reports and to create a directional business case. For more information, see the [Best practices](#discovery-best-practices) section.
+ Use application-rationalization models – Establish or adopt base application rationalization models for migration. Include the selection of key application attributes, weighting for prioritization, and initial R type (rehost, replatform, refactor (re-architect), repurchase, retain, retire) based on the 6 Rs decision tree.
+ Identify initial migration candidates – What applications could be moved now to establish or extend AWS foundations and gain experience? At this stage, the model should prioritize simple workloads with low levels of dependencies (for example, zero-three).
+ Plan ongoing assessments – Plan for the next portfolio assessment activities, such as performing a detailed assessment of prioritized workloads.
+ Plan communications – Establish a communication plan or cadence for your stakeholders and a scope-control mechanism. It is normal for the scope to change as the migration program progresses. Ensure that there is a single source of truth for portfolio data and that changes to the scope are tracked, assessed, and communicated.

## Outcomes
<a name="discovery-outcomes"></a>
+ Documented business drivers, outcomes, goals, and technical guiding principles.
+ An initial inventory of applications and infrastructure, and identified data gaps. This is an initial view of the portfolio that will be iterated and refined in further stages.
+ A directional business case and estimated cost to migrate.
+ A list of three-five applications that are initial migration candidates.
+ A communication plan for portfolio-related activities, milestones, and scope changes.

## Best practices
<a name="discovery-best-practices"></a>
+ Focus on the stage objectives and keep analysis at a high level. Adopt a progressive approach to data collection, and do not wait for a complete dataset before moving forward.
+ Avoid analysis paralysis. Focus on identifying the data gaps and driving actions to close those gaps.
+ Procure specialized discovery tooling. Programmatic data, typically obtained through automated tooling, has the higher level of trust and should be preferred before written documentation, static data, and institutional knowledge.
+ Work with the identified stakeholders to remove blockers.
+ Assign a single-threaded leader to the application portfolio assessment workstream.
+ Consider using [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) for your directional business case, or explore the AWS Partner Network tools and offerings for [TCO and AWS pricing](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-pricingtco-tools.html).
+ Consider [AWS Professional Services](https://aws.amazon.com/professional-services/) and [AWS Partners](https://partners.amazonaws.com/) that could help you accelerate business outcomes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
