---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/flux.html
---

# Flux
<a name="flux"></a>

Flux is another tool for Kubernetes that implements GitOps principles in a unique way.

## GitOps support
<a name="flux-gitops"></a>
+ **Git as the single source of truth**: Flux uses Git repositories as the definitive source for defining the desired state of the system. All configuration for applications and infrastructure is stored in Git.
+ **Declarative configuration**: Flux works with declarative descriptions of the desired state of your cluster. These descriptions are typically Kubernetes manifests, Helm charts, or Kustomize overlays.
+ **Automated aynchronization**: Flux continuously monitors the Git repository for changes. When it detects changes, it automatically applies them to the cluster.
+ **Kubernetes-native**: Flux is built as a set of Kubernetes controllers and custom resources. It uses the extension mechanisms in Kubernetes to provide GitOps capabilities.
+ **Pull-based deployment model**: Unlike traditional push-based CI/CD systems, Flux uses a pull-based model. The cluster pulls the desired state from Git instead of using an external system to push changes.
+ **Continuous reconciliation**: Flux constantly compares the actual state of the cluster with the desired state in Git. It automatically corrects any drift that's detected between these states.
+ **Multi-tenancy**: Flux supports multi-tenancy through its concepts of *Kustomizations* and *HelmReleases*. Different teams can manage their own parts of the configuration independently.
+ **Progressive delivery**: Flux supports advanced deployment strategies, such as canary releases and A/B testing, through its Flagger component.
+ **Helm integration**: Flux includes native support for Helm, so you can easily manage Helm releases through GitOps.
+ **Image update automation**: Flux can automatically update container images in Git when new versions are available in the container registry.
+ **Kustomize support**: You can use the native support provided by Flux for Kustomize to customize and patch Kubernetes manifests.
+ **Security and RBAC**: Flux integrates with Kubernetes RBAC for access control. It supports secrets management through various backends.
+ **Observability**: Flux provides status information and metrics about reconciliation and operations. It integrates with monitoring tools for enhanced observability.
+ **Event-driven architecture**: Flux uses an event-driven approach to implement reconciliations and updates.
+ **Extensibility**: The tool is designed to be extensible, so you can add custom controllers and resources.
+ **Cross-cluster synchronization**: Flux supports the management of multiple clusters from a single set of repositories.
+ **Dependency management**: It allows for defining dependencies between different parts of your system and ensures the correct order of operations.
+ **Webhook receivers**: You can configure Flux to receive webhooks from Git providers or other systems to start immediate reconciliation.

By implementing these GitOps principles, Flux provides a robust and flexible system for managing Kubernetes clusters and applications. It ensures that your infrastructure and applications are always in sync with your Git repositories, and provides consistency, reliability, and ease of management in complex Kubernetes environments. The tool's Kubernetes-native approach and focus on automation make it particularly well-suited for cloud-native environments.

For scenarios and requirements that Flux can address, see [Flux use cases](use-cases.md#flux-use-cases) later in this guide. For a comparison between Argo CD and Flux, see [Feature comparison](use-cases.md#argo-flux-comparison) later in this guide.

For additional information, see the [Flux documentation](https://fluxcd.io/flux/).

## Architecture
<a name="flux-architecture"></a>

The following diagram illustrates a GitOps-driven CD workflow that uses Flux within an EKS cluster. For detailed information, see the [Flux documentation](https://fluxcd.io/flux/).

![Flux architecture and workflow on AWS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/images/guide-img/b6f49161-b2c5-42aa-b1d8-b0781836edb7/images/e8e3bf71-f2ff-4e6e-945d-789011201868.png)

where:
+ **Step 1: Pull request (PR) merge**. A developer commits changes to Kubernetes manifests or Helm charts that are stored in a Git repository. When the PR has been reviewed and merged into the main branch, the desired state of the application is updated in source control.
+ **Step 2: Repository sync**. Flux runs within a dedicated namespace in the EKS cluster and continuously monitors the configured Git repository. When it detects changes, it pulls the latest updates to reconcile the declared state.
+ **Step 3: Deployment to target namespace**. Flux compares the desired state from Git with the live state in the cluster. It then applies the necessary changes to the target workload namespace so that the application is deployed or updated accordingly.
