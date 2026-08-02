---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html
---

# Optimize multi-account serverless deployments by using the AWS CDK and GitHub Actions workflows
<a name="optimize-multi-account-serverless-deployments"></a>

*Sarat Chandra Pothula and VAMSI KRISHNA SUNKAVALLI, Amazon Web Services*

## Summary
<a name="optimize-multi-account-serverless-deployments-summary"></a>

Organizations deploying serverless infrastructure across multiple AWS accounts and environments often encounter challenges like code duplication, manual processes, and inconsistent practices. This pattern’s solution shows how to use the AWS Cloud Development Kit (AWS CDK) in Go and GitHub Actions reusable workflows to streamline multi-account serverless infrastructure management. This solution demonstrates how you can define cloud resources as code, implement standardized continuous integration/continuous deployment (CI/CD) processes, and create modular, reusable components.

By using these tools, organizations can efficiently manage cross-account resources, implement consistent deployment pipelines, and simplify complex serverless architectures. The approach also enhances security and compliance by enforcing standardized practices for use with AWS accounts, ultimately improving productivity and reducing errors in serverless application development and deployment.

## Prerequisites and limitations
<a name="optimize-multi-account-serverless-deployments-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Identity and Access Management (IAM) [roles and permissions](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam.html) are in place for the deployment process. This includes permissions to access Amazon Elastic Container Registry (Amazon ECR) repositories, create AWS Lambda functions, and any other required resources across the target AWS accounts.
+ AWS Command Line Interface (AWS CLI) version 2.9.11 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ AWS Cloud Development Kit (AWS CDK) version 2.114.1 or later, [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) and [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_bootstrap).
+ Go 1.22 or later, [installed](https://go.dev/doc/install).
+ Docker 24.0.6 or later, [installed](https://docs.docker.com/engine/install/).

**Limitations**
+ **Language compatibility **– Go is a popular language for serverless applications. However, in addition to Go, the AWS CDK supports other programming languages, including C\#, Java, Python, and TypeScript. If your organization has existing code bases or expertise in other languages, you might need to adapt or learn Go to fully use the solution described in the pattern.
+ **Learning curve **– Adopting the AWS CDK, Go (if it’s new to the organization), and GitHub reusable workflows might involve a learning curve for developers and DevOps teams. Training and documentation might be required to ensure smooth adoption and effective use of these technologies.

## Architecture
<a name="optimize-multi-account-serverless-deployments-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Architecture of AWS CDK and GitHub Actions workflows for multi-account serverless infrastructure management.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8d61917b-bd27-44fa-ae95-55358aaf8812/images/a4b36793-95c7-42f7-a92f-99b4722c9c64.png)

This solution performs the following steps:

1. The developer clones the repository, creates a new branch, and makes changes to the application code in their local environment.

1. The developer commits these changes and pushes the new branch to the GitHub repository.

1. The developer creates a pull request in the GitHub repository, proposing to merge their feature or new feature branch into the main branch.

1. This pull request triggers the continuous integration (CI) GitHub Actions workflow. The CI and the continuous deployment (CD) workflows in this pattern use reusable workflows, which are predefined, modular templates that can be shared and executed across different projects or repositories. Reusable workflows promote standardization and efficiency in the CI/CD processes.

1. The CI workflow sets up the necessary environment, generates a Docker tag for the image, and builds the Docker image using the application code.

1. The CI workflow authenticates with AWS by using the central AWS account GitHub OIDC role. For CI workflows, the central AWS account GitHub OIDC role uses AWS Security Token Service (AWS STS) to obtain temporary credentials. These credentials allow the role to build and push Docker images to the Amazon ECR repository of the central AWS account.

1. The CI workflow pushes the built Docker image to Amazon ECR.

1. The CI workflow stores the image tag to the Systems Manager Parameter Store.

1. After the CI workflow completes successfully, the Docker image tag is output.

1. When triggering the CD workflow, the developer manually inputs the image tag of the Docker image that they want to deploy. This image tag corresponds to the tag that was generated and pushed to Amazon ECR during the CI workflow.

1. The developer manually triggers the CD workflow, which uses the CD reusable workflow.

1. The CD workflow authenticates with AWS using the central AWS account GitHub OIDC role. For the CD workflow, AWS STS is first used to assume the central AWS account GitHub OIDC role. Then, this role assumes the CDK bootstrap roles for target account deployments.

1. The CD workflow uses the AWS CDK to synthesize AWS CloudFormation templates.

1. The CD workflow deploys the application to the target AWS account by using CDK deploy, using the manually specified image tag for the Lambda function.

## Tools
<a name="optimize-multi-account-serverless-deployments-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions. CloudFormation is an integral part of the AWS CDK deployment process. The CDK synthesizes CloudFormation templates and then uses CloudFormation to create or update the resources in the AWS environment.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides secure, hierarchical storage for configuration data management and secrets management.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.
+ [Go](https://go.dev/doc/install) is an open source programming language that Google supports.

**Code repository**

The code for this pattern is available in the GitHub [aws-cdk-golang-serverless-cicd-github-actions](https://github.com/aws-samples/aws-cdk-golang-serverless-cicd-github-actions) repository.

## Best practices
<a name="optimize-multi-account-serverless-deployments-best-practices"></a>
+ **Modular design** – Organize your AWS CDK code into modular and reusable constructs or stacks, promoting code reuse and maintainability across multiple accounts and projects.
+ **Separation of concerns** – Separate the infrastructure code from the application code, allowing for independent deployment and management of each component.
+ **Versioning and immutability** – Treat your infrastructure as code (IaC), and use Git for version control. Embrace immutable infrastructure principles by creating new resources instead of modifying existing ones.
+ **Testing and validation** – Implement comprehensive testing strategies, including unit tests, integration tests, and end-to-end tests, to help support the correctness and reliability of your AWS CDK code and deployments.
+ **Security and compliance** – Follow AWS security best practices, such as least-privilege access, secure communication, and data encryption. Implement compliance checks and auditing mechanisms to ensure adherence to organizational policies and regulatory requirements. Implement security best practices for container images, such as scanning for vulnerabilities, enforcing image signing, and adhering to compliance requirements for your organization.
+ **Monitoring and logging** – Set up monitoring and logging mechanisms to track the health and performance of your serverless applications and infrastructure. Use AWS services like Amazon CloudWatch, AWS CloudTrail, and AWS X-Ray for monitoring and auditing purposes.
+ **Automation and CI/CD** – Use GitHub reusable workflows and other CI/CD tools to automate the build, testing, and deployment processes, which can help support consistent and repeatable deployments across multiple accounts.
+ **Environment management** – Maintain separate environments (for example, development, staging, and production). Implement strategies for promoting changes between environments, ensuring proper testing and validation before production deployments.
+ **Documentation and collaboration** – Document your infrastructure code, deployment processes, and best practices to facilitate knowledge sharing and collaboration within your team.
+ **Cost optimization** – Implement cost monitoring and optimization strategies, such as rightsizing resources, making use of auto-scaling, and taking advantage of AWS cost optimization services such as AWS Budgets and AWS Cost Explorer.
+ **Disaster recovery and backup** – Plan for disaster recovery scenarios by implementing backup and restore mechanisms for your serverless applications and infrastructure resources.
+ **Continuous improvement** – Review regularly and update your practices, tools, and processes to align with the latest best practices, security recommendations, and technological advancements in the serverless ecosystem.
+ **Improve security posture** – Use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) to improve the security posture of your virtual private cloud (VPC) by configuring interface VPC endpoints for Amazon ECR, AWS Lambda, and AWS Systems Manager Parameter Store.

## Epics
<a name="optimize-multi-account-serverless-deployments-epics"></a>

### Set up the environments
<a name="set-up-the-environments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon ECR repository in the central AWS account. | To share container images across multiple AWS accounts, you must configure cross-account access for Amazon ECR. First, create an Amazon ECR repository in the central AWS account.<br />To create an Amazon ECR repository, run the following command:<pre>aws ecr create-repository --repository-name sample-repo</pre><br />In a later task, grant pull access to the other AWS accounts that need to use the container image. | AWS DevOps |
| Add cross-account permissions to the Amazon ECR repository. | To add cross-account permissions to the Amazon ECR repository in the central AWS account, run the following code:<pre>{<br />  "Version": "2008-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Sid": "LambdaECRImageRetrievalPolicy",<br />      "Effect": "Allow",<br />      "Principal": {<br />        "Service": "lambda.amazonaws.com"<br />      },<br />      "Action": [<br />        "ecr:BatchGetImage",<br />        "ecr:GetDownloadUrlForLayer",<br />      ],<br />      "Condition": {<br />        "StringLike": {<br />          "aws:sourceArn": "arn:aws:lambda:<Target_Region>:<Target_Account_ID>:function:*"<br />        }<br />      }<br />    },<br />    {<br />      "Sid": "new statement",<br />      "Effect": "Allow",<br />      "Principal": {<br />        "AWS": "arn:aws:iam::<Target_Account_ID>:root"<br />        },<br />      "Action": [<br />        "ecr:BatchGetImage",<br />        "ecr:GetDownloadUrlForLayer",<br />      ],<br />    }<br />  ] <br />}</pre> | AWS DevOps |
| Configure a role for GitHub OIDC role in the central AWS account. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html) | AWS DevOps |
| Bootstrap the AWS environment in the target AWS accounts. | Set up a CDK environment in a specific AWS account and AWS Region that enables cross-account deployments from a central account and applies least-privilege principles to the CloudFormation execution role.<br />To [bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) an AWS environment, run the following command:<pre>cdk bootstrap aws://<Target_Account_ID>/<Target_Region> --trust <Central_Account_ID> --cloudformation-execution-policies arn:aws:iam::aws:policy/<Least_Privilege_Policy></pre> | AWS DevOps |
| Grant central AWS account OIDC role access to the target AWS account bootstrap roles. | The CDK bootstrap creates the following IAM roles that are designed to be assumed by the central AWS account during various stages of the CDK deployment process:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html)<br />Each role has specific permissions tailored to its purpose, following the least-privilege principle. The `Target_Account_ID` and `Target_Region` in each role name help to indicate that these roles are unique across different AWS accounts and Regions. This approach supports clear identification and management in multi-account, multi-Region setups.<pre>Target Account CDK Bootstrap Roles<br />arn:aws:iam::<Target_Account_ID>:role/cdk-deploy-role-<Target_Account_ID>-<Target_Region><br />arn:aws:iam::<Target_Account_ID>:role/cdk-file-publishing-role-<Target_Account_ID>-<Target_Region><br />arn:aws:iam::<Target_Account_ID>:role/cdk-image-publishing-role-<Target_Account_ID>-<Target_Region><br />arn:aws:iam::<Target_Account_ID>:role/cdk-lookup-role-<Target_Account_ID>-<Target_Region></pre>[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html)<br />To update the permissions policy for the OIDC role in the central AWS account, use the following code:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": "sts:AssumeRole",<br />            "Resource": [<br />                "arn:aws:iam::<Target_Account_ID>:role/cdk-deploy-role-<Target_Account_ID>-<Target_Region>",<br />                "arn:aws:iam::<Target_Account_ID>:role/cdk-file-publishing-role-<Target_Account_ID>-<Target_Region>",<br />                "arn:aws:iam::<Target_Account_ID>:role/cdk-image-publishing-role-<Target_Account_ID>-<Target_Region>",<br />                "arn:aws:iam::<Target_Account_ID>:role/cdk-lookup-role-<Target_Account_ID>-<Target_Region>"<br />            ]<br />        }<br />    ]<br /> }<br /></pre> | AWS DevOps |

