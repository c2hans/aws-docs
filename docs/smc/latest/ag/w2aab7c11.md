---
source_url: https://docs.aws.amazon.com/smc/latest/ag/w2aab7c11.html
---

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html).

# Security in AWS Service Management Connector
<a name="w2aab7c11"></a>

Service Management Connector uses the roles and permissions that an IAM user requires to access your specific AWS resources and services. Service Management Connector requires two IAM user roles, *SyncUser* and *EndUser*, to perform various integration operations. For more information, see your chosen Connector to identify the IAM permissions for a specific integration.

Service Management Connector is not within the scope of any AWS compliance programs. Using Service Management Connector to access a service does not alter that service’s compliance.

 **Encryption at rest** — Service Management Connector does not store any customer data. The connector installs Tables and Schemas on third-party platforms that can store credentials in the platform’s database. All credentials are encrypted and masked to comply with platform best practices.

 **Encryption in transit** — By default, AWS encrypts all data transmitted between external platforms and Service Management Connector by sending data through a HTTPS/TLS connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Management Connector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query smc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
