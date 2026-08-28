---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-rpolicies.html
---

# Role policies for PAM authentication
<a name="config-rpolicies"></a>

If you configure the cluster to use PAM authentication, then when you create a user on the LDAP server, you assign a role policy. The role policies exist in Conductor Live, not on your LDAP server.

**To view role policies**

1. Log into the primary Conductor Live as an administrator.

1. On the menu bar, choose **Settings**. Then choose **Roles Policies** from the left bar.

   Information about the supported role policies appears. Set up PAM authentication to use these role policies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
