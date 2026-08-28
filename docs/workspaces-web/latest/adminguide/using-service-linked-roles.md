---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/using-service-linked-roles.html
---

# Using service-linked roles for Amazon WorkSpaces Secure Browser
<a name="using-service-linked-roles"></a>

Amazon WorkSpaces Secure Browser uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to WorkSpaces Secure Browser. Service-linked roles are predefined by WorkSpaces Secure Browser and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up WorkSpaces Secure Browser easier because you don’t have to manually add the necessary permissions. WorkSpaces Secure Browser defines the permissions of its service-linked roles, and unless defined otherwise, only WorkSpaces Secure Browser can assume its roles. The defined permissions include the trust and permissions policies. The permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your WorkSpaces Secure Browser resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Topics**
+ [Service-linked role permissions for WorkSpaces Secure Browser](slr-permissions.md)
+ [Creating a service-linked role for WorkSpaces Secure Browser](create-slr.md)
+ [Editing a service-linked role for WorkSpaces Secure Browser](edit-slr.md)
+ [Deleting a service-linked role for WorkSpaces Secure Browser](delete-slr.md)
+ [Supported regions for WorkSpaces Secure Browser service-linked roles](slr-regions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
