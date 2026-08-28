---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/how-the-solution-works.html
---

# How the solution works
<a name="how-the-solution-works"></a>

## Ingest workflow
<a name="ingest-workflow"></a>

When a new video is added to the source Amazon Simple Storage Service (Amazon S3) bucket, an AWS Lambda function starts the ingest step function. The ingest step function includes:

 **Video on demand solution ingest workflow**

![ingest workflow](http://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/ingest-workflow.png)

+  **Input Validate** - Parses the input to the workflow, checks for the source video file, and defines the workflow configuration using the AWS Lambda function environment variables. If turned on, this step downloads the metadata file and overwrites the default environment variables with the variable definitions in the metadata file (metadata and video version only). For more information, refer to [Metadata file](metadata-file.md).
+  **MediaInfo** - Generates a signed Amazon S3 URL for the source video and runs MediaInfo to extract metadata about the video.
+  **DynamoDB Update** - Takes accumulated data from each step and stores it in Amazon DynamoDB.
+  **SNS Notification** - Sends an Amazon SNS notification with a summary of the ingest process.
+  **Process Execute** - Starts the processing workflow.

## Processing workflow
<a name="processing-workflow"></a>

When the ingest workflow is complete, it starts the processing workflow. The processing workflow includes:

 **Video on demand solution ingest workflow**

![processing workflow](http://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/processing-workflow.png)

+  **Profiler** - Gets the source video’s height and width from the metadata file, defines the settings for frame capture (if turned on), and chooses which template to use for encoding based on the source video’s height. For example, if the source video is greater than or equal to 1080p, the 1080p job template will be used.
+  **Encoding Profile Check, Accelerated Transcoding Check, and Frame Capture check** - Helps visualize which settings the profiler step applied.
+  **Encode Job Submit** - Submits the encoding job with the template defined by the profiler to MediaConvert.
+  **Dynamo Update** - Takes accumulated data from each step and stores it in Amazon DynamoDB.

## Publishing workflow
<a name="publishing-workflow"></a>

When encoding is complete, an EventBridge rule invokes an AWS Lambda function that starts the publishing process. The publishing process includes:

 **Video on demand solution publishing workflow**

![publishing workflow](http://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/publishing-workflow.png)

+  **Output Validate** - Checks the event data for the completed encoding job, gets the GUID from the MediaConvert notification, gets the asset details from Amazon DynamoDB, and generates the Amazon S3 and Amazon CloudFront URLs for the MediaConvert outputs.
+  **Archive Choice** - If Glacier or Glacier Deep Archive was activated, this step tags the source video with a unique identifier and the archive to invoke the Amazon Glacier lifecycle policy.
+  **MediaPackage Choice** - If you configure the solution to use MediaPackage, this step takes the output from MediaConvert and uses it as a source for a MediaPackage asset, which contains all the information MediaPackage requires to ingest file-based video content.
+  **DynamoDB Update** - Updates Amazon DynamoDB table with the event data.
+  **SQS Choice** - If activated, this step sends all workflow outputs to an SQS queue that is ingested into upstream workflows or processes.
+  **SNS Choice** - If activated, this step sends an Amazon SNS notification with a summary of the workflow and the Amazon CloudFront URLs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
