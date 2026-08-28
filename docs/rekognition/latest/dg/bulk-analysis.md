---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis.html
---

# Bulk analysis
<a name="bulk-analysis"></a>

**Note**
Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Amazon Rekognition feature availability changes](rekognition-availability-changes.md).
**This change does not impact the availability of other Amazon Rekognition features.**

Amazon Rekognition Bulk Analysis lets you process a large collection of images asynchronously by using a manifest file with the [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html) operation. The output for each individual image matches the output returned by the operation that you use for analysis.

Currently, Rekognition supports analysis with the [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) operation.

You will be charged for the number of images that have been successfully processed by the job. The results of a finished job are outputted to a specified Amazon S3 bucket.

Note that Bulk Analysis does not support the Amazon A2I integration.

The API can detect animated or illustrated content types, and information about the detected content type is returned as part of the response.

**Topics**
+ [Processing images in bulk](to-process-images-in-bulk.md)
+ [Bulk analysis output manifests](bulk-analysis-output-manifests.md)
+ [Content type](bulk-analysis-content-type.md)
+ [Verifying predictions and training adapters](bulk-analysis-pred-verify.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
