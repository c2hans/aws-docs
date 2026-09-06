---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/best-practices.html
---

# Best practices for choosing a GitOps tool
<a name="best-practices"></a>

This section provides considerations, tips, and best practices for choosing a GitOps tool for your EKS cluster. The right choice depends on your specific context, requirements, and long-term strategy. It's often beneficial to conduct a proof of concept with your top choices before you make a final decision.

Assess your organization's needs and capabilities:
+ Consider your team's current skill set and willingness to learn new tools.
+ Evaluate the complexity of your Amazon EKS environment. (For example, are you using a single cluster or multiple clusters?)
+ Determine your specific requirements for compliance, security, and scalability.

  Best practice: Create a detailed requirements document that outlines required features and useful, but not required, capabilities.

Evaluate tool maturity and adoption:
+ Research the maturity of potential GitOps tools and their adoption rates in the industry.
+ Look for tools that have a proven track record in Amazon EKS environments.

  Best practice: Prioritize tools that have been widely adopted and have a strong presence in the Cloud Native Computing Foundation (CNCF) network.

Consider integration with your existing toolchain:
+ Assess how well the GitOps tool integrates with your current CI/CD pipeline, monitoring solutions and other operational tools.
+ Look for native integrations with AWS services such as IAM, Amazon ECR, and CloudWatch.

  Best practice: Create a proof of concept to test integration capabilities before you make a final decision.

Evaluate security features:
+ Prioritize tools that have robust role-based access control (RBAC) capabilities and integrate well with IAM.
+ Look for features that support secure secrets management and policy enforcement.

  Best practice: Choose a tool that supports GitOps-based security practices, including policy as code and automated compliance checks.

Assess scalability and performance:
+ Consider how the tool performs with large numbers of applications and clusters.
+ Evaluate its impact on cluster performance and resource consumption.

  Best practice: Conduct performance testing with workloads that are similar to your production environment to make sure that the tool can handle your scale.

Consider multi-cluster and multi-environment support:
+ If you have, or plan to have, multiple EKS clusters, prioritize tools that have strong multi-cluster management capabilities.
+ Look for features that support consistent deployments across different environments (such as development, staging, and production).

  Best practice: Choose a tool that allows for centralized management of multiple clusters while maintaining environment-specific configurations.

Evaluate observability and monitoring capabilities:
+ Look for tools that provide clear visibility into the state of your deployments and cluster health.
+ Consider how well the tool integrates with your existing monitoring and logging solutions.

  Best practice: Prioritize tools that offer customizable dashboards and alerting mechanisms for proactive issue detection.

Assess the learning curve and documentation:
+ Evaluate the quality and comprehensiveness of the tool's documentation.
+ Consider the availability of training resources and community support.

  Best practice: Choose a tool that has well-maintained documentation, active community forums, and official training programs or certifications.

Consider cost and resource utilization:
+ Evaluate both the direct costs (such as licensing and support) and indirect costs (such as operational overhead and training costs) of adopting the tool.
+ Assess the tool's efficiency in terms of compute and storage resource consumption.

  Best practice: Perform a total cost of ownership (TCO) analysis that includes both short-term and long-term costs.

Evaluate flexibility and customization options:
+ Look for tools that let you customize workflows to fit your specific needs.
+ Consider the extensibility of the tool through plugins or APIs.

  Best practice: Choose a tool that balances default functionality with the ability to customize for your unique requirements.

Assess continuous delivery and progressive deployment capabilities:
+ Look for tools that support advanced deployment strategies such as canary releases and blue/green deployments.
+ Evaluate the ease of implementing and managing these strategies.

  Best practices: Prioritize tools that offer built-in support for progressive delivery patterns to minimize risk in your deployments.

Consider vendor lock-in and portability:
+ Assess the tool's dependencies on specific cloud providers or technologies.
+ Consider the ease of migrating to a different tool in the future if needed.

  Best practice: Favor tools that use open standards and provide export capabilities for your GitOps configurations.

Evaluate community support and extensions:
+ Look at the size and activity of the user community.
+ Assess the availability of third-party integrations and plugins.

  Best practice: Join community forums or user groups to get firsthand experiences from other users before you make a decision.

Consider compliance and audit requirements:
+ Evaluate how well the tool supports your compliance needs, including audit trails and reporting.
+ Look for features that help maintaining and demonstrate compliance.

  Best practice: Choose a tool that provides comprehensive audit logs and supports the generation of compliance reports.

Assess rollback and disaster recovery capabilities:
+ Evaluate the ease and reliability of rollback mechanisms.
+ Consider how the tool supports disaster recovery scenarios.

  Best practice: Test rollback and recovery processes thoroughly as part of your evaluation.
