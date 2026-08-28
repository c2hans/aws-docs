---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/deployment-ecs.html
---

# Deploying to Amazon EC2 Container Service
<a name="deployment-ecs"></a>

**Important**
The new **Publish to AWS** feature is designed to simplify how you publish .NET applications to AWS. You may be asked if you want to switch to this publishing experience after you choose **Publish Container to AWS**. For more information, see [Working with Publish to AWS in Visual Studio](publish-experience.md).

Amazon Elastic Container Service is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon EC2 instances.

To deploy applications on Amazon Elastic Container Service, your application components must be developed to run in a Docker container. A Docker container is a standardized unit of software development, containing everything that your software application needs to run: code, runtime, system tools, system libraries, etc.

The Toolkit for Visual Studio provides a wizard that simplifies publishing applications through Amazon ECS. This wizard is described in the following sections.

For more information about Amazon ECS, go to the [Elastic Container Service documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html). It includes an overview of [Docker basics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html) and [creating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html).

**Topics**
+ [Specify AWS Credentials](deployment-ecs-specify-credentials.md)
+ [Deploy an ASP.NET Core 2.0 App (Fargate) (Legacy)](deployment-ecs-aspnetcore-fargate.md)
+ [Deploy an ASP.NET Core 2.0 App (EC2)](deployment-ecs-aspnetcore-ec2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
