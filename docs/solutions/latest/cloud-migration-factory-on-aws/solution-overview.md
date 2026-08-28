---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/solution-overview.html
---

# Coordinate and automate large scale migrations to the AWS Cloud using the Cloud Migration Factory on AWS solution
<a name="solution-overview"></a>

The Cloud Migration Factory on AWS solution is designed to coordinate and automate manual processes for large-scale migrations involving a substantial number of applications. This solution helps enterprises improve performance and prevents long cutover windows by providing an orchestration platform for migrating workloads to AWS at scale. [AWS Professional Services](https://aws.amazon.com/professional-services/), [AWS Partners](https://aws.amazon.com/partners/), and other enterprises have already used this solution to help customers migrate thousands of servers to the AWS Cloud.

This solution helps you to:
+ Integrate the many different types of tools that support migration, such as discovery tools, migration tools, and configuration management database (CMDB) tools.
+ Automate migrations that involve many small, manual tasks, which take time to run and are slow and hard to scale.

For a complete end-to-end deployment guide using this solution, refer to [Automating large-scale server migrations with Cloud Migration Factory](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/welcome.html) in the *AWS Prescriptive Guidance Cloud Migration Factory Guide*.

This implementation guide discusses architectural considerations and configuration steps for deploying the Cloud Migration Factory on AWS solution in the Amazon Web Services (AWS) Cloud. It includes links to [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates that launch and configure the AWS services required to deploy this solution using AWS best practices for security and availability.

The guide is intended for IT infrastructure architects, administrators, and DevOps professionals who have practical experience architecting in the AWS Cloud.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution in the `us-east-1` Region is USD $14.31 per month for AWS resources. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](supported-aws-regions.md)  |
| View or download the AWS CloudFormation templates included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation templates](aws-cloudformation-templates.md)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
