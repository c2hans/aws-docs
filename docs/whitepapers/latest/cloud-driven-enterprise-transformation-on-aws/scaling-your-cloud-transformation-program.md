---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/scaling-your-cloud-transformation-program.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scaling your cloud transformation program
<a name="scaling-your-cloud-transformation-program"></a>

Teams do not need to be configured or operate identically, even in a well-defined “factory model”. Consistent with agile principles, teams should be empowered to find the best ways to collaborate within their teams, even when working in a large structured migration program.

*Table 6 – Traditional vs. modern views of implementation controls *

|  Traditional view  |  Modern view  |
| --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/scaling-your-cloud-transformation-program.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/cloud-driven-enterprise-transformation-on-aws/scaling-your-cloud-transformation-program.html)  |

 **Launch a cloud enablement engine to foster engineering best practices and reuse**

 To meet your cloud transformation objectives, take specific actions in a number of tracks:
+ Launch detailed on-premises discovery to collect baseline dependency, sizing, and performance date for the entire environment
+  Establish program, governance, and factory operating mode
+ Assign core teams and launch sprint planning for the first one or two portfolio groups to move next, and begin planning for portfolio segment migration sequencing over the course of the full program
+ Begin detailed design on complex applications (“big rocks”) for initial portfolio move groups
+ Set up an SME team to assess entire portfolio for systems with tight coupling to mainframe and midrange systems
+ Begin development of a plan to decouple, resolve, or remove these dependencies

 Launch a parallel cloud enablement engine (CEE) to:
