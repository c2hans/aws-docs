---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/design.html
---

# Best practices for the design phase
<a name="design"></a>

The design phase of a greenfield SAP implementation is the foundation for a successful build phase.  In this phase, you work with your infrastructure stakeholders to collect requirements and document the architecture. There are also additional alignments that you must consider. You must ensure that various project stakeholders agree upon a timeline, landscape strategy, and SAP on AWS architecture, including high availability (HA) and disaster recovery (DR) environments.  This section provides recommendations for addressing some of the challenges that you might encounter in the design phase of your project.

## Create delivery timeline and landscape diagrams
<a name="landscape-diagrams"></a>

Build an infrastructure delivery timeline as soon the business transformation project timeline is shared with you.  This helps you plan ahead and get alignment within the infrastructure team. The primary input for building the timeline comes from the system integrators (SIs) on the SAP project team.  Work back to derive the dates for when the SAP Basis team should complete their work and when the infrastructure should be ready for the SAP Basis team to install the SAP applications.

Considerations:
+ A visual representation of the delivery timeline enables the team to quickly understand what is being built, the required-by dates, and possible resource contentions.   It also allows key stakeholders to visualize the environments that are being built, the duration of the project, and the hand-off between AWS and the SAP Basis team in an easy to comprehend manner.

![Delivery timeline for an SAP on AWS greenfield project.](https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/0a582649-501b-4d87-b865-696a63951913.png)

+ A typical greenfield SAP implementation spans a year or more. It includes times when the infrastructure team doesn't actively build infrastructure components, so it's important to consider the activities and deliverables during that time.  Examples of activities to map include HA setup and testing, DR setup and testing, performance testing, and building automation scripts.
+ In a greenfield implementation, the concepts of landscape and environments can be confusing to understand. A color-coded timeline that differentiates between environments and landscapes (N, N\+1, N\+2) can help stakeholders understand this matrix of information quickly.

  Here is an example of a typical high-level SAP landscape diagram. The boxes represent environments, which are a collection of applications (for example, SAP S/4HANA), and the landscapes are a collection of environments used for a particular release.
![Landscape diagram for an SAP on AWS greenfield project.](https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/1bac4a41-5e68-4c0a-a404-58bccf6cd328.png)
+ When you create the roadmap, we recommend that you revisit the high-level roadmap and conduct long-range planning on a quarterly basis until the team has become established. In addition to the migration, include other roadmap items such as workstreams for cloud center of excellence (CCoE), operations automation, security and compliance, and cloud disaster recovery.

## Understand regional services and document decisions
<a name="regional"></a>

At the beginning of the design phase, we recommend that you spend time understanding and discussing the services that are available at a particular AWS Region so that you can choose the primary Region correctly.  Specifically, high-performance instances are often required for SAP, so you must ensure that those resources are available in the primary or secondary Regions. Choose an [instance type that is certified for SAP applications](https://aws.amazon.com/sap/instance-types/). Make sure that the instance type is available in the AWS Regions of choice. A quick and easy way to determine this is to use the [AWS Command Line Interface (AWS CLI) command for instance type offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-type-offerings.html). If services aren't currently available in the Region that you want to use for your implementation, consider the lead time for ordering the infrastructure for that Region.

Confirm, reconfirm, and document Region-related decisions.  Circulate those decisions across the larger project team so that key stakeholders are informed. If there is an architecture review board for the project, be sure to present this topic to give everyone an opportunity to weigh in before the decision is solidified.

Considerations:
+ A key consideration is boundary systems that integrate with SAP.  If you're hosting boundary or satellite applications on AWS, it's best to host SAP in the same primary Region, to prevent any unnecessary discussions about latency.  Even if you confirm that latency is not an issue, it will be difficult to explain why boundary applications are built in a different Region than your SAP applications to your stakeholders.
+ The disaster recovery (DR) site should also be the same for SAP and systems that integrate with SAP so that DR testing can be coordinated realistically. Different systems might require different solutions. For example, a large SAP system such as BusinessObjects or Winshuttle might not work with AWS Elastic Disaster Recovery and might need a different solution that uses an Amazon Relational Database Service (Amazon RDS) database.
+ Make sure that the solutions and optimizations work with SAP systems. Service teams typically build services that aren't always SAP-specific for large enterprise systems.

## Establish naming conventions
<a name="naming-conventions"></a>

Thoroughly vet and document naming conventions for the host, SAP environment, virtual private cloud (VPC), and AWS accounts. Be sure to follow existing standards or conventions.  In a greenfield implementation, you will probably have to define your naming conventions from scratch.  Be consistent.  For example, if you call the VPC *Pre-Prod*, the SAP environment *UAT*, and the AWS account *TST*, it will be challenging to associate these three names from a support perspective.  Be sure to gain consensus and assign names in which every character has a meaning, but leave room for flexibility.  For example, do not hardcode the Region name into the server name, in case you have to switch to another Region in the future.  Avoid using the naming convention you're using for your on-premises servers.  Instead, recommend a flexible cloud naming convention if your organization doesn't already have one.

Considerations:
+ Use [AWS tagging](https://docs.aws.amazon.com/ARG/latest/userguide/tagging.html) for information that can change.
+ Do not put non-production environments in production VPCs.   If that's a requirement, make sure that there's a valid reason before you agree.

## Document all decisions
<a name="document-decisions"></a>

We recommend that you thoroughly document every variation of each decision, who made the decision, on what date, and who was present.  Store decisions in a public place, such as Atlassian Confluence or a spreadsheet, and ensure proper signoff on the decision.  A stakeholder or team member might forget the consensus that was reached and challenge a decision later in the design or build phase.  If that happens, you want to have data readily available to address any questions.   Here are examples of key decisions to document:
+ Region decisions
+ Applications that are HA relevant
+ Disaster recovery decisions
+ Environment support model during the project phase
+ Backup and restore methods and tools
+ VPC structure
+ AWS account decisions
+ Security decisions

In addition, track all product feature requests and document how long it took the team to implement the changes.
