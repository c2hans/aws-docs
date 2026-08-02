---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-6.html
---

# Tenet 6. Use containers strategically
<a name="tenet-6"></a>

Containers can play a valuable role in supporting a multicloud strategy, but it's important to recognize their limitations as well. Using containers is generally a good idea for any modern, cloud-native application, because they provide benefits to portability and consistency across different environments. Containers are platform-agnostic, which means that they can run on any cloud platform or infrastructure that supports containerization technology, such as Kubernetes. Organizations that use containers can develop and package their applications once and then deploy them consistently across multiple cloud providers or on-premises environments, without the need for significant modifications. By encapsulating application code, dependencies, and runtime environment within a container, you can achieve a high degree of portability, which enables you to move workloads seamlessly between cloud providers or between the cloud and on-premises data centers.

However, containers might not solve every use case or eliminate all the challenges an organization might face in adopting a multicloud strategy. Containers work best with modern, microservices-based architectures, but they might not be as well-suited for large, monolithic applications. Additionally, although containers can address certain aspects of portability, such as the application runtime, they do not automatically resolve issues around data management, security policies, and other cross-cloud dependencies. Organizations still need to carefully plan and architect their multicloud solutions to ensure consistent data management, unified security controls, and seamless integration between cloud-hosted and on-premises components.

**Our guidance:**
+ Use each cloud provider's native container management capabilities to maximize business value and accelerate delivery. This approach ensures optimal performance while avoiding the complexity of creating cloud-agnostic solutions that rarely deliver meaningful returns.
+ Develop container strategies that address the complete operational picture, including data management, security, and cross-cloud dependencies. Focus on business outcomes when you make container architecture decisions.
