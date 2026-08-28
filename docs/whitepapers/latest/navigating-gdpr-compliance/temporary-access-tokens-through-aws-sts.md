---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/temporary-access-tokens-through-aws-sts.html
---

# Temporary Access Tokens Through AWS STS
<a name="temporary-access-tokens-through-aws-sts"></a>

Customers can use the [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) to create and provide trusted users with temporary security credentials that grant access to customers' AWS resources. Temporary security credentials work almost identically to the long-term access key credentials that customers provide for their IAM users, with the following differences:
+ Temporary security credentials are for short-term use. Customers can configure the amount of time that they are valid, from 15 minutes up to a maximum of 12 hours. After temporary credentials expire, AWS does not recognize them or allow any kind of access from API requests made with them.
+ Temporary security credentials are not stored with the user. Instead, they are generated dynamically and provided to the user when requested. When (or before) temporary security credentials expire, a user can request new credentials, if that user has permissions to do so.

These differences provide the following advantages when customers use temporary credentials:
+ Customers do not have to distribute or embed long-term AWS security credentials with an application.
+ Temporary credentials are the basis for roles and identity federation. Customers can provide access to their AWS resources to users by defining a temporary AWS identity for them.
+ Temporary security credentials have a limited customizable lifespan. Because of this, customers do not have to rotate them or explicitly revoke them when they're no longer needed. After temporary security credentials expire, they cannot be reused. Customers can specify the maximum amount of time the credentials are valid.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
