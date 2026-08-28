---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-permissions.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# IAM roles needed for the MGN connector
<a name="mgn-connector-permissions"></a>

To use MGN connector you must have these required IAM roles for individual accounts and AWS Organizations networks:
+ **MGNConnectorInstallerRole**
+ **AWSApplicationMigrationConnectorManagementRole**
+ **AWSApplicationMigrationConnectorSharingRole\_{{management-account-id}}** Needed in an individual account. Also needed in an organization, on *every* account, including the management account.

**Individual account: **For an MGN connector in an individual account, create these roles as described in [Create roles manually](create-permissions-manually.md).

**Multiple accounts: **If the MGN connector manages source servers from multiple accounts, set up the global view feature and set up your AWS Organization, as described in [Manage large-scale migrations with global view](global-view.md). After you set up your AWS Organization:

1. Create the MGNConnectorInstallerRole and the AWSApplicationMigrationConnectorManagementRole as described in [Create roles manually](create-permissions-manually.md).

1. Configure the CloudFormation StackSet to create the AWSApplicationMigrationConnectorSharingRole\_{{management-account-id}} role per management account. Use the template "Enable Application Migration Service Connector access". Instructions are in [Deploy role using a CloudFormation template ](CloudFormation_Template.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
