---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-slurm-user-management-active-directory.html
---

# Integrate HyperPod clusters with Active Directory
<a name="sagemaker-hyperpod-slurm-user-management-active-directory"></a>

In practical use cases, HyperPod clusters are typically used by multiple users: machine learning (ML) researchers, software engineers, data scientists, and cluster administrators. Instead of statically creating users on each instance, you can use [Lightweight Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) on Wikipedia and LDAP over TLS/SSL (LDAPS) to integrate with a directory service such as [AWS Directory Service for Microsoft Active Directory](https://aws.amazon.com/directoryservice/). For more information, see the blog post [Integrate HyperPod clusters with Active Directory for seamless multi-user login](https://aws.amazon.com/blogs/machine-learning/integrate-hyperpod-clusters-with-active-directory-for-seamless-multi-user-login/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
