---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/detailed-business-case.html
---

# Detailed business case
<a name="detailed-business-case"></a>

In this stage, we recommend validating and expanding the scope of the business case to provide a greater level of detail to support the transformation program. The quickly assembled initial directional business case is designed to provide enough confidence to invest in the foundational steps and next level of detailed planning.

Developing a detailed business case supports this planning process in the following ways:
+ Providing financial analyses that inform decisions on what should be migrated and modernized, which options to select and how to phase and prioritize the work
+ Validating, refining, and developing the original directional financial case by re-examining in detail:
  + The infrastructure cost-reduction potential
  + The internal IT productivity and any outsourced operations efficiencies
  + The estimates for the investments needed for program setup, migration, and modernization
+ Identifying, estimating the scale of, and setting up the process for tracking the further value drivers that migration brings

In the detailed business case, you establish the following:
+ The objective basis on which to secure the mandate and investment to implement at least the first phase of migration
+ The baseline minimum financial performance expectation for the program
+ Clarity over the financial basis on which various migration design and prioritization decisions are made, so that when circumstances and people change over the course of the program, the new leadership can make informed choices.
+ Insight into incremental areas of cost optimization to be explored after initial usage data becomes available as workloads are migrated and start operation
+ Estimates for the value that cloud transformation brings to the business from increased resilience and agility
+ The associated KPIs, metrics, and assumptions used to estimate the financial return from improved resilience and agility, which then form the baseline for driving the primary benefits realization out of the program

## Determine the scenarios needed for the case
<a name="determine-scenarios-needed"></a>

When building the detailed business case, it is usually necessary to develop multiple scenarios to support the various purposes that the business case is used for.

**Minimum change scenario** – To assess the minimum financial performance expectation, prepare a scenario that assumes the minimum expected change to the status quo. This scenario, as a worst-case backstop, provides is useful support when getting the mandate to invest in the migration. This scenario models the minimum expected degree of capacity growth and minimum changes for other quality-of-service needs, such as availability and resilience. The least change creates the lowest cost and least resource inefficiencies for the current operating model.

**Most likely scenario** – To inform program strategy and prioritization decisions, prepare the scenario that reflects what the business expects to happen. This scenario should include the likely peak utilization growth or reduction and the upgrade costs to meet demand for high levels of service quality (especially availability and resilience) from the business.

**Other specific scenarios** – Where it is still necessary to make an assumption that could have a large impact on the business case, develop scenarios in which the assumption holds true or not. However, we recommend keeping the number of these alternate scenarios at the absolute minimum. Any more than three-four scenarios in total slow progress, and become expensive, confusing, and difficult to maintain. Wherever possible, conduct experiments and work to remove larger assumptions.

## Validate and refine the infrastructure and migration cost model
<a name="validate-refine-infrastructure-migration-cost-model"></a>

After you have completed the portfolio analysis and prepared the design and sizing of the target AWS services, refine the running cost estimates for the current operating model (COM) and future operating model (FOM) on AWS for each scenario. It is usually necessary to refine the estimates for the following:
+ **COM infrastructure costs** of hypervisor host server, bare-metal server, storage, network device, security appliance hardware refreshes, installation, and maintenance. Calculate these with actual pricing and discount levels for the capacity needed for the scenario.
+ **COM data center and collocated facilities costs**, including space, cooling, power, racks, uninterruptible power supply (UPS), cabling, physical security systems, sized for the growth and specified to meet the capacity, and high availability and disaster recovery (DR) levels for the scenario.
+ **COM network services costs**, including costs for WAN links, content delivery networks, and virtual private networks (VPNs), calculated using contracted pricing for the connectivity, bandwidth, throughput, and latency needs for the scenario.
+ **COM application and infrastructure software costs** based on existing contracts to provide the growth or reduction of usage for the scenario.
+ **FOM AWS utility costs**, including tech support and managed services as needed, based on the refined service architecture, instance sizes, preferred pricing model, expected usage, and usage volatility.
+ **FOM application licensing** based on final application design, the configuration of the infrastructure running the applications, growth over time, and license transferability rules.
+ **FOM migration and modernization cost estimates**, refined to reflect the baseline migration wave plan for the scenario, and detailed to provide costs for each workload, especially for those to be replatformed, repurchased, or refactored.
+ **FOM decommissioning costs**, including estimates of asset write-off and contract early termination costs, revised to reflect decommissioning timing in the baseline migration wave plan, verification of what assets can be repurposed and what assets can be switched around to minimize write-offs, and the cost of disposal of the physical assets and media.
+ **Migration parallel run costs** refined to reflect the timing of each migration cutover and each existing service decommissioning.

