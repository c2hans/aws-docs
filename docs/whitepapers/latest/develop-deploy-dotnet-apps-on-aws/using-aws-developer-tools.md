---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/using-aws-developer-tools.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using AWS Developer Tools
<a name="using-aws-developer-tools"></a>

There are a number of services collectively known as the [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/), which are designed to solve common DevOps requirements and provide development agility and continuous innovation.

You may already be using a CI/CD pipeline. Although you can continue using your favorite tools and easily integrate them with AWS Services, you can also use AWS developer tools to create a complete pipeline, or complement or extend the other tools you are using. Using AWS Developer Tools relieves you from managing infrastructure of your CI/CD pipeline tools, and helps you increase the efficiency and productivity of your infrastructure and developers.

## Version Control
<a name="version-control"></a>

Most .NET developers are familiar with GitHub repositories, and are well versed in using them to collaborate on software development projects.

Maintaining a Git repository for a single project is simple, but as the number of projects grows, managing a Git repository can become burdensome. You have to make sure your source control server is available all the time, its performance does not degrade, and its storage is scaled to cater for increasing demand.

[AWS CodeCommit](https://aws.amazon.com/codecommit/) is a fully managed source control service that enables you to securely host private Git repositories in a highly scalable way. You can use AWS CodeCommit to store anything from your source code to other binaries and dependencies that go with your code. AWS Toolkit for Visual Studio integrates AWS CodeCommit.

For example, you might be developing an ASP.NET web application that also includes external DLL dependency files and several gigabytes of graphics and other multimedia files. Separating source code from binary files increases the risk of inconsistencies and bugs that have nothing to do with the code. Using AWS CodeCommit, you can store all of these in one repository and avoid such problems.

As an alternative to AWS CodeCommit, both [AWS CodeBuild](https://aws.amazon.com/codebuild/) and [AWS CodePipeline](https://aws.amazon.com/codepipeline/) integrate with GitHub, and AWS CodeBuild also integrates with [Bitbucket](https://bitbucket.org/product).

## Build and Package Applications
<a name="build-and-package-applications"></a>

Building the source code is one of the key steps in any CI/CD pipeline. Once a new version is committed in your source control system, you need a build service to pull the latest version, build and package it so the new version can be deployed in a target environment.

One way to do this is using build servers that you dedicate for this purpose. However, as the number of concurrent projects and number of builds in each project grows, these build servers have to be scaled out to provide more build capacity. Otherwise, your builds wait in a queue, which can result in decreased productivity of your developers.

[AWS CodeBuild](https://aws.amazon.com/codebuild/) is a fully managed build service that compiles source code, runs tests, and produces software packages that are ready to deploy. It seamlessly scales and concurrently processes multiple builds, eliminating waiting time and increasing developer productivity. You only pay for time the build container is running.

AWS CodeBuild includes a pre-packaged build environment for .NET Core and/or .NET 5 on Linux and Windows. Alternatively, you can use pre-built Docker images such as official Microsoft images for the .NET, or create your own custom build environment by creating a Docker image.

For details about creating a custom build environment for .NET Framework, see [this entry](https://aws.amazon.com/blogs/devops/extending-aws-codebuild-with-custom-build-environments-for-the-net-framework/) on the [AWS DevOps Blog](https://aws.amazon.com/blogs/devops/).

Development teams often rely on both open-source software packages, and those packages are built within their organization. IT leaders must be able to control access to and validate the safety of these software packages. Teams need a way to find up-to-date packages that have been approved for use by their IT leaders. To address these challenges, IT leaders turn to central artifact repository services to store and share packages. However, existing solutions often require teams to purchase licenses for software solutions that are complex to set up, scale, and operate. You can use [AWS CodeArtifact](https://aws.amazon.com/codeartifact/) to overcome these challenges.

CodeArtifact is a pay-as-you go artifact repository service that scales based on the needs of the organization. With CodeArtifact, there is no software to update or servers to manage. In just a few clicks, IT leaders can set up central repositories that enable development teams to find and use the software packages they need. IT leaders can also approve packages and control distribution across the organization, ensuring development teams consume software packages that are safe for use.

CodeArtifact is a fully managed artifact repository service that enables organizations of any size to securely store, publish, and share software packages used in their software development process. CodeArtifact can be configured to automatically fetch software packages and dependencies from public artifact repositories so developers have access to the latest versions. CodeArtifact works with commonly used package managers and build tools such as [NuGet](https://www.nuget.org/), [Apache Maven](https://maven.apache.org/), [Gradle](https://gradle.org/), [npm](https://www.npmjs.com/), [yarn](https://yarnpkg.com/), [twine](https://twinery.org/), and [pip](https://pypi.org/project/pip-tools/), making it easy to integrate into existing development workflows.

## Application Deployment
<a name="application-deployment"></a>

After a new application version is built and packaged, it must be deployed in a target environment for end users to access it. There are a couple of common deployment strategies, including mutable in-place deployment, or immutable deployments when the entire infrastructure stack is replaced.

There are a variety of ways to deploy .NET applications, and [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) is a deployment service that integrates with [AWS CodePipeline](https://aws.amazon.com/codepipeline/) and helps automate application deployments to Amazon EC2 instances, Amazon ECS services, on-premises instances, and serverless Lambda functions. It supports in-place mutable deployment, and immutable deployment using the blue-green deployment model.

The AWS CodePipeline Service can also be used for deployment and integrates with a number of deployment providers, including AWS CloudFormation, AWS Elastic Beanstalk, Amazon ECS, Service Catalog, and AWS CodeDeploy.

## Building a CI/CD Pipeline
<a name="building-a-cicd-pipeline"></a>

Each of the previously discussed developer tools can be used individually or in combination with your existing tools, but you can also integrate them together to form a complete end-to-end CI/CD pipeline.

[AWS CodePipeline](https://aws.amazon.com/codepipeline/) is an orchestration service that enables you to model the different stages of your software release process. It can be integrated with other AWS developer tools for building, testing and deploying your software versions. It can also easily be extended to adapt to your specific needs. You can use its pre-built plugins or your own custom plugins in any step of your release process.

For example, you can pull your source code from GitHub, use your on-premises [Jenkins](https://www.jenkins.io/) build server, run load tests using a third-party service, or pass on deployment information to your custom operations dashboard.
