---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/choosing-a-host-operating-system.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Choosing a Host Operating System
<a name="choosing-a-host-operating-system"></a>

Although Windows remains the natural choice for legacy applications using the .NET Framework, the cross-platform nature of .NET 5 means Linux is now an equally viable choice for new and future .NET applications. One of the challenges in choosing an OS is that they have broadly reached a state of commoditization. The current focus on OS evolution is largely about increased efficiency of resource use, as shown by the growing popularity of containers, and the future lure of library operating systems.

Another factor driving the choice of OS is the current architectural wisdom to explicitly declare and isolate dependencies, as promoted by the [12-factor app](https://aws.amazon.com/blogs/compute/applying-the-twelve-factor-app-methodology-to-serverless-applications/) approach, which also aligns to the [single process model of containers](https://www.programmersought.com/article/94153031976/). Given the rich set of services built into Windows, it is common for legacy .NET Framework applications to implicitly depend on a variety of services, such as [Active Directory](https://azure.microsoft.com/en-us/services/active-directory) for authentication and authorization, [COM\+](https://docs.microsoft.com/windows/win32/cossdk/com--application-overview) for distributed transaction processing, or [Distributed File System](https://docs.microsoft.com/windows/win32/dfs/distributed-file-system-dfs-functions) (DFS) for file sharing. However, with the move toward explicitly declaring and isolating such dependencies, relying on Windows’ intrinsic features no longer holds the lure for .NET applications that it once did.

.NET 5 also makes it possible to avoid licensing cost and implications of the Windows operating system. .NET applications liberated from underlying operating system (OS) license restrictions can easily scale in and out to address contemporary IT demands.
