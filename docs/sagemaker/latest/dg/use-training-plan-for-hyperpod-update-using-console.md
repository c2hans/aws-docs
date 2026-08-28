---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-hyperpod-update-using-console.html
---

# Update a SageMaker HyperPod cluster on training plans using the SageMaker AI console
<a name="use-training-plan-for-hyperpod-update-using-console"></a>

You can update, remove, or add a training plan to an existing SageMaker HyperPod cluster using the SageMaker AI console UI. To update the instance group of an SageMaker HyperPod cluster, follow these steps:

1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. In the left navigation pane, choose **Hyperpod**.

1. Navigate to the cluster's details page by following the hyperlink associated with the cluster name.

1. When configuring an instance group, you can update your plan to align with your new compute capacity needs.

![SageMaker AI console interface showing a modal window for updating an instance group within an SageMaker HyperPod cluster. The form includes fields for instance group name, instance type, quantity, instance capacity (with options for on-demand and training plans), and a directory path for on-create lifecycle script.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/training-plans/tp-update-hyperpod-clusters.png)

Review and update your cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
