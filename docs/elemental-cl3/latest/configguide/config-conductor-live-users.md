---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-users.html
---

# Managing users in Conductor Live
<a name="config-conductor-live-users"></a>

If you have enabled user authentication, you must add users to the cluster. After you've added users, you can manage existing users and add new users. If you don't enable user authentication, there is no need to create users. However, we strongly advise against deploying a cluster without user authentication enabled.

You perform user management tasks as follows:
+ If you've set up with local authentication on the cluster, you manage users and user roles using AWS Elemental Conductor Live, as described in this section.
+ If you've set up with PAM authentication on the cluster, you manage users on your organization's LDAP server.

**Note**
The username of a user is case sensitive.

**Topics**
+ [Types of users](users-types.md)
+ [Adding users to Conductor Live](conductor-live-config-users.md)
+ [Adding users to worker nodes](config-conductor-live-users-add-workers.md)
+ [Role policies for PAM authentication](config-rpolicies.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
