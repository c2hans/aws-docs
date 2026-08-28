---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

 This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## Ingest
<a name="ingest"></a>

 To invoke the video processing workflow, you must upload the source video assets to the source S3 bucket through standard tools. For example, you can use the [AWS Management Console](https://aws.amazon.com/console/), [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI), or third-party tools that interface with Amazon S3.

 By default, this solution creates an `assets01` folder in the root of the source S3 bucket with a `job-settings.json` file. Each time you upload a video to the `assets01` folder, or any other folder that you created:

1.  An Amazon S3 [event notification](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) invokes the `job-submit` Lambda function.

1.  The `job-submit` Lambda function:

   1.  Receives the details for the source video from the event.

   1.  Applies the settings contained in the job settings file in the same top-level folder as the uploaded video in Amazon S3.

   1.  Submits a job to MediaConvert using the processed job settings file.

 To help you track the job in MediaConvert, the solution includes the following in the submitted job:
+  Name of the workflow defined at deployment
+  A globally unique identifier (GUID) created by the `job-submit` Lambda function

## Encoding
<a name="encoding"></a>

 The solution supports MediaConvert QVBR encoding mode, which ensures consistent, high-quality video transcoding with the smallest file size for any type of source video content.

 By default, this solution includes a sample encoding job settings file that encodes your source videos into MP4, SD and HD formats of HLS, and SD and HD formats of DASH. You can overwrite the provided encoding job settings to use [output formats that are supported by MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-outputs.html).

 The sample job settings file created as part of the CloudFormation deployment has the QVBR rate control activated with [accelerated transcoding](https://docs.aws.amazon.com/mediaconvert/latest/ug/accelerated-transcoding.html) set to `PREFERRED`. This generates the following output:
+  HLS ABR with 5 renditions @ 1920x1080, 1280x720, 960x540, 640x360, 480x270

 To change the settings, you can update or replace the job settings file in Amazon S3 with your own settings. For details, refer to [Exporting and importing AWS Elemental MediaConvert jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/exporting-and-importing-jobs.html) in the *MediaConvert User Guide*. To ensure validity of the job settings file, only export jobs that have successfully run and completed.

## Processing
<a name="processing"></a>

 This solution includes an EventBridge rule configured to invoke the `job-complete` Lambda function each time an encoding job starts up, completes successfully, or fails in MediaConvert. This function retrieves the details of the job from the event and generates the CloudFront URLs for the MediaConvert outputs. The solution then adds details for the input file, job settings, and outputs to a `jobs-manifest.json` file stored at the root of the source S3 bucket. The following is an example `jobs-manifest.json` file.

```
{
  "Jobs":
    {
        "jobId-0001": {
            "FileInput": "s3://SOURCE_BUCKET/example.mp4",
            "JobSettings": {...},
            "Outputs": {
                "HLS": "https://cloudfront.net/..."
              }
        },
        "jobId-0002": {
            "FileInput": "s3://SOURCE_BUCKET/example2.mp4",
            "JobSettings": {...},
            "Outputs": {
                "HLS": "https://cloudfront.net/..."
              }
        }
    }
    ...

}
```

 The `job-complete` Lambda function also sends a summary of the job and the outputs to the Amazon SNS topic created at deployment. Errors from the encoding process are also captured by the Lambda function and sent to the SNS topic.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

|  AWS service  |  Description  |
| --- | --- |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  Core. This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment.  |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  Core. Accelerates delivery of the video content from the destination S3 bucket to end users.  |
|  [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)  |  Core. Transcodes media files from their source format into HLS ABR files.  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  Core. Provides job submit functions without provisioning or managing servers.  |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  Core. Sends notifications of completed jobs.  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Core. Provides the storage for source video files and the outputs from MediaConvert.  |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  Supporting. Logs metrics about encoding jobs in MediaConvert.  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  Supporting. Invokes the Lambda job complete function.  |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  Supporting. Provides application-level resource monitoring and visualization of resource operations and cost data.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
