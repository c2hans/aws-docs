---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/base-container.html
---

# Using the AL2023 base container image
<a name="base-container"></a>

The AL2023 container image is built from the same software components that are included in the AL2023 AMI. It's available for use in any environment as a base image for Docker workloads. If you're using the Amazon Linux AMI for applications in [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), you can containerize your applications with the Amazon Linux container image.

Use the Amazon Linux container image in your local development environment and then push your application to AWS using [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/userguide/) (Amazon ECS). For more information, see [Using Amazon ECR images with Amazon ECS](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html) in the *Amazon Elastic Container Registry User Guide*.

The Amazon Linux container image is available on Amazon ECR Public. You can provide feedback for AL2023 through your designated AWS representative or by filing an issue in the [amazon-linux-2023 repo](https://github.com/amazonlinux/amazon-linux-2023/issues) on GitHub.

****To pull the Amazon Linux container image from Amazon ECR Public****

1. Authenticate your Docker client to the Amazon Linux Public registry. Authentication tokens are valid for 12 hours. For more information, see [Private registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html) in the *Amazon Elastic Container Registry User Guide*.
**Note**
The **get-login-password** command is supported using the latest version of AWS CLI version 2. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

   ```
   $ aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

   The output is as follows.

   ```
   Login succeeded
   ```

1. Pull the Amazon Linux container image by running the **docker pull** command. To view the Amazon Linux container image on the Amazon ECR Public Gallery, see [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux).
**Note**
When you pull the AL2023 Docker container image, you can use the tags in one of the following formats:
To get the latest version of the AL2023 container image, use the `:2023` tag.
To get a specific version of AL2023, you can use the following format:
`:2023.{{[0-7 release quarter]}}.{{[release date]}}.{{[build number]}}`
The following examples use the tag `:2023` and pull the most recent available container image of AL2023.

   ```
   $ docker pull public.ecr.aws/amazonlinux/amazonlinux:2023
   ```

1. (Optional) Run the container locally.

   ```
   $ docker run -it --security-opt seccomp=unconfined public.ecr.aws/amazonlinux/amazonlinux:2023 /bin/bash
   ```

**To pull the AL2023 container image from Docker Hub**

1. Pull the AL2023 container image using the **docker pull** command.

   ```
   $ docker pull amazonlinux:2023
   ```

1. (Optional) Run the container locally.

   ```
   $ docker run -it amazonlinux:2023 /bin/bash
   ```
**Note**
The container image of AL2023 uses only the `dnf` package manager to install software packages. This means that there's no `amazon-linux-extras` or equivalent command to use for additional software.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
