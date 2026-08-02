---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-cluster.html
---

# Custom Slurm settings for AWS PCS clusters
<a name="slurm-custom-settings-cluster"></a>

The following custom Slurm settings are supported at the cluster level:
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageEnforce](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageEnforce)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageTRES](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageTRES)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStoreFlags](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStoreFlags)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_AuthAltParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_AuthAltParameters)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterParameters)
**Note**
For more information on CLI Filters in AWS PCS, see [Configure Slurm CLI Filter Plugins on an AWS PCS cluster](slurm-cli-filter-plugins-configure.md).
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterPlugins](https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterPlugins)
**Note**
For more information on CLI Filters in AWS PCS, see [Configure Slurm CLI Filter Plugins on an AWS PCS cluster](slurm-cli-filter-plugins-configure.md).
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_CommunicationParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_CommunicationParameters)
**Important**
AWS PCS disables the HTTP endpoint by default. To enable it, specify `enable_http`.
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_DefMemPerCPU](https://slurm.schedmd.com/slurm.conf.html#OPT_DefMemPerCPU)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1](https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_EnforcePartLimits](https://slurm.schedmd.com/slurm.conf.html#OPT_EnforcePartLimits)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_FairShareDampeningFactor](https://slurm.schedmd.com/slurm.conf.html#OPT_FairShareDampeningFactor)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_FirstJobId](https://slurm.schedmd.com/slurm.conf.html#OPT_FirstJobId)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckInterval](https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckInterval)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckNodeState](https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckNodeState)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckProgram](https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckProgram)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_JobRequeue](https://slurm.schedmd.com/slurm.conf.html#OPT_JobRequeue)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_LaunchParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_LaunchParameters)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_Licenses](https://slurm.schedmd.com/slurm.conf.html#OPT_Licenses)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_MetricsType](https://slurm.schedmd.com/slurm.conf.html#OPT_MetricsType)
**Note**
For more information on Metrics in AWS PCS, see [Slurm metrics in AWS PCS](slurm-metrics.md).
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_MinJobAge](https://slurm.schedmd.com/slurm.conf.html#OPT_MinJobAge)
**Note**
AWS PCS supports a minimum value of 5 seconds for `MinJobAge`.
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptExemptTime](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptExemptTime)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptParameters)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptType](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptType)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityCalcPeriod](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityCalcPeriod)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityDecayHalfLife](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityDecayHalfLife)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFavorSmall](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFavorSmall)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFlags](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFlags)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityMaxAge](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityMaxAge)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityUsageResetPeriod](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityUsageResetPeriod)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAge](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAge)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAssoc](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAssoc)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightFairshare](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightFairshare)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightJobSize](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightJobSize)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightPartition](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightPartition)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightQOS](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightQOS)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightTRES](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightTRES)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1](https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_PrologFlags](https://slurm.schedmd.com/slurm.conf.html#OPT_PrologFlags)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExit](https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExit)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExitHold](https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExitHold)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_SchedulerParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_SchedulerParameters)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters)
**Note**
AWS PCS supports the `CR_Socket` and `CR_Socket_Memory` values on Slurm version 25.11 and later.
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_SrunPortRange](https://slurm.schedmd.com/slurm.conf.html#OPT_SrunPortRange)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_TaskEpilog](https://slurm.schedmd.com/slurm.conf.html#OPT_TaskEpilog)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_TaskPluginParam](https://slurm.schedmd.com/slurm.conf.html#OPT_TaskPluginParam)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_TaskProlog](https://slurm.schedmd.com/slurm.conf.html#OPT_TaskProlog)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_TrackWCKey](https://slurm.schedmd.com/slurm.conf.html#OPT_TrackWCKey)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepProgram](https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepProgram)
+ [https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepTimeout](https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepTimeout)
