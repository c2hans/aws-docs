---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/weave.html
---

# Weave GitOps
<a name="weave"></a>

Weave GitOps was developed by Weaveworks, which is the company that introduced the term *GitOps*. This tool provides a comprehensive GitOps solution that builds upon the core GitOps principles.

## GitOps support
<a name="weave-gitops"></a>
+ **Git as the single source of truth**: Weave GitOps uses Git repositories as the authoritative source for defining the desired state of the system. All configurations, including application manifests, infrastructure definitions, and policies, are stored in Git.
+ **Declarative configuration**: The system relies on declarative descriptions of the entire system state. These descriptions are typically Kubernetes manifests, Helm charts, or other declarative formats.
+ **Automated synchronization**: Weave GitOps continuously monitors Git repositories for changes. When it detects changes, it automatically applies them to the target environment.
+ **Kubernetes-native architecture**: Weave GitOps is built as a set of Kubernetes controllers and custom resources. It uses the  extension mechanisms in Kubernetes to provide GitOps capabilities.
+ **Continuous reconciliation**: This tool constantly compares the actual state of the cluster with the desired state that's defined in Git. It automatically corrects any drift detected between these states.
+ **Multi-cluster management**: Weave GitOps supports the management of multiple Kubernetes clusters from a single control plane. It enables consistent application deployment across different environments.
+ **Policy as code**: Weave GitOps incorporates the concept of policy as code for enforcing security and compliance rules. Policies are version-controlled alongside application code and infrastructure definitions.
+ **Progressive delivery**: This tool supports advanced deployment strategies such as canary releases and blue/green deployments. It integrates with Flagger for automated, progressive delivery.
+ **Observability and dashboards**: Weave GitOps provides built-in dashboards for monitoring the state of applications and clusters. It offers insights into reconciliation processes and cluster health.
+ **Secure by design**: The tool implements security best practices, including RBAC integration and secrets management. It supports various authentication methods and integrates with enterprise identity providers.
+ **Extensibility and integration**: The tool is designed to work with a wide range of cloud-native tools. It supports popular tools such as Flux, Helm, and Kustomize.
+ **Self-service developer platforms**: Weave GitOps enables the creation of self-service platforms for developers. It provides templates and guardrails for application deployment.
+ **GitOps automation**: The tool automates many aspects of the GitOps workflow, including pull request generation for updates.
+ **Continuous delivery pipelines**: It integrates with CI/CD systems to create end-to-end delivery pipelines.
+ **Audit and compliance**: Weave DevOps provides a complete audit trail of all changes and actions. It helps you meet compliance requirements through version control and automated processes.
+ **Scalability**: The tool is designed to scale from small projects to large, enterprise-grade deployments.
+ **Team collaboration**: Weave GitOps facilitates collaboration between development and operations teams through Git-based workflows.
+ **GitOps as a service**: This tool offers GitOps as a managed service, which simplifies adoption and management.
+ **Hybrid and multi-cloud support**: Weave GitOps enables consistent management across different cloud providers and on-premises environments.
+ **Continuous security**: The tool integrates security scanning and policy enforcement throughout the deployment process.

Weave GitOps implements these principles to provide a comprehensive GitOps solution that goes beyond basic deployment automation. It aims to create a complete operational model for cloud-native applications that focuses on security, scalability, and ease of use. By adhering to these GitOps principles, Weave GitOps helps organizations achieve consistent, auditable, and efficient management of their Kubernetes environments across multiple clusters and cloud providers.

For more information, see the [Weave GitOps documentation](https://docs.gitops.weaveworks.org/docs/intro-weave-gitops/).

## Architecture
<a name="weave-architecture"></a>

The following diagram illustrates a GitOps-driven CD workflow that uses Weave GitOps within an EKS cluster. For detailed information, see the [Weave GitOps repository](https://github.com/weaveworks/weave-gitops).

![Weave GitOps architecture and workflow on AWS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/images/guide-img/b6f49161-b2c5-42aa-b1d8-b0781836edb7/images/0eff2686-47f4-422e-92d1-4412bdc9af09.png)

where:
+ **Step 1: Pull request (PR) merge**. A developer commits changes to Kubernetes manifests or Helm charts that are stored in a Git repository. When the PR has been reviewed and merged into the main branch, the desired state of the application is updated in source control.
+ **Step 2: Repository sync**. Weave GitOps runs within the Flux namespace in the EKS cluster and continuously monitors the configured Git repository. When it detects changes, it pulls the latest updates to reconcile the declared state.
+ **Step 3: Deployment to target namespace**. Weave GitOps compares the desired state from Git with the live state in the cluster. It then applies the necessary changes to the target workload namespace so that the application is deployed or updated accordingly.
