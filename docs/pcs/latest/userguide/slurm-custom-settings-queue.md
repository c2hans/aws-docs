---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-queue.html
---

# Custom Slurm settings for AWS PCS queues
<a name="slurm-custom-settings-queue"></a>

The following custom Slurm settings are supported at the queue level:

**Important**
QOS values referenced in `AllowQos`, `DenyQos`, or `QOS` settings must already exist in the Slurm accounting database. Otherwise, Slurm might fail to apply the configuration. For more information about Slurm accounting, see [Slurm accounting in AWS PCS](slurm-accounting.md).
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_AllowAccounts](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowAccounts)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_AllowQoS](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowQoS)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_Default](https://slurm.schedmd.com/slurm.conf.html#OPT_Default)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_DefaultTime](https://slurm.schedmd.com/slurm.conf.html#OPT_DefaultTime)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_DenyAccounts](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyAccounts)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_DenyQoS](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyQoS)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_ExclusiveUser](https://slurm.schedmd.com/slurm.conf.html#OPT_ExclusiveUser)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_GraceTime](https://slurm.schedmd.com/slurm.conf.html#OPT_GraceTime)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_MaxTime](https://slurm.schedmd.com/slurm.conf.html#OPT_MaxTime)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_OverSubscribe](https://slurm.schedmd.com/slurm.conf.html#OPT_OverSubscribe)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PowerDownOnIdle](https://slurm.schedmd.com/slurm.conf.html#OPT_PowerDownOnIdle)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityJobFactor](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityJobFactor)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityTier](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityTier)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_QOS](https://slurm.schedmd.com/slurm.conf.html#OPT_QOS)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_TRESBillingWeights](https://slurm.schedmd.com/slurm.conf.html#OPT_TRESBillingWeights)