### Build the Docker image
<a name="build-the-docker-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the project repository. | To clone this pattern’s [GitHub repository](https://github.com/aws-samples/aws-cdk-golang-serverless-cicd-github-actions), run the following command:<pre>git clone https://github.com/aws-samples/aws-cdk-golang-serverless-cicd-github-actions.git</pre> | AWS DevOps |
| Go to the Dockerfile path. | To navigate to the Dockerfile path, run the following command:<pre>cd lambda</pre> | AWS DevOps |
| Authenticate Docker with Amazon ECR. | Amazon ECR requires secure access to your private container repositories. By signing in this way, you're allowing Docker on your local machine or CI/CD environment to interact with Amazon ECR securely.<br />To authenticate Docker with Amazon ECR, run the following command:<pre>aws ecr get-login-password --region <AWS_REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com</pre><br />Revise the placeholders `AWS_REGION` and `AWS_Account_ID` with your information. | AWS DevOps |
| Build the Docker image. | To build the Docker image, run the following command:<pre>docker build --platform linux/arm64 -t sample-app .</pre> | AWS DevOps |
| Tag and push the Docker Image. | To tag and push the Docker image to the Amazon ECR repository, run the following commands:<pre>docker tag sample-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<ECR_REPOSITORY>:<DOCKER_TAG></pre><pre>docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<ECR_REPOSITORY>:<DOCKER_TAG></pre><br />Revise the placeholders `AWS_Account_ID`, `AWS_REGION`, `ECR_REPOSITORY`, and `DOCKER_TAG` with your information. | AWS DevOps |

