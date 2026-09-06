---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/containers-and-windows-subsystem-for-linux-on-amazon-workspaces.html
---

# Containers and Windows subsystem for Linux on Amazon WorkSpaces
<a name="containers-and-windows-subsystem-for-linux-on-amazon-workspaces"></a>

## Containers and Amazon WorkSpaces
<a name="containers-and-amazon-workspaces"></a>

End user computing is often approached by customers who are looking to service container workloads with Amazon WorkSpaces. While possible, this is not the preferred or recommended solution. Customers looking to unlock the potential cost and operational savings of containers are strongly encouraged to evaluate [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) and/or [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS).

 In cases where customer requirements mandate enabling containers using Amazon WorkSpaces, a [technical how-to](https://aws.amazon.com/blogs/desktop-and-application-streaming/how-to-configure-amazon-workspaces-with-windows-and-docker/) has been published that enables the use of Docker. Customers should be informed that this requires other trailing services, and that there are increased costs and complexity when compared with decoupled, native container services.

## Windows subsystem for Linux
<a name="winlinux"></a>

 With the launch of Windows Server 2019 as the underlying operating system for Amazon WorkSpaces, customers have been eager to implement Windows Subsystem for Linux (WSL), specifically WSL2. Because WSL2 invokes a virtual machine (Hyper-V) in order to perform its functions, it cannot run on Amazon WorkSpaces, which are managed by AWS hypervisors. Customers should know that only WSL1 will be available for this reason, and understand [the differences between WSL1 and WSL2](https://docs.microsoft.com/en-us/windows/wsl/compare-versions).
