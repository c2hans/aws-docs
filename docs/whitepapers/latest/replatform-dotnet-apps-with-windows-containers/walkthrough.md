---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/walkthrough.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Walkthrough
<a name="walkthrough"></a>

 This walkthrough uses the [MvcMusicStore](https://github.com/aws-samples/dotnet-modernization-music-store) application to demonstrate how to replatform an ASP.NET MVC and Entity Framework-based application that runs on Internet Information Services (IIS) to Windows containers. You will use a tool named [AWS App2Container](https://aws.amazon.com/app2container/) to containerize and deploy it. This tool is provided free of charge and it automates many of the steps necessary to convert an existing VM-based IIS application to one hosted in a container. Additionally, the tool can be used to deploy the containerized application to AWS and create a CI/CD pipeline so that changes to the application can be reliably pushed to the deployment environment. This walkthrough focuses on only the application component (not the database migration) of the following architecture.

![Diagram showing application architecture for MvcMusicStore](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/application-architecture.png)

 For this walkthrough, there are three stages:

1.  **Prerequisites** — Prepare the AWS environment for replatforming.

1.  **Containerization** — Use App2Container to analyze and containerize the app.

1.  **Deployment** — Use App2Container to deploy the containerized app to Amazon ECS and create a CI/CD pipeline.

**Note**
 Do not forget to end your AWS resources upon completion of the walkthrough. This can be accomplished by going to the CloudFormation service in the [AWS Management Console](https://aws.amazon.com/console/) and deleting each stack.

**Topics**
+ [Prerequisites](prerequisites.md)
+ [Connect to deployment](connect-to-deployment.md)
+ [Set up App2Container prerequisites](set-up-app2container-prerequisites.md)
+ [Install and initialize App2Container](install-and-initialize-app2container.md)
+ [Containerization](containerization.md)
+ [Deployment](deployment.md)
