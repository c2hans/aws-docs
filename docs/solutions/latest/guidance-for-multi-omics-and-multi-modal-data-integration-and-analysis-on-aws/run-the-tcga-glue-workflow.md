---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/run-the-tcga-glue-workflow.html
---

# Run the TCGA Glue workflow
<a name="run-the-tcga-glue-workflow"></a>

 This guidance includes an example AWS Glue workflow to process the TCGA data. You can run the workflow using either the AWS Command Line Interface (AWS CLI) or the AWS Glue console.

 To start the workflow using the AWS CLI, run the following command:

```
aws glue start-workflow-run --name TCGAWorkflow
```

 Use the following process to run the crawler in the AWS Glue console.

1.  Sign in to the [AWS Glue console](https://console.aws.amazon.com/glue/home).

1.  Choose **Workflows** from the left navigation menu. On the **Workflows** page, select the name of the example workflow `—TCGAWorkflow`.

1.  Choose **Actions** and select **Run**.