### Deploy the AWS CDK app
<a name="deploy-the-cdk-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Synthesize the CDK stack with environment-specific variables. | To generate the CloudFormation template for your infrastructure as defined in your CDK code, run the following command:<pre>ENV=<environment> IMAGETAG=<image_tag> ECR_ARN=<ecr_repo_arn> cdk synth</pre><br />Revise the following placeholders with your information:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html) | AWS DevOps |
| Deploy the CDK stack. | To deploy the CDK stack to your AWS account, run the following command. The `--require-approval never` flag means that the CDK will automatically approve and execute *all *changes. This includes changes that the CDK would normally flag as needing manual review (such as IAM policy changes or removal of resources). Make sure that your CDK code and CI/CD pipeline are well-tested and secure before using the `--require-approval never` flag in production environments.<pre>ENV=<environment> IMAGETAG=<image_tag> ECR_ARN=<ecr_repo_arn> cdk deploy --require-approval never</pre> | AWS DevOps |

### Automate CI/CD using GitHub Actions workflows
<a name="automate-ci-cd-using-github-actions-workflows"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a feature branch, and add your changes. | Use the cloned repository that you created earlier, create a feature branch, and then add your changes to the application code. Use the following commands:<pre>git checkout -b <feature_branch><br />git add .<br />git commit -m "add your changes"<br />git push origin <feature_branch></pre><br />Following are examples of changes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html)<br />GitHub Actions will use the reusable workflows and trigger the CI/CD pipelines. | AWS DevOps |
| Merge your changes. | Create a pull request, and merge your changes to main. | AWS DevOps |

