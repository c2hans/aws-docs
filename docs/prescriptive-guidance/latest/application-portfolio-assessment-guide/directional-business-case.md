---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/directional-business-case.html
---

# Creating a directional business case
<a name="directional-business-case"></a>

Stakeholders from across the business should understand and buy into the business case for transformation each step along the way.

In the early stages, it's important to quickly show enough potential value from a migration program, so that you can secure the resources needed to plan and establish the program. The directional business case is designed to provide reasonable confidence in achieving compelling business value with the limited data that can be collected early.

After the program is established, the business case is developed further. The detailed case provides greater accuracy, a more complete picture of the program value, and insight into planning priorities. It defines and quantifies the planned business outcomes that the organization buys into, and it sets the baseline against which your program governance office can then steer the program and measure its achievements.

## Fixing the scope of the directional business case
<a name="fix-scope"></a>

A directional business case is typically assembled rapidly, within 2–4 weeks. It needs to generate enough confidence so that you can secure the resources to establish the core team, engage AWS Partners if needed, and as a minimum, complete the [prioritized applications assessment](prioritized-applications-assessment.md) and [portfolio analysis and migration planning](portfolio-analysis-migration-planning.md) stages.

Typically, directional business cases that support portfolio migrations are created as one of the following:
+ A simple *total cost of ownership (TCO)*** **comparison between the as-is infrastructure landscape and the post-migration AWS service architecture. The comparison shows the difference in expected run rates for given workload volumes.
+ A business case** **that shows the net present value (NPV), return on investment (ROI), payback period, modified internal rate of return (MIRR) and 3-5 year cash-flow analyses for migrating to AWS inclusive of migration costs vs staying as-is.

The directional business case scope is typically limited to one of the following:
+ A comparison of the infrastructure technology costs
+ A comparison of the infrastructure technology and operations costs

In general, the larger the portfolio, the less developed the case needs to be. This is because broader assumptions can be made without significantly affecting the result. For a smaller portfolio, any change will have a greater impact, so more detail is required.

Start by building the base infrastructure cost comparison. Then decide if the comparison is sufficiently compelling before you continue. Usually, portfolios of more than 400 servers will show a positive business case on infrastructure cost reduction alone within 3 years of operation on AWS, or 250 servers within 5 years, although this can vary. For smaller portfolios, more detail may be needed.

Conversely, it is rarely useful to examine other business value components at this stage, such as value derived from improved resilience or business agility, unless the total migration scope is fewer than about 5 workloads or 50 servers.

## Focus value drivers
<a name="focus-value-drivers"></a>

The infrastructure technology TCO comparison compares a model of the as-is infrastructure costs with a basic model of the AWS service bill of materials needed to run your workloads with equivalent performance and availability. Many optimizations can be done. At this stage, however, the focus is on the following list because they are easier to assess and typically yield about 30 percent TCO savings, which is enough to move forward:
+ **Compute elasticity** – Map servers whose usage is not 100 percent, such as development or UAT servers running 8x5 (24 percent usage), 10x5 (30 percent), or 10x6 (36 percent), and disaster recovery (DR) servers running at 2 percent, to on-demand services that are billed only when used.
+ **Procure with a savings plan** – Plan to procure production servers and other servers with high usage (greater than36 percent) with a suitable savings plan to reduce costs by up to 75 percent. Options include 1-year and 3-year commitments, with differing levels of upfront payments to secure greater discounts.
+ **Remove zombies** – Identify servers with CPU utilization of less than 2 percent that you can confirm are no longer needed, and remove them from the cost analysis.
+ **Compute right-sizing** – Use CPU and memory utilization time series data to assess for each server the compute power and memory needed. Then select the Amazon Elastic Compute Cloud (Amazon EC2) instance to fit.
+ **Relational database management system (RDBMS) license right-sizing** – Reassess your RDBMS licensing needs after compute right-sizing on your database servers, compare Bring Your Own License (BYOL) and Procuring license from AWS, and explore the potential of Amazon Relational Database Service (Amazon RDS) to increase savings.
+ **Storage** – Right-size the total storage volume needed, and identify the input/output operations per second (IOPS) needs across the portfolio. Determine how much can be moved to object storage with different SLAs and costs.

