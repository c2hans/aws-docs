---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/aws-application-design-and-migration-strategy.html
---

# AWS application design and migration strategy
<a name="aws-application-design-and-migration-strategy"></a>

Designing and documenting the future state of your application is a key migration success factor. We recommend creating a design for any type of migration strategy, no matter how simple or complex. Creating the design will surface potential blockers, dependencies, and opportunities to optimize the application even in cases where the architecture is not expected to change. In addition, the resulting design will serve as a base for further evolution after the migration.

Besides the importance of the design process, it can also become a blocker and impact migration speed. This happens because of legacy architectural review processes that were conceived for on-premises systems. We recommend that you review your architectural review and approval process and focus on establishing architectural patterns or types that can be preapproved. Do not underestimate the effort of reviewing architectures for hundreds or thousands of applications, and take the opportunity to modernize the process.

The following list contains resources to aid the design process:
+ [AWS Architecture Center](https://aws.amazon.com/architecture/) combines tools and guidance, such as the AWS Well-Architected Framework. Also, it provides reference architectures that you can use for your application.
+ [The Amazon Builders' Library](https://aws.amazon.com/builders-library/) contains several resources about how Amazon builds and operates software.
+ [AWS Solutions Library](https://aws.amazon.com/solutions/) offers a collection of cloud-based solutions, vetted by AWS, for dozens of technical and business problems. It includes a large collection of reference architectures.
+ [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/) provides strategies, guides, and patterns that aid the design process and migration best practices.
+ [AWS Documentation](https://docs.aws.amazon.com/) contains information about AWS services, including User Guides and API References.
+ [Getting Started Resource Center](https://aws.amazon.com/getting-started/) provides several hands-on tutorials and deep dives to learn the fundamentals so that you can start building in AWS.

Depending on where you are in the cloud journey, AWS foundations might already exist. These AWS foundations include the following:
+ AWS Regions have been identified.
+ Accounts have been created or can be obtained on demand.
+ General networking has been implemented.
+ Foundational AWS services have been deployed within the accounts.

Conversely, you might be early in the process, and AWS foundations are not yet established. A lack of established foundations could limit the scope of your application design or require further work to define them. If this is the case, we recommend defining and implementing the foundational design of the landing zone in parallel with the application design work. The application design helps to identify requirements such as AWS account structure, networking, virtual private cloud (VPCs), Classless Inter-Domain Routing (CIDR) ranges, shared services, security, and cloud operations.

 [AWS Control Tower](https://aws.amazon.com/controltower/) provides the easiest way to set up and govern a secure, multi-account AWS environment, called a landing zone. AWS Control Tower creates your landing zone using AWS Organizations, which provides ongoing account management and governance and implementation of AWS best practices based experience working with thousands of customers as they move to the cloud.

## Application future state
<a name="application-future-state"></a>

Start by establishing the initial migration strategy for this application. At this point, the strategy is considered initial because it could change as part of the future state design, which can uncover potential limitations. To validate initial assumptions, see the [6 Rs decision tree](prioritization-and-migration-strategy.md#migration-r-type). Also, document potential migration phases. For example, will this application be migrated in a single event (all components are migrated at the same time)? Or is this a phased migration (some components are migrated later)?

Note that migration strategies for a given application might not be unique. This is because multiple R types could be used to migrate the application components. For example, the initial approach could be to lift and shift the application without changes. However, an application's components might reside in different infrastructure assets that might require diverse treatments. For example, an application is made up of three components, each running on a separate server, and one of the servers runs a legacy operating system that isn't supported in the cloud. That component will require a replatform approach, while the other two components, running in supported server versions, can be rehosted. It is key to assign a migration strategy to each application component and associated infrastructure that is being migrated.

Next, document the context and problem, and link existing artifacts that define the current state:
+ Why is this application being migrated?
+ What are the proposed changes?
+ What are the benefits?
+ Are there any major risks or blockers?
+ What are the current downsides?
+ What is in scope and out of scope?

## Repeatability
<a name="repeatability"></a>

Throughout the design work, consider how this solution and architecture for this application can be reused for other applications. Can this solution be generalized?

## Requirements
<a name="requirements"></a>

Document the functional and nonfunctional requirements for this application, including security. This includes current and future state requirements, depending on the migration strategy chosen. Use the information gathered during the detailed application assessment to guide this process.

## To-be architecture
<a name="to-be-architecture"></a>

Describe the future architecture for this application. Consider creating a reusable diagram template that contains building blocks for your source environment (on-premises) and target AWS environment (for example, target AWS Region, account, VPCs, and Availability Zones).

Create a table of components that are being migrated and components that will be new. Include other applications and services (either on premises or in the cloud) that interact with this application.

The following table lists example components. It does not represent a reference architecture or vetted configuration.

|
|
| Name | Description | Details |
| --- |--- |--- |
| Application | External service (inbound connection) | Service consumes data from exposed API. |
| DNS | Name resolution (internal) | Amazon Route 53 deployed as part of baseline account settings |
| Application Load Balancer | Distributes traffic among backend services | Replaces on-premises load balancer. Migrate Pool A. |
| Application security | DdoS protection | Implemented by using AWS Shield |
| Security group | Virtual firewall | Limit access to application instances on port 443 (inbound). |
| Server A | Front-end | Rehost, using Amazon Elastic Compute Cloud (Amazon EC2). |
| Server B | Front-end | Rehost using Amazon EC2. |
| Server C | Application logic | Rehost using Amazon EC2. |
| Server D | Application logic | Rehost using Amazon EC2. |
| Amazon Relational Database Service (Amazon RDS) – Amazon Aurora | Database | Replaces servers E and F |
| Monitoring and alerting | Change control | Amazon CloudWatch |
| Audit logging | Change control | AWS CloudTrail |
| Patching and remote access | Maintenance | AWS Systems Manager |
| Resource access | Secure access control | AWS Identity and Access Management (IAM) |
| Authentication | User access | Amazon Cognito |
| Certificates | SSL/TLS | AWS Certificate Manager |
| API 1 | External API | Amazon API Gateway |
| Object storage | Image hosting | Amazon Simple Storage Service (Amazon S3) |
| Credentials | Management and hosting of credentials | AWS Secrets Manager |
| AWS Lambda function | Retrieval of database credentials and API keys | AWS Lambda |
| Internet gateway | Outbound internet access | Internet gateway to a VPC |
| Private subnet 1 | Backend and DB | Availability Zone 1 – VPC 1 |
| Private subnet 2 | Backend and DB | Availability Zone 2 – VPC 1 |
| Public subnet 1 | Front-end | Availability Zone 1 – VPC 1 |
| Public subnet 2 | Front-end | Availability Zone 2 – VPC 1 |
| Backup services | Databases and EC2 instance backup | AWS Backup |
| DR | Amazon EC2 resiliency | AWS Elastic Disaster Recovery |

After the components have been identified, plot them in a diagram using your preferred tool. Share the initial design with the key application stakeholders, including application owners, enterprise architects, and the platform and migration teams. Consider asking the following questions:
+ Does the team generally agree with the design?
+ Can the operations teams support it?
+ Can the design be evolved?
+ Are there other options?
+ Does the design comply with architectural standards and security policies?
+ Are any components missing (for example, code repositories, CI/CD tooling, VPC endpoints)?

## Architectural decisions
<a name="architectural-decisions"></a>

As part of the design process, you will likely find more options for the overall architecture or specific parts of it. Document these options alongside the rationale for a preferred or selected option. These decisions can be documented as architectural decisions.

Ensure that the main options are listed and described with enough detail for a new reader to understand the options and reasons behind a decision to use one option over another.

## Software lifecycle environments
<a name="software-lifecycle-environments"></a>

Document any changes to current environments. For example, test and development environments will be recreated in AWS and not migrated.

## Tagging
<a name="tagging"></a>

Describe mandatory and recommended tagging for each infrastructure component as well as the tagging value for this design.

## Migration strategy
<a name="migration-strategy"></a>

By this point of the design, the initial assumptions about migration strategy should be validated. Confirm that there is consensus on the chosen R strategy. Document the overall application migration strategy and the strategies for individual application components. As mentioned previously, different application components might require different R types for migration.

In addition, align the migration strategy to key business drivers and outcomes. Also, describe any phased approach to migration, such as the movement of components in different migration events.

For more information about determining your 6 Rs, see the [AWS Migration Hub strategy recommendations](https://aws.amazon.com/blogs/aws/new-strategy-recommendations-service-helps-streamline-aws-cloud-migration-and-modernization/).

## Migration patterns and tools
<a name="migration-patterns-tools"></a>

With a defined migration strategy for the application and infrastructure components, you can now explore specific technical patterns. For example, a rehost strategy can be implemented by migration tooling such as [AWS Transform MGN](https://aws.amazon.com/application-migration-service/). If you don't need to replicate the state or data, you can achieve the same outcome by redeploying the application using an Amazon Machine Image (AMI) and an application deployment pipeline.

Similarly, to replatform or refactor (re-architect) an application, you can use tools such as [AWS App2Container](https://aws.amazon.com/app2container/), [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/), [AWS Schema Conversion Tool(AWS SCT)](https://aws.amazon.com/dms/schema-conversion-tool/) , [AWS DataSync](https://aws.amazon.com/datasync/). For containerizing, you can use [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/), or [AWS Fargate](https://aws.amazon.com/fargate/). When repurchasing, you can use an AMI for a specific product or a software as a service (SaaS) solution from [AWS Marketplace](https://aws.amazon.com/marketplace/).

Evaluate the different patterns and options that are available for achieving the goal. Consider pros and cons, and migration operational readiness. To help with your analysis, use the following questions:
+ Can migration teams support these patterns?
+ What is the balance between cost and benefits?
+ Can this application, service, or component be moved to a managed service?
+ What is the effort to implement this pattern?
+ Is there any regulation or compliance policy preventing the use of a specific pattern?
+ Can this pattern be reused? Reusable patterns are preferred. However, sometimes a pattern will be used only one time. Consider balance between the effort of a single-use pattern over an alternative reusable pattern.

[AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/) contains a variety of migration patterns and techniques.

## Service management and operations
<a name="service-management-and-operations"></a>

When creating application designs for migration to AWS, consider operational readiness. When evaluating readiness requirements with your application and infrastructure teams, consider the following questions:
+ Are they ready to operate it?
+ Are incident response procedures defined?
+ What is the expected service level agreement (SLA)?
+ Is separation of duty required?
+ Are the different teams ready to coordinate support actions?
+ Who is responsible for what?

## Cutover considerations
<a name="cutover-considerations"></a>

Considering the migration strategy and patterns, what is important to know at the moment the application is migrated? Cutover planning is a post-design activity. However, document any considerations for activities and requirements that can be anticipated. For example, document the requirement to perform a proof of concept, if applicable, and outline the test, audit, or validation requirements.

## Risks, assumptions, issues, and dependencies
<a name="risks-assumptions-issues-dependencies"></a>

Document any open risks, assumptions, and potential issues that are not yet resolved. Assign clear ownership to these items, and track progress so that the overall design and strategy can be approved for implementation. In addition, document key dependencies for implementing this design.

## Estimating run cost
<a name="estimating-run-cost"></a>

To estimate the cost of your target AWS architecture, use the [AWS Pricing Calculator](https://calculator.aws/). Add your infrastructure components as defined by your design, and obtain an estimated run cost. Factor in software licenses that are required for your application components and that are not already included in the AWS services that you will use.
