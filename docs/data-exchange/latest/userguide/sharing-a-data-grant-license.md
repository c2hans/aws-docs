---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/sharing-a-data-grant-license.html
---

# Sharing an AWS Data Exchange data grant license in an organization
<a name="sharing-a-data-grant-license"></a>

When you accept a data grant, you receive a license that allows you to share the underlying data set under the following conditions:
+ The data grant sender allows you to share the underlying data set.
+ Your AWS account belongs to an organization. For more information about AWS Organizations, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

**Note**
You can only share access with accounts in your organization.

The following topics explain how to share licenses across accounts.

**Topics**
+ [Prerequisites for license sharing](#data-grant-prerequisites-license-sharing)
+ [Viewing your licenses](data-grant-viewing-licenses.md)
+ [Sharing your licenses](data-grant-sharing-license.md)

## Prerequisites for license sharing
<a name="data-grant-prerequisites-license-sharing"></a>

Before you can share licenses, you must complete the following setup tasks:
+ In the AWS Data Exchange console, use the **Data Grant settings** page to enable integration with AWS Organizations.
+ Give AWS Data Exchange permission to read information about accounts in your organization and manage licenses on your behalf so that it can create the associated license grants when you share your licenses. For more information, see [Using service-linked roles for AWS Data Exchange](using-service-linked-roles-adx.md), in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
