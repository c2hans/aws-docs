---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorial-create-ami-terraform.html
---

# Creating a custom AMI with Terraform
<a name="tutorial-create-ami-terraform"></a>

When using AWS ParallelCluster, you only pay for the AWS resources that are created when you create or update AWS ParallelCluster images and clusters. For more information, see [AWS services used by AWS ParallelCluster](aws-services-v3.md).

**Prerequisites**
+  Terraform v1.5.7\+ is installed.
+ [AWS ParallelCluster API](api-reference-v3.md) v3.8.0\+ is deployed in your account. See [Creating a cluster with Terraform](tutorial-create-cluster-terraform.md).
+ IAM role with the permissions to invoke the ParallelCluster API. See [Required permissions](tutorial-create-ami-terraform-permissions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
