---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-studio-inference.html
---

# Deploying models in Studio

You can deploy models to HyperPod clusters with Amazon EKS orchestration using a single-page form in Amazon SageMaker Studio.

## Deploying a model
<a name="sagemaker-hyperpod-studio-inference-deploy"></a>

The inference form collects all of a deployment's settings on a single page.

To deploy a model, open your cluster in Studio, choose the **Workloads** tab, and open the **Inference** table. Choose **Create**, and complete the following sections of the form. Review the YAML preview, and then choose **Submit**:

**Details**
Enter a name and description for the deployment, and add labels to organize it.

**Namespace**
Select the namespace for the deployment.

**Model source**
Select a JumpStart model, a registered or deployable model, an Amazon S3 path, or an Amazon FSx path.

**Compute**
Select a compute configuration or specify the instance type, GPU, CPU, memory, and EFA manually. For more information, see [Settings](sagemaker-hyperpod-studio-tabs-settings.md).

**Environment**
Enter the container image URI, the entry command, and any environment variables.

**Endpoint**
Specify the SageMaker endpoint that serves the deployed model.

**Configurations**
Add any additional configurations the deployment needs.

## Viewing, searching, and managing deployments
<a name="sagemaker-hyperpod-studio-inference-list"></a>

The **Inference** table lists your model deployments with their status. Search and filter the list to find a deployment, then choose **Actions** on a row.

| Action | What it does |
| --- | --- |
| Refresh | Refreshes the table. |
| Delete | Deletes the deployment. |
| Edit | Changes the number of replicas. |
| Clone | Creates a copy of the deployment configuration. |
| Stop | Stops the deployment. |

## Viewing deployment details
<a name="sagemaker-hyperpod-studio-inference-details"></a>

Choose a deployment name to open its detail page. The page has the following tabs:

**Pods**
Lists the pods. Select a pod to see its **Metrics**, **Activity**, and **Details**.

**Metrics**
Shows embedded metrics for the deployment.

**Activity**
Shows the Kubernetes conditions and events, and CloudWatch Logs.

**Settings**
Shows the runtime configuration, including namespace, compute, environment, storage, governance, and configurations.

**Details**
Shows the name, description, and type.

## Testing a deployment
<a name="sagemaker-hyperpod-studio-inference-test"></a>

Deploying a model creates a SageMaker endpoint with **Models**, **Settings**, and **Playground** tabs. To test the model, open the endpoint and choose the **Playground** tab.
