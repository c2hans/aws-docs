---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/disassociate-oidc-identity-provider.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disassociate an OIDC identity provider from your cluster
<a name="disassociate-oidc-identity-provider"></a>

If you disassociate an OIDC identity provider from your cluster, users included in the provider can no longer access the cluster. However, you can still access the cluster with [IAM principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal).

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the **OIDC Identity Providers** section, select **Disassociate**, enter the identity provider name, and then select `Disassociate`.
