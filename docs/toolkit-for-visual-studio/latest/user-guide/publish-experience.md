---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/publish-experience.html
---

# Working with Publish to AWS in Visual Studio
<a name="publish-experience"></a>

**Publish to AWS** is an interactive deployment experience that assists you with publishing your .NET applications to AWS deployment targets, supporting applications targeting .NET Core 3.1 and later. Working with Publish to AWS keeps your work flow inside of Visual Studio by making these deployment features available, directly from your IDE:
+ The ability to deploy your application with a single click.
+ Deployment recommendations based on your application.
+ Automatic Dockerfile creation, as is relevant and required by your deployment destination's environment (deployment target).
+ Optimized settings for building and packaging your applications, as required by your deployment target.

**Note**
For additional information about publishing .NET Framework applications, see the guide [Creating and deploying .NET applications on Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.html)
You can also access Publish to AWS from the .NET CLI. For more information, see the [Deploy .NET applications on AWS](https://aws.github.io/aws-dotnet-deploy/) guide.

**Topics**
+ [Prerequisites](#publish-experience-prerequisities)
+ [Supported application types](#publish-experience-apptypes)
+ [Publishing applications to AWS targets](#publish-experience-deployment)

## Prerequisites
<a name="publish-experience-prerequisities"></a>

To successfully publish .NET applications to an AWS service, install the following to your local device:
+ .NET Core 3.1\+(which includes .NET5 and .NET6): For additional information about these products and download information, visit the [Microsoft download site](https://dotnet.microsoft.com/download).
+ Node.js 14.x or later version: Node.js is required to run AWS Cloud Development Kit (AWS CDK). To download or obtain more information about Node.js, visit the [Node.js download site](https://nodejs.org/en/download/).
**Note**
Publish to AWS utilizes AWS CDK to deploy your application and all of its deployment infrastructure as a single project. For more information about AWS CDK see the [Cloud Development Kit](https://docs.aws.amazon.com/cdk/v1/guide/home.html) guide.
+ (Optional) Docker is used when deploying to a container-based service such as Amazon ECS. For more information and to download Docker, see the [Docker download](https://docs.docker.com/get-docker/) site.

## Supported application types
<a name="publish-experience-apptypes"></a>

Before publishing to a new or exiting target, begin by creating or opening one of the following project types in Visual Studio:
+ ASP.NET Core application
+ .NET Console application
+ Blazor WebAssembly application

## Publishing applications to AWS targets
<a name="publish-experience-deployment"></a>

When publishing to a new target, Publish to AWS will guide you through the process by making recommendations and using common settings. If you need to publish to a target that was set up previously, your preferences are stored and can be adjusted, or are immediately available for one-click deployment.

**Note**
**Toolkits integration with the .NET CLI Server:**
Publishing launches a .NET server process on the localhost to perform the publication process.

### Publish to a new target
<a name="publish-experience-deployment-newtarget"></a>

The following describes how to configure your Publish to AWS deployment preferences, when you're publishing to a new target.

1. From the **AWS Explorer**, expand the **Credentials** drop-down menu, then choose the AWS profile that corresponds with the region and AWS services that are required for your deployment.

1. Expand the **Region** drop-down menu, then choose the AWS region that contains the AWS services that are necessary for your deployment.

1. From the Visual Studio **Solutions Explorer** pane, open the context menu for (right-click) the project's name, and choose **Publish to AWS**. This will open **Publish to AWS**.

1. From **Publish to AWS**, choose **Publish to New Target** to configure a new deployment.
**Note**
To modify your default deployment credentials, choose or click the **Edit** link located next to the **Credentials** section, in **Publish to AWS**.
To bypass the target configuration process, choose **Publish to Existing Target**, then pick your preferred configuration from the list of your previous deployment targets.

1. From the **Publish Targets** pane, choose an AWS service to manage your application deployment.

1. When you are satisfied with your configuration, choose **Publish** to start the deployment process.
**Note**
After initiating a deployment, **Publish to AWS** displays the following status updates:
During the deployment process, **Publish to AWS** displays information about the deployment's progress.
Following the deployment process, **Publish to AWS** indicates if the deployment succeeded or failed.
After a successful deployment, the **Resources** panel offers additional information about the resource that was created. This information will vary depending on the type of application and deployment configuration.

### Publish to an existing target
<a name="publish-experience-deployment-existingtarget"></a>

The following describes how to republish your .NET application to an existing AWS target.

1. From the **AWS Explorer**, expand the **Credentials** drop-down menu, then choose the AWS profile that corresponds with the region and AWS services that are required for your deployment.

1. Expand the **Region** drop-down menu, then choose the AWS region that contains the AWS services that are necessary for your deployment.

1. From the Visual Studio **Solutions Explorer** pane, right-click the project's name and choose **Publish to AWS** to open **Publish to AWS**.

1. From **Publish to AWS**, choose **Publish to Existing Target** to select your deployment environment from a list of existing targets.
**Note**
If you have recently published any applications to the AWS Cloud, those applications are displayed in Publish to AWS.

1. Select the publishing target that you want to deploy your application to, then click **Publish** to start the deployment process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
