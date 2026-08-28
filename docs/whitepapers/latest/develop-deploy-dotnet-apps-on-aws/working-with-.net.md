---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/working-with-.net.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Working with .NET
<a name="working-with-.net"></a>

With the release of .NET 5, .NET is working to provide a uniform runtime to customers, allowing access to a single set of APIs, tools, and languages to target multiple platforms such as mobile, Internet of Things (IoT), and the cloud. The .NET Framework no longer receives any new features or updates, although it continues to be included in the Windows operating system. Although previous runtimes will continue to be supported for a while, both .NET Framework and .NET Core developers can now move on to use .NET 5 for new applications.

![A chart depicting the layers of .NET unified runtime.](http://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/images/dotnet-apps2.png)

*.NET 5 unified runtime *

## .NET Core / .NET 5
<a name="net-core-.net-5"></a>

.NET 5 is a modern, open-source, cross-platform implementation of .NET, and runs on Windows, Linux, macOS, and other devices. .NET 5 is the evolution of .NET Core. Although .NET Core provided many of the same interfaces and method signatures as the .NET Framework, there were a variety of differences, making it potentially difficult to migrate applications from the .NET Framework to .NET Core. However, .NET 5 removes most of those differences and has made it possible to unify those legacy platforms.

As the next generation after .NET Core, .NET 5 is now the recommended platform for modern scalable and high-performance applications, and, unlike .NET Framework, its design makes it ideal for targeting microservices architectures. You can run .NET 5 applications on AWS as direct deployments on Windows or Linux EC2 instances, on Windows or Linux containers running on EC2 instances, serverless Linux containers running on [AWS Fargate](https://aws.amazon.com/fargate/), or serverless [AWS Lambda](https://aws.amazon.com/lambda/) functions. These services are discussed in more detail in later sections of this whitepaper.

Going forward in this whitepaper, whenever .NET 5 is mentioned, the same statements also apply to .NET Core. We explicitly call out any differences for .NET 5 and .NET Core use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
