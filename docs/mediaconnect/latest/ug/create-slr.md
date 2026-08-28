---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/create-slr.html
---

# Creating a service-linked role for MediaConnect
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you create an associated MediaConnect resource in the AWS Management Console, the AWS CLI, or the AWS API, MediaConnect creates the service-linked role for you.

**Important**
This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. Also, if you were using the MediaConnect service before January 1, 2023, when it began supporting service-linked roles, then MediaConnect created the AWSServiceRoleForMediaConnect role in your account. To learn more, see [A new role appeared in my IAM account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create an associated MediaConnect resource, MediaConnect creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the **MediaConnect** use case. In the AWS CLI or the AWS API, create a service-linked role with the `MediaConnect` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
