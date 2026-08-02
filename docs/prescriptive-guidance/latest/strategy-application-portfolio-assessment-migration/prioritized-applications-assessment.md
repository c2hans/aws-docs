---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/prioritized-applications-assessment.html
---

# Prioritized applications assessment
<a name="prioritized-applications-assessment"></a>

After initial application migration candidates are identified, a detailed assessment of those applications accelerates migration outcomes by enabling cloud foundations to be designed and implemented. If those foundations already exist, the application assessment assists with further developing the target environment to meet migration requirements. This stage provides enough data to produce target architecture designs and to define a migration strategy for prioritized applications that can be migrated now to gain confidence and experience. The output of this stage will feed directly into other program workstreams, such as security, migration, and landing zone for implementation. For more information, see [Mobilize your organization to accelerate large-scale migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/welcome.html).

Similarly to the previous stage, identifying key stakeholders is instrumental to understanding data requirements. Business unit leads and senior managers, application owners, application and enterprise architects, and migration and platform leads are typically involved.

**Tip**
For details and guidance, see the relevant section in the [Application portfolio assessment guide for AWS Cloud migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/prioritized-applications-assessment.html).

## High-level objectives and actions
<a name="prioritize-objectives"></a>
+ Confirm prioritized applications – Establish a baseline for the list of applications that will be analyzed in detail. To accelerate time-to-value. We recommend keeping this list in the range of three-five applications.
+ Identify stakeholders – Who is impacted by and who benefits from the migration of these applications? Ensure that these stakeholders are part of the detailed analysis of the prioritized applications.
+ Create detailed application assessments – Thoroughly investigate the current state architecture and technology, strategic roadmap, application lifecycle, operations, security, dependencies, risks, and issues for the prioritized applications. What is the level of confidence on the current understanding of this application?
+ Map out an initial AWS design – Include target architecture and technology choices, architectural decisions and patterns, licensing, security, operational, functional and nonfunctional requirements:
  + What is the architecture for this application in the cloud, and how will it operate there?
  + Can this design be implemented and operated?
  + Do you need to deploy cloud foundations or extend them?

Depending on your current level of cloud adoption, a complete design might not be achievable if these applications represent your first cloud deployments and the broader platform decisions have not yet been made or a wider migration program has not been established. However, the process of designing the target architecture will surface foundational requirements and current gaps or blockers, and it will clarify actions that must be taken.
+ Migration strategy and patterns – Evaluate preferred approaches and available automations, migration tooling and techniques, and cutover considerations. What is the preferred migration approach? Can it be documented as a reusable pattern? What migration tools are available? What are the high-level cutover activities?
+ Estimate the run rate for these applications – Use historical performance data and available tooling to project costs when running these applications on AWS. Is this a predictable workload? Are there any identified usage patterns? What is the effort required to migrate?

## Outcomes
<a name="prioritize-outcomes"></a>
+ Validated list of prioritized applications
+ List of identified application-migration stakeholders
+ Documented current state architecture
+ Documented initial target architecture and migration strategy for migration candidates
+ Identified migration patterns and tooling
+ Documented platform requirements, such as security, AWS infrastructure, and operations
+ Documented cutover considerations as input for migration planning
+ Estimated run rate

## Best practices
<a name="prioritize-best-practices"></a>
+ Reuse architectural patterns defined by your organization.
+ Document architectural decisions for these applications as patterns that can be reused in subsequent detailed assessments.
+ Identify key dependencies and address them. What is preventing this application from moving to the cloud now?
+ Consult [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) and [security best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/).
+ Consult the [AWS Pricing Calculator](https://calculator.aws/) to estimate the cost for your architecture solution.
+ The sooner migrations are started the sooner data gaps will become clearer. Plan to migrate the prioritized applications while performing the next stage of portfolio assessment.
