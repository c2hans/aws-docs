---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorial-create-ami-terraform-deploy.html
---

# Deploy the AMI
<a name="tutorial-create-ami-terraform-deploy"></a>

To deploy the AMI, run the standard Terraform commands in order.

1. Build the project:

   ```
   terraform init
   ```

1. Define the deployment plan:

   ```
   terraform plan -out tfplan
   ```

1. Deploy the plan:

   ```
   terraform apply tfplan
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
