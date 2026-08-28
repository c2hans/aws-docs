---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/qualifying-building-blocks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Qualifying Building Blocks
<a name="qualifying-building-blocks"></a>

 Customers frequently want to know how AWS gives developers freedom to use any AWS service while still maintaining regulatory compliance and fast development. To address this problem you can leverage technology, but this also involves changes in process design to move away from blocking steps and towards guardrails. The changes required to your processes and IT operating model is beyond the scope of this whitepaper. However, we cover the core steps of a supporting process to qualify building blocks which is one tactic for maintaining regulatory compliance more efficiently.

 The infrastructure building block concept as defined by GAMP is an approach to qualify individual components or combinations of components which can then be put together to build out the IT infrastructure. The approach is applicable to AWS services.

 The benefit of this approach is that you can qualify one instance of a building block once and assume all the other instances will perform the same way reducing the overall effort across applications. The approach also enables customers to change a building block without needing to re-qualify all of the others or re-validate the applications dependent upon the infrastructure.

## Service Approval
<a name="service-approval"></a>

 Service approval is a technique used by many customers as part of architecture governance, that is, it’s used across regulated and non-regulated workloads. Customers often consider multiple regulations when approving a service for use by development teams. For example, you may allow all services to be used in sandbox accounts, but may restrict the services in an account to only HIPAA-eligible services if the application is subject to HIPAA regulations.

 Service approval is implemented through the use of [AWS Organizations and Service Control Policies](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-in-aws-organizations-to-enforce-healthcare-compliance-in-your-aws-account/).

 You could take this approach to allow services to be used as part of GxP relevant applications. For example, a combination of ISO, PCI, SOC, and HIPAA-eligibility may provide sufficient confidence. Sometimes, customers want to implement automated controls over the approved service as described in [Approving AWS services for GxP workloads](https://aws.amazon.com/blogs/industries/approving-aws-services-for-gxp-workloads/).

 You may prefer to follow a more rigorous qualification process like the following building block qualification.

## Building Block Qualification
<a name="building-block-qualification"></a>

 The qualification of AWS service *building blocks* follows a process based on the GAMP IT Infrastructure Control and Compliance guidance documents ‘Infrastructure Building Block Concept’ (Section 9 / Appendix 2 of GAMP IT).

 According to EU GMP, the definition of [qualification](https://ec.europa.eu/health/sites/health/files/files/eudralex/vol-4/pdfs-en/glos4en200408_en.pdf) is: “Action of proving that any equipment works correctly and actually leads to the expected results.” The equipment also needs to continue to lead to the expected results over its lifetime.

 In other words, your process should show that the building block works as intended and is kept under control throughout its operational life. There will be written procedures in place and, when executed, records will show that the activities actually occurred. Also, the staff operating the services need to be appropriately trained. This process is often described in an SOP describing the overall qualification and commissioning strategy, the scope, roles and responsibilities, a deliverables list and any good engineering practices that will be followed to satisfy qualification and commissioning requirements.

 With the number of AWS services, it can be difficult for you to qualify all AWS services at once. An iterative and risk-based approach is recommended where services are qualified in priority order. Initial prioritization will take into account the needs of the first applications moving to cloud and then the prioritization can be reassessed as demand for cloud services increases.

## Design Stage
<a name="design-stage"></a>

### Requirements
<a name="requirements"></a>

 The first activity is to consider the requirements for the building block. One approach is to look at the service API definition. Each AWS service has a clearly documented API describing the entire functionality of that service. Many service APIs are extensive and support some advanced functionality. However, not all of this advanced functionality may be required initially so any existing business use cases can be considered to help refine the scope.

 For example, when noting Amazon S3 requirements, you include the core functionality of creating/deleting buckets and the ability to put/get/delete objects. However, you may not include the lifecycle policy functionality because this functionality is not yet needed. These requirements are captured in the building block requirements specification / requirements repository.

 It’s also important to consider non-functional requirements. To ensure suitability of a service you can look at the services SLA and limits.

### Gap Analysis
<a name="gap-analysis"></a>

 Where application requirements already exist, in the same way you can restrict the scope, you can also identify any gaps. Either the gap can be addressed by including more functionality for the building block, like bringing the Amazon S3 Bucket Lifecycle functionality into scope, or the service is not suitable for satisfying the requirements and an alternate building block should be used.

 If no other service seems to meet the requirements, you can custom develop a service, or make a feature request to AWS for service enhancement.

### Risk Assessment
<a name="risk-assessment"></a>

 Infrastructure is qualified to ensure reliability, security, and business continuity for the validated applications running on it. These three dimensions are usually included as part of any risk assessment. The published AWS SLA provides confidence in AWS services reliability. Data regarding the current status of the service plus historical adherence to SLAs is available from [https://status.aws.amazon.com](https://status.aws.amazon.com). For confidence in security, the AWS certifications can be checked for the relevant service. For business continuity, AWS builds to guard against outages and incidents, and accounts for them in the design of AWS services, so when disruptions do occur, their impact on customers and the continuity of services is as minimal as possible.

 This step is also not only for GxP qualification purposes. The risk assessment should include any additional checks for other regulations such as HIPAA.

 When assessing the risks for a cloud service, it’s important to consider the relationship to other building blocks. For example, an Amazon RDS database may have a relationship to the Amazon VPC building block because you decided a database is only allowed to exist within the private subnet of a VPC. Therefore, the VPC is taking care of many of the risks around access control. These dependencies will be captured in the risk assessment and then focus on additional risks specific to the service, or residual risks which cannot be catered for by the surrounding production environment.

 Each cloud service building block goes through a risk assessment that identifies a list of risks. For each identified risk, a mitigation plan is created. The mitigation plan can influence one or more of the following components:
+  Service Control Policy
+  Technical Design/Infrastructure as Code Template
+  Monitoring & Alerting of Automated Compliance Controls

 A risk can be mitigated through the use of Service Control Policies (SCPs) where a service or specific operation is deemed too risky and its use explicitly denied through such a policy. For example, you can use an SCP to restrict the deletion of an Amazon S3 object through the AWS Management Console. Another option is to control service usage through the technical design of an approved Infrastructure as Code (IaC) template where certain configuration parameters are restricted or parameterized. For example, you may use an AWS CloudFormation template to always configure an Amazon S3 bucket as private. Finally, you can define rules that feed into monitoring and alerting. For example, if the policy states Amazon S3 buckets cannot be public, but this configuration is not enforced in the infrastructure template, then the infrastructure can be monitored for any public Amazon S3 buckets. When an S3 bucket is configured as public, an alert triggers remediation, such as immediately changing a bucket to private.

### Technical Design
<a name="technical-design"></a>

 In response to the specified requirements and risks, an architecture design specification will be created by a Cloud Infrastructure Architect describing the logical service building block design and traceability from risk or requirement to the design. This design specification will, among other things, describe the capabilities of the building block to the end users and application development teams.

### Design Review
<a name="design-review"></a>

 To verify that the proposed design is suitable for the intended purpose within the surrounding IT infrastructure design, a design review can be performed by a suitably trained person as a final check.

## Construction Stage
<a name="construction-stage"></a>

 The logical design may be captured in a document, but the physical design is captured in an Infrastructure as Code (IaC) template, like an AWS CloudFormation template. This IaC template is always used to deploy an instance of the building block ensuring consistency. For one approach, see the [Automating GxP compliance in the cloud: Best practices and architecture guidelines](https://aws.amazon.com/blogs/industries/automating-gxp-compliance-in-the-cloud-best-practices-and-architecture-guidelines/) blog post.

 The IaC template will use parameters to deal with workload variances. As part of the design effort it will be determined, often by IT Quality and Security, which parameters affect the risk profile of the service and so should be controlled and which parameters can be set by the user. For example, the name of a database can be set by the template user and generally does not affect the risk profile of a database service. However, any parameter controlling encryption does affect the risk profile and therefore is fixed in the template and not changeable by the template user.

 The template is a text file that can be edited. However, the rules expressed in the template are also automated within the surrounding monitoring and alerting. For example, the rule stating that the encryption setting on a database must be set can be checked by automated rules. Therefore, a developer may override the encryption setting in the development environment, but that change isn’t allowed to progress to a validated environment or beyond.

 At this point, automated test scripts can be prepared for executing during the qualification step to generate test evidence. The author of the automated tests must be suitably trained and a separate and suitably trained person performs a code review and/or random testing of the automated tests to ensure the quality level.

 The automated tests ensure the building block initially functions as expected. These tests can be run again to ensure the building block continues to function as expected, especially after any change. However, to ensure nothing has changed once in production, you should identify and create automated controls. Using the Amazon S3 example again, all buckets should be private. If a public bucket is detected, it can be switched back to private and an alert raised and notification sent. You can also determine the individual that created the S3 bucket and revoke their permissions.

 The final part of construction is the authoring and approval of any needed additional guidance and operations manuals. For example, how to recover a database would be included in the operations manual of an Amazon RDS building block.

## Qualification and Commissioning Stage
<a name="qualification-and-commissioning-stage"></a>

 It’s important to note that infrastructure is deployed in the same way for every building block, i.e. through [AWS CloudFormation](https://aws.amazon.com/cloudformation/) using an Infrastructure as Code template. Therefore, there is usually no need for building block specific installation instructions. Also, you are confident that every deployment is done according to specification and has the correct configuration.

 **Automated Testing**

 If you want to generate test evidence, you can demonstrate that the functional requirements are fulfilled and that all identified risks have been mitigated, thus indicating the building block is fit for its intended use, through the execution of the automated tests created during construction. The output of these automated tests are captured into a secure repository and can be used as test evidence.

 This automation deploys the building block template into a test environment, executes the automated tests, captures the evidence, and then destroys the stack again avoiding any ongoing costs.

 Testing may only make sense in combination with other building blocks. For example, the testing of a NAT gateway can only be done within an existing VPC. One alternative is to test within the context of standard archetypes, i.e. a complete stack for a typical application architecture.

## Handover to Operations Stage
<a name="handover-to-operations-stage"></a>

 The handover stage ensures that the cloud operation team is familiar with the new building block and is trained in any service specific operations. Once the operations team approves the new building block, the service can be approved by changing a Service Control Policy (SCP). The Infrastructure as Code template can be made available for use by adding it into the [Service Catalog](https://aws.amazon.com/servicecatalog) or other secure template repository.

 If the response to a risk was a SCP or Monitoring Rule change, then the process to deploy those changes are triggered at this stage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
