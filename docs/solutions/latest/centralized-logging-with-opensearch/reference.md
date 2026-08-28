---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting anonymized metrics for this solution and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each Centralized Logging with OpenSearch deployment
+  **Timestamp** - Data-collection timestamp
+  **Version** - Solution version deployed
+  **Data** - Data includes Region where the solution stack is deployed, request type (whether the stack was created, updated, or deleted), template type used, log pipeline parameters, log pipeline alarm parameters, and OpenSearch version and size.

Examples of collected data by type:

Stack Deployment Data

```
{ "Region": "us-east-1", "RequestType": "Create", "Template": "CentralizedLogging" }
```

Pipeline Management Data

```
{ "metricType": "PIPELINE_MANAGEMENT", "isCrossAccountIngestion": false, "sourceType": "RDS", "engineType": "OpenSearch", "logProcessorType": "AWS Lambda", "pipelineType": "Service", "region": "us-east-1", "logSourceType": "S3", "status": "CREATE_COMPLETE", "pipelineId": "aee1c87c-2531-4fd1-b600-0c8071556967" }
```

Pipeline Alarm Management Data

```
{ "metricType": "PIPELINE_ALARM_MANAGEMENT", "pipelineType": "APP", "region": "us-east-1", "operation": "CREATE", "pipelineId": "dc8c1afa-1e22-4397-8c8b-963df8ac688a" }
```

OpenSearch Metrics Data

```
{ "metricType": "OPENSEARCH_METRICS", "proxyEnabled": true, "freeStorageSpace": 7000, "nodeCount": 2, "region": "us-east-1", "domainVersion": "2.17", "domainId": "cb25869992309965be0f36096463bcb9", "clusterUsedSpace": 100 }
```

AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the solution CloudFormation templates from the [solution landing page](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Modify the CloudFormation template mapping section from:

   ```
   AnonymousData:
     SendAnonymizedUsageData:
       Data: Yes
   ```

   to:

   ```
   AnonymousData:
     SendAnonymizedUsageData:
       Data: No
   ```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, choose **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in the [Automated deployment](automated-deployment.md) section of this guide.

## Contributors
<a name="contributors"></a>
+ Manish Jangid
+ Bryce Lee
+ Owen Chang
+ Haiyun Chen
+ Aiden Dai
+ Lalit Grover
+ Eva Liu
+ Robin Luo
+ James Ma
+ Joe Shi
+ Charles Wei
+ Ming Xu

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
