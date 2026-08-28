---
source_url: https://docs.aws.amazon.com/mwaa/latest/userguide/manage-access.html
---

# Managing access to an Amazon MWAA environment
<a name="manage-access"></a>

Amazon Managed Workflows for Apache Airflow needs to be permitted to use other AWS services and resources used by an environment. You also need to be granted permission to access an Amazon MWAA environment and your Apache Airflow UI in AWS Identity and Access Management (IAM). This section describes the execution role used to grant access to the AWS resources for your environment and how to add permissions, and the AWS account permissions you need to access your Amazon MWAA environment and Apache Airflow UI.

**Topics**
+ [Accessing an Amazon MWAA environment](access-policies.md)
+ [Service-linked role for Amazon MWAA](mwaa-slr.md)
+ [Amazon MWAA execution role](mwaa-create-role.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)
+ [Apache Airflow access modes](configuring-networking.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
