---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-end-user.html
---

# User Pool End User Experience for Amazon WorkSpaces Applications
<a name="user-pool-end-user"></a>

The following steps summarize the initial connection experience for users in the user pool.

1. You create new users in the Region you want by specifying their email addresses.

1. WorkSpaces Applications sends them a welcome email.

1. You assign one or more stacks to the users.

1. WorkSpaces Applications sends them an optional notification email. This email includes information about how to access the stacks that are newly assigned to them.

1. The users connect to the login portal by entering the information included in the welcome email, and they set a permanent password. The login portal link never expires and can be used any time.

1. They sign in to WorkSpaces Applications by entering their email address and permanent password.

1. After they sign in, the users can view their application catalogs.

The login portal link provided in the welcome email should be saved for future use, as it does not change and is valid for all users in the user pool. The login portal URL and users in the user pool are managed on a per-Region basis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
