---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/seamless-integration-with-azure-devops.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Seamless Integration with Azure DevOps
<a name="seamless-integration-with-azure-devops"></a>

The main integration point for Azure DevOps with AWS is through Azure DevOps pipelines. You can configure Azure DevOps pipeline to build, test, package and release software to different AWS environments. You can use the following methods for this integration.

## AWS Tools for Azure DevOps
<a name="aws-tools-for-azure-devops"></a>

[AWS Tools for Azure DevOps](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-vsts-tools) is available on the [Azure DevOps Extension Marketplace](https://marketplace.visualstudio.com/azuredevops?WT.mc_id=azure-blog-antchu). To install these extensions, navigate to the Extensions Marketplace through Azure DevOps. You can also install them on your on-premises Azure DevOps Server.

After installation, you can choose from a set of pipeline tasks that can be included in your pipeline to integrate with AWS.

These building blocks can then be used to construct complex deployment pipelines. The following figure shows an example pipeline designed to build, test, and publish an ASP.NET Core web application to an AWS Elastic Beanstalk environment.

![An example pipeline designed to build, test, and publish an ASP.NET Core web application to an AWS Elastic Beanstalk environment.](http://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/images/dotnet-apps6.png)

* Pipeline for building, testing, and deploying an ASP.NET Core application to AWS Elastic Beanstalk *

**Pipeline step descriptions**

1.  Executes .NET Core build task, such as Git pull

1.  Executes .NET Core build task

1.  Executes .NET Core test task

1.  Executes .NET Core publish task

1.  Copies an AWS Elastic Beanstalk manifest file into the bundle

1.  Creates a zip archive from newly published website content.

1.  Uploads the zip archive to an S3 bucket.

1.  Deploys the application in an AWS Elastic Beanstalk environment.

## Custom Scripts
<a name="custom-scripts"></a>

If you need functionalities beyond those provided through extensions published by AWS, or if you need more fine-grained control over your pipeline, you can use AWS CLI or AWS Tools for Windows PowerShell to create a custom task or step in Azure DevOps pipeline.
