---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/deployment-chapt.html
---

# Deploying to AWS
<a name="deployment-chapt"></a>

The Toolkit for Visual Studio supports application deployment to AWS Elastic Beanstalk containers or CloudFormation stacks.

**Note**
If you are using Visual Studio Express Edition:
You can use the [Docker CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.use-ecr.html) to deploy applications to Amazon ECS containers.
You can use the [AWS Management Console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deployment.newapp.html) to deploy applications to Elastic Beanstalk containers.
For Elastic Beanstalk deployments, you must first create a web deployment package. For more information, see [How to: Create a Web Deployment Package in Visual Studio](http://msdn.microsoft.com/en-us/library/dd465323.aspx). For Amazon ECS deployment, you must have a Docker image. For more information, see [Visual Studio Tools for Docker](http://docs.microsoft.com/en-us/aspnet/core/publishing/visual-studio-tools-for-docker).

**Topics**
+ [Publish to AWS](publish-experience.md)
+ [AWS Lambda](lambda-cli-publish.md)
+ [Deploying to AWS Elastic Beanstalk](deployment-beanstalk.md)
+ [Deploying to Amazon EC2 Container Service](deployment-ecs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
