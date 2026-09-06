---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/continuous-assessment-improvement.html
---

# Continuous assessment and improvement
<a name="continuous-assessment-improvement"></a>

After a migration program has been established to implement a migration wave plan, the application portfolio assessment focuses on continuous iteration of the portfolio data and detailed assessments for each wave. In addition, as workloads are migrated, these can be further assessed for optimization and modernization. This stage focuses on gathering application and infrastructure details to validate target architecture and technology choices. It also focuses on outlining specific platform requirements, such as security, operations, and cloud infrastructure, that can be converted into implementation designs and migration cutover plans for each migration wave.

**Tip**
 For more details and guidance, see the relevant section in the [Application portfolio assessment guide for AWS Cloud migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/continuous-assessment-and-improvement.html).

## High-level objectives and actions
<a name="continuous-objectives"></a>
+ Application assessments – Group detailed application assessments equivalent to migration waves. For each wave of applications, follow the same objectives and actions that are defined in the [Prioritized applications assessment](prioritized-applications-assessment.md) section.
+ Application optimization and modernization assessment – Address technical debt, new business requirements, usage and cost analysis, best practices, transformation patterns, industry trends, pain points, and operational efficiency. What have you learned about this application running in the cloud? What [new AWS services](https://aws.amazon.com/new/) have been released? What are the available architectures for this application? What benefits do those architectures provide?
+ Evolving and tracking the business case – Track the benefits achieved against the baseline detailed business case to maintain stakeholder support and keep momentum. Also, expand the case to include further modernization to drive value from improved resilience and agility. Provide information about deeper cost optimization using newly acquired post-migration usage data, giving leadership the basis to prioritize ongoing investment in the program.
+ Optimization and evolution – Iterate and expand portfolio rationalization models for optimization and portfolio evolution.

## Outcomes
<a name="continuous-outcomes"></a>

Migration outcomes include the following:
+ Validated migration scope for each wave
+ Documented target architecture and migration strategy for applications in a given migration wave
+ Identified and validated migration patterns and tooling
+ Documented platform requirements, such as security, AWS infrastructure, and operations, and migration cutover considerations for each wave

Optimization outcomes include the following:
+ Portfolio rationalization models and business outcomes
+ Refined business case articulating the additional value that further optimization and modernization provides, including which applications to prioritize.
+ Proposed architecture and technology changes and expected benefits
+ Platform requirements, such as security, AWS infrastructure, and operations
+ Implementation plan

## Best practices
<a name="continuous-best-practices"></a>
+ Reuse architectural patterns defined by your organization. Consider using [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) to create and manage catalogs of IT services that are approved by your organization for use on AWS.
+ Document architectural and technology decisions that can be converted into reusable patterns.
+ Identify key dependencies. What is preventing this application from moving to the cloud now? What is preventing this application from being optimized or modernized after it is in AWS?
+ Consult [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) and [security best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/).
+ Maintain alignment of migration and optimization or modernization activities to business outcomes.
+ Maintain the evolving business case. Track benefits realization as the basis for steering the program.
+ Consider long-term strategic views of the application portfolio in the context of evolving business drivers.
