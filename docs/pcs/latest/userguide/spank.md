---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/spank.html
---

# Extend Slurm functionality on AWS PCS with SPANK plugins
<a name="spank"></a>

Use SPANK (Slurm Plug-in Architecture for Node and job Kontrol) plugins to extend and modify Slurm's behavior during job launch and execution on AWS PCS clusters. SPANK plugins provide a generic interface to intercept and modify job launch stages.

Install SPANK plugins on your compute node AMI and configure them to customize your Slurm cluster's behavior for your workload requirements. For more information about SPANK, see the [SPANK documentation](https://slurm.schedmd.com/spank.html) on the SchedMD website.

**Contents**
+ [Install SPANK plugins on AWS PCS](spank_install.md)
+ [Configure SPANK plugins on AWS PCS](spank_configure.md)
+ [Frequently asked questions about SPANK plugins on AWS PCS](spank_faq.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
