---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform.html
---

# Build and push Docker images to Amazon ECR using GitHub Actions and Terraform
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform"></a>

*Ruchika Modi, Amazon Web Services*

## Summary
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-summary"></a>

This pattern explains how you can create reusable GitHub workflows to build your Dockerfile and push the resulting image to Amazon Elastic Container Registry (Amazon ECR). The pattern automates the build process of your Dockerfiles by using Terraform and GitHub Actions. This minimizes the possibility of human error and substantially reduces deployment time.

A GitHub push action to the main branch of your GitHub repository initiates the deployment of resources. The workflow creates a unique Amazon ECR repository based on the combination of the GitHub organization and repository name. It then pushes the Dockerfile image to the Amazon ECR repository.

## Prerequisites and limitations
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An active GitHub account.
+ A [GitHub repository](https://docs.github.com/en/get-started/quickstart/create-a-repo).
+ Terraform version 1 or later [installed and configured](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).
+ An Amazon Simple Storage Service (Amazon S3) bucket for the [Terraform backend](https://developer.hashicorp.com/terraform/language/settings/backends/s3).
+ An [Amazon DynamoDB](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjO95K9xqCCAxW-KIMDHfOvD7IYABADGgJzZg&gclid=EAIaIQobChMIzveSvcagggMVviiDAx3zrw-yEAAYASADEgJYWfD_BwE&ohost=www.google.com&cid=CAASJuRoKjv_llGjIU3liZ4T2IRecPqw0dVHSvjZ7bee1lvcc36K_lO_&sig=AOD64_1b294pq65HiFN-T1YxQAuXmRu_hw&adurl&ved=2ahUKEwjhiY29xqCCAxUgzjgGHRu6CAIQqyQoAnoECAkQDQ) table for Terraform state locking and consistency. The table must have a partition key named `LockID` with a type of `String`. If this isn't configured, state locking will be disabled.
+ An AWS Identity and Access Management (IAM) role that has permissions to set up the Amazon S3 backend for Terraform. For configuration instructions, see the [Terraform documentation](https://developer.hashicorp.com/terraform/language/settings/backends/s3#assume-role-configuration).

**Limitations **

This reusable code has been tested only with GitHub Actions.

## Architecture
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-architecture"></a>

**Target technology stack**
+ Amazon ECR repository
+ GitHub Actions
+ Terraform

**Target architecture**

![Workflow to create reusable GitHub workflows to build Dockerfile and push image to Amazon ECR.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c39c110e-cbe5-459e-a0aa-de27e884fb10/images/298e0e16-3054-49b7-8695-db510e0df2df.png)

The diagram illustrates the following:

1. A user adds a Dockerfile and Terraform templates to the GitHub repository.

2. These additions initiate a GitHub Actions workflow.

3. The workflow checks whether an Amazon ECR repository exists. If not, it creates the repository based on the GitHub organization and repository name.

4. The workflow builds the Dockerfile and pushes the image to the Amazon ECR repository.

## Tools
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-tools"></a>

**Amazon services**
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container registry service that’s secure, scalable, and reliable.

**Other tools**
+ [GitHub Actions](https://docs.github.com/en/actions) is integrated into the GitHub platform to help you create, share, and run workflows within your GitHub repositories. You can use GitHub Actions to automate tasks such as building, testing, and deploying your code.
+ [Terraform](https://developer.hashicorp.com/terraform/intro) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises infrastructure.

**Code repository**

The code for this pattern is available in the GitHub [Docker ECR Actions Workflow](https://github.com/aws-samples/docker-ecr-actions-workflow) repository.
+ When you create GitHub Actions, Docker workflow files are saved in the `/.github/workflows/` folder of this repository. The workflow for this solution is in the [workflow.yaml](https://github.com/aws-samples/docker-ecr-actions-workflow/blob/main/.github/workflows/workflow.yaml) file.
+ The `e2e-test` folder provides a sample Dockerfile for reference and testing.

## Best practices
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-best-practices"></a>
+ For best practices for writing Dockerfiles, see the [Docker documentation](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).
+ Use a [VPC endpoint for Amazon ECR](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). VPC endpoints are powered by AWS PrivateLink, a technology that enables you to privately access Amazon ECR APIs through private IP addresses. For Amazon ECS tasks that use the Fargate launch type, the VPC endpoint enables the task to pull private images from Amazon ECR without assigning a public IP address to the task.

## Epics
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-epics"></a>

### Set up the OIDC provider and GitHub repository
<a name="set-up-the-oidc-provider-and-github-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure OpenID Connect. | Create an OpenID Connect (OIDC) provider. You will use the provider in the trust policy for the IAM role used in this action. For instructions, see [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) in the GitHub documentation. | AWS administrator, AWS DevOps, General AWS |
| Clone the GitHub repository. | Clone the GitHub [Docker ECR Actions Workflow](https://github.com/aws-samples/docker-ecr-actions-workflow) repository into your local folder:<pre>$git clone https://github.com/aws-samples/docker-ecr-actions-workflow</pre> | DevOps engineer |

### Customize the GitHub reusable workflow and deploy the Docker image
<a name="customize-the-github-reusable-workflow-and-deploy-the-docker-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize the event that initiates the Docker workflow. | The workflow for this solution is in [workflow.yaml](https://github.com/aws-samples/docker-ecr-actions-workflow/blob/main/.github/workflows/workflow.yaml). This script is currently configured to deploy resources when it receives the `workflow_dispatch` event. You can customize this configuration by changing the event to `workflow_call` and calling the workflow from another parent workflow. | DevOps engineer |
| Customize the workflow. | The [workflow.yaml](https://github.com/aws-samples/docker-ecr-actions-workflow/blob/main/.github/workflows/workflow.yaml) file is configured to create a dynamic, reusable GitHub workflow. You can edit this file to customize the default configuration, or you can pass the input values from the GitHub Actions console if you're using the `workflow_dispatch` event to initiate deployment manually.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform.html) | DevOps engineer |
| Deploy the Terraform templates. | The workflow automatically deploys the Terraform templates that create the Amazon ECR repository, based on the GitHub event you configured. These templates are available as `.tf` files at the [root of the Github repository](https://github.com/aws-samples/docker-ecr-actions-workflow/tree/main). | AWS DevOps, DevOps engineer |

## Troubleshooting
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Issues or errors when you configure Amazon S3 and DynamoDB as the Terraform remote backend. | Follow the instructions in the [Terraform documentation](https://developer.hashicorp.com/terraform/language/settings/backends/s3) to set up the required permissions on the Amazon S3 and DynamoDB resources for the remote backend configuration. |
| Unable to run or start the workflow with the `workflow_dispatch` event. | The workflow that's configured to deploy from the `workflow_dispatch` event will work only if the workflow is configured on the main branch as well. |

## Related resources
<a name="build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform-resources"></a>
+ [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows) (GitHub documentation)
+ [Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow) (GitHub documentation)
