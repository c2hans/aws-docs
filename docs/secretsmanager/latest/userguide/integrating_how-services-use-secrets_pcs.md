---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_pcs.html
---

# How AWS Parallel Computing Service uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_pcs"></a>

AWS Parallel Computing Service (AWS PCS) is a managed service that makes it easier to run and scale high performance computing (HPC) and distributed machine learning workloads on AWS.

To connect to the cluster job scheduler, AWS PCS creates a [managed secret](service-linked-secrets.md) with the prefix `pcs` to store the scheduler key. The cost of storing the secret is included with the charge for AWS PCS. AWS PCS automatically deletes the secret when you delete your AWS PCS cluster. For more information, see [Working with cluster secrets in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_secrets.html) in the *AWS PCS User Guide*.

**Important**
Don't modify or delete AWS PCS cluster secrets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