## Data needs
<a name="data-needs"></a>

The table in [Understanding initial assessment data requirements](understanding-initial-assessment-data-requirements.md) shows the data required to build each part of a directional business case, and whether it is mandatory or optional.

To build the case, you need the infrastructure subset of the initial planning data plus cost data. Determining how to identify the infrastructure to include depends on your business goal:
+ If the program's objective is to migrate and modernize specific applications, build the infrastructure portfolio based on what the applications need, taking into consideration infrastructure that is shared.
+ If the program's objective is infrastructure-centric, such as migrating out of a data center whose lease is due to expire, application mapping isn't needed for infrastructure TCO comparisons.

Data that is marked as optional (such as CPU and memory peak utilization for servers) can usually be replaced with standard benchmark values. You can discuss this with an AWS Partner or AWS Professional Services. Or you can extrapolate the values from data points that are available in part of your portfolio (such as data collected by a hypervisor). The larger the portfolio, the more accurate this is.

## Building infrastructure TCO comparisons
<a name="building-infrastructure-tco-comparisons"></a>

Tools are vital to constructing infrastructure TCO comparisons. [AWS Professional Services](https://aws.amazon.com/professional-services/) or an [AWS Partner](https://aws.amazon.com/migration/partner-solutions/) can provide help with all types of directional case, especially if you plan to engage them to assist in the wider migration process.

There are tools available to do the following:
+ Collect inventory data.
+ Collect utilization data.
+ Provide accurate as-is infrastructure cost benchmarking data.
+ Identify and remove zombies.
+ Make right-sizing assessments.
+ Recommend purchasing options.
+ Compare software licensing options.
+ Produce simple graphical cash-flow analyses.

[Migration Evaluator](https://aws.amazon.com/migration-evaluator/) from AWS is one option. It provides all of these capabilities as a **free managed service. You** can request Migration Evaluator through your AWS account manager or AWS Migration Competency Partner or by submitting [a request online](https://pages.awscloud.com/Migration-Evaluator-request.html). Migration Evaluator has been designed specifically as a point solution to produce infrastructure technology TCO comparisons and quickly.

Key advantages:
+ Free of charge
+ Agent-less discovery or manual configuration of inventory data where tool-based discovery is restricted
+ Dedicated support to assist deployment, configuration, data collection, and building the base case, or directional business case
+ Convenience of SaaS operation, but can run data collection entirely within the customer network to support scrubbing before loading into the analytics engine
+ Strong support for Microsoft license right-sizing
+ Full data-export capabilities

Key limitations:
+ Assesses only x86 architecture servers (Windows and Linux)
+ Limited options to configure or calibrate benchmark as-is cost data
+ No support for modeling operations cost optimization
+ No support for migration cost modeling
+ No direct support for building business cases beyond TCO comparisons

If you decide to use a commercial discovery tool for portfolio discovery and analysis capabilities such as application stack and interdependency discovery, it will usually provide infrastructure TCO comparison as well. For guidance on the use of tools for portfolio discovery and assessment, see [Evaluating the need for discovery tooling](understanding-initial-assessment-data-requirements.md#discovery-tooling). To review and compare the key capabilities of the market-leading tools, see [Discovery, Planning, and Recommendation migration tools](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools/).

## Building in operational cost optimization
<a name="building-operational-cost-optimization"></a>

IT operations productivity improvement is often a significant value contributor for migrations. On average, after migration to AWS, IT operational staff productivity increases by 62 percent through migration, according to the International Data Corporation (IDC) whitepaper [Fostering Business and Organizational Transformation to Generate Business Value with Amazon Web Services](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-BV%20IDC%202018.pdf?aliId=1614258770). However, there are two challenges with sizing and including these benefits in the directional case.

First, assessing the full range of productivity gains requires extensive data gathering and is more appropriate for the [detailed business case](detailed-business-case.md). This challenge can be resolved by focusing on a few elements that are more easily assessed and sized with simple benchmark data but that still show significant advantage.

Second, focusing on productivity as a source of cost reduction can generate concern and negativity among key customer stakeholders and program members. Make sure that you provide clarity over how the benefit will be realized and what that means for the people impacted. Such problems can be avoided by clarifying that this will only enhance the team's roles:
+ The migration program includes a track to develop and move internal operations staff into new roles, such as joining DevSecOps teams building infrastructure as code automations and test automations that will drive growth for the team.
+ The benefit can be realized by rescoping and resizing operations outsourcing contracts, so that internal staff can increase their focus on higher-value activities

Approach constructing this business case element based on what operations transformations you want to consider:
+ If you have an existing in-house operations team, upskill the team members, and show the expected productivity improvement.
+ Alternatively, migrate away from your current operations solution to AWS Managed Services (AMS) or to an alternative managed services offering from an AWS Partner.

For the first transformation, to get a conservative financial estimate of the improved productivity that can be included in the case, we recommend the following:

1. Focus on server management operations productivity specifically. It tends to be a significant proportion of operations effort, can be more easily assessed, and is more readily verified later.

1. Calculate staffing needed based on benchmarks for number of servers that can be managed by each full-time equivalent (FTE) employee. On premises, that number is about 150 severs. On AWS, it's about 400 servers.

1. Apply these metrics to the number of on-premises servers compared with the number of EC2 instances.

1. Multiply the time saved with a blended cost rate for the whole operations team.

You can then check your results with either approach by verifying the result does not greatly exceed the average productivity gains by role provided in the following table (data sourced from the IDC whitepaper [Fostering Business and Organizational Transformation to Generate Business Value with Amazon Web Services](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-BV%20IDC%202018.pdf?aliId=1614258770).

|
|
| Role | Efficiency gain |
| --- |--- |
| IT infrastructure management | 62% |
| IT support | 59% |
| Application management | 43% |
| Database management | 19% |
| Application development | 25% |

For the second transformation, you can add the operational cost savings by directly comparing the current total operations and support cost for the in-scope portfolio with the cost of the managed service being considered.

To obtain the cost of the managed service, provide your AWS account manager or any [AWS Managed Services Partner](https://aws.amazon.com/managed-services/partners/) with your proposed AWS Bill of Materials, your service level choice (Plus or Premium), and your AMS package (AMS Accelerate or AMS Advanced). This will provide you with a total cost of managed services for the AWS service components of the transformed solution. Similarly, you could obtain pricing from an AWS Partner that offers its own managed services package based its own parameters.

## Expanding to a full directional business case
<a name="full-directional-business-case"></a>

In general, to assemble a full directional business case, build the TCO comparison, with or without the IT productivity element, and estimate all the migration and modernization costs. Then create a cash flow that covers pairs of migrate-and-modernize and don't-migrate-and-modernize scenarios.

The most basic case is preparation of a single pair of scenarios, where the don't-migrate-and-modernize scenario is your current situation and the migrate-and-modernize scenario has the following characteristics:
+ No growth or shrinkage in transactional volume, compute, or networking capacity
+ Steady low-volume growth in storage requirements
+ Quality-of-service capabilities (such as availability, durability, throughput, and performance) matching the existing system's capabilities

For all but very small portfolios, this fits the objectives of building a directional case well. It demonstrates enough value quickly to gain the mandate to move forward.

For smaller portfolios, it can be valuable to add pairs of migrate-and-modernize and don't-migrate-and-modernize scenarios that demonstrate other aspects of the increased value of cloud migration, such as:
+ A mix of moderate and high-capacity growth requirements across workloads where that growth is expected
+ Inclusion of enhanced resilience, such as high availability, DR, and fault tolerance
+ Improved global performance with edge computing, content delivery network (CDN), multi-Region database replication.
+ Any other specific improved quality of service that you have made a business priority for the program

For these scenarios, make sure that the costs and cash-flow implications of upgrading the current non-cloud infrastructure architecture to match the new specification are estimated accurately. The most direct way to obtain this estimate can be requesting a quotation from a systems integrator, especially if they are also an AWS Consulting Partner with Migration Competency, who can support you with both the migrate-and-modernize and the don't-migrate-and-modernize scenarios.

For each pair of scenarios, assemble a case comprising the following:
+ The costs of the don't-migrate-and-modernize scenario. In the most basic case, this includes:
  + The total cost of ownership over the business case term for the current infrastructure configuration
  + Periodic increases in compute, storage, and network traffic consumption
+ The costs of the migrate-and-modernize; scenario, including:
  + Setting up the program, which includes detailed discovery, migration planning, detailed business case development, establishing the core team and upskilling them, establish a landing zone if not already in place, and establishing security management and operations integration for migrated workloads
  + The workload migration and modernization costs
  + The migration infrastructure costs, including network connections, data migration services such as [AWS Snowball Edge](https://aws.amazon.com/snowball/) and [AWS DataSync](https://aws.amazon.com/datasync/), and the AWS utility costs for the architecture needed during the migration process itself (for example, for testing)
  + The ramp-up of AWS utility costs over the course of the migration as waves go live, and the ramp down of the existing infrastructure costs as it is replaced by AWS based services and decommissioned
+ The decommissioning costs and write-offs for any stranded assets

## Estimating migration and modernization program setup
<a name="estimating-migration-and-modernization-program-setup"></a>

To set up a program for success, you might need to run a series of foundational activities to build baseline capabilities and the detailed plan if this has not been done before. These foundational activities include the following:

1. Performing detailed portfolio discovery, migration planning, and detailed business case development, as described in the [Portfolio analysis and migration planning](portfolio-analysis-migration-planning.md) section, plus the documenting the cost of any discovery tools used.

1. Establishing a cloud business and technical core team and developing in-house skills through training and hiring. Identify the members of the IT organization that will need training, and allocate a training budget for each person.

1. Establishing a [landing zone](https://aws.amazon.com/solutions/implementations/aws-landing-zone/) and configuring it to support the cost, operational, and security governance capabilities you will need.

AWS Consulting Partners can help provide estimates for items 1 and 3.

### Estimating migration and modernization costs
<a name="estimating-migration-and-modernization-costs.30d972c9-a147-5e96-9cbc-98457248608c"></a>

To meet the objectives for a directional business case and demonstrate *just enough* commercial potential to proceed to the next phase, keep migration and modernization cost estimation as basic as possible.

To this end, we recommend that you prepare the directional business case by focusing on the applications falling into the following migration strategies:
+ Retire
+ Retain
+ Relocate
+ Rehost
+ Replatform
+ Repurchase

Typically, about 70 percent of workloads can be rehosted, relocated or replatformed, and another 5 percent can be retired. Assessing the applications by migration strategy usually addresses the core of the cost reduction case.

Estimating costs for refactoring, or re-architecting**,** can be complex. It is not practical to attempt this within the time frame given to preparing a directional business case. As discussed previously in [Determining the R type for the migration](prioritization-and-migration-strategy.md#migration-r-type), consider using rehost, relocate, or replatform strategies for your first phase of migration and modernization. These R strategies will likely accelerate initial payback, reduce implementation risk, and improve the business case in the short term. It is also materially easier for your application teams to modernize applications that are running within the AWS environment than those that are not. Estimates for refactoring (re-architecting) specific applications are best added when the [detailed business case](detailed-business-case.md) is prepared.

### Estimating effort for migration by strategy
<a name="estimating-effort-for-migration-by-strategy.68a74030-6989-5440-89e8-24737301321d"></a>

Each migration is different. Before committing any budgets or plans, seed workload estimates for the migration activities from the team who will be responsible for the project, whether that is your in-house applications teams, AWS Professional Services or an AWS Partner organization.

To help build the directional case, the following table provides indicative ranges of effort for the different treatments. These ranges assume that a medium-to-large portfolio is being migrated and that the migration team is trained and experienced. For small portfolios, it is best to have the team responsible for the migration prepare the estimate even for a directional case.

|
|
| Migration strategy | Estimation process | Elements | Person hours | Person hours |
| --- |--- |--- |--- |--- |
| Retain | Do nothing, with no cost, no benefits, and no reduction in technology debt. | – | – | – |
| Retire | Estimate decommissioning the hardware equipment used, if any. | – | – | – |
| Relocate | Estimate copying the workload within VMware using VMware tools. This includes copying the data, smoke testing to verify, and any hardware decommissioning. The effort to relocate VMs is typically less than for low-complexity rehost patterns. | – | – | – |
| Rehost | Estimate copying the workload and data with an image copy, smoke testing, high availability (HA) and disaster recovery (DR) testing where appropriate for production servers, and any hardware decommissioning. The best practice is to use tools such as [AWS Transform MGN](https://aws.amazon.com/application-migration-service/). Divide workloads into low, medium, and high complexity, based on factors such as whether a database or other infrastructure software is running, database complexity, whether clustered, integration complexity, and data volumes.  | Effort per app per server | Migration | HA/DR test |
| Low | 10–14 | 3–5 |
| Medium | 16–24 | 4–6 |
| High | 26–38 | 8–12 |
| Replatform | For replatform migrations that include upgrades to operating system or RDBMS version, take the estimate for a rehost, and add time to run a rebuild and smoke test on the new platform. If the replatform includes changing the technology of the platform, estimate additional time for the use of the conversion tools, such as [AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/) and [AWS Database Migration Service](https://aws.amazon.com/dms/), and a more complete application test. An example of changing the technology is migrating away from a proprietary commercial database to an open source replacement. | Effort per app per server | Version up | Technology change |
| Low | Add 1–3 | Add 10–15 |
| Medium | Add 2–5 | Add 20–30 |
| High | Add 4–8 | Add 40–60 |
| Repurchase | Estimate data extraction, transformation, and uploading into the newly purchased SaaS service replacement, and any hardware decommissioning. | – | – | – |

### Estimating migration infrastructure costs
<a name="estimating-migration-infrastructure-costs.fef93719-1e74-5598-af75-7c653f62b1f2"></a>

Include estimates for the infrastructure that you will use over the course of the migration. Typically, these estimates comprise:
+ A budget for connectivity and data exchange services for workload and data migration from the current environment to AWS
+ A budget for the AWS services (especially compute and storage) needed for hosting the migrated workloads during the migration, testing, and cutover processes
+ The ramping up of AWS utility costs as each migration wave is completed
+ The decommissioning costs of the existing infrastructure that will no longer run the migrated workloads

For data exchange, examine your total data volumes and assess the feasibility of using networking. If you have provisioned an [AWS Direct Connect](https://aws.amazon.com/directconnect/) link or [Site-to-Site VPN](https://aws.amazon.com/vpn/) from AWS to a point on your WAN ahead of time for operational use after the migration, you can use that resource up to its service quota.

If your network capacity is insufficient, a short-term increase in internet bandwidth with a virtual private network (VPN) is often a highly cost-effective solution. If not, AWS media exchange devices such as [AWS Snowball Edge](https://aws.amazon.com/snowball/) and [AWS Snowball Edge](https://aws.amazon.com/snowcone/) offer solutions in most AWS Regions. Also, for very high-volume data migration, consider including budget for [AWS DataSync](https://aws.amazon.com/datasync/), which improves reliability and can accelerate transfers irrespective of the media used.

Modeling the ramp up of AWS services and the ramp down of existing infrastructure is important for the cash flow analysis element of the business case. At this stage, you are not likely to have a wave plan to determine exactly when costs will be incurred. We recommend the following:
+ Ramping up the costs for AWS at a constant rate over the migration.
+ Ramping down costs for the existing infrastructure you plan to decommission at a constant rate over the same duration.

Starting the AWS cost ramp up 1-2 months before the existing infrastructure ramp down. This provides 1 month of AWS utility usage to conduct the migration for each wave. It includes time for testing, and additional time to complete the decommissioning work needed to stop incurring costs on the replaced infrastructure.

### Estimating decommissioning costs
<a name="estimating-decommissioning-costs.ff030f84-cce0-50fe-9b3c-499176120c37"></a>

Decommissioning equipment that cannot be redeployed, and disposing of it in a legal and environmentally friendly way, can incur some small costs. However, for a directional business case, typically the only potentially material sum is the cost of writing off any remaining book value of the replaced assets.

For the directional business case, we recommend that you do the following:
+ Review your asset list.
+ Identify those that would be decommissioned.
+ To reduce the write-off, examine the opportunities for switching devices around so that newer devices on the list can be used to replace older, more fully depreciated assets.
+ Make an assessment of the future book value of the assets that would be decommissioned at that point.
+ Include this as the migration cost of decommissioning.

### Assembling and adjusting the full directional business case
<a name="assembling-and-adjusting-the-full-directional-business-case.6b772d69-7f05-5a36-a27f-44e2c42808ed"></a>

After you prepare the full set of costs for each pair of scenarios, construct a discounted cash flow statement for each and graph them. We recommend building directional business cases over the same period as the hardware refresh cycle. This is typically 5 years for servers, storage, and network devices. When you use the same period as the hardware refresh cycle, the costs of exactly one refresh are included in the as-is costs for each scenario.

Then calculate the key financial metrics that you need for getting approval to move to the next phase of the program. We usually include the following:
+ The net present value (NPV) to gauge the absolute value of the cost reductions and productivity gains assessed
+ The payback period in months to verify that returns are sufficiently fast
+ The final run-rate comparison to verify whether the process is taking enough cost out over the term
+ The return on investment (ROI) and modified investment rate of return (MIRR) to assess the relative financial performance of the program over other demands on capital your organization may be prioritizing

Use the first iteration of the case to determine whether the expected financial performance means that refinements should be made, as in the following examples:
+ If payback is too slow, consider options to accelerate and reduce the cost of migration, such as the following:
  + Use AWS Partners or AWS Professional Services to expand the available resources and further parallelize migrating workloads with more basic patterns.
  + For workloads running in VMware, compare the relocate strategy to the rehost or replatform strategy, at least for the initial phase. Using the relocate strategy can reduce migration cost and increase migration speed.
  + Where technically feasible, push workloads that require more complex replatform or refactor (re-architect) strategies into a future phase, outside the scope of the initial business case.
+ If ROI and MIRR are too low, consider the following:
  + Are the scenarios that you are considering too conservative? Do you have a scenario that reflects the most likely capacity growth and elasticity needs? Do you have scenarios that compare the costs inclusive of the increases in quality of service within your objectives?
  + Can you refine the scope of the application portfolio to be migrated in the first phase to focus on workloads that will yield stronger returns, such as those with lower current utilization or expensive disaster recovery (DR) needs?
  + Can refine the scope of the application portfolio to initially exclude specific workloads that achieve less commercially? For example, can you postpone workloads for which third-party software licenses become more expensive due to different terms for deployment in public cloud infrastructure?
+ If the final run-rate comparison does not meet the expected target, explore the following:
  + First, confirm that the other metrics meet expectations. The directional business case is primarily to show that there is sufficient financial opportunity to justify starting the next phase of migration preparation.
  + Identify a list of the opportunities to continue to improve cost performance on AWS after the initial phase of migration.

Include an assessment of the list of opportunities when preparing the detailed business case. In addition, include an opportunities assessment in the ongoing maintenance of the case and the month-to-month cost-optimization process after migration is complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