## Refine the IT productivity and IT operations and support efficiency value model
<a name="refine-it-productivity-it-operations-support-efficiency-value-model"></a>

As with the directional business case, there are two primary approaches to refining and developing the value model around IT operations and support. The approach that you choose depends on whether the COM is managed in-house or with contractors or outsourced services:

### Internal team productivity improvement
<a name="internal-team-productivity-improvement.53441e7b-2d1e-5e42-81f0-ed1ddac9abde"></a>

Where IT operations and support are managed in house, the focus of the business case is on the following:
+ Identifying and quantifying the productivity gains from migration and any operational automation that is included in scope
+ Validating that the time freed up for the in-house team can be readily and productively applied to other typically higher-value activities, giving opportunities for progression and greater reward to the team and more value to the organization

Assess the benefit needs analysis of how much time each member in each role within the team spends on their various regular activities, and guidance on the expected reduction in workload for different activities.

The following table provides initial guidance for the typical levels of workload reduction by activity for those tasks that consume the bulk of IT operations and support effort across the different roles in the team. The table includes a description of how the productivity is achieved.

**Note**
** **The activities listed are typically performed by team members in several different roles, so the productivity saving for each task should be assessed across the full set of roles in the team. For example, in IT operations teams organized by infrastructure tower (such as compute, storage, and networking), capital expenditure planning and budgeting might be common to tower leads for each tower.

