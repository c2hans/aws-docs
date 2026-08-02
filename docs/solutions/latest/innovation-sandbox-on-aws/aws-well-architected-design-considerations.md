---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

We architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) to benefit this solution.

The Innovation Sandbox on AWS solution implements operational excellence through:
+  **Automated operations**
  + Automates sandbox environment setup, configuration, and infrastructure deployment.
  + Deploys standardized policies and guardrails across accounts.
  + Reduces manual intervention in account lifecycle management.
+  **Event response**
  + Implements automated responses to budget thresholds.
  + Provides a Cloudwatch Application Insights dashboard for monitoring and alerts.
  + Enables quick identification and resolution of issues, using predefined CloudWatch Log Insight queries and X-Ray traces.
+  **Standard definitions**
  + Creates consistent Organizational Unit (OU) structure across implementations.
  + Establishes standardized security policies.
  + Maintains uniform budget control mechanisms.

## Security
<a name="security"></a>

We architected this solution using principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) to benefit this solution.

The solution implements comprehensive security controls:
+  **Identity and access management**
  + Integrates with AWS IAM Identity Center for centralized access control.
  + Automatically implements least privilege permissions.
  + Enforces role-based access across sandbox accounts.
+  **Network security**
  + Isolates sandbox environments from production systems.
  + Restricts access to internal networks.
  + Controls network traffic through automated WAF policies.
+  **Data protection**
  + Prevents access to sensitive corporate resources.
  + Implements service control policies for data protection.
  + Maintains isolation between sandbox environments.

## Reliability
<a name="reliability"></a>

We architected this solution using principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to benefit this solution.

The solution ensures reliability through:
+  **Distributed design**
  + Implements multi-account architecture.
  + Uses AWS Organizations for management.
  + Maintains separation of concerns across accounts.
+  **Automated recovery**
  + Implements automated resource management.
  + Enables account recycling and clean-up.
  + Provides consistent environment configuration.
+  **Change management**
  + Automates policy deployment.
  + Maintains consistent controls across accounts.
  + Enables standardized environment updates.

## Performance efficiency
<a name="performance-efficiency"></a>

We architected this solution using principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) to benefit this solution.

The solution maintains performance efficiency by:
+  **Resource selection**
  + Allows administrators to specify approved services and Regions.
  + Enables right-sizing of resources for sandbox environments.
  + Provides flexibility in resource configuration.
+  **Automated environment provisioning**
  + Blueprint deployment automates infrastructure setup for sandbox accounts.
  + Allows users to get started with pre-configured resources.
+  **Monitoring**
  + Creates a centralized CloudWatch Application Insights dashboard.
  + Tracks resource utilization across accounts.
  + Enables performance optimization through metrics.

## Cost optimization
<a name="cost-optimization"></a>

We architected this solution using principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) to benefit this solution.

The solution optimizes costs through multiple mechanisms:
+  **Resource management**
  + Automatically manage accounts (clean-up or freeze) when budget thresholds are reached.
  + Freeze: Prevents creation of new resources at budget limits.
  + Clean-up: Enables account recycling to optimize usage.
+  **Cost controls**
  + Implements multi-tier budget threshold monitoring.
  + Provides visibility into spending across accounts.
  + Reduces monthly cost overruns through automated controls.

**Note**
Identification of cost/budget overrun per account is best effort due to Cost Explorer service limitation.
+  **Resource lifecycle**
  + Manages resource termination based on budget limits and/or lease duration.
  + Enables account reuse through automated clean-up.
  + Optimizes account utilization through recycling.

## Sustainability
<a name="sustainability"></a>

We architected this solution using principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) to benefit this solution.
+ The solution uses managed and serverless services where possible to minimize the environmental impact.
