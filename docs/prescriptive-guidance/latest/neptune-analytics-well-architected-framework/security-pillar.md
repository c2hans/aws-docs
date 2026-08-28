---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-analytics-well-architected-framework/security-pillar.html
---

# Security pillar
<a name="security-pillar"></a>

Cloud security is the highest priority at AWS. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations. Security is a shared responsibility between you and AWS. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of AWS security as part of [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Neptune, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors, including the sensitivity of your data, your company's requirements, and applicable laws and regulations. For more information about data privacy, see the [Data Privacy FAQs](https://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post.

The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) of the AWS Well-Architected Framework helps you understand how to apply the shared responsibility model when you use Neptune Analytics. The following topics explain how to configure Neptune Analytics to meet your security and compliance objectives. You also learn how to use other AWS services that help you monitor and secure your Neptune Analytics resources. The security pillar includes the following key focus areas:
+ Data security
+ Network security
+ Authentication and authorization

## Implement data security
<a name="data-security"></a>

Data leakage and breaches put your customers at risk and can cause substantial negative impact on your company. The following best practices help protect your customer data from inadvertent and malicious exposure:
+ Graph names, tags, IAM roles, and other metadata should not contain confidential or sensitive information, because that data might appear in billing or diagnostic logs.
+ URIs or links to external servers stored as data in Neptune should not contain credential information to validate requests.
+ A Neptune Analytics graph is encrypted at rest. You can use the default key or an AWS Key Management Service (AWS KMS) key of your choosing to encrypt the graph. You can also encrypt snapshots and data that's exported to Amazon S3 during bulk import. You can remove the encryption when the import is complete.
+ When you use the openCypher language, practice proper input validation and [parameterization](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/best-practices-content.html#best-practices-content-2) techniques to prevent SQL injection and other forms of attacks. Avoid constructing queries that use string concatenation with user-supplied input. Use parameterized queries or prepared statements to safely pass input parameters to the graph database. For more information, see [Examples of openCypher parameterized queries](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-parameterized-queries.html) in the Neptune documentation.

## Secure your networks
<a name="network-security"></a>

You can enable a Neptune Analytics graph for public connectivity so it can be reached from outside a virtual private cloud (VPC). This connectivity is disabled by default. The graph requires IAM authentication. The caller must obtain an identity and have permissions to use the graph. For example, to [run an openCypher query,](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExecuteQuery.html) the caller would need to have read, write, or delete permissions on the specific graph.

You can also [create private endpoints](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreatePrivateGraphEndpoint.html) for the graph to access the graph from within a VPC. When you create the endpoint, you specify the VPC, subnets, and security groups to restrict access to call the graph.

To protect your data in transit, Neptune Analytics enforces SSL connections through HTTPS to the graph. For more information, see [Data protection in Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/data-protection.html) in the Neptune Analytics documentation.

## Implement authentication and authorization
<a name="authentication"></a>

Calls to a Neptune Analytics graph require IAM authentication. The caller must obtain an identity and possess sufficient permissions to perform the action on the graph. For descriptions of API actions and their required permissions, see the [Neptune Analytics API documentation](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_Operations.html). You can [enforce condition checks](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptuneanalytics.html#amazonneptuneanalytics-policy-keys) to restrict access by tag.

IAM authentication uses the [AWS Signature Version 4 (SigV4) protocol](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html). To simplify usage from your application, we recommend that you use an [AWS SDK](https://aws.amazon.com/developer/tools/). For example, in Python, use the [Boto3 client for Neptune Graph](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html), which abstracts SigV4.

When you load data into the graph, [batch loading](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/batch-load.html) uses the IAM credentials of the caller. The caller must have permissions to download data from Amazon S3 with the trust relationship set up so that Neptune Analytics can assume the role to load the data into the graph from Amazon S3 files.

[Bulk import](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import.html) can be performed either during graph creation (by the infrastructure team) or on an existing, empty graph (by the data engineering team that has permissions to start import tasks). In both cases, Neptune Analytics assumes the IAM role that the caller provides as input. This role gives it permission to read and list the contents of the Amazon S3 folder where input data is staged.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
