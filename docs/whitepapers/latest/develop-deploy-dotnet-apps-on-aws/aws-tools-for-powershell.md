---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/aws-tools-for-powershell.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Tools for PowerShell
<a name="aws-tools-for-powershell"></a>

PowerShell is a scripting environment built on .NET, and is widely used as the standard scripting tool on Windows, but is also available for MacOS, and Linux. Although primarily used for executing OS-level management scripts, PowerShell is frequently used by .NET developers as part of their build and deployment pipelines.

[AWS Tools for PowerShell](https://aws.amazon.com/powershell/) enables developers to directly access AWS Services from within PowerShell scripts, enabling them to manage and interact with AWS Services with their standard toolset, and removing the need to call the AWS SDK for .NET directly from within scripts.

**AWS Tools for .NET CLI**

[These tool extensions](https://github.com/aws/aws-extensions-for-dotnet-cli) are focused on building .NET Core and ASP.NET Core applications and deploying them to AWS Services (AWS Elastic Beanstalk, Amazon ECS, and AWS Lambda). Many of these deployment commands are the same commands the AWS Toolkit for Visual Studio uses to perform its deployment features. This enables you to do initial deployment in Visual Studio, and then transition from Visual Studio to the command line and automate the deployment.

For example, with the AWS Lambda .NET CLI tool extension configured, you can deploy a Lambda function from the command line in the Lambda function's project root directory.
