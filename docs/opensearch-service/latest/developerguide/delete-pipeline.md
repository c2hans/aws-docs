---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/delete-pipeline.html
---

# Deleting Amazon OpenSearch Ingestion pipelines
<a name="delete-pipeline"></a>

You can delete an Amazon OpenSearch Ingestion pipeline using the AWS Management Console, the AWS CLI, or the OpenSearch Ingestion API. You can't delete a pipeline when has a status of `Creating` or `Updating`.

## Console
<a name="delete-pipeline-console"></a>

**To delete a pipeline**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines). You'll be on the Pipelines page.

1. Select the pipeline that you want to delete and choose **Actions**, **Delete**.

1. Confirm deletion and choose **Delete**.

## CLI
<a name="delete-pipeline-cli"></a>

To delete a pipeline using the AWS CLI, send a [delete-pipeline](https://docs.aws.amazon.com/cli/latest/reference/osis/delete-pipeline.html) request:

```
aws osis delete-pipeline --pipeline-name "{{my-pipeline}}"
```

## OpenSearch Ingestion API
<a name="delete-pipeline-api"></a>

To delete an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the [DeletePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_DeletePipeline.html) operation with the following parameter:
+ `PipelineName` – the name of the pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
