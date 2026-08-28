---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-v3-custom-slurm-config.html
---

# Seeing errors with custom Slurm configuration
<a name="troubleshooting-v3-custom-slurm-config"></a>

Starting in AWS ParallelCluster version 3.6.0, you can no longer target single `prolog` or `epilog` scripts by including them in a custom Slurm configuration. In AWS ParallelCluster version 3.6.0 and later versions, you must locate custom `prolog` and `epilog` scripts in the respective `Prolog` and `Epilog` folders. These folders are configured by default to point to:
+ `Prolog` points to `/opt/slurm/etc/scripts/prolog.d/`.
+ `Epilog` points to `/opt/slurm/etc/scripts/epilog.d/`.

We recommend that you keep the `90_plcuster_health_check_manager` prolog script and the `90_pcluster_noop` epilog script in place.

Slurm runs the scripts in reverse alphabetical order. Both the `Prolog` and `Epilog` folder must contain at least one file. For more information, see [Slurm `prolog` and `epilog`](slurm-prolog-epilog-v3.md) and [Slurm configuration customization](slurm-configuration-settings-v3.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
