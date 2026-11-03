---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/working-with-.net.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Working with .NET
<a name="working-with-.net"></a>

With the release of .NET 5, .NET is working to provide a uniform runtime to customers, allowing access to a single set of APIs, tools, and languages to target multiple platforms such as mobile, Internet of Things (IoT), and the cloud. The .NET Framework no longer receives any new features or updates, although it continues to be included in the Windows operating system. Although previous runtimes will continue to be supported for a while, both .NET Framework and .NET Core developers can now move on to use modern .NET for new applications.

![A chart depicting the layers of .NET unified runtime.](https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/images/dotnet-apps2.png)

*Modern .NET unified runtime *

## .NET Core and modern .NET
<a name="net-core-.net-5"></a>

Modern .NET is a modern, open-source, cross-platform implementation of .NET, and runs on Windows, Linux, macOS, and other devices. Modern .NET is the evolution of .NET Core. Although .NET Core provided many of the same interfaces and method signatures as the .NET Framework, there were a variety of differences, making it potentially difficult to migrate applications from the .NET Framework to .NET Core. However, modern .NET removes most of those differences and has made it possible to unify those legacy platforms.

As the next generation after .NET Core, modern .NET is now the recommended platform for modern scalable and high-performance applications, and, unlike .NET Framework, its design makes it ideal for targeting microservices architectures. You can run modern .NET applications on AWS as direct deployments on Windows or Linux EC2 instances, on Windows or Linux containers running on EC2 instances, serverless Linux containers running on [AWS Fargate](https://aws.amazon.com/fargate/), or serverless [AWS Lambda](https://aws.amazon.com/lambda/) functions. These services are discussed in more detail in later sections of this whitepaper.

In this whitepaper, *modern .NET* refers to .NET 5 and later releases, which are the evolution of .NET Core. At the time of this update, .NET 10 is the current Long Term Support (LTS) release; .NET 5 reached end of support in May 2022. For current release status, see the [Microsoft .NET lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core) on the Microsoft Learn website.