## Troubleshooting
<a name="optimize-multi-account-serverless-deployments-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `AccessDenied` errors when deploying resources across AWS accounts, for example, `AccessDenied: User not authorized to perform: "sts:AssumeRole"`. | To help resolve this issue, do the following to verify cross-account permissions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html) |
| Compatibility issues because of version mismatches, for example, `undefined: awscdkStack` error with an outdated CDK version. | To help resolve this issue, do the following to verify that you’re using the required versions of the AWS CDK and Go:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html) |
| CI/CD pipeline failures, for example, `Error: No such file or directory` because of incorrect YAML configuration or `Permission denied` for protected branches. | To help resolve issues with the GitHub Actions configuration, verify that the reusable workflows are properly referenced and configured. |

## Related resources
<a name="optimize-multi-account-serverless-deployments-resources"></a>

**AWS resources**
+ [AWS Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)
+ [AWS CDK Workshop](https://cdkworkshop.com/60-go.html)
+ [AWS Cloud Development Kit Library](https://pkg.go.dev/github.com/aws/aws-cdk-go/awscdk/v2)
+ [Create a Lambda function using a container image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
+ [Identity and Access Management for Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam.html)
+ [Working with the AWS CDK in Go](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-go.html)

**Other resources**
+ [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) (GitHub documentation)
+ [Golang Documentation](https://golang.org/doc/)
+ [Quickstart for GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart) (GitHub documentation)
+ [Reusing workflows](https://docs.github.com/en/actions/sharing-automations/reusing-workflows) (GitHub documentation)
