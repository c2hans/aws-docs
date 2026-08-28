---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/compute-node-initialization-vpc-limit-v3.html
---

# Seeing `An error occurred (VcpuLimitExceeded)` in `slurm_resume.log` when I fail to run a job, or in `clustermgtd.log`, when I fail to create a cluster
<a name="compute-node-initialization-vpc-limit-v3"></a>

Check the vCPU limits on your account for the specific Amazon EC2 instance type that you are using. If you see zero or fewer vCPUs than you are requesting, request an increase for your limits. For information about how to view current limits and request new limits, see [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
