---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/developing-a-business-driven-cloud-strategy.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Developing a business-driven cloud strategy
<a name="developing-a-business-driven-cloud-strategy"></a>

Working with customers, AWS sees two main factors inhibiting progress on a tactical level:
+  Technology teams are challenged when making decisions on the AWS architecture to find a clear path forward that balances modernization and migration progress.
+  A lack of clear criteria to balance between the effort required to achieve the platform transformation and the need to continue to deliver new business capabilities (such as feature releases) on existing systems.

Engineers and architects often see the move to AWS as an opportunity to deliver on aspirational projects and implement multiple major changes. Moving to project mode with dedicated team resources from business and IT teams will accelerate change, but do not refactor everywhere. Successful companies take an approach that balances speed, addresses technical debt where it inhibits modernization, and defers lower priority optimization until after deployment on AWS.

Always map technical debt to business value by prioritizing effort along strategic modernization themes aligned to business objectives (such as time to market) or strategic initiatives (such as near real-time data availability, next best action, customer 360, and personalization).

* Table 2 – Traditional vs. modern view of IT migration strategy *

|  Traditional view  |  Modern view  |
| --- | --- |
|  Try to develop a cloud strategy based only on asset data and technical considerations. +   Server / VM-based strategy  <br />+   Start with easy / cloud-compatible applications  <br />+   Focus on deployments in development environment  <br />+   Leave challenging problems for next year   |  Business requirements drive cloud strategy and migration path. +  Modernize what matters  <br />+  Prioritize degree of change based on business value (move to managed, cloud native, microservices)  <br />+  Empower builders with secure self-service  <br />+  Address technical debt and End of Serviceable Life (EOL) across the application “full stack” to support business capability gaps, security, and resiliency requirements  <br />+  Start design, planning, and build for toughest migrations while migrating simpler use cases to accelerate experience  <br />+  Business applications in production on AWS as a primary program health KPI   |

 It matters how your business processes are supported by your application portfolio. Your business priorities should matter too, as well as your transformation timeline. Along with the [7 Rs](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html) (seven migration strategies for moving applications to the cloud), three cloud migration strategies emerge:
+ **Move, then optimize (move quickly, then continue optimizing where there is business value)** — Move quickly with traditional lift and shift to capitalize on immediate run cost savings, then optimize in the cloud. Identify longer term modernization and refactoring opportunities during design review, and place them in the backlog to address after migrating to AWS. In some cases, systems that are planned for run-out in 3-5 years might benefit from migration to a co-location facility adjacent to an [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), so that dependent, cloud-ready workloads can move before rewriting systems to resolve dependencies.
+ **Modernize what matters (larger refactoring, such as the mainframe where there is business value)** — If priorities and resources are aligned, invest in incremental or full modernization depending on the business value, technical debt, and other priorities. Begin evaluation of opportunities to resolve structural dependencies on legacy workloads, including high technical debt systems and common mainframe and mid-range systems. Retire, re-purchase, retain, or refactor these legacy workloads based on business need.
+ **Minimal optimization to fix problems stopping you from moving faster** —Upgrade or renew outdated technologies across the full stack, and decouple legacy systems to address pain points that slow down development of new capabilities or drag resources into non-differentiated work. In most cases, this also require close coordination with application, testing teams, and business product owners to determine how far to modernize before migrating to AWS.

 Navigating those three strategies across your business applications portfolio will enable the flywheel for your cloud transformation.

