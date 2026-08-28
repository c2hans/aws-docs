---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/default-access.html
---

# Default access policy
<a name="default-access"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  |

In the Enterprise edition, you can configure specific permissions for the AWS services that an Amazon Quick user can access. If no such configuration occurs, Quick uses a default set of permissions based on the user's settings. The current behavior is displayed in a blue information box.

**To change the default resource access for all users (to use when no other permissions are configured)**

1. Sign in to Amazon Quick.

1. At upper right, choose the profile icon, and then choose **Manage Quick**.

1. Under **Permissions**, choose **Default access policy**.

1. Choose one of the following:
   + Allow access to all AWS data and resources to all users and groups.
   + Deny access to all AWS data and resources to all users and groups.

1. Choose **Update**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
