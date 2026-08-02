---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/use-cases.html
---

# Argo CD and Flux use cases
<a name="use-cases"></a>

This section focuses on two tools, Argo CD and Flux, which provide pure GitOps functionality. In this context, *pure GitOps* refers to a model where a Git repository serves as the single source of truth for the desired state of applications and infrastructure. All changes are made through Git commits, and the system automatically synchronizes the live environment to match the state that's defined in the repository. No manual intervention is required outside of Git operations.

## General considerations
<a name="considerations"></a>
+ You might prefer to use Argo CD in environments where visual management and application-centric workflows are important.
+ You might choose Flux if you require lighter-weight solutions, strong multi-tenancy, or deep integration with the broader Cloud Native Computing Foundations (CNCF) network.
+ Argo CD often appeals to teams that are transitioning from traditional CI/CD to GitOps because of its intuitive UI.
+ Flux is often favored in cloud-native environments where CLI-based workflows and IaC practices are already established.

Ultimately, the choice between Argo CD and Flux often depends on your specific organizational needs, existing tooling, and team preferences. Both tools are capable of handling most GitOps scenarios, so we recommend that you evaluate them based on your specific use cases and requirements.

## Argo CD use cases
<a name="argo-cd-use-cases"></a>

Visual management:
+ When you need a user-friendly UI to manage deployments and visualize application states.
+ For teams that prefer a graphical interface for monitoring and troubleshooting.

Application-centric approach:
+ When you want to manage deployments at the application level instead of managing individual resources.
+ For organizations that structure their deployments around application concepts.

Multi-cluster management:
+ When managing deployments across multiple clusters is a primary requirement.
+ For complex, distributed environments with many clusters.

Rollback and sync waves:
+ When you need fine-grained control over the deployment process, including sync waves and manual interventions.
+ For scenarios that require complex rollback strategies.

Integration with existing tools:
+ When you're already using other tools in the Argo project such as Argo Workflows and Argo Events.

Enterprise environments:
+ For large enterprises that need robust RBAC and single sign-on integration by default.

## Flux use cases
<a name="flux-use-cases"></a>

Lightweight deployments:
+ When you need a more lightweight, less resource-intensive GitOps solution.
+ For edge computing or IoT scenarios where resources might be constrained.

Automated image updates:
+ When automatic detection and deployment of new container images is a key requirement.
+ For teams that focus on continuous deployment with frequent image updates.

Multi-tenancy:
+ When strong multi-tenancy support is needed, especially in shared cluster environments.
+ For service providers or large organizations that have strict separations between teams or projects.

IaC:
+ When managing both applications and infrastructure through the same GitOps workflow is important.
+ For teams that are heavily invested in the IaC paradigm.

Helm integration:
+ When extensive use of Helm charts is part of your deployment strategy.
+ For environments that have complex Helm-based deployments.

CNCF project integration:
+ When tight integration with other CNCF projects is important.
+ For organizations that align with CNCF technologies and principles.

Modular architecture:
+ When you need flexibility to use only specific components of the GitOps toolkit.
+ For teams that want to build custom GitOps workflows by using modular components.

Progressive delivery:
+ When advanced deployment strategies such as canary releases or A/B testing are core requirements.

## Feature comparison
<a name="argo-flux-comparison"></a>

|
|
| Area | Argo CD | Flux |
| --- |--- |--- |
| Support for core GitOps principles | Yes | Yes |
| Architecture | End-to-end application for implementing Kubernetes GitOps workflows | Provides Kubernetes CRDs and controllers for GitOps |
| Setup | Simple | Complex |
| Helm support | Yes | Yes |
| Kustomize support | Yes | Yes |
| Integrated GUI | CLI and fully-featured web UI | CLI and optional lightweight web interface |
| RBAC support | Granular control | Kubernetes native RBAC |
| Multi-tenancy and multi-cluster support | Excellent support for multi-cluster | Excellent support for multi-tenancy |
| Single sign-on authentication | Yes | Yes |
| Sync automation | Ability to sync windows | Ability to set reconcillation intervals |
| Partial sync | Yes | No |
| Reconciliation process | Supports manual and automatic syncs. Several different strategies are available. | Supports manual and automatic syncs. |
| Extentensibility | Supports custom lugins. Limited customization options. | Supports custom controller. Good extensibility and third-party integrations. |
| Cummunity support | Large and active community. | Smaller but growing community. |
| Scalability | Good scalability, but limited by the web UI's data-fetching rate. Community analysis suggests support for tens of thousands of applications. | Clear guides for horizontal and vertical scalability, up to tens of thousands of applications. |