+ Evaluate business case options
+ Review application roadmaps and help determine whether to refactor, retire, emulate, or decommission legacy mainframe and midrange platforms
+ Translate [DB2](https://www.ibm.com/products/db2-database), [SAS](https://www.sas.com/en_us/home.html), [Oracle](https://www.oracle.com/index.html), or [Teradata](https://www.teradata.com/) legacy data workloads to modern cloud services

AWS customers have access to a wide variety of quick-starts, migration patterns, open-source vendor architecture patterns, and a wealth of other patterns available to move quickly. Efficient teams who look for reusable patterns, perform careful security reviews, and build on top of prior work will move faster. Customers who set up a CEE with a pattern library and light review process can enable multiple teams across their enterprise to move quickly, shortcut non-differentiated design work, and focus on making improvements to their application performance.

AWS often works with customers to scan the application environment, identify common architectures, then develop complete designs for these patterns. This pattern-based approach can often cover a large portion of portfolio that might include simple vendor applications, application with low rates of change, or applications moving to the cloud that are on a [sunset](https://whatis.techtarget.com/definition/sunsetting) or [ringfence](https://en.wikipedia.org/wiki/Ringfencing) (no planned investment) path. With this approach, builders pick up an approved security and networking-approved template including gold AMIs, make minor adjustments, get approval on any requested changes to pattern if required, then build and go. This unlocks velocity from your teams, as the sprint flow for these pattern-based deployments can focus on resolving hard-coding issues, connection issues, or other issues found as teams progress through each environment cutover.

With these templated accelerators and common design documents, design reviews can easily be managed by a small team of cloud engineering SMEs. It is feasible for a team of expert cloud engineers using this templated approach to review all design patterns and to suggest changes, revisions, optimizations, and pattern re-use opportunities. Simultaneously, these reviewers can ensure that corporate standards are met for design and resiliency, and aligned with application tier and business criticality. If this function is not entirely centralized in this program, distribution of these review tasks by application type, technology, or business unit would all be feasible as appropriate.

A CEE that supports learning and re-use, people change, cloud adoption, and innovation is an important enabler to accelerate enterprise transformation. Migrating to the cloud provides an opportunity to re-think the IT architecture function, and from a traditional central design team, to federate architecture work, drive secure pattern re-use, set standards, cross-pollinate teams, and help solve the most challenge business problems.

Teams that use [Service Catalog](https://aws.amazon.com/servicecatalog/) to design, review, and approve re-useable capabilities, or stacks, enable teams to move faster by presenting secure, re-usable assets and only reviewing incremental changes to approved patterns, if required for a particular use case. For more information, see [Working with stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html).

**Launch a people change strategy on day 1**

In 2018, [Gartner](https://www.gartner.com/en) found that 88% of enterprise IT organizations have a cloud-first strategy, yet 86% of enterprise infrastructure spent is still directed to technology on-premises. While large organizations want to take advantage of cloud benefits, they have not undergone the necessary transformation within their organization to be successful. The existing culture, process, and tools block them from going “all-in” with AWS, even when they understand it is the right move for their business.

The lack of cloud skills and experience is a particularly difficult issue for enterprises to overcome. IT teams struggle to learn new skills while managing their current responsibilities. Many IT organizations are unable to recruit new cloud talent. This leaves leaders with a difficult decision: “Do we slow down delivery to give our teams time to transition to the cloud?”

The reality is that teams can be activated on AWS in a short period of time. The fastest way to achieve this is to learn by doing, by moving production workloads to AWS. With infrastructure as code, re-use of patterns, and under the guidance of AWS, AWS Partners, and internal expertise, it is possible to quickly enable teams on AWS. Teams engaged in migration efforts can sometimes get up to speed on AWS, infrastructure as code, and automation within 12-16 weeks. Supplementing on-the-job training with role-specific training paths and investing in educating business stakeholders helps teams succeed. See [Training and Certification](https://aws.amazon.com/training/) for more information on role-specific training paths.

You can do much more on AWS with fewer people compared to traditional siloed enterprise, on-premises operations. The key to transformation is to ignite your people’s curiosity, communicate the value proposition to learn new skills, and describe a new model where your staff can spend more time building and less time on non-differentiated heavy lifting.

People enablement through the migration process can also enable transformation in delivery and ownership to align with speed-to-market and better IT and business collaboration. The migration process is a good opportunity to re-evaluate the operations posture, including, in some cases, a move to a “run what you build” services model where the core development team may have “full stack” responsibility, including operations performance and improvements. There is no better place for experimentation with new roles and responsibilities than during the transformation program.

For a large organization, there may be a number of adaptations of teaming models, but several foundational items are common. As described earlier, such standards can be established through a central CEE or a dedicated project organization.

Team capabilities, working style, and technical obstacles will vary by team and application portfolio. AWS has learned from large-scale migrations that team members with an appetite to learn by doing on AWS can rapidly increase their confidence, skill set, and capabilities.

In addition to reinforcing the collaboration, agile methodologies, and move towards the DevOps model where appropriate, your transformation program democratizes technical skills across the IT lifecycle. An operations engineer can learn DevOps skills. Application developers can assume ownership for infrastructure provisioning and operation. Test engineers can help design a migration plan that improves test coverage and code scan automation using the corporate [CI/CD](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html) toolchain. Everyone can adapt the mindset of “security is job zero”. This process empowers teams, broadens opportunity, improves collaboration, and unlocks the creative potential of joint-disciplinary teams. The key is to get moving and gain cloud skills from this experience, fail, experiment, innovate, and delight customers.

Not everyone will be open to change. Not all staff will embrace the opportunity. Some staff may hold on to control of specific steps and processes with the goal of improving job security. Good leaders will identify and coach those who are blockers to change, use the process to cross-train and share tasks, and close documentation gaps to reduce the need to call an SME on weekends or vacation. This may also require adjustment of team members if some are not aligned with new ways of working.

There is an opportunity to move out of traditional “hero” mindset, where the most talented staff become indispensable, but are also a bottleneck and a single point of failure.

By improving documentation, automation, and using infrastructure as code to democratize build functions, a company’s IT expertise can focus on building value and business capabilities, and spend less time on non-differentiated tasks and fire-fighting.

There is a value proposition for employees. Late-night and weekend coverage for operations can be delegated, and team members can take a vacation without concern. This should be considered a key aspect of a company’s resiliency strategy, and must be supported by leadership to expand the definition of impact and value of their most talented employees.

**Work closely with finance teams to shift to cloud**

Budgeting a large cloud transformation program requires new skills. Transitioning from on-premises financial management of IT spend to AWS presents a great opportunity, using services tagging discipline to provide transparency of system costs, and architectural and resiliency cost / benefit trade-offs.

Organizations are initially uncomfortable with the shift from the precision of the cost of acquiring on-premises hardware for 4-5 years to the more flexible, adaptable, uncertain world of cloud cost management. With a disciplined migration approach, companies have achieved cost savings while migrating to AWS. They have enabled ongoing optimization as they right-size deployments and unlock additional value from moving faster and spending time on activities that create value. AWS recommends the [https://aws.amazon.com/executive-insights/content/how-to-think-like-a-digital-cfo/](https://aws.amazon.com/executive-insights/content/how-to-think-like-a-digital-cfo/) whitepaper for more information on the broader topic of cloud financial management.
