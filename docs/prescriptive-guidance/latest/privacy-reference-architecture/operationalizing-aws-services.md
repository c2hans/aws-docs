---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/operationalizing-aws-services.html
---

# Operationalizing AWS privacy services
<a name="operationalizing-aws-services"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

For many, privacy is cross-cutting. Many different teams have a part to play, including regulatory, compliance, and engineering teams. When your organization has started to define the key people and policy components of your privacy program, you can map controls against a privacy compliance framework for consistent operations. A framework can serve as a rubric for implementing foundational and application-specific privacy controls for personal data in your AWS environment.

Regardless of the framework that customers use to categorize their privacy requirements, privacy compliance, privacy engineering, and application teams often need to work together to achieve implementation goals. For example, regulatory and compliance teams might provide the high-level requirements, and engineering and application teams configure AWS services and features to align to these requirements. Starting with a control framework can help you define more prescriptive organizational and technical controls.

When defining the technical controls of AWS services and features, another key decision is whether a control should apply to the entire organization, an OU, an account, or a specific resource. Some services and features are a great fit for implementing controls across your full AWS organization. For example, [blocking public access to Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) is a specific control that is preferably configured at the organization root rather than individually for each account. However, your retention policies might vary from application to application, which means that you might apply the control at the resource level.

To help you accelerate operationalizing privacy in your organization, AWS offers audit and compliance advisory services for your AWS workloads. For more information, [contact AWS SAS](https://pages.awscloud.com/GLOBAL-aware-LN-AWS-Security-Assurance-Services-2020-reg.html).
