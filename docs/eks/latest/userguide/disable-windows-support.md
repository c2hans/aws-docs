---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/disable-windows-support.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disable Windows support
<a name="disable-windows-support"></a>

1. If your cluster contains Amazon Linux nodes and you use [security groups for Pods](security-groups-for-pods.md) with them, then skip this step.

   Remove the `AmazonVPCResourceController` managed IAM policy from your [cluster role](cluster-iam-role.md). Replace {{eksClusterRole}} with the name of your cluster role.

   ```
   aws iam detach-role-policy \
       --role-name eksClusterRole \
       --policy-arn arn:aws:iam::aws:policy/AmazonEKSVPCResourceController
   ```

1. Disable Windows IPAM in the `amazon-vpc-cni` ConfigMap.

   ```
   kubectl patch configmap/amazon-vpc-cni \
                       -n kube-system \
                       --type merge \
                       -p '{"data":{"enable-windows-ipam":"false"}}'
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
