---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/pulumi.html
---

# Pulumi
<a name="pulumi"></a>

Pulumi is an IaC platform that isn't exclusively designed for GitOps. However, it can be used effectively to implement GitOps principles, especially for cloud infrastructure and Kubernetes deployments.

## GitOps support
<a name="pulumi-gitops"></a>
+ **IaC**: Pulumi lets you define your infrastructure by using general-purpose programming languages such as Python, TypeScript, and Go. This code-based approach aligns with the GitOps emphasis on versioned, declarative configurations.
+ **Git as the single source of truth**: Infrastructure code in Pulumi can be stored and version-controlled in Git repositories. This ensures that Git serves as the single source of truth for infrastructure definitions.
+ **Declarative desired state**: Although Pulumi uses programming languages, it still describes the desired state of infrastructure declaratively. The code defines what the infrastructure should look like, not the step-by-step process to create it.
+ **Automated synchronization**: Pulumi can be integrated with CI/CD pipelines to automatically apply changes when code is updated in Git. This enables continuous deployment of infrastructure changes, which is a key GitOps principle.
+ **Multi-cloud and Kubernetes support**: Pulumi supports a wide range of cloud providers and Kubernetes, so you can follow GitOps practices across diverse environments. The tool enables consistent management of resources across different platforms.
+ **State management**: Pulumi manages the state of infrastructure, which can be stored remotely and securely. This state management is crucial for GitOps practices, and ensures consistency between the defined state and the actual state of your infrastructure.
+ **Drift detection and reconciliation**: Pulumi can detect differences between the desired state (in code) and the actual state of infrastructure. It reconciles these differences in alignment with the GitOps principle for continuous reconciliation.
+ **Policy as code**: You can define and enforce policies as code by using Pulumi CrossGuard. This enables version-controlled, GitOps-style management of compliance and security policies.
+ **Secrets management**: Pulumi provides secure ways to manage sensitive information within infrastructure code. It supports integration with external secrets management systems, which is crucial for GitOps security practices.
+ **Modular and reusable components**: Pulumi supports the creation of reusable components and modules. This modularity aligns with GitOps practices for managing complex, multi-environment deployments.
+ **Preview and plan**: Pulumi offers the ability to preview changes before applying them. This supports the GitOps principle of safe, predictable changes to infrastructure.
+ **Rollbacks and history**: Pulumi maintains a history of deployments and supports rollbacks to previous states. This aligns with GitOps principles of traceability and reversibility.
+ **Continuous delivery for infrastructure**: Pulumi can be integrated into CI/CD pipelines for continuous delivery of infrastructure changes. It supports automated testing and validation of infrastructure code.
+ **RBAC and access control**: Pulumi provides role-based access control for managing who can make changes to infrastructure. This supports GitOps security and governance practices.
+ **Observability and logging**: Pulumi offers logging and monitoring capabilities for infrastructure changes. These capabilities support the observability aspect of GitOps practices.
+ **Integration with other tools**: Pulumi can integrate with various tools in the cloud. This flexibility allows for comprehensive GitOps workflows.
+ **Environment management**: Pulumi supports the management of multiple environments (development, staging, production) by using the same codebase with different configurations. This aligns with GitOps practices for consistent multi-environment management.
+ **Dependency management**: Pulumi handles dependencies between resources, and ensures the correct order of operations. This is crucial for complex GitOps deployments that involve interdependent components.
+ **Custom resource providers**: Pulumi lets you create custom providers to manage any API-driven service. This extends GitOps practices to a wide range of resources beyond standard cloud offerings.
+ **Collaboration features**: Pulumi supports team collaboration through shared state and access controls. This facilitates GitOps workflows in team environments.

By using these Pulumi features, organizations can implement GitOps practices for their infrastructure, especially in scenarios where they need fine-grained control or complex logic, or want to manage a diverse set of cloud and on-premises resources within a single, consistent framework.

Pulumi's approach to GitOps is unique because it brings the power and flexibility of general-purpose programming languages to infrastructure management while adhering to GitOps principles. This can be particularly advantageous for teams that prefer to work with familiar programming languages and want to apply software engineering best practices to infrastructure management.

The key differentiator of Pulumi in GitOps is its use of standard programming languages to define infrastructure. Traditional GitOps tools often use YAML or domain-specific languages, whereas Pulumi allows for more complex logic, better code reuse, and easier integration with existing development workflows.

For more information, see the [Pulumi documentation](https://www.pulumi.com/docs/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
