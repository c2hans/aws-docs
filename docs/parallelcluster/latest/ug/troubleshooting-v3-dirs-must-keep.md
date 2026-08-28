---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-v3-dirs-must-keep.html
---

# Replacing directories
<a name="troubleshooting-v3-dirs-must-keep"></a>

Some directories can't be replaced. If you're having issues replacing the directory, that might be the case. The following directories are shared between the nodes and can't be replaced.
+  `/opt/intel` - This includes Intel MPI, Intel Parallel Studio, and related files.
+  `/opt/slurm` - This includes Slurm Workload Manager and related files. (Conditional, only if `Scheduler: slurm`.)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
