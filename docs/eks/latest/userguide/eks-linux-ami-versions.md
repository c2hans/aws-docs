---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve Amazon Linux AMI version information
<a name="eks-linux-ami-versions"></a>

Amazon EKS optimized Amazon Linux AMIs are versioned by Kubernetes version and the release date of the AMI in the following format:

```
k8s_major_version.k8s_minor_version.k8s_patch_version-release_date
```

Each AMI release includes various versions of [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/), the Linux kernel, and [containerd](https://containerd.io/). The accelerated AMIs also include various versions of the NVIDIA driver. You can find this version information in the [Releases](https://github.com/awslabs/amazon-eks-ami/releases) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
