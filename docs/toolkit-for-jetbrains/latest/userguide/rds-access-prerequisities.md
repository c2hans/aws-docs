---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/rds-access-prerequisities.html
---

# Prerequisites for accessing Amazon RDS databases
<a name="rds-access-prerequisities"></a>

Before you can connect to an Amazon RDS database using AWS Toolkit for JetBrains, you need to complete the following tasks:
+ [Create a DB instance and set up its authentication method](#db-authentication)
+ [Download and install DataGrip](#datagrip-info)

## Creating an Amazon RDS DB instance and configuring an authentication method
<a name="db-authentication"></a>

 AWS Toolkit for JetBrains enables you to connect to an Amazon RDS DB instance that's already been created and configured in AWS. A DB instance is an isolated database environment running in the cloud that can contain multiple user-created databases. For information about creating DB instances for the supported database engines, see [ Getting started with Amazon RDS resources](Amazon RDS User GuideCHAP_GettingStarted.html) in the *Amazon RDS User Guide*.

When connecting to a database using AWS Toolkit for JetBrains, users can choose to authenticate using IAM credentials or Secrets Manager. The following table describes key features and information resources for both options:

| Authentication methods | How it works | More information |
| --- | --- | --- |
| Connect with IAM credentials | With IAM database authentication, you don't need to store user credentials in the database because authentication is managed externally using AWS Identity and Access Management (IAM) credentials.<br />By default, IAM database authentication is disabled on DB instances. You can enable IAM database authentication (or disable it again) using the AWS Management Console, AWS CLI, or the API.  |  + [Identity and access management in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html) in the *Amazon RDS User Guide*. <br />+ AWS Knowledge Center article: [How do I allow users to authenticate to an Amazon RDS MySQL DB instance using their IAM credentials?](https://aws.amazon.com/premiumsupport/knowledge-center/users-connect-rds-iam)  |
| Connect with AWS Secrets Manager | A database administrator can store credentials for a database as a secret in Secrets Manager. Secrets Manager encrypts and stores the credentials within the secret as the *protected secret text*.<br />When an application with permissions accesses the database, Secrets Manager decrypts the protected secret text and returns it over a secured channel. The client parses the returned credentials, connection string, and any other required information and then uses that information to access the database. |  + [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*. <br />+ [Tutorial: Rotating a secret for an AWS database](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_db-rotate.html) in the *AWS Secrets Manager User Guide*. <br />+ AWS Security Blog: [Rotate Amazon RDS database credentials automatically with Secrets Manager](https://aws.amazon.com/blogs/security/rotate-amazon-rds-database-credentials-automatically-with-aws-secrets-manager/).  |

## Working with Amazon RDS databases using DataGrip
<a name="datagrip-info"></a>

After you've connected to an Amazon RDS data source, you can start interacting with it. By using DataGrip from JetBrains, you can carry out database tasks such as writing SQL, running queries, and importing/exporting data. Features provided by DataGrip are also available in the database plugin for a range of JetBrains IDEs. For information about DataGrip, see [https://www.jetbrains.com/datagrip/](https://www.jetbrains.com/datagrip/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
