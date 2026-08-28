---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/scaling-amazon-eks-infrastructure/network-scaling.html
---

# Network scaling
<a name="network-scaling"></a>

Network scaling in Kubernetes is critical for maintaining seamless communication between services and supporting efficient data flow in dynamic environments. Scaling the network infrastructure helps to make sure that the cluster can handle varying levels of traffic without experiencing bottlenecks or latency issues. Kubernetes provides tools and mechanisms to scale network resources, allowing organizations to maintain optimal performance as traffic patterns change.

This elasticity in network scaling enhances the overall user experience by ensuring fast and reliable connections. Network scaling also optimizes the use of network resources, helping to reduce the costs associated with underutilized or overburdened network components.

Furthermore, effective network scaling is vital for supporting high availability and resilience. By dynamically adjusting network capacity and routing, organizations can ensure that services remain accessible and responsive even during periods of peak demand or unexpected traffic spikes. This approach allows for better utilization of cloud networking resources, ensuring that the infrastructure is always aligned with current requirements.

This section discusses the following types of network scaling:
+ [Amazon VPC CNI plugin for Kubernetes](#plugin)
+ [Custom networking](#networking)
+ [Prefix delegation](#prefix)
+ [Amazon VPC Lattice](#lattice)

## Amazon VPC CNI plugin for Kubernetes
<a name="plugin"></a>

The Amazon VPC Container Network Interface (CNI) plugin for Kubernetes is a critical component in Amazon EKS. The [VPC CNI plugin](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html) provides advanced networking capabilities by integrating Kubernetes pods with Amazon VPC. With this plugin, each pod is assigned a unique IP address from the virtual private cloud (VPC), thereby enhancing network isolation and performance. As clusters grow and network demands fluctuate, the Amazon VPC CNI plugin plays a key role in ensuring efficient and scalable network operations.

The plugin automatically manages the allocation and routing of IP addresses within the VPC, simplifying network management and reducing the risk of IP conflicts. It supports features like prefix delegation, which allows for more flexible IP management.

The VPC CNI Plugin helps organizations optimize network performance, enhance security, and reduce the risk of IP exhaustion. These capabilities are especially valuable for large-scale, dynamic environments where network demands fluctuate, such as microservices architectures, high-density workloads, and multi-tenant applications.

The Amazon VPC CNI Plugin provides the following key features:
+ **Enhanced networking** – The VPC CNI plugin allows each pod to receive its own IP address directly from the VPC, providing strong isolation and network performance. This approach is crucial for workloads requiring high network throughput and low latency.
+ **Prefix delegation** – To overcome IP address exhaustion issues in large clusters, prefix delegation dynamically allocates larger blocks of IPs to nodes, which are then subdivided for pod use. This approach ensures efficient IP utilization and simplifies network scaling.
+ **Custom networking** – Users can configure custom network interfaces (ENIs) for pods, which helps distribute pod traffic across multiple interfaces, reducing network congestion and improving scalability.
+ **Support for IPv6** – By enabling IPv6 in Amazon EKS clusters, users can significantly expand the available IP address space, facilitating the scaling of large, distributed applications without the constraints of IPv4 limitations.
+ **Integration with Kubernetes** – The VPC CNI Plugin works seamlessly with Kubernetes networking components, ensuring that IPs are managed efficiently across pods, services, and external endpoints, and it supports advanced features like security groups for pods.

## Custom networking
<a name="networking"></a>

Custom networking in Amazon EKS enables the assignment of specific network interfaces to pods, providing enhanced control over IP address management and network traffic. This approach is especially useful in scenarios where IP address exhaustion is a concern or when there is a need to segregate network traffic for security, compliance, or performance reasons. [Custom networking](https://docs.aws.amazon.com/eks/latest/best-practices/custom-networking.html) helps organizations efficiently manage IP address space, segregate traffic, and ensure scalable network performance.

With custom networking, administrators can manage network resources more efficiently. Admins can use custom networking to help make sure that pods have the necessary network isolation and that the cluster can scale without encountering IP address limitations.

Custom networking provides the following key features:
+ **Enhanced IP management** – Custom networking allows the assignment of specific network interfaces (ENIs) to pods, helping to manage IP address exhaustion by distributing pod traffic across multiple ENIs. This capability is particularly important in clusters with high-density workloads.
+ **Traffic segregation** – With custom network interfaces, you can separate pod traffic based on specific criteria, such as application type or security requirements. This approach provides greater control over how traffic flows within and outside the cluster.
+ **Support for IPv6** – Custom networking in Amazon EKS also supports IPv6, offering a solution to the limitations of IPv4 addresses. The network can scale efficiently without IP address conflicts, even in large-scale deployments.
+ **Scalability and flexibility** – As the cluster scales, custom networking enables dynamic management of network interfaces. New pods are assigned appropriate network resources without manual intervention. This approach helps maintain a flexible and scalable network environment that can adapt to changing workloads.

## Prefix delegation
<a name="prefix"></a>

Prefix delegation in Kubernetes, particularly within Amazon EKS, is designed to streamline and optimize IP address management as clusters scale. By dynamically allocating larger blocks of IP addresses (prefixes) to nodes, [prefix delegation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) reduces the risk of IP exhaustion and simplifies the management of IP space.

This approach enhances network efficiency, minimizes fragmentation, and helps clusters scale smoothly without manual IP range adjustments. Prefix delegation is particularly valuable for large-scale deployments, high-density workloads, and environments where flexible, dynamic IP management is critical to maintaining network performance and scalability.

Prefix delegation provides the following key features:
+ **Efficient IP address management** – Prefix delegation allows for dynamic allocation of IP ranges, reducing the risk of IP exhaustion and ensuring efficient use of available IP space.
+ **Simplified network management** – By allowing nodes to handle their own IP allocations, prefix delegation minimizes network fragmentation and simplifies the routing process, making it easier to scale clusters as needed.
+ **Support for large-scale deployments** – In large clusters with high-density workloads, prefix delegation enables seamless scaling by allowing new nodes to join the cluster without manual IP range adjustments.

## Amazon VPC Lattice
<a name="lattice"></a>

[Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) enables efficient and secure service-to-service communication within and across VPCs, particularly in microservices architectures. VPC Lattice uses security measures like security groups and network access control lists (network ACLs) in addition to AWS Identity and Access Management (IAM) integration for fine-grained application authentication. A layer-7 proxy service at the heart of VPC Lattice offers connection, load balancing, authentication, authorization, observability, traffic management, and service discovery.

By simplifying networking and security configurations, VPC Lattice helps organizations optimize traffic management, enhance application performance, and scale seamlessly across multiple VPCs and AWS Regions. This is especially valuable for distributed applications that require consistent and reliable networking, such as microservices, cross-Region deployments, and complex cloud-native environments.

Amazon VPC Lattice provides the following key features:
+ **Service-to-service networking** – VPC Lattice simplifies the networking and security configuration between services within a microservices architecture. It provides a unified platform for managing communication, so that services can scale independently while maintaining high performance and security.
+ **Cross-VPC networking** – VPC Lattice is crucial for managing traffic across multiple VPCs or Regions. It provides a consistent networking framework that allows services to communicate seamlessly, regardless of their physical location. This capability is particularly important for large-scale applications that span multiple VPCs or geographic Regions.
+ **Enhanced security management** – By integrating security policies directly into the network layer, VPC Lattice supports service-to-service communication that's both secure and efficient. This feature reduces the complexity of managing security across a distributed environment, allowing for easier scaling and reduced operational overhead.
+ **Simplified traffic management** – VPC Lattice offers advanced traffic management features, including routing, load balancing, and failover mechanisms. With these features, traffic is distributed efficiently across services, optimizing network performance and enhancing the scalability of the application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