![A diagram showing business strategy-driven transformation approach](https://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/images/CT3.jpg)

*Cloud transformation flywheel model *

Customers often think about modernization as an “all or nothing” move to cloud-native architecture. There are so many variations between a “lift and shift” and full-stack refactoring. When you adopt a mindset that you are not just planning to survive four to five years of on-premises infrastructure lifecycle, you have options to put optimization ideas in your system backlog and prioritize improvements after going live on AWS.

With so many options, analysis paralysis can set in. Tackle the change volume that your teams can manage, along with other delivery priorities. Tackle the modernization projects that unlock the most value. Empower teams to make these trade-off decisions, and encourage decision-making and movement over perfection. The most important thing is to make decisions efficiently, understanding that delaying decisions is a decision to do nothing.

Evaluating options that are not realistic based on team skills, resources, or other priorities get a lot of companies stuck in analysis paralysis. Embracing a mindset of data-driven, continuous improvement permits teams to focus on incremental change, smaller steps, and using performance data and feedback to inform the ongoing path of modernization and optimization.

![A diagram of the application portfolio rationalization decision model](https://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/images/CloudTransformation4.png)

*Application portfolio rationalization decision model *

 On AWS, a number of quick paths to modernization can be adopted, such as:
+  **Infrastructure as code** – Automate provisioning of infrastructure using templates, quick starts, and secure stacks vended through the [Service Catalog](https://aws.amazon.com/servicecatalog/).
+  **Incremental deployment automation** – Move toward automated deployments for middleware and application code, leveraging a common cloud-based code pipeline with controls built in and adoption of [DevSecOps](https://www.devsecops.org/) practices.
+  **Auto-scaling** – Allowing horizontal scaling, instance swaps, and self-healing / auto-recovery mechanisms to automate manual operations tasks.
+  **Enhanced resiliency** – Standard pipeline to enable redeployment / failover to another [Availability Zone (AZ) or Region](https://aws.amazon.com/about-aws/global-infrastructure/?p=ngi&loc=1) for business-critical applications with resiliency / disaster recovery requirement.
+  **Move to managed services** to reduce undifferentiated heavy lifting such as managed databases ([Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) and so on).
+  **Move to containers** – Begin to break down monoliths into smaller services and containerize applications for ease of management and deployment, starting with components for which [Docker images](https://docs.docker.com/engine/reference/commandline/images/) are ready off the shelf.
+  **Opportunistic refactoring** – Rewrite particular pieces of your application stack; for example, by moving event-driven components to serverless (such as [AWS Lambda](https://aws.amazon.com/lambda/), [AWS Step Functions](https://aws.amazon.com/step-functions/), and [AWS Batch](https://aws.amazon.com/batch/)), or your proprietary database engine to AWS-native data stores (such as [Amazon Aurora](https://aws.amazon.com/rds/aurora/)).
+  **Standardize application layers** – standardize application stack and architecture; for example, consolidate technologies for web / app / middleware layers where minimum refactoring is sufficient (such as moving to an [Apache Tomcat](http://tomcat.apache.org/) shared layer).
+  **Repurchase** – For example, move to Software as a Service (SaaS) or purchase a replacement from the [AWS Marketplace](https://aws.amazon.com/marketplace) for cloud-based commercial off the shelf (COTS) applications.

 Using this approach, a number of common patterns and paths emerge, as shown in Table 3:

* Table 3 – Application deployment patterns *

 Select the pattern and the path (mode of migration) based on relative business value, rate of change, team skills, and capacity.

<table>
<thead>
  <tr><th> Pattern </th><th> Automated migration </th><th> Pattern-based migration </th><th> Bespoke / custom architecture </th><th colspan="2"> Incremental automation and resiliency </th><th> Average % of mix</th></tr>
</thead>
<tbody>
  <tr><td> </td><td> Includes VMware Cloud on AWS or <a href="https://www.cloudendure.com/">CloudEndure</a> </td><td> Containers or pattern build, review incremental changes if required, leverage pre-built quick-starts </td><td> Custom architecture </td><td> During move (pipeline deployment) </td><td> Move, then optimize </td><td> </td></tr>
  <tr><td> Refactor (re-write, decouple, move to managed, or cloud-native) </td><td> </td><td> <b>X</b> </td><td> <b>X</b> </td><td> <b>X</b> </td><td> </td><td> ~5-10% </td></tr>
  <tr><td> Repurchase / Replace (drop and shop) </td><td colspan="5"> Move to SaaS or purchase a replacement from AWS Marketplace and migrate users to new platform. </td><td> &lt;5% </td></tr>
  <tr><td> Replatform (shift and reshape) </td><td> </td><td> <b>X</b> </td><td> <b>X</b> </td><td> <b>X</b> </td><td> </td><td> ~40% </td></tr>
  <tr><td> Rehost (lift and shift) </td><td> <b>X</b> </td><td> <b>X</b> </td><td> </td><td> <b>X</b> </td><td> <b>X</b> </td><td> ~40% </td></tr>
  <tr><td> Relocate </td><td> <b>X</b> </td><td> </td><td> </td><td> </td><td> <b>X</b> </td><td> &lt;5% </td></tr>
  <tr><td colspan="2"> Plus: Retain on premises, forklift from colocation, or Retire </td><td> </td><td> </td><td> </td><td> </td><td> ~5-10% </td></tr>
</tbody>
</table>

There are trade-offs for each path. Automated, tool-based migration is a replica of on-premises configuration, and will not improve your capability for continuous deployment or resolve any technical debt. Automated rehosting is the fastest path, and might be particularly useful if there is a divestiture or requirement for avoiding impact on existing vendor support arrangements. This can also be a path for rapid migration for time-sensitive data center exits, but it will still require close coordination with business stakeholders for testing and UAT, as well as a complete understanding of dependencies between applications.

The pattern-based approach for “like for like” migrations can help teams move at scale, re-use common design patterns, and add in incremental resiliency and DevOps capabilities with limited change to the application.

A custom migration would apply to complex, multi-tier, business critical applications (“big rocks”) requiring bespoke architecture. Based on the business case and competing priorities for time and resources, this path could still range from incremental changes to full modernization or re-write as required. This custom category includes large-scale databases and application re-writes that also might require refactoring of business workloads or business processes.
