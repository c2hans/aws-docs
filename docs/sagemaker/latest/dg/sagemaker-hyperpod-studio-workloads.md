---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-workloads.html
---

# Workloads

The **Workloads** tab shows the training jobs and model deployments running on your cluster. To view it, in Studio choose **HyperPod** in the navigation pane, select your cluster, and choose the **Workloads** tab. If you are having any issues with viewing tasks, see [Troubleshooting](sagemaker-hyperpod-studio-troubleshoot.md).

The tables include:

------
#### [ For Slurm clusters ]

For Slurm clusters, the tasks currently in the Slurm job scheduler queue are shown in the table. The information shown for each task includes the task name, status, job ID, partition, run time, nodes, created by, and actions.

For a list and details about past jobs, use the [`sacct`](https://slurm.schedmd.com/sacct.html) command from the Slurm documentation in JupyterLab or a Code Editor terminal. The sacct command shows historical information about jobs that have finished or are complete in the system. It provides accounting information, including job resource usage like memory and exit status.

By default, all Studio users can view, manage, and interact with all available Slurm tasks. To restrict the viewable tasks to Studio users, see [Restrict task view in Studio for Slurm clusters](sagemaker-hyperpod-studio-setup-slurm.md#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view).

------
#### [ For Amazon EKS clusters ]

For Amazon EKS clusters, the table shows `PyTorchJob` (Kubeflow), `HyperPodPyTorchJob`, `MPIJob`, `TFJob`, `RayCluster`, `RayJob`, and `RayCronJob` tasks. You can filter by task type under **Task type**. The information shown for each task includes the task name, status, namespace, priority class, and creation time.

By default, all users can view jobs across all namespaces. To restrict the viewable Kubernetes namespaces available to Studio users, see [Restrict task view in Studio for EKS clusters](sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view). If a user cannot view tasks and is asked to provide a namespace, they need to get that information from their administrator.

For Amazon EKS clusters, you can also submit and manage training jobs and model deployments from Studio. For more information, see [Submitting training jobs in Studio](sagemaker-hyperpod-studio-training.md) and [Deploying models in Studio](sagemaker-hyperpod-studio-inference.md).

------

**Topics**
+ [Submitting training jobs in Studio](sagemaker-hyperpod-studio-training.md)
+ [Deploying models in Studio](sagemaker-hyperpod-studio-inference.md)
+ [Resource ownership](sagemaker-hyperpod-studio-resource-ownership.md)
