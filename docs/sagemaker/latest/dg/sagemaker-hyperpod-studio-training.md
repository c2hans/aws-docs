---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-training.html
---

# Submitting training jobs in Studio

You can submit distributed training jobs to HyperPod clusters with Amazon EKS orchestration using a single-page form in Amazon SageMaker Studio, without writing Kubernetes manifests or using the command line. As you complete the form, Studio updates the YAML preview in real time so you can review it before submitting.

The form supports the following task types:
+ `RayJob`: For Ray workloads.
+ `HyperPodPyTorchJob`: Run by the HyperPod training operator.

If you prefer the command line, you can submit the same jobs with the SageMaker HyperPod CLI or with `kubectl`. For more information, see [Running jobs on HyperPod clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-run-jobs.html).

## Submitting a training job
<a name="sagemaker-hyperpod-studio-training-submit"></a>

The training form collects all of a job's settings on a single page.

To submit a training job, open your cluster in Studio, choose the **Workloads** tab, and open the **Training** table. Select a task type from the **Task** filter, and then choose **Create**. Complete the following sections of the form. Review the YAML preview, and then choose **Submit**:

**Details**
Enter a name and description for the job, and add labels to organize it.

**Namespace**
Select the namespace for the job.

**Compute**
Select a compute configuration or specify the instance type, GPU, CPU, memory, and EFA manually. For more information, see [Settings](sagemaker-hyperpod-studio-tabs-settings.md).

**Environment**
Enter the container image URI, the entry command, and any environment variables.

**Storage**
Add Amazon FSx and Amazon S3 mounts for your datasets, training data, and checkpoints.

**Configurations**
Add any additional configurations the job needs.

## Viewing, searching, and managing training jobs
<a name="sagemaker-hyperpod-studio-training-view"></a>

The **Workloads** tab lists your training jobs with their status in the **Training** table. Search and filter the list to find a job, then choose **Actions** on a row.

| Action | What it does |
| --- | --- |
| Refresh | Refreshes the table. |
| Stop | Stops the job. |
| Clone | Creates a copy of the job configuration. |
| Delete | Deletes the job. |

## Viewing training job details
<a name="sagemaker-hyperpod-studio-training-details"></a>

Choose a training job name to open its detail page. The page has the following tabs:

**Pods**
Lists the pods. Select a pod to see its **Metrics**, **Activity**, and **Details**.

**Metrics**
Shows the embedded metrics for the job.

**Activity**
Shows the Kubernetes conditions timeline, CloudWatch events, and CloudWatch Logs.

**Settings**
Shows the runtime configuration, including namespace, compute, environment, storage, governance, and configurations.

**Details**
Shows the name, description, and type.
