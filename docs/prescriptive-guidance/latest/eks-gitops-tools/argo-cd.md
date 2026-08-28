---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/argo-cd.html
---

# Argo CD
<a name="argo-cd"></a>

Argo CD is a widely used GitOps continuous delivery (CD) tool for Kubernetes that complies with several key GitOps principles.

## GitOps support
<a name="argo-cd-gitops"></a>
+ **Declarative configuration**: Argo CD uses declarative configurations that are stored in Git repositories. The desired state of the application and infrastructure is defined in YAML files. These configurations describe what should be deployed, not how to deploy them.
+ **Version control system as the single source of truth**: Git repositories serve as the single source of truth for the entire system. All changes to the application and infrastructure are made through Git. This ensures a complete audit trail and the ability to roll back to any previous state.
+ **Automated synchronization**: Argo CD continuously monitors the Git repository for changes. When changes are detected, it automatically synchronizes the actual state of the cluster with the desired state that's defined in Git. This ensures that the cluster always reflects the state that's described in the repository.
+ **Kubernetes-native**: Argo CD is designed specifically for Kubernetes environments. It leverages the declarative nature and custom resources in Kubernetes for managing applications.
+ **Self-healing and drift detection**: Argo CD regularly compares the live state of the cluster with the desired state in Git. If it detects any drift (differences between the actual and desired states), it can automatically correct these discrepancies.
+ **Multi-cluster and multi-tenancy support**: Argo CD can manage multiple Kubernetes clusters from a single instance. It supports multi-tenancy, so different teams can manage their applications independently.
+ **Application definition**: Applications in Argo CD are defined by using the Application CRD (custom resource definition). This allows for a Kubernetes-native way of defining what should be deployed and how.
+ **Separation of deployment and release**: Argo CD separates the deployment of code from its release to users. This is achieved through various deployment strategies such as blue/green or canary deployments.
+ **Observability and auditability**: Argo CD provides a web UI and CLI for observing the state of applications and clusters. All actions are logged to provide a clear audit trail of changes and deployments.
+ **Security and RBAC**: Argo CD integrates with Kubernetes role-based access control (RBAC). It supports single sign-on integration for authentication and authorization.
+ **Pluggable architecture**: Argo CD supports various source control management systems, Helm charts, Kustomize, and other Kubernetes manifest formats. This flexibility allows it to fit into diverse environments and workflows.
+ **Continuous delivery (CD)**: Although Argo CD focuses on continuous delivery, it can be integrated with continuous integration (CI) tools to create a complete CI/CD pipeline.

By adhering to these GitOps principles, Argo CD provides a robust, scalable, and secure way to manage Kubernetes deployments. It ensures that the operational state of your system is always in sync with the desired state that's defined in your Git repository, and promotes consistency, reliability, and ease of management in complex Kubernetes environments.

For scenarios and requirements that Argo CD can address, see [Argo CD use cases](use-cases.md#argo-cd-use-cases) later in this guide. For a comparison between Argo CD and Flux, see [Feature comparison](use-cases.md#argo-flux-comparison) later in this guide.

For additional information, see the [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/).

## Architecture
<a name="argo-cd-architecture"></a>

The following diagram illustrates a GitOps-driven CD workflow that uses Argo CD within an EKS cluster. For detailed information, see the [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/).

![Argo CD architecture and workflow on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/images/guide-img/b6f49161-b2c5-42aa-b1d8-b0781836edb7/images/27c10271-89d8-4143-ab7b-52249b327e42.png)

where:
+ **Step 1: Pull request (PR) merge**. A developer commits changes to Kubernetes manifests or Helm charts that are stored in a Git repository. When the PR has been reviewed and merged into the main branch, the desired state of the application is updated in source control.
+ **Step 2: Repository sync**. Argo CD runs within a dedicated namespace (`argocd`) in the EKS cluster and continuously monitors the configured Git repository. When it detects changes, it pulls the latest updates to reconcile the declared state.
+ **Step 3: Deployment to target namespace**. Argo CD compares the desired state from Git with the live state in the cluster. It then applies the necessary changes to the target workload namespace so that the application is deployed or updated accordingly. This includes managing Kubernetes resources such as deployments, services, ConfigMaps, and secrets to maintain cluster consistency with the Git source of truth.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
