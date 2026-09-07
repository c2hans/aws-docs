---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/qualification-strategy-for-life-science-organizations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Qualification Strategy for Life Science Organizations
<a name="qualification-strategy-for-life-science-organizations"></a>

 One of the concerns for regulated enterprise customers becomes how to qualify and demonstrate control over a system when so much of the responsibility is now shared with a supplier. The purpose of a Qualification Strategy is to answer this question. Some customers view a Qualification Strategy as an overarching Validation Plan. The strategy will employ various tactics to address the regulatory needs of the customer.

 To better scope the Qualification Strategy the architecture should be viewed in its entirety. Enterprise scale customers typically define the architecture similar to the following:

![Layered architecture](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/layered-architecture.png)

*Layered architecture *

 The diagram illustrates a layered architecture where a large part is delegated to AWS. From this approach, a Qualification Strategy can be defined to address four main areas:

1.  How to work with AWS as a supplier of services.

1.  The qualification of the regulated landing zone.

1.  The qualification of building blocks.

1.  Supporting the development of GxP applications.

 The situation also changes slightly if the customer leverages a service provider, like [AWS Managed Services](https://aws.amazon.com/managed-services), where the build, operation and maintenance of the landing zone is done by the service provider. Conversely, for workloads that must remain on-premises, [AWS Outposts](https://aws.amazon.com/outposts/) extends AWS services including compute, storage and networking to customer sites. Data can be configured to be stored locally, and customers are responsible for controlling access around Outposts equipment. Data that is processed and stored on-premises is accessible over the customer’s local network. In this case, customer responsibility extends into the *AWS Services* box (*Figure 3*).

![Layered architecture with service provider](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/layered-arch-service-provider.png)

*Layered architecture with service provider *

 In this situation, even more responsibility is delegated by the customer and so the controls that are typically to be put in place by the customer to control their own operations, now need adaptations to check that similar controls are implemented by the service provider. The controls that are inherited from AWS, are shared or that remain with the customer were covered previously in the [Shared Security Responsibility Model](shared-security-responsibility-model.md) section of this whitepaper.

 This section describes these layers at a high level. These layers are expanded upon in later sections of this whitepaper.

## Industry Guidance
<a name="industry-guidance"></a>

 The following guidance is at a minimum, a best practice for your environment. You should still work with your professionals to ensure you comply with applicable regulatory requirements.

 The same basic principles that govern on-premises infrastructure qualification also apply to cloud-based systems. Therefore, this strategy uses a tactic of leveraging and building upon that same industry guidance, using a cloud perspective, based on the following ISPE GAMP Good Practice Guides:
+  GAMP Good Practice Guide: IT Infrastructure Control and Compliance 2nd Edition
+  GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems

![Mapping industry guidance to architecture layers](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/map-industry-guidance.png)

* Mapping industry guidance to architecture layers *

## Supplier Assessment and Management
<a name="supplier-assessment-and-management"></a>

 Industry guidance suggests you leverage a supplier’s experience, knowledge and documentation as much as possible. However, with so much responsibility now delegated to a supplier, the supplier assessment becomes even more important. A regulated company is still ultimately accountable for demonstrating that a GxP system is compliant, even if a supplier is responsible for parts of that system, so the regulated customer needs to establish enough trust in their supplier.

 The cloud service provider must be assessed to first determine if they can deliver the services offered, but also to determine the suitability of their quality system and that it is systematically followed. The supplier needs to show that they have a QMS and follow a documented set of procedures and standards governing activities such as:
+  Infrastructure Qualification and Operation
+  Software Development
+  Change Management
+  Release Management
+  Configuration Management
+  Supplier Management
+  Training
+  System security

 Details of the AWS QMS are covered in the [software](quality-infrastructure-and-support-processes.md) section of this whitepaper. The capabilities of AWS to satisfy these areas may be reassessed on a periodic basis, typically by reviewing the latest materials available through AWS Artifact (i.e. AWS certifications and audit reports).

 It is also important to consider and plan how operational processes that span the shared responsibility model will operate. For example, how to manage changes made by AWS to services used as part of your landing zone or applications, incident response management in cases of outages, or portability requirements should there be a need to change cloud service provider.

## Regulated Landing Zone
<a name="regulated-landing-zone"></a>

 One of the main functions of the landing zone is to provide a solid foundation for development teams to build on, and address as many regulatory requirements as possible, thus removing the responsibility from the development teams.

 The GAMP IT Infrastructure Control and Compliance guidance document follows a platform-based approach to the qualification of IT infrastructure which aligns perfectly with a customer’s need to qualify their landing zone. [AWS Control Tower](https://aws.amazon.com/controltower/) provides the easiest way to set up and govern a new, secure, multi-account AWS environment based on best practices established through AWS’ experience working with thousands of enterprises as they move to the cloud. See [AWS Control Tower features](https://aws.amazon.com/controltower/features/) for further details of what is included in a typical landing zone.

 GAMP also describes two scenarios for approaching platform qualification.
+  The first scenario is independent of any specific application and instead considers generic requirements for the platform, or landing zone.
+  The second scenario is where the requirements of the platform are derived directly from the applications that will run on the platform.

 For many customers, when first building their landing zone, the exact nature of the applications that will run on it is unclear. Therefore, this paper follows scenario 1 and approaches the qualification independent of any specific application. The objective of the landing zone is to provide application teams with a solid foundation upon which to build while addressing as many regulatory requirements as possible so the regulatory burden on the application team is reduced.

### Tooling and Automation
<a name="tooling-and-automation"></a>

 Many customers include common tooling and automation as part of the landing zone so it can be qualified and validated once and used by all development teams. This common tooling is often within the shared services account of the landing zone.

 For example, standard tooling around requirements management, test management, CI/CD, etc. need to be qualified and validated.

 Similarly, any automation of IT processes also needs to be validated. For example, it’s possible to automate the Installation Qualification (IQ) step of your Computer Systems Validation process.

### Leveraging Managed Services
<a name="leveraging-managed-services"></a>

 Instead of building and operating a landing zone yourself, you have the option of delegating this responsibility. This delegation could be to AWS by making use of [AWS Managed Services](https://aws.amazon.com/managed-services) or to a partner within the [AWS Partner Network](https://aws.amazon.com/partners/) (APN). This means the service provider is responsible for building a landing zone based on AWS best practices, operating it in accordance with industry best practices and providing sufficient evidence to you in meeting your expectations.

## Building Blocks
<a name="building-blocks"></a>

 When it comes to the virtualized infrastructure and service instances supporting an application, there are two approaches to take.

1.  Commission service instances for a specific application. Each application team therefore takes care of their own qualification activities, but possibly causing duplication of qualification effort across application/product teams.

1.  Define ‘building blocks’ to be used across all applications. Create standard reusable building blocks that can be qualified once, and used many times.

 To reduce the overall effort and the increase developer productivity, this paper assumes the use of option 2.

 A ‘building block’ could be a single AWS service, such as Amazon EC2 or Amazon RDS, a combination of AWS services, such as Amazon VPC and NAT Gateway, or a complete stack, such as a three-tier web app or ML Ops stack.

 The qualification of ‘building blocks’ follows a process based on the GAMP IT Infrastructure Control and Compliance guidance document’s ‘9.2 Infrastructure Building Block Concept’.

 To accelerate application development, you could create a library of these standardized and pre-qualified building blocks which are made available to development teams to easily consume.

## Computer System Validation
<a name="computer-system-validation"></a>

 With a solid and regulatory compliant foundation from the supplier assessment and landing zone, you can look at improving your existing Computer Systems Validation (CSV) standard operating procedure (SOP). Most customers already have existing SOPs around Computer Systems Validation. Many customers also state that their processes are old, slow and very manual in nature and view moving to the cloud as an opportunity to improve these processes and automate as much as possible.

 The ‘building block’ approach described earlier is already a great accelerator for development teams, enabling them to stitch together pre-qualified building blocks to form the basis of their application. However, the application team is still responsible for the Validation of their application including Installation Qualification (IQ).

 Again, this is another area where customer approach varies. Some customers follow existing processes and still generate documentation which is stored in their Enterprise Document Management System. Other customers have fully adopted automation and achieved ‘near zero documentation’ by validating their tool chain and relying on the data stored in those tools as evidence.

## Validation During Cloud Migration
<a name="validation-during-cloud-migration"></a>

 One important point that may be covered in a Qualification Strategy is the overarching approach to Computer System Validation (CSV) during migration. If you are embarking on a migration effort, part of the analysis of the application portfolio will be to identify archetypes, or groups of applications with similar architectures. A single runbook can be developed and then repeated for each of the applications in the group, speeding up migration.

 At this point, if the applications are GxP relevant, the CSV/migration strategy can also be defined for the archetype and repeated for each application.
