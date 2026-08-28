---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/metadata-file.html
---

# Metadata file
<a name="metadata-file"></a>

When you set the solution to ingest source videos and metadata files, the source Amazon Simple Storage Service (Amazon S3) bucket is configured with an event notification that invokes the workflow when you upload a JSON file.

**Note**
The JSON file does not need a specific name, but it must have the JSON file extension. We recommend naming the JSON file the same name as the video file for consistency and ease of reference.

To invoke the workflow, you must upload a JSON metadata file. If you only upload a source video file, the workflow will not start.

**Important**
You must upload the source video file to the Amazon S3 bucket before you upload the metadata file. Note that the upload must complete before you upload the metadata file.

The definitions in the metadata file overwrite the default settings you specified when you deployed the solution. This allows you to define different workflow configurations for each source video. If you do not specify a definition in the metadata file, the solution will use the default value you set during deployment. Note that the metadata file must include a definition for **srcVideo**.

The following example metadata files shows all available variable definitions.

```
{
 "srcVideo": "string",
 "archiveSource": "DISABLED|GLACIER|DEEP_ARCHIVE",
 "frameCapture": boolean,
 "srcBucket":"string",
 "destBucket":"string",
 "cloudFront":"string",
 "jobTemplate_2160p":"string",
 "jobTemplate_1080p":"string",
 "jobTemplate_720p":"string",
 "acceleratedTranscoding":"DISABLED|PREFERRED|ENABLED",
 "enableSqs": boolean ,
 "enableSns": boolean ,
 "jobTemplate":"custom-job-template",
 "InputRotate":"DEGREE_0|DEGREES_90|DEGREES_180|DEGREES_270|AUTO"
}
```

The following sample JSON metadata file will overwrite the default settings for the **Archive Source Content** and **Enable Frame Capture** AWS CloudFormation template parameters for the `example.mpg` file. The file will also set the job template for AWS Elemental MediaConvert to `custom-job-template`.

```
{
 "srcVideo": "example.mpg",
 "archiveSource": "GLACIER",
 "frameCapture":false,
 "jobTemplate":"custom-job-template"
}
```

The Video on Demand on AWS solution also supports adding additional metadata, such as title, genre, or any other information, you want to store in Amazon DynamoDB.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
