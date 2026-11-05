---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/gxp-systems-assurance-layered-approach.html
---

# GxP systems assurance – The layered approach
<a name="gxp-systems-assurance-layered-approach"></a>

GxP regulations require you to demonstrate control over the environment within which GxP workloads will operate. A top-level assurance model is a good starting point to explain how each layer of the entire cloud environment will be kept under a state of control. The layered model that follows provides a structure to perhaps guide the creation of new quality management system (QMS) documents or highlight existing QMS documents in need of revision.

## The layered approach
<a name="the-layered-approach"></a>

One of the concerns for regulated enterprise customers becomes how to qualify and demonstrate control over a system when so much of the responsibility is now shared with a supplier. The purpose of the layered approach is to help answer this question.

To better scope the effort, the architecture should be viewed in its entirety. Enterprise scale customers typically define the high-level architecture similar to the following.

The layered model shows the same shared responsibility model with AWS responsible for the first foundational layers. The customer is then responsible for layers 2 and above but these layers are often owned by different internal teams, such as a platform team and the application development teams.

## Layers 0 and 1 – AWS
<a name="layers-0-and-1-aws"></a>

Demonstrating control starts at the lowest level of the model with a supplier assessment. This assessment should consider the AWS Global Infrastructure, the AWS services that will be used, where the shared responsibility boundary falls for each service, and use the documentation available from AWS Artifact. For GxP compliance purposes the most popular documents are often the SOC 2 and C5 reports, certifications such as ISO 9001, ISO 27001, ISO 27017, ISO 27018, and the AWS Quality Management System Overview document.

## Layer 2 – Landing zone
<a name="layer-2-landing-zone"></a>

This layer focuses on providing secure and compliant access to the underlying cloud services through accounts. A landing zone (LZ) is a well-architected, multi-account environment, which is a starting point from which you can deploy workloads and applications.

You can create an LZ through AWS Organizations or to expedite the creation of a complex multi-account environment AWS has developed the Landing Zone Accelerator (LZA), which you can use to describe your LZ in a template and use automation to deploy it. This has the advantage of simplifying change management of the LZ itself and demonstrating control. Any change to the LZ would involve a change to the template which is version controlled, approved, and then deployed through the automated pipeline, increasing control and consistency.

Organizational units (OUs) can be used to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach policy-based control to an OU and all accounts within the OU automatically inherit the policy. This enables the grouping of accounts subject to certain compliance regimes like GxP and apply appropriate policy controls.

Policies in AWS Organizations enable you to apply additional types of management to the AWS accounts in your organization. These are very useful when demonstrating control over the environment and can be linked to GxP requirements. There are 2 policy types, management and authorization.

Management policies enable you to centrally configure and manage AWS services and their features. One example is backup policies, which help you centrally manage and apply backup plans to the AWS resources across your AWS organization's accounts. This type of policy can be attached to an OU containing all GxP accounts to ensure backups are taken so ALCOA\+ requirements can be satisfied. Another example is tag policies, which can be used to standardize the tags attached to the AWS resource in your accounts. This will help identify resources used as part of GxP workloads and help with configuration management and an application inventory.

Authorization policies help you centrally manage the security of AWS accounts in your organization. One common GxP related request is to only allow approved services to be used as part of GxP workloads. For a service to be approved it must have been reviewed and there must be evidence available that the services is being maintained under a state of control by the cloud service provider. For example, your policy might state that only services within the scope of specific compliance programs, like SOC2, ISO 9001, ISO 27001, will be approved for general use and the audit reports and certifications will form the evidence. This policy can be implemented through service control policies (SCPs), which can control which services are allowed. Other workloads with specific regulatory constraints might require additional controls. For example, only allowing HIPAA-eligible services for the processing, storage or transmission of PHI data. This variance in compliance controls can be accommodated through the use of policies applied to different OUs.

Guardrails are governance rules for security, operations, and compliance that you can define and apply either across your AWS environment or to specific groups of accounts. Guardrails protect users from making choices that aren't aligned with your overall requirements and another great way of demonstrating control over your environment. Guardrails are classified as either preventive or detective.

Preventive guardrails establish intent and prevent deployment of resources that don't conform to your policies. For example, require AWS CloudTrail to be enabled in all accounts.

Detective guardrails continuously monitor deployed resources for non-conformance and generate alerts when detected. You can automate responses to alerts to take action. For example, disallow public read access to Amazon S3 buckets. These capabilities move away from static point in time compliance checks and closer to achieving a continuous compliance stance.

When vending new accounts for application teams, having a secure account baseline is a great way of demonstrating control. For example, drop default VPC, install approved VPC, deploy security roles and stacks, hook up CloudTrail for logging, and so on. When using the previously mentioned Landing Zone Accelerator (LZA), vending new baselined accounts is simply a matter of updating the LZA template and triggering a deployment.

