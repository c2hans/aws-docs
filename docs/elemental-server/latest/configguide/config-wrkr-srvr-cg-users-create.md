---
source_url: https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-users-create.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Create New User Roles
<a name="config-wrkr-srvr-cg-users-create"></a>

The policies determine what actions a user can perform on the node. AWS Elemental Server comes with administrator, manager, operator, and viewer default policies. You can't edit these default policies, but you can create new ones if the defaults don't meet your requirements.

**To create new user roles**

1. Log in to the AWS Elemental Server web interface using administrator credentials.

1. Hover over **Settings** and choose **Roles**.

1. On the **Roles** screen, assign a name to the new user role, select the actions to include, and choose **Create**. The new role appears in the list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
