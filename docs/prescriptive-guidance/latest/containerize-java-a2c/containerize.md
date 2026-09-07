---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/containerize.html
---

# Containerize and migrate
<a name="containerize"></a>

If the application server meets all the prerequisites and can run all the AWS App2Container (A2C) tasks, follow the instructions in the [App2Container documentation](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html).

If the application server can't run all the App2Container tasks, use a worker machine. Split the App2Container tasks between the application server and the worker machine.

On the application server, you install and initialize App2Container. Then you analyze the Java applications that are running on the application server. The analysis generates the analysis.json file. Then generate the archive and upload it to an Amazon Simple Storage Service (Amazon S3) bucket or manually copy the archive to the worker machine.

On the worker machine, containerize the application to generate a Docker image. Based on the application type, App2Container takes a conservative approach, known as *process mode*, to identify dependencies. In process mode, all nonsystem files on the application server are included in the container image. In such cases, it is possible that a large image is generated. Then deploy the application to Amazon ECS or Amazon EKS. During containerization, a [deployment.json](https://docs.aws.amazon.com/app2container/latest/UserGuide/config-deployment.html#config-deployment-json) file is created, which is then used by the [generate-app-deployment](https://docs.aws.amazon.com/app2container/latest/UserGuide/cmd-generate-appdeploy.html) command.

For more information on splitting the tasks between the application server and a worker machine, see the [App2Container documentation](https://docs.aws.amazon.com/app2container/latest/UserGuide/cmd-generate-appdeploy.html).

If the application server can only be accessed remotely, run App2Container tasks from a worker machine using remote commands. For more information, see the [Migrate on-premises Java applications to AWS using AWS App2Container](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-on-premises-java-applications-to-aws-using-aws-app2container.html) pattern.

## Solution architecture
<a name="architecture"></a>

The following diagram shows the process and an example architecture for containerizing Java applications using App2Container:

1. On the application servers, set up prerequisites, install App2Container, discover applications, and extract applications.

1. On the worker machine, set up prerequisites, install App2Container, copy extracted applications to the worker machine, containerize, generate deployment, deploy the AWS CloudFormation template and the CI/CD pipeline.

1. App2Container uploads the image to Amazon Elastic Container Registry (Amazon ECR), provisions Amazon ECS, and provisions the pipeline.

1. AWS CodePipeline pulls the code from AWS CodeCommit.

1. CodePipeline pushes the code to AWS CodeBuild.

1. The CI/CD pipeline pushes the Docker images to Amazon ECR.

![Diagram of the data center and the CI/CD pipeline and VPC in the AWS Cloud.](https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/images/guide-img/ace2956a-8fd7-4706-9472-ed4af12c70ed/images/a6422115-dafa-4c3b-94a1-8c6f489e711b.png)
