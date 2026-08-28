---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/baseline-application-portfolio.html
---

# Establishing a baseline for the application portfolio
<a name="baseline-application-portfolio"></a>

To create high-confidence migration wave plans, you must establish a baseline for the portfolio of applications and its associated infrastructure. A portfolio baseline provides a comprehensive view of the migration scope, including technical dependencies and migration strategy. The portfolio baseline provides clarity about which applications are in-scope of migration and that the data points outlined in the [Understanding complete assessment data requirements](understanding-complete-assessment-data-requirements.md) section are collected. Likewise, all the associated infrastructure (compute, storage networks) is understood and mapped to the applications.

Technical dependencies can be described in four categories:
+ **Application-to-infrastructure** dependencies establish the link between software and physical or virtual hardware. For example, there is a dependency between a CRM application and the virtual machines where it is installed.
+ **Application-component** dependencies describe how components running in different infrastructure assets interact. An example of an application-component dependency is a web front end running on virtual machines, with an application layer running on a different virtual machine, and a database running on a database cluster.
+ **Application-to-application** dependencies relate to the interaction between different applications or its components. An example of an application-to-application dependency is a payment-processing application and a stock-management application. These applications are independent, but they constantly interact using defined API operations or shared datasets.
+ **Application-to-infrastructure services** dependencies are technically application-to-application dependencies, given that the infrastructure service is itself an application. However, we recommend categorizing these separately. The main reason is that infrastructure services typically are shared by many applications, so they have a long trail of dependencies. They also typically follow a different migration strategy and pattern.

  For example, a load balancer can contain balancing pools for several applications. What matters is the dependency to the pool, which is likely to be migrated individually, alongside the dependent application, while the load balancer itself is retained or retired.

  In addition, individualizing application-to-infrastructure service dependencies helps to avoid false dependency groups. A false dependency group is when several business applications are grouped together, implying that having a common dependency to an infrastructure service forces them to be migrated at the same time. For example, authentication services, such as Active Directory, are likely to be associated with large groups of applications. The key is to filter infrastructure service dependencies out, and to enable these services in AWS.

For more information about how to work with dependencies to create migration groups see the [Wave planning](wave-planning.md) section.

When you establish a baseline for the portfolio, we recommend that you confirm a migration strategy for each application component. The migration strategy will be one of the 6 Rs for migration (see the [Iterating the 6 Rs migration strategy](iterating-7-rs-migration-strategy-selection.md) section). In the portfolio baseline, one of the 6 Rs should be associated with each application. A 6 R strategy should also be associated with each of the application's infrastructure components.

To establish a baseline version of the portfolio, including dependencies and migration strategies, use automated discovery tooling (see [Evaluating the need for discovery tooling](understanding-initial-assessment-data-requirements.md#discovery-tooling)). Complement the data with information gathered from key stakeholders such as application owners and infrastructure teams. Keep gathering data until you obtain a complete portfolio inventory that matches the attributes and level of fidelity outlined in the [data requirements section](understanding-complete-assessment-data-requirements.md) for this stage. The resulting dataset will be instrumental in driving the migration.

Consider that, depending on the extent of your migration scope and the available tooling, this activity can take several weeks to complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
