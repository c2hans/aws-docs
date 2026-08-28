---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-create.html
---

# Create new user roles
<a name="config-wrkr-lv-cg-users-create"></a>

The policies determine what actions a user can perform on the AWS Elemental Live node. Elemental Live comes with administrator, manager, operator, and viewer default policies. You can't edit these default policies, but you can create new ones if the defaults don't meet your requirements.

**To create new user roles**

1. Log in to the Elemental Live web interface using administrator credentials.

1. Hover over **Settings** and choose **Roles**.

1. On the **Roles** screen, assign a name to the new user role, select the actions to include, and choose **Create**. The new role appears in the list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
