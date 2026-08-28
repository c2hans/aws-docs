---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-refactor-linux.html
---

# Refactor to modern .NET and move to Linux
<a name="net-refactor-linux"></a>

## Overview
<a name="net-refactor-linux-overview"></a>

Modernizing legacy .NET Framework apps can help you improve security, performance, and scalability. An effective way to modernize .NET Framework apps is to migrate them to a modern .NET version (6\+). Here are some of the key benefits for moving these applications to open-source .NET:
+ To reduce Windows licensing costs by running them on a Linux operating system
+ Take advantage of the availability of modern languages
+ Get performance that's optimized to run on Linux

Many organizations are still running older versions of the .NET Framework. This can pose security risks, since the vulnerabilities in the older versions are no longer addressed by Microsoft. Microsoft has ended support for recent versions of .NET Framework 4.5.2, 4.6, and 4.6.1. It's very important to evaluate the risks and benefits for continuing to run the older versions of the framework. To reduce risk and reduce costs, it can be worth investing the time and effort into refactoring to a modern version of .NET.

## Cost impact
<a name="net-refactor-linux-cost"></a>

Consider a general purpose EC2 instance type (m5), which offers a balance of compute, memory, and networking resources. These instances are suitable for a variety of applications such as web servers, mid-sized databases, and source code repositories.

