---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/logging-considerations.html
---

# Important considerations for logging in Amazon EKS
<a name="logging-considerations"></a>

This section discusses important considerations to keep in mind when you implement logging in Amazon EKS.
+ **Performance impact** – Excessive logging can affect application performance. Be mindful of the volume and frequency of logs generated.
+ **Cost management** – Log storage and processing can incur significant costs, especially at scale. Implement log retention policies and consider using log aggregation to reduce costs.
+ **Security and compliance** – Make sure that logs don't contain sensitive information such as passwords or personal data. Implement encryption for logs in transit and at rest. Consider compliance requirements such as General Data Protection Regulation (GDPR) or Health Insurance Portability and Accountability Act (HIPAA) when you handle logs.
+ **Scalability** – Make sure that your logging solution can scale with your cluster size and log volume. Consider using buffering and batching for log transmission.
+ **Log retention** – Define and implement appropriate log retention periods. Balance compliance requirements against storage costs.
+ **Access control** – Implement proper AWS Identity and Access Management (IAM) roles and policies for log access. Follow the [least privilege principle](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) for log management.
+ **Log consistency** – Use consistent log formats across different applications and services. Use structured logging for easier parsing and analysis.
+ **Time synchronization** – Synchronize time across all nodes to get consistent timestamps in logs.
+ **Resource allocation** – Allocate appropriate resources (such as CPU and memory) for logging agents. Monitor the resource usage of logging components.
+ **Fargate considerations** – Fargate has specific logging mechanisms that differ from EC2-based nodes. Understand the limitations and capabilities of [Fargate logging](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html).
+ **Multi-tenant clusters** – In multi-tenant environments, make sure that logs are properly isolated between tenants.
+ **Log parsing and analysis** – Consider the tools and skills required for effective log analysis. Implement log parsing for structured data extraction.
+ **Monitoring the logging system** – Set up monitoring for the logging infrastructure itself. Generate alerts for logging system failures or backlogs.
+ **Network impact** – Be aware of the network bandwidth used by log transmission. Consider using compression for log data.
+ **Kubernetes events** – Don't overlook Kubernetes events as a source of important information.
+ **Control plane logging** – Understand the implications and costs of enabling control plane logging.
+ **Debugging capabilities** – Make sure that your logging solution allows for easy debugging and troubleshooting.
+ **Integration with existing tools** – Consider how your Amazon EKS logging solution integrates with existing monitoring and alerting tools.
+ **Testing** – Regularly test your logging setup, especially after cluster upgrades.
+ **Documentation** – Maintain clear documentation of your logging architecture and practices.
+ **Log aggregation latency** – Be aware of any latency in log aggregation and how it might affect real-time monitoring.
