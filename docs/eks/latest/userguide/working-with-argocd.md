---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/working-with-argocd.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with Argo CD
<a name="working-with-argocd"></a>

With Argo CD, you define applications in Git repositories and Argo CD automatically syncs them to your Kubernetes clusters. This enables declarative, version-controlled application deployment with automated drift detection.

## Prerequisites
<a name="_prerequisites"></a>

Before working with Argo CD, you need:
+ An EKS cluster with the Argo CD capability created (see [Create an Argo CD capability](create-argocd-capability.md))
+ A Git repository containing Kubernetes manifests
+  `kubectl` configured to communicate with your cluster

## Common tasks
<a name="_common_tasks"></a>

The following topics guide you through common Argo CD tasks:

 ** [Configure repository access](argocd-configure-repositories.md) ** - Configure Argo CD to access your Git repositories using AWS Secrets Manager, AWS CodeConnections, or Kubernetes Secrets.

 ** [Register target clusters](argocd-register-clusters.md) ** - Register target clusters where Argo CD will deploy applications.

 ** [Working with Argo CD Projects](argocd-projects.md) ** - Organize applications and enforce security boundaries using Projects for multi-tenant environments.

 ** [Configure Argo CD settings](argocd-configure-settings.md) ** - Configure Argo CD behavior using the `argocd-cm` ConfigMap, including custom health checks for Custom Resources.

 ** [Create Applications](argocd-create-application.md) ** - Create Applications that deploy from Git repositories with automated or manual sync policies.

 ** [Use ApplicationSets](argocd-applicationsets.md) ** - Use ApplicationSets to deploy applications across multiple environments or clusters using templates and generators.

## Access the Argo CD UI
<a name="_access_the_argo_cd_ui"></a>

Access the Argo CD UI through the EKS console:

1. Open the Amazon EKS console

1. Select your cluster

1. Choose the **Capabilities** tab

1. Choose **Argo CD**

1. Choose **Open Argo CD UI**

The UI provides visual application topology, sync status and history, resource health and events, manual sync controls, and application management.

## Upstream documentation
<a name="_upstream_documentation"></a>

For detailed information about Argo CD features:
+  [Argo CD Documentation](https://argo-cd.readthedocs.io/) - Complete user guide
+  [Application Spec](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/) - Full Application API reference
+  [ApplicationSet Guide](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/) - ApplicationSet patterns and examples
+  [Argo CD GitHub](https://github.com/argoproj/argo-cd) - Source code and examples
