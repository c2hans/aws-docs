---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/identity-perimeter.html
---

# Identity perimeter
<a name="identity-perimeter"></a>

The objective for identity perimeter is to ensure that only trusted identities can access your resources.

Identity perimeter for Amazon Bedrock requires more nuanced controls than traditional applications because AI workloads involve multiple types of principals with varying access patterns. You must secure human users invoking models through applications, service principals performing automated AI operations, and cross-account scenarios where external entities need limited access to specific models.

This diagram is a high level illustration of an identity perimeter.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/images/guide-img/4f7d8782-326c-45ca-95dd-0c4e97e42271/images/76be02e2-f6bb-461f-95b6-ad3249ff7e89.png)

Figure 3.1 High level illustration of identity perimeter

1. Resource policies allow only trusted identities from your AWS organization to accessAmazon Bedrock resources

2. Resource policies deny access from external AWS accounts and untrusted principals

3. VPC endpoint policies allow access only to organizational identities

This section covers the essential components of implementing identity perimeter controls for Amazon Bedrock:
+ Organizational boundary - Implementing organization-wide restrictions using `aws:PrincipalOrgID`
+ Training data protection - Securing Amazon S3 buckets and datasets used for model training
+ Knowledge base data isolation - Protecting data sources and vector stores with resource policies
+ Sensitive log data protection - Securing Amazon CloudWatch logs containing AI interactions
+ AWS KMS key policies - Implementing encryption-based access controls for AI resources
+ AWS Lambda resource policies - Controlling service access to Lambda functions in AI workflows
+ VPC endpoint policies - Managing identity access through private network endpoints
+ Cross-account sharing - Securing multi-account scenarios while maintaining proper identity boundaries
+ Monitoring violations - Detecting and responding to identity perimeter breaches
+ Best practices - Identity perimeter implementation recommendations and guidelines

Each subsection provides practical implementation guidance, code examples, and best practices specific to Amazon Bedrock's unique security requirements.

**Note**
These identity perimeter examples provide foundational patterns but may not cover all organizational structures or authentication scenarios. Adapt the policies to your specific identity providers, compliance requirements, and multi-account architecture. Always test identity controls in non-production environments and consult IAM documentation for the latest policy syntax and condition keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
