---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html
---

# AWS Security Reference Architecture (AWS SRA) – core architecture
<a name="introduction"></a>

*Avik Mukherjee, Amazon Web Services*

The Amazon Web Services (AWS) Security Reference Architecture (AWS SRA) is a holistic set of guidelines for deploying the full complement of AWS security services in a multi-account environment. Use it to help design, implement, and manage AWS security services so that they align with AWS recommended practices. The recommendations are built around a single-page architecture that includes AWS security services*—*how they help achieve security objectives, where they can be best deployed and managed in your AWS accounts, and how they interact with other security services. This overall architectural guidance complements detailed, service-specific recommendations such as those found on the [AWS Security Documentation website](https://docs.aws.amazon.com/security/).

The architecture and accompanying recommendations are based on our collective experiences with AWS enterprise customers. This document is a reference—a comprehensive set of guidance for using AWS services to secure a particular environment—and the solution patterns in the [AWS SRA code repository](code-repo.md) were designed for the specific architecture illustrated in this reference. Each customer will have different requirements. As a result, the design of your AWS environment might differ from the examples provided here. **You will need to modify and tailor these recommendations to suit your individual environment and security needs. **Throughout the document, where appropriate, we suggest options for frequently seen alternative scenarios.

The AWS SRA is a living set of guidance and is updated periodically based on new service and feature releases, customer feedback, and the constantly changing threat landscape. Each update will include the revision date and the associated [change log](doc-history.md).

Although we rely on a one-page diagram as our foundation, the architecture goes deeper than a single block diagram and must be built on a well-structured foundation of fundamentals and security principles. You can use this document in two ways: as a narrative or as a reference. The topics are organized as a story, so you can read them from the beginning (foundational security guidance) to the end (discussion of code samples you can implement). Alternatively, you can navigate the document to focus on the security principles, services, account types, guidance, and examples that are most relevant to your needs.

This document is divided into the following sections and an appendix:
+ [About the AWS SRA library](about-sra-library.md) provides an overview of the technical guidance and code included in the AWS SRA collection of publications.
+ [The value of the AWS SRA](value.md) discusses the motivation for building the AWS SRA, describes how you can use it to help improve your security, and lists key takeaways.
+ [Security foundations](foundations.md) reviews the AWS Cloud Adoption Framework (AWS CAF), the AWS Well-Architected Framework, and the AWS Shared Responsibility Model, and highlights elements that are especially relevant to the AWS SRA.
+ [AWS Organizations, accounts, and IAM guardrails](organizations.md) introduces the AWS Organizations service, discusses the foundational security capabilities and guardrails, and gives an overview of our recommended multi-account strategy.
+ [The AWS Security Reference Architecture](architecture.md) is a single-page architecture diagram that shows functional AWS accounts, and the security services and features that are generally available.
+ [AI/ML for security](ai-ml.md) describes how different AWS services use artificial intelligence and machine learning (AI/ML) in the background to help you achieve specific security objectives. You can include these AWS services in your design to take advantage of advanced security features.
+ [Building your security architecture ‒ A phased approach](phases.md) provides guidance on how you can build your own security architecture in six iterative phases, based on the reference provided by the AWS SRA.
+ [AWS SRA best practices checklist](checklist.md) distills the recommendations discussed throughout the guide into a checklist that you can follow as you build your version of the security architecture.
+ [IAM resources](iam-resources.md) presents a summary and set of pointers for AWS Identity and Access Management (IAM) guidance that are important to your security architecture.
+ [Code repository for AWS SRA examples](code-repo.md) provides an overview of the associated [GitHub repository](https://github.com/aws-samples/aws-security-reference-architecture-examples) that will help developers and engineers deploy some of the guidance and architecture patterns presented in this document. You can deploy the samples by using AWS CloudFormation or Terraform by HashiCorp. They support both AWS Control Tower and non‒AWS Control Tower environments.

The [appendix](appendix.md) contains a list of the individual AWS security, identity, and compliance services, and provides links to more information about each service. The [Document history](doc-history.md) section provides a change log for tracking versions of this document.

## Attachments
<a name="attachments-91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
