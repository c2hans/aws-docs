---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/update-individual-projects-vpc.html
---

# Update VPC configuration and projects
<a name="update-individual-projects-vpc"></a>

Updating the VPC configuration for the domain will apply to new projects created after that point automatically. Projects that had been created when a VPC configuration did not exist will have the VPC configuration applied only after the project is updated.

## Update VPC
<a name="update-vpc-settings"></a>

![Update VPC configuration in Amazon SageMaker Unified Studio](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/vpc/VPC_Edit.png)

To update a VPC, complete the following steps:

1. From the domain administration page, choose **Settings** in the left navigation pane.

1. Under the **Actions** column, select **Update**.

1. Update the VPC, Subnets, or Security group.

1. Choose **Update**.

## Update project with VPC configuration
<a name="update-project-vpc-config"></a>

To a project with VPC configuration settings, complete the following steps:

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. From the projects list, choose the project you want to update.

1. On the project detail page, you will see a banner at the top indicating "Configurations have changed. Please update this project to access the latest configuration."

1. In the banner, choose **Update**.

1. Confirm the update when prompted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
