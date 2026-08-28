---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html
---

# Modernizing .NET with AWS Transform
<a name="dotnet"></a>

The AWS Transform agent for .NET can help you modernize your .NET applications to be compatible with cross-platform .NET. This capability is called .NET modernization. After [AWS Transform environment](transform-environment.md) in AWS Transform, you can create a .NET modernization transformation job.

## Experiences
<a name="experiences"></a>

AWS Transform is available in several experiences:
+ **Web console**: for large-scale transformation of up to 500 repositories at a time.
+ **Visual Studio IDE**: developer-led transformation of a solution or project working alongside agent interactively and iteratively. Recommended for medium to large projects.

You can freely shift between web console and IDE to work on a transformation job.

You can also invoke AWS Transform from other IDEs and AI code companions:
+ **Kiro**: transform from Kiro using the AWS Transform for Kiro power.
+ **Other AI code companions**: transform from your preferred AI coding assistants using AWS Transform MCP agents.

## Capabilities and key features
<a name="capabilities"></a>
+ Analyze .NET Framework codebases from your source control systems, which includes private NuGet support, identifying cross repository dependencies, and providing an analysis report.
+ Automated transformation of legacy .NET Framework applications to cross-platform .NET, email notifications, and a transformation summary report.
+ Easy integration with the source control platforms (BitBucket, GitHub, and GitLab) to ingest existing code and commit transformed code to a new branch.
+ Validation of transformed code through unit tests.

## Supported versions and project types
<a name="supported-versions"></a>

AWS Transform supports transformation for these versions of .NET:
+ .NET Framework 3.5\+
+ .NET Core 3.1
+ .NET 5.x\+
+ .NET 8

AWS Transform can transform to these target .NET versions:
+ .NET 8
+ .NET 10

AWS Transform supports transformation of these types of projects (C\# only):
+ Class libraries
+ Console applications
+ ASP.NET:
  + Model View Controller (MVC), including front-end Razor Views
  + Single Page Application (SPA) back-ends (business logic layers)
  + Web API
  + Web Forms
+ Unit test projects (NUnit, xUnit, and MSTest)
+ Windows Communication Foundation (WCF) services
+ Projects with provided cross-platform versions for third-party or private NuGet packages. If a cross-platform equivalent is missing or unavailable, AWS Transform for .NET will attempt a best-effort conversion.

AWS Transform can also transform the following project types to modern .NET. This is a preview feature, and may not transform as completely as supported project types.
+ WinForms desktop projects.
+ WPF desktop projects.
+ Xamarin mobile projects.
+ Projects written in VB.NET.

## Limitations
<a name="limitations"></a>

For more information on quotas and limitations for AWS Transform, see [Quotas for AWS Transform](transform-limits.md).

AWS Transform does not transform the following:
+ Blazor UI components
+ Win32 DLLs that don't have core compatible libraries
+ Repositories that do not contain any solutions.

AWS Transform will not modify the original repo branches, and can only write to a separate target branch specified in your transformation plan.

## Human intervention
<a name="human-intervention"></a>

During the porting of .NET Framework applications to cross-platform .NET, you may be requested to provide input or approvals in the following scenarios:
+ Set up a connector to your source code and permissions
+ Validate the proposed modernization plan
+ Upload missing package dependencies as NuGets
+ Review and accept the transformed code

## More information
<a name="more-information"></a>

You can modernize your .NET code by using either the AWS Transform web application or the AWS Toolkit for Visual Studio.
+ [Modernizing your .NET code by using the AWS Transform web application](dotnet-web-app.md)
+ [Modernizing .NET in the IDE](dotnet-ide.md)
+ [Best practices for .NET transformations](dotnet-best-practices.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
