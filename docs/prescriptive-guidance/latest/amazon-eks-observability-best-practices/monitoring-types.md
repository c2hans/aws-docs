---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/monitoring-types.html
---

# Types of monitoring in Amazon EKS
<a name="monitoring-types"></a>

Effective observability in Amazon EKS involves infrastructure, application, and security monitoring activities.

## Infrastructure monitoring
<a name="infrastructure"></a>

Infrastructure monitoring is a fundamental component of Amazon EKS observability that provides deep insights into the health and performance of your Kubernetes cluster's foundational elements. At its core, it involves tracking the vital signs of both control plane components and worker nodes, and making sure that the underlying platform remains stable and efficient.
+ **Control plane monitoring** is crucial because it oversees key components such as the API server, etcd database, and scheduler. By monitoring API server latency, you can quickly identify performance bottlenecks that might affect application deployments or scaling operations. Etcd performance monitoring validates that the cluster's state database operates efficiently and prevents data consistency issues that could impact the entire cluster.
+ **Node-level monitoring** is equally critical because it focuses on the compute resources that run your containerized workloads. This includes tracking CPU utilization, memory consumption, disk I/O, and network performance across all worker nodes. Understanding these metrics helps prevent resource exhaustion, optimize node scaling decisions, and ensure appropriate capacity planning.
+ **Network monitoring** plays a vital role in maintaining reliable communication between pods, services, and external resources. By monitoring network throughput, latency, and connection states, you can identify connectivity issues early and ensure smooth application communication. Storage monitoring complements network monitoring by tracking volume performance, capacity utilization, and I/O patterns, to help prevent data-related bottlenecks.

Infrastructure monitoring serves as an early warning system for potential issues, enables proactive maintenance, and ensures optimal resource allocation. Without robust infrastructure monitoring, you risk unexpected downtime, degraded performance, and inefficient resource usage that can significantly impact business operations and costs.

## Application monitoring
<a name="application"></a>

Application monitoring is essential for maintaining healthy, performant, and reliable containerized applications in your Amazon EKS environment. This level of monitoring focuses on the actual workloads that run within your cluster and provides critical insights into how your applications behave, perform, and interact with other services.

Application monitoring includes container-level monitoring, service-level monitoring, and distributed tracing.
+ At the **container level**, application monitoring tracks crucial metrics such as container health status, restart counts, and resource consumption patterns. These metrics help you identify problematic containers that might be consuming excessive resources or experiencing frequent restarts, which could indicate underlying issues such as memory leaks or configuration problems. By monitoring container lifecycle events, you can ensure proper application behavior and quickly troubleshoot deployment issues.
+ **Service-level monitoring** provides visibility into application performance and reliability metrics such as response times, error rates, and request throughput. These metrics are vital for maintaining service-level objectives (SLOs) and ensuring a positive end-user experience. You can track latency across different service endpoints, identify performance bottlenecks, and monitor error patterns to maintain application reliability.
+ **Distributed tracing** is another critical aspect of application monitoring, especially in microservices architectures. By implementing tracing, you can follow requests as they flow through different services, understand dependencies, and identify performance bottlenecks. This end-to-end visibility helps you optimize service interactions and troubleshoot complex issues that span multiple components.

Custom application metrics play a crucial role in providing business-specific insights. These might include metrics such as order processing rates, user login frequencies, or transaction success rates. You can correlate these custom metrics with infrastructure and container metrics to better understand how infrastructure performance affects business operations and to make data-driven decisions for scaling and optimization.

The importance of application monitoring lies in its ability to provide a comprehensive view of application health and performance. This monitoring enables you to maintain high service quality, quickly resolve issues, and continuously optimize your applications to meet business objectives.

## Security monitoring
<a name="security"></a>

Security monitoring in Amazon EKS is a critical activity that helps organizations maintain the integrity, confidentiality, and compliance of their Kubernetes environments. This comprehensive security approach combines continuous surveillance, threat detection, and compliance monitoring to protect containerized workloads from potential security risks and unauthorized access. It includes authentication and authorization monitoring, network security monitoring, and configuration and compliance monitoring.
+ **Authentication and authorization monitoring** forms the first line of defense by tracking all attempts to access the cluster. This includes monitoring API server requests, tracking successful and failed login attempts, and auditing role-based access control (RBAC) changes. By maintaining detailed audit logs of who accessed which resources and when, you can quickly detect potential security breaches, unauthorized access attempts, or privilege escalation activities. This is particularly crucial in multi-tenant environments where maintaining strict access controls is essential.
+ **Network security monitoring** focuses on detecting and preventing unauthorized communication between pods and services. By monitoring network policy violations and unusual traffic patterns, you can identify potential security threats such as container escape attempts or lateral movement within the cluster. This includes tracking both internal cluster communication and external traffic patterns to ensure that containers communicate only with authorized endpoints and follow defined security policies.
+ **Configuration and compliance monitoring** is essential for maintaining security baselines and meeting regulatory requirements. It involves scanning container images continuously for vulnerabilities, monitoring runtime security, and tracking configuration changes that might impact the security posture. Regular compliance audits ensure adherence to industry standards and organizational security policies, and configuration drift detection helps prevent unauthorized changes that could introduce security risks.

Security monitoring in Amazon EKS provides the necessary visibility and control to help protect against modern security threats while ensuring compliance with regulatory requirements. By implementing comprehensive security monitoring, your organization can maintain a strong security posture, respond quickly to security incidents, and demonstrate compliance with various regulatory standards.
