---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/aliases.html
---

# `[aliases]` section
<a name="aliases"></a>

**Topics**

Specifies aliases, and enables you to customize the `ssh` command.

Note the following default settings:
+ `CFN_USER` is set to the default user name for the OS
+ `MASTER_IP` is set to the IP address of the head node
+ `ARGS` is set to whatever arguments the user provides after *`pcluster ssh cluster_name`*

```
[aliases]
# This is the aliases section, you can configure
# ssh alias here
ssh = ssh {CFN_USER}@{MASTER_IP} {ARGS}
```

[Update policy: This setting is not analyzed during an update.](using-pcluster-update.md#update-policy-setting-ignored)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
