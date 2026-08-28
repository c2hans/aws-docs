---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/security.html
---

# Security
<a name="security"></a>

 `eksctl` provides some options that can improve the security of your EKS cluster.

## `withOIDC`
<a name="_withoidc"></a>

Enable [`withOIDC`](https://geoffcline.github.io/eksctl-schema-demo/#iam-withOIDC) to automatically create an [IRSA](iamserviceaccounts.md) for the amazon CNI plugin and limit permissions granted to nodes in your cluster, instead granting the necessary permissions only to the CNI service account.

The background is described in [this AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/cni-iam-role.html).

## `disablePodIMDS`
<a name="_disablepodimds"></a>

For managed and unmanaged nodegroups, [`disablePodIMDS`](https://geoffcline.github.io/eksctl-schema-demo/#nodeGroups-disablePodIMDS) option is available prevents all non host networking pods running in this nodegroup from making IMDS requests.

**Note**
This can not be used together with [`withAddonPolicies`](iam-policies.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
