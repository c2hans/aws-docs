---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/create-addir-v3.html
---

# Create an Active Directory
<a name="create-addir-v3"></a>

Make sure that you create an Active Directory (AD) before you create your cluster. For information about how to choose the type of active directory for your cluster, see [Which to choose](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html#choosing_an_option) in the *AWS Directory Service Administration Guide*.

If the directory is empty, add users with user names and passwords. For more information, see the documentation that's specific to [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html) or [Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups.html).

**Note**
AWS ParallelCluster requires every Active Directory user directory to be in the `/home/$user` directory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
