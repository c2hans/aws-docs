---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/using-the-amazon-aws-security-incident-response-console.html
---

# Using the AWS Security Incident Response console
<a name="using-the-amazon-aws-security-incident-response-console"></a>

 To access https://console.aws.amazon.com/security-ir/, you must have a minimum set of permissions. These permissions must allow you to list and view details about the AWS Security Incident Response resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

 You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

 Attach the AWS Security Incident Response Access or ReadOnly AWS managed policy to ensure that users and roles can use the service console. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
