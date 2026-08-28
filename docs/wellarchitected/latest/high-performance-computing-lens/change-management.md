---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/change-management.html
---

# Change management
<a name="change-management"></a>

| HPCREL02: How do you reliably manage software packages and dependencies across users? |
| --- |
|   |

 HPC workloads often consist of software packages with complex dependencies. Managing software and dependencies, with specific versioning requirements, across many users, can be complex. Consider the following best practices when building out your architecture.

## HPCREL02-BP01 Install software packages in a shared location to simplify multi-user, multi-resource software requirements management
<a name="hpcrel02-bp01"></a>

 Installing software packages on shared storage, such as Amazon Elastic File System (EFS), allows users across compute environments and clusters access the same versioned set of packages. Dependencies can also be installed using a custom AMI, or using a post-install script, such as configured with [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-v3.html).

### Implementation guidance
<a name="implementation-guidance-10"></a>

 Install software in shared location for multi-user or multi-resource environments. Single resource environments can use a custom AMI or separate Amazon Elastic Block Store (Amazon EBS) volume, and multi-resource environments can use shared storage, such as Amazon Elastic File System (Amazon EFS).

## HPCREL02-BP02 Use package managers to simplify software dependency management when possible
<a name="hpcrel02-bp02"></a>

 Managing HPC applications can potentially be simplified with package managers, such as Spack, SBGrid, and EasyBuild. AWS hosts a Spack binary cache for fast installation of commonly used HPC packages and applications. Leveraging a package manager simplifies dependency management for system admins while providing exact versioning per user requirements.

### Implementation guidance
<a name="implementation-guidance-11"></a>

 Consider a package manager to simplify software dependencies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
