---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video-tagging-stream-processor.html
---

# Add tags to a new stream processor
<a name="streaming-video-tagging-stream-processor"></a>

**Note**
Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Amazon Rekognition feature availability changes](rekognition-availability-changes.md).
**This change does not impact the availability of other Amazon Rekognition features.**

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a user-defined key and value.

You can add tags to a stream processor as you create it using the `CreateStreamProcessor` operation. Specify one or more tags in the `Tags` array input parameter. The following is a JSON example for the `CreateStreamProcessor` request with tags.

```
{
       "Name": "streamProcessorForCam",
       "Input": {
              "KinesisVideoStream": {
                     "Arn": "arn:aws:kinesisvideo:us-east-1:nnnnnnnnnnnn:stream/inputVideo"
              }
       },
       "Output": {
              "KinesisDataStream": {
                     "Arn": "arn:aws:kinesis:us-east-1:nnnnnnnnnnnn:stream/outputData"
              }
       },
       "RoleArn": "arn:aws:iam::nnnnnnnnnnn:role/roleWithKinesisPermission",
       "Settings": {
              "FaceSearch": {
                     "CollectionId": "collection-with-100-faces",
                     "FaceMatchThreshold": 85.5
              },
              "Tags": {
      "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
       }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
