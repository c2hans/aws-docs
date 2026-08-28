---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/network-policy-disable.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Disable Kubernetes network policies for Amazon EKS Pod network traffic
<a name="network-policy-disable"></a>

Disable Kubernetes network policies to stop restricting Amazon EKS Pod network traffic.

1. List all Kubernetes network policies.

   ```
   kubectl get netpol -A
   ```

1. Delete each Kubernetes network policy. You must delete all network policies before disabling network policies.

   ```
   kubectl delete netpol <policy-name>
   ```

1. Open the aws-node DaemonSet in your editor.

   ```
   kubectl edit daemonset -n kube-system aws-node
   ```

1. Replace the `true` with `false` in the command argument `--enable-network-policy` in the `args:` in the `aws-network-policy-agent` container in the VPC CNI `aws-node` daemonset manifest.

   ```
        - args:
           - --enable-network-policy=false
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
