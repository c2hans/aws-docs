---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/rancher-fleet.html
---

# Rancher Fleet
<a name="rancher-fleet"></a>

Rancher Fleet is a GitOps-at-scale solution that is designed specifically for managing multiple Kubernetes clusters. It adheres closely to GitOps principles while focusing on scalability and multi-cluster management.

## GitOps support
<a name="rancher-fleet-gitops"></a>
+ **Git as the single source of truth**: Fleet uses Git repositories as the authoritative source for defining the desired state of applications and resources across multiple clusters. All configurations, including Kubernetes manifests, Helm charts, and custom resources, are stored in Git.
+ **Declarative configuration**: Fleet works with declarative descriptions of the desired state for applications and resources. These can be raw Kubernetes YAML, Helm charts, Kustomize files, or Fleet-specific custom resources.
+ **Automated synchronization**: Fleet continuously monitors Git repositories for changes. It automatically applies changes to the target clusters when it detects differences between the Git state and the cluster state.
+ **Multi-cluster management**: Fleet is designed specifically to manage deployments across multiple Kubernetes clusters. It can handle thousands of clusters from a single control plane.
+ **Kubernetes-native architecture**: Fleet is built as a set of Kubernetes custom resources and controllers. It uses the extension mechanisms in Kubernetes for GitOps operations.
+ **Continuous reconciliation**: Fleet constantly compares the actual state of clusters with the desired state that's defined in Git. It automatically corrects any drift detected between these states.
+ **Cluster grouping and targeting**: Fleet enables you to group clusters and target deployments to specific groups or individual clusters. It supports consistent application deployment across different environments and cluster types.
+ **Layered configurations**: Fleet supports layered configurations, which provide base configurations with environment-specific overlays. This aligns with GitOps practices of managing multiple environments efficiently.
+ **Helm integration**: Fleet provides native support for Helm charts and provides easy management of complex applications. It can version and manage Helm releases through GitOps workflows.
+ **Custom resource definitions (CRDs)**: Fleet uses custom resources such as GitRepo and Bundle to define deployments. These CRDs provide a Kubernetes-native way to define GitOps workflows.
+ **Security and RBAC**: Fleet integrates with Kubernetes RBAC for access control. It supports secure management of sensitive information and credentials.
+ **Observability**: Fleet provides status information about the synchronization state of clusters and applications. It offers insights into GitOps processes across the fleet of clusters.
+ **Scalability**: Fleet is designed to scale to manage thousands of clusters efficiently. It supports large-scale GitOps operations in enterprise environments.
+ **Dependency management**: You can define dependencies between different resources and applications. Fleet ensures that the correct order of operations is followed in complex deployments.
+ **Customization and extensibility**: Fleet supports custom scripts and lifecycle hooks for advanced customization of deployments. It allows for integration with existing tools and workflows.
+ **Offline and air-gapped support**: Fleet can operate in environments that have limited or no internet connectivity. It supports GitOps workflows in high-security or regulated environments.
+ **Progressive rollouts**: Fleet supports staged rollouts across clusters, which allow for controlled and gradual deployment strategies.
+ **Unified management interface**: Fleet provides a single interface for managing GitOps workflows across all clusters. It simplifies operations in complex, multi-cluster environments.
+ **Integration with other Rancher tools**: Fleet integrates with other Rancher tools to provide a comprehensive Kubernetes management solution.
+ **Audit trail and compliance**: Fleet maintains a clear audit trail of all changes and deployments. It helps you meet compliance requirements through version-controlled, Git-based operations.

Rancher Fleet implements these GitOps principles with a strong focus on scalability and multi-cluster management. Its design is particularly suited for organizations that manage large numbers of Kubernetes clusters across different environments, data centers, or cloud providers.

The key differentiator of Fleet is its ability to handle GitOps at scale. This feature makes it especially valuable for large enterprises or managed service providers that manage numerous clusters. Tools such as Argo CD or Flux are often used for individual cluster management, whereas Fleet is designed to manage GitOps across a large fleet of clusters.

By adhering to these GitOps principles, Rancher Fleet provides a solution for organizations that want to implement consistent, scalable, and automated management of applications and resources across a diverse and large-scale Kubernetes environment.

For more information, see the [Fleet documentation](https://fleet.rancher.io/).

## Architecture
<a name="rancher-fleet-architecture"></a>

For architecture and workflow information, see the [Fleet repository](https://github.com/rancher/fleet).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
