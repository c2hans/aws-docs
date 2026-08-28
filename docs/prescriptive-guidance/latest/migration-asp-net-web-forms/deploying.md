---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-asp-net-web-forms/deploying.html
---

# Deploying ASP.NET Web Forms applications on AWS
<a name="deploying"></a>

## Managing NuGet packages
<a name="nuget-manage"></a>

NuGet is a repository that contains and manages code packages for .NET. An application can have two types of NuGet packages installed: publicly available packages from [nuget.org](https://www.nuget.org/) or custom-built packages that are published to an internal repository. Pulling down packages from nuget.org requires that the instances building the application have outbound internet access. For some users, internet access might not be desirable because of security concerns or network restrictions.

To solve this issue, you can provision a managed artifact (NuGet) repository to download packages from external sources such as nuget.org. You can use AWS CodeArtifact, which is a fully managed artifact repository service, as a NuGet package repository. For more information, see the AWS blog post [Using NuGet with AWS CodeArtifact](https://aws.amazon.com/blogs/devops/using-nuget-with-aws-codeartifact/). Other popular third-party options include [Nexus](https://help.sonatype.com/repomanager2/.net-package-repositories-with-nuget) and [Artifactory](https://www.jfrog.com/confluence/display/JFROG/NuGet+Repositories). This approach allows you to cache publicly available packages within your private repository and reduces the need for direct internet access during the build process. If you want more control over which packages can be downloaded, you can disable external access. In this case, developers will have to push both their own NuGet packages and any other third-party packages they need to the repository.

To configure your application to use the NuGet package repository, create a `NuGet.config` file in the project root or solution root directory. This file specifies the package sources that NuGet should use when restoring packages. The following example shows how to configure the `NuGet.config` file to use CodeArtifact:

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <packageRestore>
        <!-- Allow NuGet to download missing packages -->
        <add key="enabled" value="True" />
        <!-- Automatically check for missing packages during build in Visual Studio -->
        <add key="automatic" value="True" />
    </packageRestore>
    <packageSources>
        <add key="MyRepo" value="https://my_domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/nuget/my_repo/v3/index.json" />
    </packageSources>
</configuration>
```

In this example, replace `https://my_domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/nuget/my_repo/v3/index.json` with the actual URL of your CodeArtifact repository. You can find this URL on the [CodeArtifact console](https://console.aws.amazon.com/codesuite/codeartifact/start) or by running the `aws codeartifact get-repository-endpoint` command.

**Important**

+ Configuring the `NuGet.config` file affects all projects within the same directory structure. If you want to use different package sources for different projects, create separate `NuGet.config` files for each project or solution.
+ Make sure that the instances building the application have the necessary permissions and network access to connect to the NuGet package repository (such as CodeArtifact). For more information about obtaining credentials, see [Use CodeArtifact with the nuget or dotnet CLI](https://docs.aws.amazon.com/codeartifact/latest/ug/nuget-cli.html) in the CodeArtifact documentation.

## Building an application
<a name="nuget-build"></a>

When you migrate legacy ASP.NET Web Forms applications to AWS, you continue using the Microsoft Build Engine (MSBuild) as the central tool for building the applications. MSBuild is typically bundled with Visual Studio, but you can download and use the standalone MSBuild executable from Microsoft without installing Visual Studio. This approach is particularly useful when you build your Web Forms application on AWS, where you can use Windows instances or Docker containers with MSBuild installed.

There are two main steps required to build an ASP.NET Web Forms application: restoring the NuGet packages and building the application. The specifics of how these steps are performed might vary depending on the CI/CD tool you choose to use. For example, if you use AWS CodeBuild, the build process is executed inside a Docker container.

### Restore NuGet packages
<a name="restore-nuget-packages.c722137c-8b87-5b7d-b369-a945f3c5b879"></a>

Before you build your application, you must restore the NuGet packages required by the project. You can do this by using either MSBuild or NuGet Command Line Interface (CLI) commands, executed in the project's root directory.

Using MSBuild:

```
msbuild -t:restore
```

Using NuGet CLI:

```
nuget restore
```

### Build using MSBuild
<a name="build-using-msbuild.db425730-d949-51d5-868e-0b00b7ad324c"></a>

After you restore the NuGet packages, you can proceed with the main build command that produces the deployment artifacts. The command typically specifies the project file, the build configuration (for example, `Release`), and the output directory for the built artifacts.

```
msbuild <ProjectName>.csproj /p:Configuration=Release /p:OutDir=<OutDir>
```

For more information about MSBuild options, see [MSBuild command-line reference](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference) in the Microsoft documentation.

For more information about building an ASP.NET application with AWS CodeBuild, see the AWS blog post [Creating CI/CD pipelines for ASP.NET 4.x with AWS CodePipeline and AWS Elastic Beanstalk](https://aws.amazon.com/blogs/devops/creating-ci-cd-pipelines-for-asp-net-4-x-with-aws-codepipeline-and-aws-elastic-beanstalk/).

## Deploying an application
<a name="nuget-deploy"></a>

After you build your Web Forms application, you deploy the artifacts to the target environment on AWS. In most scenarios, you can zip and upload the built artifacts to an Amazon Simple Storage Service (Amazon S3) bucket for easy distribution and deployment. For instructions, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).

There are two main options for deploying the artifacts to an Amazon EC2 instance: manual and automated.

### Manual deployment
<a name="manual-deployment.103f1473-9507-5c46-b0ad-92f1fe476493"></a>

This option involves using the EC2 instance user data to include scripts that will perform the following tasks:
+ Install Internet Information Services (IIS)
+ Pull and unpack the build artifacts from the Amazon S3 bucket
+ Create and configure the IIS application

Although this approach provides flexibility, it requires manual intervention and might become challenging to manage as your application scales or if it undergoes frequent updates.

### Automated deployment
<a name="automated-deployment.fb0294da-70e6-52f8-a616-3e2edb77a681"></a>

The recommended approach is to use [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) for automated and repeatable deployments. CodeDeploy seamlessly integrates with other AWS services such as AWS CodeBuild and AWS CodePipeline, so you can create a complete CI/CD pipeline for your ASP.NET Web Forms application. With CodeDeploy, you can define deployment strategies such as rolling and blue/green updates to ensure minimal downtime and smooth transitions between application versions.

For more information and examples on setting up CI/CD pipelines for ASP.NET Web Forms applications by using CodePipeline, CodeBuild, and CodeDeploy, see the AWS blog post [Creating CI/CD pipelines for ASP.NET 4.x with AWS CodePipeline and AWS Elastic Beanstalk](https://aws.amazon.com/blogs/devops/creating-ci-cd-pipelines-for-asp-net-4-x-with-aws-codepipeline-and-aws-elastic-beanstalk/).

By using AWS services such as CodeBuild, CodeDeploy, and CodePipeline, you can streamline the build and deployment processes for your migrated ASP.NET Web Forms applications, and ensure consistent and reliable deployments to AWS infrastructure.

For additional information about automated deployments, see the AWS blog post [Generating CI/CD Pipelines for Containerized ASP.NET Applications using AWS App2Container](https://aws.amazon.com/blogs/modernizing-with-aws/generating-ci-cd-pipelines-for-containerized-asp-net-applications-using-aws-app2container/) and the information about [building a CI/CD pipeline for legacy .NET Framework applications](https://repost.aws/questions/QUqSD-rVsFQBKYcrJGQt754w/net-4-7-application-on-ec2-windows) in AWS re:Post.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
