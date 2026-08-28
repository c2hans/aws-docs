---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/application-portfolio-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Application portfolio management
<a name="application-portfolio-management"></a>

 **Manage and optimize your application portfolio in support of your business strategy.**

 Applications underpin your business capabilities and link them to the [associated resources](https://aws.amazon.com/blogs/mt/increase-application-visibility-governance-using-aws-service-catalog-appregistry/). An accurate and complete application inventory will help you identify opportunities for rationalization, [migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-portfolio-discovery/welcome.html), and [modernization](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-modernizing-applications/welcome.html). An effective application portfolio management capability will help you minimize application sprawl, facilitate application lifecycle planning, and ensure ongoing alignment with your cloud transformation strategy.

## Start
<a name="start-4"></a>
+  **Define your organizations overarching business capabilities** — Applications underpin your business capabilities and shared services underpin applications. Having a coherent and complete view of how technology supports the business enables more thoughtful cloud transformation decisions and provides levers for technology and data synergies. For example, applications supporting the same business capabilities will often have integration or data inter-dependencies, and efficiencies can be gained from co-migration. Applications supporting critical business capabilities will often be seen as strategic and may require rapid feature creation or enhancements.

   Consistent hosting strategy for applications supporting a business capability affords leaders additional de-risking, efficiency and cost savings levers. For example, a business capability fully hosted in the cloud can be isolated into its own organizational zone in preparation for divestiture, within hours or days. This can greatly de-risk an organization and reduce transitional service agreement (TSA) costs. The reverse of this can be done in the event of a merger or acquisition, where an organizational zone can be used for acquired business capability application ecosystems. This approach enables security postures to be put in place quickly and allows for strategic integration decisions to be made over time.
+  **Align applications to business capabilities** — Define applications in terms of the overarching business capabilities. Assign business-related metadata, such as business criticality, business purpose, and business owner. Assign data-related metadata, such as data sensitivity (personally identifiable information (PII)), compliance ([The Health Insurance Portability and Accountability Act](https://aws.amazon.com/compliance/hipaa-compliance/) (HIPAA)), and data classification (internal, public, and confidential). In addition to business-driven requirements for rapid innovation or opportunity for operational cost reduction, data (often coupled with business capability) is a significant input into the cloud migration calculus and must be considered during a migration.
+  **Map applications to the underpinning software products and associated resources** — Build a complete picture of each application by sourcing data from related enterprise systems, such as enterprise architecture, IT service management (ITSM), and project and portfolio management. Identify a technology owner that will be responsible to periodically enrich and validate application metadata in collaboration with a business owner. Key metadata may include application type (such as WebApp, SaaS, mainframe, database), application architecture (such as monolith, distributed), [disaster recovery options](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) (such as backup and restore, pilot light, warm standby, multi-site active/active), licensing costs, estimated annual costs for infrastructure, inter-dependencies, and so on.

   For non-cloud-native applications, analyze in the context of the seven common migration strategies ([7 Rs](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/overview.html)) for moving applications to the AWS Cloud (retain, retire, rehost, re-platform, repurchase, refactor, relocate). Add the most applicable “R” to the inventory for each non-cloud-native application. At this point, there is a fact-based, comprehensive Application Inventory. An accurate and complete application inventory will help you identify opportunities for rationalization, migration, and modernization.

## Advance
<a name="advance-4"></a>

 Assess the health of your application portfolio on a regular basis with a view to maximizing the value that your organization derives from its application investments. Cloud based applications offer a multitude of benefits that not only include cost reduction but can also be a source of revenue generation.

 Consider the following sample questions when assessing your application portfolio.
+  Is the application strategic and does it require rapid experimentation, innovation, and feature additions?
+  Is the application in a steady-state and a candidate for cloud migration?
+  Does the application have disproportionately high infrastructure costs or licensing fees?
+  Does the application perform the same business function (such as financial reporting) that other applications support? Are there opportunities for consolidation and economies of scale?
+  Is the application mission critical and does it require high availability?
+  Is the application experiencing functionality sprawl? Is there an opportunity to rearchitect?

 A recurring assessment cadence ensures ongoing alignment with your cloud transformation strategy, and helps determine where potential cloud services could help you become more competitive, address optimization needs, and reduce costs.

## Excel
<a name="excel-4"></a>

 Shared services and databases are systems that support the business specific applications. As these types of systems are migrated to the cloud, plan to integrate with consuming applications in a simple and repeatable manner. The completed application inventory will articulate the volume of consuming applications and vision for each. Having insight to move a foundational database that supports multiple consuming services that will individually be replaced, refactored, repurchased, re-platformed or relocated to the cloud first can save a lot of integration time and effort in the future.

 Automate application portfolio intelligence by using tools such as [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and your existing [ITSM](https://en.wikipedia.org/wiki/IT_service_management) tools. AppRegistry allows you to create a repository of your applications and associated cloud resources. This allows the technical context of your applications and resources across your environments to evolve and [stay up-to-date with limited manual intervention](https://aws.amazon.com/blogs/mt/increase-application-visibility-governance-using-aws-service-catalog-appregistry/).

 These capabilities enable enterprise stakeholders to obtain the information they require for informed strategic and tactical decisions about cloud resources. For example, AppRegistry enables senior leadership to get a full view of cloud deployments, the CCoE team to understand the full set of applications and resources provisioned, security team to identify resources involved in security events, and the risk and compliance team to obtain a view of all resources within an application that currently meet specific compliance certifications.

 We recommend that the application portfolio vision be a collaborative ongoing assessment by the technology and business leadership. Having an automated approach to assemble the technical metadata allows for accelerated and effective decision making.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
