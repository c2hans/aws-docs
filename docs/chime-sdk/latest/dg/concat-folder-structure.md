---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/concat-folder-structure.html
---

# Understanding the Amazon S3 bucket folder structure for Amazon Chime SDK concatenation pipelines
<a name="concat-folder-structure"></a>

The Amazon S3 buckets for media concatenation pipelines use this folder structure:

```
{{S3 bucket path}}/
  audio
  video
  composited-video
  data-channel
  meeting-events
  transcription-messages
```

**Note**
If you specify a prefix when you create a media pipeline, the path to the folders becomes *bucket name*/*prefix*. Without a prefix, the path becomes *bucket name*/*media pipeline ID*. You specify a prefix in the `Destination` field of the `S3BucketSinkConfiguration` object. The concatenated file names consist of *media pipeline ID*.mp4 for media files and *media pipeline ID*.txt for text files.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
