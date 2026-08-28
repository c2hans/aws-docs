---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-roles-service.html
---

# Service roles for WorkSpaces Secure Browser
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

**Warning**
Changing the permissions for a service role might break WorkSpaces Secure Browser's functionality. Edit service roles only when WorkSpaces Secure Browser provides guidance to do so.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
