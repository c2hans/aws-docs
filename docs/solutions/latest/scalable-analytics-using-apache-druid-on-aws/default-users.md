---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/default-users.html
---

# Default users
<a name="default-users"></a>

The guidance uses Druid’s authentication and authorization module for user authentication, with basic authentication enabled by default.

During the initial deployment, it creates default users `admin` and `druid_system`, both with full permissions. The `admin` user is intended for your use, while the `druid_system` user is specifically reserved for internal system communication and operations.

Upon deployment, the guidance generates the following secrets in AWS Secrets Manager to securely store the credentials for the `admin` and `druid_system` users.

| Secret Description | Secret Example |
| --- | --- |
| Administrator user credentials for Druid cluster `<cluster name>`  |  <pre>{<br />  "password": "<password>",<br />  "username": "admin"<br />}</pre>  |
| Internal system user credentials for Druid cluster `<cluster name>`  |  <pre>{<br />  "password": "<password>",<br />  "username": "druid_system"<br />}</pre>  |

**Note**
Modifying the password in AWS Secrets Manager will not automatically change the user’s password. To update a user’s password, you must change the password using the Druid API and then update the password manually in AWS Secrets Manager.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
