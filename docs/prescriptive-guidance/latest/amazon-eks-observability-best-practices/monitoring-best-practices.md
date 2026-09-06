---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/monitoring-best-practices.html
---

# Best practices for monitoring in Amazon EKS
<a name="monitoring-best-practices"></a>

## Strategic implementation approach
<a name="implementation"></a>

A successful Amazon EKS monitoring strategy begins with a well-planned, phased implementation approach.
+ Start by identifying and monitoring critical metrics that directly affect your business operations and application reliability. This foundation should include essential infrastructure metrics, key application performance indicators, and critical security metrics. Gradually expand monitoring coverage based on operational needs and lessons learned, and make sure that each addition provides meaningful value.
+ Implement automated deployment processes by using infrastructure as code (IaC) tools such as Terraform or CloudFormation to ensure consistency and repeatability.
+ Test and validate monitoring systems to help maintain reliability and accuracy.
+ Refine monitoring parameters continuously in alignment with evolving business needs.

## Effective data management
<a name="data-mgmt"></a>

Proper data management is crucial for maintaining an efficient and cost-effective monitoring solution.
+ Implement clear data retention policies that balance historical analysis needs with storage costs.
+ Configure appropriate sampling rates for different metric types: higher frequency for critical metrics and lower frequency for less critical ones.
+ Use metric aggregation to reduce data volume while maintaining meaningful insights, especially for long-term trend analysis.
+ Implement systematic log retention and archival procedures for centralized logging systems (such as CloudWatch Logs) to manage storage costs and maintain access to important data remains accessible.
**Note**
Container-level log rotation is handled automatically by the kubelet in Amazon EKS version 1.21 or later.
+ Consider implementing a hot-warm-cold architecture for log storage to optimize both access speed and cost efficiency.

## Alert configuration and management
<a name="alert-config"></a>

Alert configuration requires careful consideration to maintain effectiveness without causing alert fatigue.
+ Define clear, actionable thresholds based on service level objectives (SLOs) and historical performance patterns.
+ Implement a tiered alert severity system that clearly differentiates between critical issues that require immediate attention and less urgent matters.
+ Make sure that alerts provide sufficient context and actionable information to facilitate quick problem resolution.
+ Establish clear escalation procedures with defined ownership and response times for different alert severities.
+ Review and refine alert configurations regularly to help maintain their relevance and effectiveness.

## Resource optimization
<a name="resource"></a>

Continuous monitoring of resource utilization is essential for maintaining cost-effective operations.
+ Implement comprehensive resource monitoring across all cluster components, including nodes, pods, and persistent volumes.
+ Configure automatic scaling based on actual usage patterns and performance requirements to ensure efficient resource utilization while maintaining performance.
+ Use cost allocation tags to track resource consumption by different teams, applications, or environments.
+ Regularly analyze resource efficiency metrics to identify optimization opportunities and implement improvements.
+ Consider implementing cost management tools to track and optimize cloud spending.

## Security
<a name="security"></a>

Security considerations should be integral to your monitoring strategy.
+ Implement [least privilege access principles](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) for all monitoring components to ensure that users and services have only the permissions they need.
+ Enable comprehensive audit logging to track all access and changes to monitoring systems.
+ Conduct regular security reviews of monitoring configurations and access patterns to identify potential vulnerabilities.
+ Implement encryption for sensitive monitoring data both in transit and at rest.
+ Integrate security monitoring with existing security information and event management (SIEM) systems for comprehensive security visibility.
