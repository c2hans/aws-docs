---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--start.html
---

# Starting an Amazon OpenSearch Ingestion pipeline
<a name="pipeline--start"></a>

You always start an OpenSearch Ingestion pipeline beginning with a pipeline that's already in the stopped state. The pipeline keeps its configuration settings such as capacity limits, network settings, and log publishing options.

Restarting a pipeline usually takes several minutes.

## Console
<a name="start-pipeline-console"></a>

**To start a pipeline**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines). You'll be on the Pipelines page.

1. Choose a pipeline. You can perform the start operation from this page, or navigate to the details page for the pipeline that you want to start.

1.  For **Actions**, choose **Start pipeline**.

## AWS CLI
<a name="start-pipeline-cli"></a>

To start a pipeline by using the AWS CLI, call the [start-pipeline](https://docs.aws.amazon.com/cli/latest/reference/osis/start-pipeline.html) command with the following parameters:
+ `--pipeline-name` – the name of the pipeline.

**Example**

```
aws osis start-pipeline --pipeline-name {{my-pipeline}}
```

## OpenSearch Ingestion API
<a name="start-pipeline-api"></a>

To start an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the [StartPipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_StartPipeline.html) operation with the following parameter:
+ `PipelineName` – the name of the pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
