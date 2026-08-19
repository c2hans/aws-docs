---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/ecr-apprunner.html
---

# Creating an App Runner service through Amazon ECR
<a name="ecr-apprunner"></a>

The following topic describes how to create and launch an AWS App Runner service from the Amazon Elastic Container Registry (Amazon ECR) node, in the AWS Toolkit for Visual Studio Code. For detailed information about the AWS App Runner and Amazon ECR services, see the [AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html) and [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) User Guides.

## Prerequisites
<a name="ecr-apprunner-prereq"></a>

Before you can create and launch an AWS App Runner from Amazon ECR in the AWS Toolkit, you must complete the following. For a detailed guide on how to complete these procedures, see the [Working with Amazon Elastic Container Registry](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/ecr-working.html) topic in this User Guide.

1. Create a `dockerfile`.

1. Build an image from your `dockerfile`.

1. Create a new repository.

1. Tag and push an image to your repository.

## Creating an AWS App Runner service from an existing Amazon ECR repository
<a name="w2aac17c33c18b7"></a>

The following procedure describes how to create an AWS App Runner service from an existing Amazon ECR repository, in the AWS Toolkit.

1. From the AWS Explorer, expand the region that contains the Amazon ECR repository you want to create an AWS App Runner service from.

1. Expand the Amazon ECR service node to view your Amazon ECR repositories.

1. Open the context menu for (right-click) the Amazon ECR repository or repository image you want to create an AWS App Runner service from.

1. From the context menu, choose **Create App Runner Service** to open the AWS App Runner creation wizard in VS Code

1. From **Enter a port for the new service (1/5)**, enter the port number you want to use, then press **Enter** to continue.

1. From **Configure environment variables (2/5)**, choose **Use file...** to browse to select browse your local files or choose **Skip** to skip this step.

1. From **Select a role to pull from ECR (3/5)**, choose an existing IAM role from the list.
**Note**
The **AppRunnerECRAccessRole** access role is required to create an AWS App Runner service from an Amazon ECR private registry. If a valid role isn't available from the list, choose the **\+ (Create Role...)** icon to automatically create and assign **AppRunnerECRAccessRole** to your registry.

1. From **Name your service (4/5)**, enter a name for your new service, then press **Enter** to continue.

1. From **Select instance configuration (5/5)** choose the **vCPU** and **Memory** configuration from the list to create your new service.

1. From the AWS Explorer, expand the **App Runner** service node to view your AWS App Runner resources. When your new service has been created successfully, the status automatically updates to **Running**.
