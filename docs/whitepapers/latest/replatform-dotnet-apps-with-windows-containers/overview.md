---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview
<a name="overview"></a>

 Containers are becoming the primary technology for packaging and deploying applications. International Data Corporation (IDC) estimates that the number of container instances installed globally by enterprises (excluding public cloud providers) increased 133 percent year-over-year to 273.5 million instances in 2020, and is expected to grow five times to 1.39 billion instances by 2023. Within this enterprise containers install base, Windows container instances accounted for 19.5 million instances (7.1 percent of total) in 2020, and is expected to grow 8 times to 156.9 million instances (11.2 percent of total) by 2023. (Source: [IDC Container Infrastructure Software Market Assessment: x86 Containers Forecast, 2018-2023, Doc\# US46185620, April 2020](https://www.idc.com/getdoc.jsp?containerId=US46185620).) The trend is clear that enterprises are adopting and standardizing the use of containers.

 Before exploring how to complete the replatforming of existing .NET applications to Windows containers, this guide examines the reasons driving enterprises toward this approach.

 The Windows operating system (OS) preexisted container technology. There were fundamental pieces of the OS that required changes to enable Windows to run in containers. Because of this, Windows containers were not introduced until 2016, three years after Docker released Linux containers. Kubernetes only recently debuted support for running Windows containers as worker nodes in April 2019.

 Because of these releases, organizations have been moving their existing .NET Framework applications to Windows containers to improve their development agility, optimize the utilization of their infrastructure resources, increase their application portability across environments, and control the boundaries of their applications with container isolation. Windows containers also created an opportunity for organizations to migrate their existing .NET applications running on end-of-life versions, such as Windows Server 2003 and Windows Server 2008, to newer Windows Server versions with minimal code changes.

 However, the benefits of Windows containers do not come without challenges. Existing development and IT teams that are well versed in building and running Windows-based applications today may lack hands-on experience with containers. This requires teams to develop new skillsets, operational techniques, and architectural designs to successfully deploy container-based applications in production. For example, when moving to Windows containers, teams must choose their Windows container type, runtime version, and orchestration engine to use. Teams must understand the technical nuances of Windows containers that require workarounds because of their early state of maturity. Additionally, new organizational practices, such as DevOps, are recommended to take full advantage of the automation that containers facilitate. All of these pieces contribute to the complexity that organizations face when adopting containers and this guide aims to demystify this picture to help teams adopt Windows containers where it makes sense for their technology stack.
