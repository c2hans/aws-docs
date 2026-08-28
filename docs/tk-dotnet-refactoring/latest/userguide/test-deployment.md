---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/test-deployment.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# What is a test deployment?
<a name="test-deployment"></a>

A test deployment is a simplified application deployment into AWS that allows you to deploy the application and validate code changes quickly.

Test deployment is intended for use during the development cycle of the application. To reduce turnaround time and costs, a test deployment is simplified in the following ways:
+ Scalability is limited to one instance of the application.
+ Because there is only one instance of the application, a load balancer is not created.
+ Amazon API Gateway is not created.
+ Route 53 Private DNS for VPCs is not created.
+ A health check is not performed on the application. You are expected to perform testing to make sure the application works as expected. For debugging, you can use logs as well as the Amazon Elastic Container Service (Amazon ECS) `execute` command to execute commands inside the application container. If the application crashes, the container and Amazon ECS task is not deleted so you can review the container contents to determine why the application crashed. Use the `deploy` command to restart the application.

## Test deployment cycle
<a name="deployment-cycle"></a>

The test development cycle consists of the following steps:

1. The developer builds the project and produces the application files, such as executable files, data files, and configuration files.

1. Toolkit for .NET Refactoring creates a container image for the application that is added to the Amazon Elastic Container Registry (Amazon ECR) of the account.

1. If a custom Docker file is specified, the container is created according to the file. Note that the file must adhere to the following guidelines, which are required for the application redeployment and restart:
   + The entire application must be located in the `/app` directory.
   + The start script for the application must be named `/app/entryfile`.

   If a custom Docker file is not specified, Toolkit for .NET Refactoring does the following:
   + The application files are placed into the `/app` directory in the container. The subdirectory structure is preserved.
   + The application start script is created, which executes the following command: `dotnet {{<application_name>}}`

1. Toolkit for .NET Refactoring creates a deployment in AWS that includes the AWS Fargate cluster, the Amazon ECS service, and the AWS Fargate task.

1. Toolkit for .NET Refactoring creates security groups for the application to provide network security. Only traffic to the specified application ports is permitted.

1. Toolkit for .NET Refactoring displays:
   + The IP address of the deployed application. You can use the IP address to connect the clients and browsers to the application ports.
   + The names of Amazon CloudWatch log groups and log streams. You can use these to view the logs of the application. Note that only console logs are supported.

1. If you change the code, data, or configuration files, rebuild the project and deploy it again.
   + If your changes include significant modifications to the application compute environment, such as open ports, the base image, or the Docker file, Toolkit for .NET Refactoring will rebuild a container image and deploy a new Amazon ECS service.
   + If the changes are limited to the application files, Toolkit for .NET Refactoring will deliver the new files to the Amazon ECS task and restart the application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
