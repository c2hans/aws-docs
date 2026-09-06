---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/capture-pipe-config.html
---

# Creating media capture pipelines for Amazon Chime SDK meetings
<a name="capture-pipe-config"></a>

Media capture pipelines capture audio, video, and content share streams, plus meeting events and data messages. All media capture pipelines save their data to an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (S3) bucket that you create. You can create one media capture pipeline per Amazon Chime SDK meeting.

The following sections explain how to create a media capture pipeline. Follow them in the order listed.

**Topics**
+ [Creating an Amazon S3 bucket for Amazon Chime SDK media capture pipelines](create-s3-bucket.md)
+ [Enabling server-side encryption for an Amazon S3 bucket for Amazon Chime SDK media capture pipelines](sse-kms.md)
+ [Enabling object level server-side encryption with AWS KMS key](using-kms-keys-for-encryption.md)
+ [Creating the Amazon Chime SDK media capture pipeline](create-capture-pipe.md)
+ [Working with Amazon Chime SDK media capture artifacts](artifacts.md)
+ [Configuring the audio folder for Amazon Chime SDK media capture pipelines](configure-audio.md)
+ [Configuring the video folder for Amazon Chime SDK media capture pipelines](configure-video.md)
+ [Understanding messages in the data-channel folder for Amazon Chime SDK media capture pipelines](data-channel.md)
+ [Understanding the Amazon S3 bucket folder structure for Amazon Chime SDK media capture pipelines](capture-folder-structure.md)
+ [Understanding meeting event files for Amazon Chime SDK media capture pipelines](meeting-events.md)
+ [Understanding transcription files for Amazon Chime SDK media capture pipelines](transcription-messages.md)
+ [Concatenating data streams for Amazon Chime SDK media capture pipelines](concatenate-streams.md)
