---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/artifacts.html
---

# Working with Amazon Chime SDK media capture artifacts
<a name="artifacts"></a>

During an Amazon Chime SDK meeting, a media capture pipeline creates the following types of artifacts.
+ Audio
+ Video
+ Data channel messages
+ Meeting events
+ Transcription messages

The pipeline creates the artifacts in a set of folders in your Amazon S3 bucket, and you can configure the audio and video folders to limit certain types of artifacts. The following sections explain the folder structure, how to configure folders, how to set permissions for your Amazon S3 bucket, and how to concatenate the artifact files.
