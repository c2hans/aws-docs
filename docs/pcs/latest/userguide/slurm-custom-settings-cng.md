---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-cng.html
---

# Custom Slurm settings for AWS PCS compute node groups
<a name="slurm-custom-settings-cng"></a>

The following custom Slurm settings are supported at the compute node group level:
+ [CpuSpecList](https://slurm.schedmd.com/slurm.conf.html#OPT_CpuSpecList)
+ [Features](https://slurm.schedmd.com/slurm.conf.html#OPT_Features)
+ [MemSpecLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_MemSpecLimit)
+ [Parameters](https://slurm.schedmd.com/slurm.conf.html#OPT_Parameters)
**Note**
AWS PCS supports `Parameters` on Slurm version 25.11 and later.
+ [RealMemory](https://slurm.schedmd.com/slurm.conf.html#OPT_RealMemory)
+ [Sockets](https://slurm.schedmd.com/slurm.conf.html#OPT_Sockets)
**Note**
AWS PCS supports `Sockets` on Slurm version 25.11 and later.
+ [Weight](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
