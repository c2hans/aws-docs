---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/aws-caf-operations-perspective.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Cloud Adoption Framework: Operations Perspective
<a name="aws-caf-operations-perspective"></a>

Publication date: **November 9, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 As the proliferation of digital technologies continues to disrupt market segments and industries, adopting Amazon Web Services (AWS) can help you transform your organization to meet changing business conditions and evolving customer needs. As the world’s most comprehensive and broadly-adopted cloud platform, AWS can help you reduce business risk; improve environmental, social, and governance (ESG) performance; increase revenue; and improve operational efficiency.

 The [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/) (AWS CAF) uses AWS experience and best practices to help you digitally transform and accelerate your business outcomes through innovative use of AWS. Use AWS CAF to identify and prioritize transformation opportunities, evaluate and improve your cloud readiness, and iteratively evolve your transformation roadmap.

 AWS CAF groups its guidance in six perspectives: *Business*, *People*, *Governance*, *Platform*, *Security*, and *Operations*. Each perspective is covered in a separate whitepaper. This whitepaper covers the Operations perspective, which focuses on ensuring that cloud services are delivered at a level that is agreed upon with your business stakeholders.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [*AWS Well-Architected Framework*](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [*AWS Well-Architected Tool*](https://aws.amazon.com/well-architected-tool/), available at no charge in the [*AWS Management Console*](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [*AWS Architecture Center*](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Millions of [AWS customers](https://aws.amazon.com/solutions/case-studies/) (including the fastest-growing startups, largest enterprises, and leading government organizations) are using AWS to [migrate and modernize](https://aws.amazon.com/migration-acceleration-program/) legacy workloads, become [data-driven](https://aws.amazon.com/executive-insights/insights/), [automate and optimize](https://aws.amazon.com/machine-learning/ml-use-cases/) business processes, and reinvent operating and [business models](https://aws.amazon.com/blogs/enterprise-strategy/reimagining-your-business-model-how-to-leverage-platforms-and-marketplaces/). Through cloud-powered digital transformation, they are able to improve their [business outcomes](https://aws.amazon.com/economics/), including reduced business risk, improved ESG performance, increased revenue, and improved operational efficiency.

 Organizational ability to effectively use the cloud to [digitally transform](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/accelerating-business-outcomes.html) (organizational cloud readiness) is underpinned by a set of [foundational capabilities](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html). A *capability* is an organizational ability to use processes to deploy resources (people, technology, and any other tangible or intangible assets) to achieve a particular outcome. The AWS CAF identifies these capabilities, and provides prescriptive guidance that thousands of organizations around the world have successfully used to improve their cloud readiness and accelerate their cloud transformation journeys.

 AWS CAF groups its capabilities in six perspectives:
+  [Business](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/business-perspective.html)
+  [People](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/people-perspective.html)
+  [Governance](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html)
+  [Platform](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/platform-perspective.html)
+  [Security](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html)
+  [Operations](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/operations-perspective.html)

 Each perspective comprises a set of capabilities that functionally-related stakeholders own or manage in their [cloud transformation journey](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html).

 The *Operations* perspective focuses on ensuring that cloud services are delivered at a level that is agreed upon with your business stakeholders. It comprises nine capabilities, as shown in the following figure (*AWS CAF Operations perspective capabilities*). Common stakeholders include infrastructure and operations leaders, site reliability engineers, and information technology service managers.

 This whitepaper provides an overview of the benefits of operating in the AWS cloud, and introduces you to the Cloud Operations services and prescriptive guidance that will help you operate efficiently and effectively at scale.

 Operations is critical to the success of every organization and its digital transformation. [Operational excellence](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.operationalExcellence.en.html) is required to ensure that your transformation achieves its purpose and that applications consistently meet their business outcomes and the expectations of their users.

 [ITIL](https://www.axelos.com/certifications/itil-service-management) and AWS CAF are compatible. Like ITIL, AWS CAF organizes and describes all of the activities and processes involved in planning, creating, managing, and supporting modern IT services. It offers practical guidance and comprehensive guidelines for establishing, developing, and running cloud-based IT capabilities.

 AWS and the [AWS Partner Network](https://aws.amazon.com/partners/find-a-partner/) (APN) provide tools and services that can help you along each step of the way. [AWS Professional Services](https://aws.amazon.com/professional-services/) is a global team of experts that provides assistance through a collection of AWS CAF aligned offerings that can help you achieve specific outcomes related to your cloud transformation.

 [AWS Managed Services](https://aws.amazon.com/managed-services/) (AMS) helps you operate your AWS infrastructure more efficiently and securely. AMS can serve as an enabler for organizations that are building up operational rigor and lack the cloud operations staff or in-house AWS skills to achieve operational excellence at scale. Using AWS services and a growing library of automations, configurations, and runbooks, AMS can augment and optimize your operational capabilities in both new and existing AWS environments.

 [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) customers can benefit from a number of [operational workshops and deep dives](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/) delivered by AWS Support experts. These services help you review the health of your cloud operations, optimize costs, and scale workloads efficiently.

![A diagram that depicts the AWS CAF Operations perspective capabilities](http://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/images/caf-operations.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
