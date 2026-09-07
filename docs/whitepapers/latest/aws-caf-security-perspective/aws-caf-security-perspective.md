---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/aws-caf-security-perspective.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Cloud Adoption Framework: Security Perspective
<a name="aws-caf-security-perspective"></a>

Publication date: **December 12, 2023** ([Document history](document-revisions.md))

 Strong security is a core enabler of digital transformation, helping organizations adopt machine learning (ML), artificial intelligence (AI), big data, and the speed and scale of the cloud to meet changing business conditions and evolving customer needs. Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform. It can help you transform your organization while reducing business risk, improving environmental, social, and governance (ESG) performance, growing revenue, and improving operational efficiency.

 The [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/) uses AWS best practices to help you accelerate your business outcomes. Use the AWS CAF to identify and prioritize transformation opportunities, evaluate and improve your cloud readiness, and iteratively evolve your transformation roadmap.

 AWS CAF groups its guidance in six perspectives: *Business*, *People*, *Governance*, *Platform*, *Security*, and *Operations*. Each perspective is covered in a separate whitepaper. This whitepaper covers the *Security* perspective, and will help you achieve the confidentiality, integrity, and availability of your data and cloud workloads.

## Introduction
<a name="introduction"></a>

 AWS CAF is an enterprise architecture framework that helps work backwards from your strategic priorities and associated business outcomes to prioritize transformation initiatives, identify capability gaps, and iteratively evolve your digital transformation roadmap. AWS CAF identifies specific organizational capabilities that underpin successful cloud transformations. These capabilities may be used to inform the construction of a cloud-ready operating model, develop cloud skills and teams, set up centers of excellence, and adapt organizational structures.

 The organizational ability to effectively use the cloud to [digitally transform](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/accelerating-business-outcomes.html) (organizational cloud readiness) is bolstered by a set of foundational [capabilities](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html). A *capability* is an organizational ability to use processes to deploy resources (people, technology, and any other tangible or intangible assets) to achieve a particular outcome. The AWS CAF identifies these capabilities and provides prescriptive guidance that thousands of organizations around the world have successfully used to improve their cloud readiness and accelerate their cloud transformation journeys.

 [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) is a complementary mechanism that can help you build secure, high-performing, resilient, and efficient workloads for a variety of applications. It provides a consistent approach for evaluating your architectures and implementing scalable designs. You should perform AWS Well-Architected reviews whenever you are ready to deploy new or optimize existing workloads on AWS.

 AWS CAF groups its capabilities in six perspectives:
+  [Business](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-business-perspective/aws-caf-business-perspective.html)
+  [People](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-people-perspective/aws-caf-people-perspective.html)
+  [Governance](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/aws-caf-governance-perspective.html)
+  [Platform](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/platform-perspective.html)
+  [Security](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html)
+  [Operations](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/aws-caf-operations-perspective.html)

 The *Security* perspective helps you achieve the confidentiality, integrity, and availability of your data and cloud workloads. It comprises nine capabilities shown in Figure 1. These are managed by stakeholders who are functionally related in their [cloud transformation journey](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html). Common stakeholders include the Board of Directors and chief executive officer (CEO). It can also include other individuals *directly* responsible for mitigating and managing risk, such as chief information security officer (CISO), chief compliance officer (CCO), internal audit leaders, and security architects and engineers.

![ADD ALTERNATE TEXT HERE for people using assistive technology.](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/images/security-perspective-capabilities.png)

 The goal of the Security perspective is to help you achieve the confidentiality, integrity, and availability of your data and workloads in the AWS Cloud, while improving your security posture. This whitepaper organizes the principles of the nine capabilities that will help you drive the transformation of your organization's security culture. For each capability, we'll discuss specific actions you can take and methods to measure progress.

 Security is a top priority for AWS. As organizations embrace the scalability and flexibility of the cloud, AWS helps them evolve their security, identity, and compliance leveraging this new environment. AWS builds security into the very core of the AWS Cloud infrastructure. It offers foundational services to help you meet your unique security requirements in the AWS Cloud.

 The goal of your security program remains the same, whether on-premises, in the cloud, or in a hybrid environment. AWS CAF helps you increase program maturity and efficacy, while shortening timelines and reducing costs. The difference in using the cloud is fundamental and impactful - you no longer manage physical security of your data centers, nor the related design, implementation, training, deployment, or maintenance of them. AWS provides and secures the data centers and manages all physical upgrades and maintenance. You can use software-based security tools to monitor and protect the flow of information into and out of your cloud resources. As an AWS customer, you reap the benefit of all the best practices of AWS policies, architecture, and operational processes that satisfy the requirements our most security-sensitive customers.

 [AWS Compliance](https://aws.amazon.com/compliance) outlines the robust controls in place at AWS for security and data protection in the AWS Cloud. AWS regularly achieves [third-party validation](https://aws.amazon.com/compliance/services-in-scope/) for thousands of global compliance requirements that we continually monitor to help you meet security and compliance needs. Security and Compliance is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) between you and AWS, with AWS being responsible for "Security of the Cloud" while you remain responsible for "Security in the Cloud".

 AWS also provides you with a wide range of information about its Information Technology (IT) control environment in whitepapers, reports, certifications, accreditations, and other third-party attestations. More information is available in the [Risk and Compliance whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html) and at the [AWS Security Center](https://aws.amazon.com/security/).

 AWS and the [AWS Partner Network](https://aws.amazon.com/partners/find-a-partner/) provide tools and services, such as workshops and trainings that can help you on this journey to implement and improve your security posture.

 AWS collaborates extensively with the security community to increase security of the AWS Cloud.

 [AWS Professional Services](https://aws.amazon.com/professional-services/) is a global team of experts that can help you achieve specific outcomes related to your cloud transformation through a collection of AWS CAF aligned offerings.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) explains the pros and cons of decisions you make when building systems in the cloud. The six pillars of the Framework describe architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. By answering a set of questions in the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), you can evaluate your workloads alongside the best practices for each pillar. This tool is available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected).

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).
