---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/sagemaker-studio-admin-best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SageMaker Studio Administration Best Practices
<a name="sagemaker-studio-admin-best-practices"></a>

Publication date: **April 25, 2023** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

[ Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) provides a single, web-based visual interface where you can perform all machine learning (ML) development steps, which improves data science team productivity. SageMaker AI Studio gives you complete access, control, and visibility into each step required to build, train, and evaluate models.

 In this whitepaper, we discuss best practices for subjects including operating model, domain management, identity management, permissions management, network management, logging, monitoring, and customization. The best practices discussed here are intended for enterprise SageMaker AI Studio deployment, including multi-tenant deployments. This document is intended for ML platform administrators, ML engineers, and ML architects.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html), we focus on how to design, deploy, and architect your machine learning workloads in the AWS Cloud. This lens adds to the best practices described in the Well-Architected Framework.

## Introduction
<a name="introduction"></a>

 When you administrate SageMaker AI Studio as your ML platform, you need best practices guidance for making informed decisions to help you scale your ML platform as your workloads grow. For provisioning, operationalizing, and scaling your ML platform, consider the following:
+  Choose the right operating model and organize your ML environments to meet your business objectives.
+  Choose how to set up SageMaker AI Studio domain authentication for user identities, and consider the domain-level limitations.
+  Decide how to federate your users’ identity and authorization to the ML platform for fine-grained access controls and auditing.
+  Consider setting up permissions and guardrails for various roles of your ML personas.
+  Plan your virtual private cloud (VPC) network topology, considering your ML workload’s sensitivity, number of users, instance types, apps, and jobs launched.
+  Classify and protect your data at rest and in transit with encryption.
+  Consider how to log and monitor various application programming interfaces (APIs) and user activities for compliance.
+  Customize the SageMaker AI Studio notebook experience with your own images and lifecycle configuration scripts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