For example, an on-demand m5.xlarge instance with 4 vCPUs and 16 GB memory on Windows Server (license included) in US East (N. Virginia) costs $274.48 monthly. The same resources on a Linux server cost $140.16 monthly. In this example, there is a 49 percent reduction in cost when you migrate your application from .NET Framework to a modern version of .NET and run your application on a Linux server. Your cost can vary depending on the options (for example, instance type, operating system, storage) you choose when selecting an [EC2 instance](https://aws.amazon.com/ec2/instance-explorer/?ec2-instances-cards.sort-by=item.additionalFields.category-order&ec2-instances-cards.sort-order=asc&awsf.ec2-instances-filter-category=*all&awsf.ec2-instances-filter-processors=*all&awsf.ec2-instances-filter-accelerators=*all&awsf.ec2-instances-filter-capabilities=*all). You can further optimize the costs by using [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) or [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-reserved-instances.html). For more details, use the [AWS Pricing Calculator](https://calculator.aws/#/) to run cost estimates. For Windows-included instances, the license cost is [$0.046 per vCPU per hour](https://aws.amazon.com/ec2/dedicated-hosts/pricing/#Pricing_for_Dedicated_Hosts), regardless of pricing model.

Porting these .NET Framework applications to modern .NET requires developer effort. You must assess your applications and their dependencies to see if they're compatible with the target platform version. [AWS Porting Assistant for .NET](https://aws.amazon.com/blogs/aws/announcing-the-porting-assistant-for-net/) is an assistive tool that scans .NET Framework applications and generates a .NET compatibility assessment, helping you port your applications to be compatible with Linux faster. The Porting Assistant for .NET identifies incompatibilities with .NET, finds known replacements, and generates a detailed compatibility assessment. After porting your solution, you must make manual code changes for your project to be compiled successfully with dependencies. This reduces the manual effort involved in modernizing your applications to Linux. If your application supports ARM processors, moving to Linux unlocks the ability to use Graviton instances. This can help you achieve an additional 20 percent in further cost reductions. For more information, see [Powering .NET 5 with AWS Graviton2: Benchmarks](https://aws.amazon.com/blogs/compute/powering-net-5-with-aws-graviton2-benchmark-results/) in the AWS Compute Blog.

There are other tools, such as [AWS Toolkit for .NET Refactoring](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html) and the [.NET Upgrade Assistant](https://learn.microsoft.com/en-us/dotnet/core/porting/upgrade-assistant-overview), which can help you with porting legacy .NET framework applications to modern .NET.

## Cost optimization recommendations
<a name="net-refactor-linux-rec"></a>

To migrate .NET Framework apps, do the following:

1. **Prerequisites** – To use Porting Assistant for .NET, you must install .NET 5\+ on the machine where you plan to analyze the application source code. The resources on the machine must have a minimum of 1.8 GHz processing speed, 4 GB of memory, and 5 Gb of storage space. For more information, see [Prerequisites](https://docs.aws.amazon.com/portingassistant/latest/userguide/porting-assistant-prerequisites.html) in the Porting Assistant for .NET documentation.

1. **Assessment** – Download Porting Assistant for .NET as an [executable](https://s3.us-west-2.amazonaws.com/aws.portingassistant.dotnet.download/latest/windows/Porting-Assistant-Dotnet.exe) (download) file. You can download and install the tool on your machine to start the assessment of your applications. The assessment page contains ported projects, packages, and APIs that are incompatible with modern .NET. For this reason, you get build errors in the solution after the assessment. You can view or download the assessment findings to a CSV file. For more information, see [Port a solution](https://docs.aws.amazon.com/portingassistant/latest/userguide/porting-assistant-port.html) in the Porting Assistant for .NET documentation.

1. **Refactoring** – After assessing the application, you can port your projects to the target framework version. When you port a solution, your project files and some of the code will be modified by the Porting Assistant. You can check the logs to review the changes to your source code. In most cases, the code will require additional effort to complete the migration and testing to make it production ready. Depending up on the application, some of the changes may include entity framework, identity, and authentication. For more information, see [Port a solution](https://docs.aws.amazon.com/portingassistant/latest/userguide/porting-assistant-port.html) in the Porting Assistant for .NET documentation.

This is a first step to modernizing your applications to containers. There could be a number of business and technical drivers to modernize your .NET Framework apps to Linux containers. One of the significant drivers is reducing the total cost of ownership by moving away from a Windows operating system to Linux. This reduces licensing costs when migrating your application to a cross-platform version of .NET and to containers to optimize resource utilization.

After your application is ported to Linux, you can use [AWS App2Container](https://aws.amazon.com/app2container/) to containerize your application. App2Container uses Amazon ECS or Amazon EKS as endpoint services that you can deploy directly to. App2Container provides all the necessary infrastructure as code (IaC) deployment artifacts to containerize your applications repeatedly.

## Additional considerations and resources
<a name="net-refactor-linux-resources"></a>
+ If you have applications built on VB.NET (a legacy framework from 2002) and want to port them to .NET 6, see the [Port legacy VB.NET applications to .NET 6.0 with Porting Assistant for .NET](https://aws.amazon.com/blogs/modernizing-with-aws/port-legacy-vb-net-applications-to-net-6-0-with-porting-assistant-for-net/) post on the Microsoft Workloads on AWS blog.
+ If you have legacy applications on Windows Communication Foundation (WCF) and want to run them on modern .NET, you can adopt CoreWCF. For more information, see the [Modernizing legacy WCF applications to CoreWCF using Porting Assistant for .NET](https://aws.amazon.com/blogs/modernizing-with-aws/migrate-wcf-apps-to-wcfcore-using-porting-assistant/) post on the Microsoft Workloads on AWS blog.
+ You can add porting assistant as an extension to your Visual Studio IDE. This enables you to perform all of the tasks necessary to convert your code without needing to switch between your IDE and the Porting Assistant for .NET tool. For more information, see the [Accelerate .NET application modernization with Porting Assistant for .NET Visual Studio IDE extension](https://aws.amazon.com/blogs/modernizing-with-aws/net-modernization-with-pa-vs-ide-extension/) post on the Microsoft Workloads on AWS blog.
+ [AWS Porting Assistant for .NET is now open source tool](https://aws.amazon.com/blogs/opensource/open-sourcing-the-porting-assistant-for-net/) with the source code and compatibility analysis components of the assessment. This can encourage your developers to use and share .NET porting knowledge and best practices.
+ You can port .NET framework applications to modern .NET on Linux by using the AWS Toolkit for .NET Refactoring. For more information, see the [Accelerate .NET modernization with AWS Toolkit for .NET Refactoring](https://aws.amazon.com/blogs/modernizing-with-aws/aws-toolkit-for-net-refactoring-launch/) post on the Microsoft Workloads on AWS blog.
+ You can [accelerate containerization and migration of ASP.NET Core applications to AWS using AWS App2Container](https://aws.amazon.com/blogs/modernizing-with-aws/containerize-asp-net-core-applications-using-aws-app2container/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
