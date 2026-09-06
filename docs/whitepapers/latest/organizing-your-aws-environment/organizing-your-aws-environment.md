---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html
---

# Organizing Your AWS Environment Using Multiple Accounts
<a name="organizing-your-aws-environment"></a>

Publication date: **April 30, 2025** ([Document history](document-history.md))

 Businesses that are starting to adopt Amazon Web Services (AWS), expanding their footprint on AWS, or planning to enhance an established AWS environment need to ensure they have a [foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html) for their cloud environment. One important aspect of their foundation is organizing their AWS environment following a multi-account strategy.

 Using multiple AWS accounts to help isolate and manage your business applications and data can help you optimize across most of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) pillars, including operational excellence, security, reliability, and cost optimization. This paper provides best practices and current recommendations for organizing your overall AWS environment. The extent to which you use these best practices depends on your stage of the cloud adoption journey and specific business needs.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Using multiple AWS accounts to help isolate and manage your business applications and data can help you optimize across most of the AWS Well-Architected Framework pillars including operational excellence, security, reliability, and cost optimization.

### Multi-account strategy best practices and recommendations
<a name="multi-account-strategy-best-practices-and-recommendations"></a>

 Businesses can benefit from considering the latest guidance for organizing their AWS environments. A multi-account strategy is key to succeed when customers are starting to adopt AWS, expanding their footprint on AWS, or planning to enhance an established AWS environment.

 Customers might have multiple teams with different security and compliance controls that need to be isolated from one another. Some might have different business processes entirely or be part of different business lines that need clarity around costs incurred.

 Customers need explicit security boundaries, a mechanism to have direct control and visibility of their limits and any throttling, and a billing separation to directly map costs to underlying projects. The isolation designed into an AWS account can help you meet these needs.

 Using multiple AWS accounts to help isolate and manage your business applications and data can help you optimize across most of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) pillars including operational excellence, security, reliability, and cost optimization.

When organizing your AWS accounts, maintain a clean security organizational unit (OU) that adheres to AWS Control Tower requirements. The security OU should contain only the essential security accounts designated by AWS Control Tower. For additional security-related accounts, create a separate OU outside the core security OU.

### AWS accounts
<a name="aws-accounts"></a>

Your cloud resources and data are contained in an AWS account, which acts as an isolation boundary for identity and access management. When you need to share resources between accounts, you must explicitly allow this access. By default, no access is allowed between accounts. For instance, if you use separate accounts for production and non-production environments, they remain isolated unless you specifically enable communication.

The optimal number of AWS accounts for an organization can range from a few to thousands. Managing multiple accounts often requires automation to minimize operational complexity and ensure alignment with security, governance, and operational requirements. AWS charges are based on resource usage, not the number of accounts.

We recommend using several accounts to separate your workloads, rather than relying on a single account. A workload is a set of components that collectively deliver business value, and it's typically the level of detail discussed by business and technology leaders. This approach simplifies meeting your requirements, even in early adoption stages. As you experience success with initial workloads, you may want to expand your use of AWS, often leading to the foundation stage of adoption. At this point, you invest in developing your cloud foundational capabilities before significantly increasing adoption.

This multi-account strategy makes it easier to manage projects, enhance security controls, and support both early-stage and foundation-stage AWS adoption. It provides the flexibility for future expansion while maintaining strong foundational capabilities, allowing your organization to scale its AWS usage effectively as needs grow.

 A workload identifies a set of components that deliver business value together. A workload is usually the level of detail that business and technology leaders communicate about. Some examples of workloads are:
+  Marketing websites
+  Ecommerce websites
+  Mobile app backends
+  Analytic platforms

 Workloads vary in levels of architectural complexity, from static websites to complex microservices, each with potentially different requirements on cost or billing identification.

### Stages of adoption
<a name="stages-of-adoption"></a>

 When initially adopting AWS, it's recommended to use a multi-account strategy rather than relying on a single account. This approach is designed to provide flexibility and scalability, even in the early stages of your cloud journey. By separating resources into distinct accounts from the start, you can more easily manage security policies, access controls, and cost optimization as your initial workloads are migrated to the cloud. This lays the groundwork for a secure and well-governed AWS environment.

 As your initial cloud projects demonstrate success, the motivation often arises to expand AWS adoption further across the organization. This leads to the foundation stage of the cloud adoption lifecycle. During this phase, you invest in evolving your core cloud capabilities, such as establishing center of excellence teams, automating provisioning, and implementing cost management best practices. Building this strong cloud foundation positions you for widespread enterprise-wide adoption down the line, allowing you to capitalize on the full breadth of benefits that the AWS platform can provide.

### Best practices
<a name="best-practices"></a>

 The best practices described in this paper are designed to help you more easily achieve your security, governance, and operational requirements through multiple accounts. The best practices were assembled based on the experiences of thousands of customers who have progressed through their cloud adoption journeys.

 The best practices can help you quickly establish the initial cloud foundation of your AWS environment, and adjust and expand your AWS environment as you gain experience both with the AWS services and how you work with the AWS Cloud.

 While organizations often have similar cloud adoption needs, each has unique requirements. Therefore, these AWS multi-account best practices are intended as guidance, not a one-size-fits-all solution. Your specific AWS environment design may differ from the examples provided, but following these practices will help you make informed decisions as you plan your cloud strategy.

### Relation to AWS Well-Architected
<a name="relation-to-aws-well-architected"></a>

 [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for their applications and workloads. Based on six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability—AWS Well-Architected provides a consistent approach for customers and partners to evaluate architectures and implement designs that can scale over time.

 The best practices for organizing your AWS environment addressed in this guide augment and support the best practices represented in the Well-Architected pillars.

### Intended audience
<a name="intended-audience"></a>

 These best practices are intended for cloud architects and technical leads who are responsible for the overall security and architecture of an AWS environment. Whether you are new to AWS or you have already been using AWS for years, your team will benefit from reviewing these best practices and comparing them to your requirements and current AWS environment.

 These best practices are intended to apply to organizations largely independent of their industry, size, expected scale of adopting AWS, and workload portfolio. Depending on your needs, not all of the best practices might apply to your situation.

 If you're just starting to experiment and learn about AWS by using a single AWS account, you don't need to consider these best practices until you begin planning for your first few production workloads.
