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
