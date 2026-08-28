---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/disassociate-oidc-identity-provider.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disassociate an OIDC identity provider from your cluster
<a name="disassociate-oidc-identity-provider"></a>

If you disassociate an OIDC identity provider from your cluster, users included in the provider can no longer access the cluster. However, you can still access the cluster with [IAM principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal).

Disassociating an OIDC identity provider is a cluster update. The cluster enters the `UPDATING` state, and the change can take several minutes to be fully applied to the cluster’s API servers. You can track the progress of the update with the [DescribeUpdate](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html) operation. If your cluster has multiple OIDC identity providers associated, you must disassociate them one at a time. Wait for each cluster update to complete before you disassociate the next provider.

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. In the **OIDC Identity Providers** section, select **Disassociate**, enter the identity provider name, and then select `Disassociate`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
