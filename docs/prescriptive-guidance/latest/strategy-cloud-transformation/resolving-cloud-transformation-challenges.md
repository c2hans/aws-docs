---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-transformation/resolving-cloud-transformation-challenges.html
---

# Resolving cloud transformation challenges
<a name="resolving-cloud-transformation-challenges"></a>

In the [Key challenges in a cloud adoption journey](cloud-transformation-challenges.md) section, we discussed the common challenges and questions that decision makers have when preparing their organization for a cloud transformation. In this section, we discuss best practices and make recommendations to help decision makers work through those challenges and questions. The recommendations are structured according to the six perspectives of the AWS CAF:
+ [Business perspective](#business-perspective)
+ [People perspective](#people-perspective)
+ [Governance perspective](#governance-perspective)
+ [Platform perspective](#platform-perspective)
+ [Security perspective](#security-perspective)
+ [Operations perspective](#operations-perspective)

## Business perspective
<a name="business-perspective"></a>

The *business perspective* helps you ensure that your cloud investments accelerate your digital transformation ambitions and business outcomes. For more information about this AWS CAF perspective, see [Business perspective: strategy and outcomes](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/business-perspective.html) in *An Overview of the AWS Cloud Adoption Framework* and see [AWS Cloud Adoption Framework: Business Perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-business-perspective/aws-caf-business-perspective.html).

Companies use cloud technology to reimagine their products, services, and revenue or business models. This involves automating, digitizing, and optimizing multiple processes, such as order to cash, procure to pay, plan to deliver, and concept to launch processes. For example, Toyota used the AWS Cloud to develop a collision assistance product that aims to improve the driving experience. For more information, see [Toyota on AWS](https://aws.amazon.com/solutions/case-studies/innovators/toyota/).

The following mechanisms can help you align your business objectives in order to maximize the benefits of cloud adoption:
+ **Envisioning workshop** – Conduct an envisioning workshop with senior leaders within the organization who expect to benefit from the cloud transformation initiatives. In the workshop, focus on identifying clear business outcomes that align with organizational strategic goals and link them to your cloud initiatives. Determining measurable business outcomes helps demonstrate the value your organization realizes through the cloud transformation journey. The result of the envisioning workshop should be to visualize and prioritize the cloud initiatives. For example, if an energy utility company wants to prioritize the adoption of smart energy meters in its customer segment, then the enabling cloud technology can be Internet of Things (IoT). IoT services can help the company gather data, process data, and provide insights about energy consumption.
+ **Alignment workshop** – Conduct an alignment workshop to guide and prepare the business and technology stakeholders for the transformation from their traditional IT environment to the cloud. This workshop should be comprised of interactive sessions, where stakeholders are challenged to reevaluate their knowledge, assumptions, expectations, and objectives for the cloud transformation. The output of this workshop should be an action plan that facilitates the transition to a cloud environment by aligning strategies across multiple categories, such as platform architecture, organization alignment, security guardrails, operational excellence, and governance controls.

These workshops can provide a snapshot of how the cloud can deliver business outcomes and which interventions or alignments are required for the other AWS CAF perspectives.

## People perspective
<a name="people-perspective"></a>

The *people perspective* helps organizations evolve to a culture of continuous growth and learning, where change becomes business-as-normal. This perspective focuses on culture, organizational structure, leadership, and the workforce. For more information about this AWS CAF perspective, see [People perspective: culture and change](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/people-perspective.html) in *An Overview of the AWS Cloud Adoption Framework* and see [AWS Cloud Adoption Framework: People Perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-people-perspective/aws-caf-people-perspective.html).

In the cloud, you can automate a wide range of management and operational tasks to support your IT infrastructure. These tasks are known as *undifferentiated* tasks because they can consume a great deal of resource bandwidth but don't directly contribute to business growth and customer experience. When you reduce the number of manually performed undifferentiated tasks, your IT resources have more time to innovate.

These changes might require that you update your operating model; organization structure; responsible, accountable, consulted, informed (RACI) matrices; and roles and responsibilities. For example, the University of Auckland in New Zealand developed the Cloud Uplift Standards and Practices (CUSP) framework as a guide for staff, teachers, and researchers to help them use the cloud to meet evolving scholastic and teaching requirements. For more information, see [University of Auckland Improves Agility, Innovation, and Resilience on AWS](https://aws.amazon.com/solutions/case-studies/university-of-auckland-case-study/).

The following mechanisms can help you align your organization's culture and people in order to make sure they are prepared for change and can realize maximize the benefits of cloud adoption:
+ **Readiness assessment **– Before starting the workload migration or modernization, complete an assessment to confirm the organization's readiness for that particular program. This assessment should do the following to evaluate whether the culture and people are ready:
  + Identify any organizational blockers
  + Validate that there is leadership support to drive change
  + Identify any skills or knowledge gaps and ensure training programs are organized to close those gaps
  + Confirm that a ramp-up plan for the migration or modernization initiative is clearly articulated
+ **Organization enablement initiative** – Create a structured initiative that details how to accelerate the cloud adoption from the people perspective. This initiative helps the organization achieve business outcomes by identifying and addressing the affects that the technology transformation would have on culture, leadership, workforce, roles, skills, and mindsets. The initiative should contain three phases:

  1. Leadership mobilization and organizational readiness

  1. Organizational enablement

  1. Organizational sustainability and adoption

These mechanisms provide insights into the actions required to prepare your organization and people for a successful cloud transformation.

## Governance perspective
<a name="governance-perspective"></a>

The *governance perspective* focuses on orchestrating the cloud initiatives, maximizing organizational benefits, and minimizing transformation-related risks. It helps you align processes to maximize ROI from the cloud adoption. For more information about this AWS CAF perspective, see [Governance perspective: control and oversight](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html) in *An Overview of the AWS Cloud Adoption Framework* and see [AWS Cloud Adoption Framework: Governance Perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/aws-caf-governance-perspective.html).

For example, an industry-leading automated wealth manager optimized its AWS environment to scale along with the company's growth. It used AWS Graviton2 processors for a cost-efficient way of improve elasticity. The adoption of AWS Graviton2–based instances reduced costs by 20 percent and runtime by 5 percent. For more information, see the [Wealthfront customer story](https://aws.amazon.com/solutions/case-studies/wealthfront-case-study/).

The following mechanisms can help you implement the control and oversight necessary to accelerate your cloud adoption journey and maximize the benefits of the cloud:
+ **Governance-at-scale assessment** – As organizations scale up their operations in the cloud, maintaining control over cloud resource usage, costs and policies can become a challenge. Your organization must assess whether its cloud environment adheres to the recommended best practices for account management, configuration management, financial management, and data management. This assessment should examine the current state and help you determine the gaps in the existing governance processes. The common stakeholders for this assessment include chief information officer (CIO), chief digital officer (CDO), chief financial officer (CFO), and chief revenue officer (CRO). The deliverables of this program should be a roadmap proposal and the next steps to build governance at scale.
+ **Governance-at-scale launch** – This phase should operationalize the recommended practices to address the gaps that were identified during the assessment. For example, for effective cost management, operate workloads by using demand-based and time-based dynamic provisioning so that you pay only for the resources that are needed.

This perspective validates that your organization is adhering to governance best practices and that it has established mechanisms for operating at scale in the cloud.

## Platform perspective
<a name="platform-perspective"></a>

The *platform perspective* focuses on migrating workloads to the cloud or modernizing legacy infrastructure and applications. One goal of this perspective is to minimize technical debt through proper planning. For more information about this AWS CAF perspective, see [Platform perspective: infrastructure and applications](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/platform-perspective.html) in *An Overview of the AWS Cloud Adoption Framework*.

For example, an Australian company, Sensis, transformed itself from a provider of legacy directories to a fully digital business by exiting its five data centers and migrating all 6,000 digital assets to the AWS Cloud. Large-scale refactoring helped Sensis ensure that its proposed cloud architecture took advantage of cloud-native capabilities as much as possible. For more information, see [Sensis Gains Cloud Agility While Reducing Infrastructure Costs with AWS](https://aws.amazon.com/solutions/case-studies/sensis/).

The following mechanisms can help you accelerate the delivery of cloud workloads and provide a roadmap for migration and modernization:
+ **R-lane analysis** – Review your organization's migration goals and its current state of readiness for the defined workload scope. Conduct an R-lane analysis to determine which migration strategies your organization will use. For more information about the migration strategies known as the *7 Rs*, see [About the migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html). The R-lane analysis helps your organization understand the workload dependencies and the actions required to effectively migrate to the cloud across multiple technical and business domains. The output is a recommendation for migration readiness and a migration plan.
+ **Application modernization assessment** – Application modernization assessment is one of the critical steps in the cloud adoption journey. It involves conducting a thorough evaluation of the current state of legacy applications and assessing their readiness for modernization. Don't base the assessment exclusively on industry standards or modern technology trends—customize your modernization assessment strategy to include business goals and company priorities. The result of the assessment should be a roadmap that helps you identify and bridge any gaps and accelerates your modernization journey. It should include recommendations for replatforming or refactoring for cloud-native architectures.
+ **SaaS transformation readiness assessment** – This assessment helps you determine the business and technical priorities for implementing a software as a service (SaaS) in your cloud environment. Structure this assessment as an interactive workshop with business leaders and engineering leaders. Discuss and make decisions regarding aspects such as building a multi-tenant architecture or defining aggregated charge-back units based on cloud resource use. Conclude the assessment by creating a document that summarizes the business and technical current state and that includes a proposed SaaS implementation architecture and roadmap.

## Security perspective
<a name="security-perspective"></a>

The *security perspective* helps you achieve confidentiality and integrity of your data and cloud workloads. It focuses on security governance by developing and maintaining security roles and policies and on security assurance by monitoring and improving the effectiveness of security controls. *Security controls* are the technical or administrative guardrails that help prevent, detect, or reduce the ability of a threat actor to exploit a security vulnerability in your AWS environment. For more information about this AWS CAF perspective, see [Security perspective: compliance and assurance](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html) in *An Overview of the AWS Cloud Adoption Framework*.

By using AWS services and tools, you can create a security design and testing strategy and implement it into your AWS Cloud environment. For example, to help protect sensitive health information and comply with Health Insurance Portability and Accountability Act (HIPAA) regulations, Amazon Care adopted Amazon GuardDuty, a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment. For more information, see [Amazon Care Improves Telehealth Services and Patient Engagement Using AWS](https://aws.amazon.com/solutions/case-studies/amazon-care-case-study/).

The following mechanisms can help you build a strong security posture in the cloud:
+ **Security blueprint assessment** – Assess the security controls in your cloud environment. Determine which data, infrastructure, and workloads are well protected by these controls and identify any areas of improvement. The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) of the AWS Well-Architected Framework focuses on how to use cloud technologies to protect data, systems, and assets in a way that can improve your security posture. It also provides best practices for architecting secure workloads on AWS. Organize the assessment around identity and access management, infrastructure security, data protection, logging and monitoring, and incident response*.* AWS offers cloud services, such as AWS Trusted Advisor, that can inspect your AWS environment and make recommendations to close security gaps. The output of the assessment is a report that includes specific recommendations, based on findings from interviews and services.
+ **Security blueprint implementation** – Create an iterative security plan that helps the organization build a core security foundation in the cloud and then rapidly transition to establishing maturity in the cloud. Build the core foundation around the [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/foundations.html). This establishes a foundation that is backed by continuous improvement of operations. Once the foundation is established, use the [AWS CAF security epics](https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/prioritizing-control-implementations.html) to implement security controls in your AWS environment. The *security epics* are groups of user stories (use cases and abuse cases). Each epic has multiple layers that help you address increasingly complex requirements and build a robust security posture. These epics represents the foundation of any AWS Cloud security program and provide a framework to mature the organization's security capabilities. In the plan, identify and prioritize the epics and abuse cases that are most applicable for your organization.

## Operations perspective
<a name="operations-perspective"></a>

The *operations perspective* focuses on ensuring that cloud services are delivered at a level that is agreed upon by key stakeholders. Automating and optimizing operations helps you effectively scale and can improve the reliability of your workloads. For more information about this AWS CAF perspective, see [Operations perspective: health and availability](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/operations-perspective.html) in *An Overview of the AWS Cloud Adoption Framework* and see [AWS Cloud Adoption Framework: Operations Perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/aws-caf-operations-perspective.html).

For example, GE Appliances has total visibility into its hybrid-cloud environment by using AWS Systems Manager and other AWS management services. This visibility has helped the company to eliminate many labor-intensive tasks and reduce average response times for security events from more than 24 hours to less than 2 hours. For more information, see the [GE Appliances case study](https://aws.amazon.com/solutions/case-studies/ge-appliances/).

The following mechanism helps you manage and operate your cloud environment in order to maximize the cloud ROI and align with your organization's strategic objectives:
+ **Cloud operating model** – Create a [cloud operating model](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model.html) that helps your team understand their part in achieving target business outcomes. An operating model helps your teams mature their capabilities in order to accelerate those business outcomes. By using the model, you can assess your cloud capability maturity against best practices. Then, you apply findings to change, improve, or redefine the model. The following should be included in the operating model:
  + Define, organize, and mature capabilities for building, managing, and running cloud environments
  + Define processes and tools for operating workloads by using cloud-first principles
  + Ensure that critical workloads are well-architected and have backup and disaster recovery (DR) plans

There are also AWS services, such as AWS Managed Services (AMS), that can help you adopt an automation-first approach. Automations help cloud operations teams focus on innovation instead of day-to-day operational activities. For more information, see [Strategy for using AWS Managed Services to achieve target business outcomes](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-managed-services-outcomes/introduction.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
