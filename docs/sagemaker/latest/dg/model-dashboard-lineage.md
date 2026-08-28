---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-lineage.html
---

# View a model lineage graph
<a name="model-dashboard-lineage"></a>

When you train a model, Amazon SageMaker AI creates a visualization of your entire ML workflow from data preparation to deployment. This visualization is called a model lineage graph. The following page describes how to view a model lineage graph in the SageMaker AI console.

Model lineage graphs use entities to represent individual steps in your workflow. For example, a basic model lineage graph might have an entity representing your training set, which is associated with an entity representing your training job, which is associated with another entity representing your model. In addition, the graph stores information about each step in your workflow. With this information, you can recreate any step in the workflow or track model and dataset lineage. For example, SageMaker AI Lineage stores the S3 URI of your input data sources with each job so you can perform further analysis of the data sources for compliance verification.

While the model lineage graph can help you view the steps in individual workflows, there are many other capabilities that you can leverage using the AWS SDK. For example, with the AWS SDK you can create or query your entities. For more information about the full set of features in SageMaker AI Lineage and example notebooks, see [Amazon SageMaker ML Lineage Tracking](lineage-tracking.md).

## View a model’s lineage graph
<a name="model-dashboard-lineage-view"></a>

**To view the lineage graph for a model, complete the following steps:**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. Choose **Governance** in the left panel.

1. Choose **Model Dashboard**.

1. In the **Models** section of the Model Dashboard, select the model name of the lineage graph you want to view.

1. Choose **View lineage** in the **Model Overview** section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
