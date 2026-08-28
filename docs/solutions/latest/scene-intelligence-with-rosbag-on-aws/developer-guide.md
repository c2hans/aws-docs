---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section provides the source code for the solution and additional customizations.

## Source code
<a name="source-code"></a>

Visit our [GitHub repository](https://github.com/awslabs/autonomous-driving-data-framework/tree/SO0279-v1.0.2) to download the source files for this solution and to share your customizations with others.

## Customization guide
<a name="customization-guide"></a>

The DAG and Apache Spark code are located in the artifacts S3 bucket. The artifacts bucket has the naming pattern of `addf-aws-solutions-artifacts-bucket-` {{<hash>}}. The following is an example:

```
s3://addf-aws-solutions-artifacts-bucket-<hash>/dags/aws-solutions/analysis-rip/image_dags/*
```

In this location, the `detect_scenes.py` file houses the Apache Spark code that applies the business logic. You can access this file, modify it to suit your use case, upload it to same S3 bucket, and [re-run the DAG](invoke-the-dag.md) in its entirety (rosbag extraction and object detection along with the Spark business logic).

**Note**
If you’re only testing the Apache Spark changes, you can just [re-run the Amazon EMR Serverless job](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs.html) in the application. A simple clone of a previously-run job runs your Apache Spark changes. Set the Apache Spark properties to include the `DynamoDB-Spark.jar` file. For instructions, see [Running jobs from the EMR Studio console](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-studio.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
