---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/tech-foundation.html
---

# Technical foundation workstream
<a name="tech-foundation"></a>

This workstream involves decisions that require significant rework if changed, so the workstream emphasizes careful design, wide consultation, and up-front investment in DevOps processes and testing.

The technical foundation workstream consists of five phases: discovery and roadmap, design, build, test, deploy, and post go-live support.

![Technical foundation workstream in contact center migrations](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/3d59eb12-aa74-43a6-9c6e-c01ce3a24442.png)

## Discovery and roadmap
<a name="discovery-and-roadmap.4c727502-3578-56cd-bb75-908cabea21d1"></a>

In this phase, you gather information and schedule workshops for the following:
+ As-is mapping – Examine systems and capabilities, gather data, and meet with SMEs to understand the current state of the contact center.
+ To-be design and gap assessment – Determine the ideal experience for all contact center agents and customers to determine project scope.
+ Gap closure plan – Outline a roadmap for building and deploying the future state of the contact center.

Workshop attendees:
+ Project managers
+ Business, solutions, technical, and security architects
+ Infrastructure platform owners

## Design
<a name="design.48c59f79-ac3e-5c45-9190-6cdd889a5160"></a>

In this phase, you produce design documents. You might have your own conventions or processes for creating design artifacts. We recommend including at least three sections in the design document: Amazon Connect Customer configuration, networking, and security. Each section will likely have different, specialized stakeholder groups to ensure effective reviews and sign-offs, so it might be more practical to create separate documents for these three areas. Stakeholders should include architects, the security and compliance team, and platform owners.

## Build
<a name="build.ba2a690b-a6b4-5409-862e-64c3e6ff3247"></a>

In this phase, you follow infrastructure as code (IaC) principles by using DevOps tools to standardize and manage stable releases. Avoid adopting a manual build process, even if it helps you get started more quickly, because this can increase the risks to stability and the number of bugs as the build becomes more complex and is promoted to the test and production environments. If you don't have your own DevOps tools, we recommend that you use AWS tools such as AWS CodePipeline and AWS CodeBuild, which can be switched on quickly. Factor the effort for setting up these tools into the scope of the project; they will be beneficial in the long term and enable you to follow DevOps principles. We recommend that you build in at least three separate AWS accounts for development, testing, and production. DevOps tools and automation can help you move code through these environments.

## Test
<a name="test.d9284d38-ca88-5127-bac5-249092ab7b4a"></a>

The test phase consists of three sequential subphases:

1. Unit testing – Testing individual infrastructure components to ensure that they are correct and within design specifications. Performed by: developers

1. Integration testing – Testing items that form integration boundaries, such as Microsoft Active Directory (AD) identity management services. Performed by: developers

1. Product testing – End-to-end testing of functional journeys throughout the infrastructure; for example, testing that each agent event is logged in the security monitoring tool, the call is taken, and the call recording is in the correct Amazon Simple Storage Service (Amazon S3) bucket. Performed by: functional test team

## Deploy
<a name="deploy.05c97aa1-7259-5009-a530-99cea6c409c2"></a>

The infrastructure must be ready to handle live traffic when user journeys are scheduled to go live. The focus in the deployment phase is to ensure that AWS service quotas meet expected call volumes and the number of concurrent agents, number porting or toll-free number service (TFNS) repointing is complete, and the health of backend systems is being monitored as live traffic volumes ramp up. The security and compliance team should also confirm that the platform is ready for live traffic from their perspective.

## Post go-live support (PGLS)
<a name="post-go-live-support--pgls-.08eff6f8-6169-5fa6-ad9c-5e63cfa65bb6"></a>

The project team remains engaged with the business as usual (BAU) support teams and end-users during the first few weeks after the new contact center goes live. The project team can help users get started on the new system, get involved in troubleshooting issues alongside the BAU support team, and improve support documentation based on feedback.
