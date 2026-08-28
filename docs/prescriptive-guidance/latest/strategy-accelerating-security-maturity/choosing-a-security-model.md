---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/choosing-a-security-model.html
---

# Choosing a security model
<a name="choosing-a-security-model"></a>

You can choose from various security models or approaches for AWS. The choice of approach and the best-fitting model depends on your audience, the target business outcomes, and the overall business process. It is possible to use a blend of multiple models.

The following are a few common models:
+ [Architectural model](#architectural-model)
+ [Maturity model](#maturity-model)
+ [Governance model](#governance-model)

Each model has its own set of benefits and drawbacks. It is important to consider which approach is best suited for your organization. Involve security professionals early in the process of modernizing your infrastructure and adopting cloud strategies. The model you choose has a significant impact on the roles and responsibilities within your organization.

## Architectural model
<a name="architectural-model"></a>

The following image shows the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html). This architectural approach provides a blueprint for a security model. This approach is best suited when you are engaging with technical teams within your organization. It helps set an  ideal future-state goal. It also aligns with many compliance and AWS frameworks.

![An architecture diagram of the AWS Security Reference Architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/b55c3e5e-9869-4cd2-8a61-6334562649bc.png)

**Advantages of the architectural model:**
+ Aligns with Health Insurance Portability and Accountability Act (HIPAA) and Health Information Trust Alliance Common Security Framework (HITRUST CSF) requirements
+ Provides an architectural perspective
+ Aligns to cloud strategies and guidance for large enterprises
+ Aligns with the [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/)
+ Aligns with the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

**Disadvantage of the architectural model:**
+ Is technology-focused rather than business-focused

## Maturity model
<a name="maturity-model"></a>

The [AWS Security Maturity Model](https://maturitymodel.security.aws.dev/en/model/) approach focuses on managing and reducing risk by prioritizing the implementation of security measures. This approach is well-suited for security directors and CISOs, but it's not business-focused.

**Advantages of the maturity model:**
+ Is security focused
+ Is a model that focuses on using an agile-based implementation approach
+ Helps you quickly reduce risk
+ Aligns with the [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/)

**Disadvantages of the maturity model:**
+ Is technology-focused rather than business-focused

## Governance model
<a name="governance-model"></a>

The [Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/capabilities.html) model uses a governance, risk management, and compliance (GRC) approach to help organizations meet security and compliance requirements. It defines the overall policies your cloud environment should follow. The capabilities within this model help you define action items, define your risk appetite, and align internal policies.

![The aspects of the Cloud Foundation on AWS governance model.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/c824fae4-ec4c-4df0-b0f3-52ab746e6c98.png)

The Cloud Foundation model is a capability and governance guide that helps you build and evolve your AWS Cloud environment. It is based on a set of definitions, scenarios, guidance, and automations. The guide includes the people, process, and technology aspects of establishing an AWS Cloud environment. It covers six categories of capabilities that are essential for a cloud foundation:
+ Governance, risk management, and compliance
+ Operations
+ Security
+ Business continuity
+ Finance
+ Infrastructure

The guide also provides examples, timelines, and further reading for each capability.

**Advantages of the governance model:**
+ Has a broad technology focus
+ Is designed for reliability
+ Uses an operational approach

**Disadvantage of the governance model:**
+ Is technology-focused rather than business-focused

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
