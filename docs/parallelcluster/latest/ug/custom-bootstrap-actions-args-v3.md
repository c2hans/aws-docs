---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-args-v3.html
---

# Arguments
<a name="custom-bootstrap-actions-args-v3"></a>

In AWS ParallelCluster 2.x the `$1` arguments was a reserved one, to store the URL of the custom script. If you want to re-use the custom bootstrap scripts created for AWS ParallelCluster 2.x with AWS ParallelCluster 3.x you need to adapt them by considering the shift of the arguments. Please refer to [Moving from AWS ParallelCluster 2.x to 3.x](moving-from-v2-to-v3.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
