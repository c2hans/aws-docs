---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/troubleshooting-job-submission-maxjobcount.html
---

# Troubleshooting job submission failures due to MaxJobCount limit
<a name="troubleshooting-job-submission-maxjobcount"></a>

**Problem:** Job submissions fail with the following error message:

```
sbatch: error: Slurm temporarily unable to accept job, sleeping and retrying
```

This error occurs even when the number of running and pending jobs appears to be well below the cluster's job limit.

**Cause:** The `MaxJobCount` limit includes all jobs tracked by Slurm, not just running or pending jobs. Completed jobs remain in Slurm's memory for a period of time (by default, 5 minutes) before being purged. During high job throughput periods, the total count of active plus recently completed jobs can exceed the limit.

You can verify the total job count by running the following command on a cluster node:

```
scontrol show jobs | grep -c JobId
```

This shows the total number of jobs Slurm is tracking, including completed jobs awaiting purge.

**Solution:** Consider one of the following approaches:
+ **Create a larger cluster** – If your workload consistently requires more concurrent jobs, create a new cluster with a larger size. For more information about cluster sizes and their limits, see [Cluster size in AWS PCS](working-with_clusters_size.md).
+ **Reduce job submission rate** – Adjust your job submission scripts to submit jobs at a slower rate, allowing completed jobs time to be purged from Slurm's tracking.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