Deployment will also typically include verification tests to demonstrate the LZ is functioning as expected. To accomplish this the deployment pipeline can include automated tests to provide the evidence that the LZ has been deployed, configured, and is working as expected.

The delivery and operations of the regulated landing zone and the associated capabilities will include a formal qualification effort and handover. This will include appropriate documentation such as designs and runbooks. This documentation needs to be maintained and updated as part of change management. See the [Good technical documentation](computer-system-validation.md#good-technical-documentation) section for further information.

A cloud center of excellence (CCoE) or cloud platform team is the team responsible for design, build, deployment, and ongoing governance and operation of the landing zone. Part of the CCoE is a Cloud Business Office (CBO), which often includes people that liaise with other parts of IT, like IT Finance. A role should exist for liaising with IT Quality and Compliance to keep track of regulatory changes, feed those as requirements to the cloud platform engineering team and define the control objectives to be automated as part of the LZ.

Demonstrating control over the IT operating environment is often a focus of an inspection. This traditionally meant showing extracts from a quality management system, standard operating procedures (SOPs), and a lot of reports and evidence showing compliance to those SOPs. With the cloud, tools like Amazon Security Lake, CloudTrail Lake, AWS Config, and AWS Audit Manager make this much easier. One key takeaway is that the CCoE should look for ways to be inspection-ready at all times.

## Layer 3 – Cloud foundations and automation
<a name="layer-3-cloud-foundations"></a>

This layer focuses on implementing foundational cloud capabilities and automation to support GxP workloads. It includes developing common capabilities like centralized logging and core networking, in addition to GxP required capabilities such as backup and restore, all properly documented for design, delivery, and operations.

The cloud foundations and automation layer includes identifying and templatizing common service configurations or building blocks that can be reused across multiple workloads, potentially undergoing formal service qualification for GxP compliance. There's a shift towards using infrastructure as code (IaC) templates for describing and deploying infrastructure, replacing traditional installation qualification protocols. Automation streamlines processes, reduces manual errors, and enables consistent deployments, including automated tests to verify correct configuration of services.

Any common tooling requirements can also be included in the landing zone and centrally managed. For example, security tooling required by a security operations center (SOC).

Similarly, the migration of workloads will involve the use of some common tooling. This tooling could be installed in a shared services account.

Data integrity is core to GxP regulations and so will be an area of focus during the migration of any GxP application. The tools used for the migration of data should include the ability to verify the data has been migrated without any impact to integrity. Plan how data integrity will be verified post migration. This can be a common approach defined for the entire migration effort and so not directly linked to an individual application. However, evidence will need to be linked to each application's databases.

## Layer 4 – Workload and application infrastructure
<a name="layer-4-workload-infrastructure"></a>

Layer 4 focuses on the unique infrastructure requirements for each workload, which are captured in infrastructure as code (IaC) templates, such as CloudFormation templates. These IaC templates are kept under version control in a source code repository, allowing for controlled modifications and versioning when infrastructure changes are needed.

Infrastructure deployment is automated using continuous integration and deployment (CI/CD) pipelines, with AWS CodePipeline coordinating the deployment process. This shifts the approach to an exception based process where manual action is only taken if CloudFormation reports an error. To maintain synchronization between the IaC template and the actual infrastructure, all changes should only be made through automation, with CloudFormation drift detection helping to identify any discrepancies.

The traditional manual installation qualification (IQ) process is replaced by automated deployments, with CloudFormation logs serving as deployment evidence. Services like AWS Config are used to continuously monitor and verify that deployed services remain compliant with configured rules, moving towards a model of continuous compliance monitoring. For example, as part of adhering to ALCOA\+ principles, Amazon S3 could be configured with versioning turned on. AWS Config can monitor this setting and alert if versioning is ever turned off. This use of IaC, automation, and cloud services like AWS Config enables us to move towards continuous compliance monitoring over static verification activities.

Application-specific documentation, including design specifications and operational runbooks, should be updated to reflect the move to cloud infrastructure and services.

## Layer 5 – Business applications
<a name="layer-5-business-applications"></a>

Layer 5 focuses on the initial validation and ongoing maintenance of the GxP applications themselves, integrating cloud activities into existing change management processes and maintaining thorough documentation throughout. For migrated workloads it involves possibly re-validating applications to ensure functionality remains intact post-migration, with the extent of testing based on the migration strategy used. Risk management is crucial, meaning a lift-and-shift approach to migrating GxP workloads is often preferred to minimize risk. Ultimately, this layer ensures that business applications remain compliant and functional in a cloud environment.
