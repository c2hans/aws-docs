---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/how-data-transfer-hub-works.html
---

# How Data Transfer Hub works
<a name="how-data-transfer-hub-works"></a>

 This Guidance has three components: a web console, the Amazon S3 transfer engine, and the Amazon ECR transfer engine.

## Web console
<a name="web-console"></a>

 This Guidance provides a simple web console, which allows you to create and manage transfer tasks for Amazon S3 and Amazon ECR.

## Amazon S3 transfer engine
<a name="amazon-s3-transfer-engine"></a>

 Amazon S3 transfer engine runs the Amazon S3 plugin and is used for transferring objects from their sources into S3 buckets. The S3 plugin supports the following features:
+  Transfer Amazon S3 objects between AWS China Regions and AWS Regions
+  Transfer objects from other cloud providers to Amazon S3
+  Transfer objects from S3 Compatible Storage service to Amazon S3
+  Support near real time transfer via S3 Event
+  Support transfer with object metadata
+  Support incremental data transfer
+  Support transfer from private payer request bucket
+  Auto retry and error handling

## Amazon ECR transfer engine
<a name="amazon-ecr-transfer-engine"></a>

 Amazon ECR engine runs the Amazon ECR plugin and is used for transferring container images from other container registries. The ECR plugin supports the following features:
+  Transfer Amazon ECR images between AWS China Regions and AWS Regions
+  Transfer from public container registry (such as Docker Hub, GCR.io, Quay.io) to Amazon ECR
+  Transfer selected images to Amazon ECR
+  Transfer all images and tags from Amazon ECR

 The ECR plugin leverages [skopeo](https://github.com/containers/skopeo) for the underlying engine. The AWS Lambda function lists images in their sources and uses Fargate to run the transfer jobs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
