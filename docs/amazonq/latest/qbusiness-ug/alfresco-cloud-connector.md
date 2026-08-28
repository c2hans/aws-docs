---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/alfresco-cloud-connector.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Alfresco (Cloud) to Amazon Q Business
<a name="alfresco-cloud-connector"></a>

**Note**
Alfresco (Cloud) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-connector.html), designed to support a broader range of enterprise use cases with enhanced flexibility.

Alfresco is a content management service (CMS) that helps customers store and manage their content. You can connect Alfresco (Cloud) instance to Amazon Q Business—using either the AWS Management Console or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API—and create an Amazon Q web experience.

**Topics**
+ [Alfresco (Cloud) connector overview](alfresco-cloud-overview.md)
+ [Prerequisites for connecting Amazon Q Business to Alfresco (Cloud)](alfresco-cloud-prereqs.md)
+ [Connecting Amazon Q Business to Alfresco (Cloud) using the console](alfresco-cloud-console.md)
+ [Connecting Amazon Q Business to Alfresco (Cloud) using APIs](alfresco-cloud-api.md)
+ [How Amazon Q Business connector crawls Alfresco (Cloud) ACLs](alfresco-cloud-user-management.md)
+ [Alfresco (Cloud) data source connector field mappings](alfresco-cloud-field-mappings.md)
+ [IAM role for Alfresco (Cloud) connector](alfresco-cloud-iam-role.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