|
|
| Operational and support activities | Level of savings | Productivity driver |
| --- |--- |--- |
| Infrastructure design | Medium | Design is simplified, with fewer parameters to be considered. |
| Capital expenditure planning and budgeting | High | OPEX-centric elastic services remove virtually all budgeting and planning issues. |
| Purchasing | High | Procurement is greatly simplified after the AWS accounts are established. |
| Capacity planning | Medium-very high | Networking and compute capacity management workload is usually all but eliminated, and for storage it is heavily simplified |
| Tuning | High-very high | Tuning is not needed for managed services and barely needed for other services because instances can be changed in size at any time. |
| Managing hardware failure | Very high | All aspects of handling hardware in the cloud are handled transparently by AWS. |
| Monitoring server availability and communications | High | Monitoring and communications are simplified extensively with AWS tool support and automation. |
| Security management | Medium | Workload is significantly reduced with AWS security capabilities and with AWS owning the [security responsibilities](https://aws.amazon.com/compliance/shared-responsibility-model/) for the AWS Cloud hardware, software, networking and facilities. |
| Network and storage upgrades, maintenance, and patches. | Very high | All aspects of network and storage maintenance in the cloud are handled transparently by AWS. |
| Racking and stacking – hardware logistics | Very high | All aspects of managing hardware in the cloud are handled transparently by AWS. |
| Backup | Medium | Backup is simplified extensively with AWS tools, flexible storage systems, and automation. |
| Managed services (such as Amazon S3, Amazon RDS, AWS Lambda, and AWS Fargate) | Very high | Managed services run on environments that are fully managed by AWS, so they require no maintenance, patching, monitoring, or provisioning management activity. |
| Device and service setup and commissioning | High-very high | Activities for hardware setup for the estate migrated to AWS are usually reduced, except for WAN connectivity devices for establishing VPNs or AWS Direct Connect connections to AWS data centers. |
| Endpoint protection and antivirus protection | High | Application and maintenance of endpoint protection and antivirus services is typically extensively automated as part of the migration design. |
| Threat, vulnerability, and risk assessments | High | AWS provides support for the elements of this, focused on the core platform and the mechanisms that AWS provides to secure architectures simplifies assessment. |
| Data center infrastructure project management | High | Project management for installation work for expansion, refresh, or decommissioning of infrastructure services. While some management of infrastructure software and services remains, this is much simpler than on-premises infrastructure, and the hardware activities are eliminated. |
| Data center facilities management | Medium-very high | The facilities management work attributable to all the servers, storage devices, security appliances, and associated racks is removed for everything that is migrated. However, some work usually remains for providing facilities for WAN link network devices and for any infrastructure that is kept on premises in a hybrid architecture. |
| Application architecture, development, management, and testing | Low | Use of agile development tool-chains, in combination with automation of application stack instantiation and destruction for building test environments as needed, reduces application development lead times and eliminates many manual test steps. |
| Installing and configuring application software | Medium | Full application stack installation and configuration is readily automated using services such as AWS CloudFormation and simplified through the use of landing zones, which can be readily configured by using AWS Control Tower. |
| IT support | Medium | Reductions in L1 and L2 support are achieved by reducing capacity and performance issues through the use of Service Catalog capabilities for self-service provisioning, increased use of low-cost high availability architectures (reducing outages and configuring automatic scaling and edge computing). |
| Database administration | Minimal-low | These activities remain mostly unchanged. They are typically resourced at the same levels for AWS as for on-premises infrastructures. |
| Infrastructure and security requirements capture, analysis, and design | Minimal |
| Documentation | Minimal |
| Application and performance monitoring | Minimal |
| L3 technical support, answering queries, and troubleshooting and problem solving | Minimal |
| Installing and configuring application software | Minimal |
| Application L3 support (excluding budgeting and long-range capacity planning) | Minimal |

The following table shows the expected savings for each level of workload reduction.

|
|
| Level | Expected |
| --- |--- |
| Very high | 85% - 100% |
| High | 60% - 90% |
| Medium | 30% - 70% |
| Low | 10% - 35% |
| Minimal | 0% - 10% |

These metrics provide a starting point for assessing productivity gains and including them in the detailed business case. Actual productivity gains vary based on the specific situation. It can be useful to calculate the productivity savings at both the midpoint and lower end of the ranges to estimate typical and conservative scenarios.

As the program progresses, it is valuable to capture actual data for time spent on each activity by role. That data builds an improved base for estimating operations and supports costs for new projects and expansions of services.

### Outsourced IT operations and support cost reduction
<a name="outsourced-it-operations-and-support-cost-reduction.70fe627e-2de5-52d3-88db-07b52dd802eb"></a>

Where IT operations and support are primarily outsourced or managed with contractors, the cost allocation for the future operating model (FOM) can be prepared by requesting quotations from AWS Partners that offer managed service solutions, including AWS Partner-led [AWS Managed Services](https://aws.amazon.com/managed-services/partners/). You can also contact your AWS account manager and request a price for AMS directly, as described in the subsection on [Building in operational cost optimization](directional-business-case.md#building-operational-cost-optimization) within the [Creating a directional business case](directional-business-case.md) section.

For the detailed business case, replace any benchmark figure with a quotation based on the revised AWS services bill of materials and expected service consumption, the AMS package and any options needed, and the service level needed. The cost will have a one-time implementation component and a consumption-based run rate.

Include any remaining IT operations, support that must be retained for any service that will not be migrated to AWS, and a one-time cost if there are any contract penalties (for example, for early termination).

## Develop the resilience value model
<a name="develop-resilience-value-model"></a>

On AWS, you can construct a wide range of high availability, disaster recovery, and fault-tolerant architectures. Consumption-based pricing means that services are charged for only when used. Together, these two factors provide exceptional cost performance for resilience.

Furthermore, AWS customers have been using this to improve their workloads' resilience. The [IDC 2018 survey](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-BV%20IDC%202018.pdf?aliId=1614258770) gives examples of participating customers achieving 73 percent fewer outages per year, a 58 percent reduction in mean time to recover (MTTR) and a 94 percent reduction in lost productivity. The same survey showed that the financial benefits derived through increased resilience were 50 percent greater than the IT infrastructure cost reduction benefit.

In addition, further resilience is achieved through modernizing the software development lifecycle for applications. Where CI/CD pipelines with test automation are introduced to support greater business agility, software defects are caught earlier in the development cycle, greatly reducing software maintenance costs.

To assess and include this value in the business case, first work with application business owners to build a picture of the *total benefit opportunity* for each workload to be migrated**. **This might include as the following items:
+ The number, average duration, and nature of interruptions in service
  + Examples of service interruptions include outages, performance slow-downs, planned batch and maintenance windows overrunning, bugs in key functions, and access throttling during peak periods.
+ Impact on revenue by interruptions of revenue-generating services, such as ecommerce systems
  + The likely number of transactions unable to be completed through service interruptions, based on the interruption time and transaction rates
  + Average value for each transaction impacted
+ The additional cost of support engineers' time to resolve defects in production systems compared to the cost of discovering them earlier in the development process
+ Impact on internal users' productivity and the cost of lost time

Then make an assessment of an expected and a more conservative reduction in time lost to service interruptions** **that the increased resilience should yield. For example, consider including the following items:
+ Reduced number of outages and MTTR using high availability architectures and improved recovery time objective (RTO) and recovery point objective (RPO)
+ Reduction in slow-downs, elimination of capacity throttling and avoidance in batch processing overruns, using capabilities such as automatic scaling
+ Reduced number of application bugs that are discovered only in production, through the implementation of CI/CD pipelines and automated regression testing on infrastructure spun up and spun down to minimize cost

Put these together for the portfolio of applications to be migrated and modernized, and calculate the expected and more conservative business value figures for each year of the case. The benefits should ramp up in line with the migration schedule and then scale in volume in line with the usage growth expectations of the contributing applications.

## Develop the business agility value model
<a name="develop-business-agility-value-model"></a>

Business agility is the prime reason that AWS customers migrate to AWS. The [IDC 2018 Survey](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-BV%20IDC%202018.pdf?aliId=1614258770) of AWS customers indicated that for them, business agility benefits accounted for 47 percent of the total benefits measured and over five times the benefits accruing from infrastructure cost reduction.

Accurately predicting all the business agility benefits that will accrue from any transformation is challenging. However, by focusing on applications that support large numbers of users or are sources of business differentiation, you can model and include a material portion of this benefit into the baseline detailed business case.

As the migration proceeds, incrementally refine and expand the business agility value model as more benefits become quantifiable. This keeps the business case relevant, so that it can be used as the primary decision support tool with which to steer the program.

To build the business agility value model, use the following guidance:
+ Select the workloads that have the opportunity to drive the greatest business performance improvement, such as:
  + Revenue-generating workloads
  + Business operations workloads with scope for driving efficiency gains and removing costs from the business
  + Business productivity tools supporting large user bases
+ For revenue and efficiency generating workloads, do the following:
  + Make a realistic and a more conservative assessment of the revenue growth or operational efficiencies that major and minor application upgrades could be expected to drive.
  + Estimate the increased number of major and minor releases per year that AWS increased application development speed and reduced infrastructure deployment time enables. Some baseline metrics for this are provided in the IDC report.
  + Calculate the realistic and more conservative benefit expectations. Map them over the period of the business case, making allowances for ramping up to full efficiency some time after the respective workloads are migrated.
+ For business productivity tools, do the following:
  + Make a realistic and a more conservative assessment of the time savings that major and a minor application upgrades could be expected to drive.
  + Estimate the average cost of people's time and effort across the impacted user base.
  + Use the figures for increased major and minor release frequency, and calculate the benefits over the term of the business case.

Because the increased developer productivity and reduced time to launch require no additional resources, add the net benefit lines for each workload into the business case cash flow model for inclusion in the discounted cashflow, NPV, ROI, MIRR, and payback calculations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
