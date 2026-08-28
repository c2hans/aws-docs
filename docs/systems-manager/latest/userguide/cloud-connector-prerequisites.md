---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/cloud-connector-prerequisites.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Prerequisites
<a name="cloud-connector-prerequisites"></a>

Before you create a Cloud Connector, complete the following prerequisites on both the AWS side and the Azure side. These steps establish OIDC-based federated authentication between AWS and Microsoft Azure.

**Important**
Make sure your AWS account is not in any service control policy (SCP) that restricts the `sts:GetWebIdentityToken` action.

**Topics**
+ [AWS prerequisites](cloud-connector-prereqs-aws.md)
+ [Azure prerequisites](cloud-connector-prereqs-azure.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
