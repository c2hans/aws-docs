---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/client-authentication.html
---

# Client authentication
<a name="client-authentication"></a>

AWS IoT supports three types of identity principals for device or client authentication:
+ [X.509 client certificates](x509-client-certs.md)
+ [IAM users, groups, and roles](iam-users-groups-roles.md)
+ [Amazon Cognito identities](cognito-identities.md)

These identities can be used with devices, mobile, web, or desktop applications. They can even be used by a user typing AWS IoT command line interface (CLI) commands. Typically, AWS IoT devices use X.509 certificates, while mobile applications use Amazon Cognito identities. Web and desktop applications use IAM or federated identities. AWS CLI commands use IAM. For more information about IAM identities, see [Identity and access management for AWS IoT](security-iam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
