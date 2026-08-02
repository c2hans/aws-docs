---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/ingest-step-functions.html
---

# Ingest Step Functions
<a name="ingest-step-functions"></a>

## Video-only workflow
<a name="video-only-workflow"></a>

When a new MP4, MPG, M4V, M2TS, or MOV video is added to the source Amazon S3 bucket, a Lambda function invokes the ingest workflow. During ingestion, source video details are added to Amazon DynamoDB, the content is validated using [MediaInfo](https://mediaarea.net/en/MediaInfo), open-source software that displays technical information about media files, and details are stored in DynamoDB.

**Important**
Source video file extensions (.mp4, .mpg, .m4v, .m2ts, or .mov) must be lowercase and file names cannot contain spaces.

## Metadata and video workflow
<a name="metadata-and-video-workflow"></a>

When a new metadata file is added to the source Amazon S3 bucket, a Lambda function invokes the ingest workflow. During ingestion, the metadata file, source video, and encoding configuration details are added to Amazon DynamoDB, the source video is validated using MediaInfo and details are stored in DynamoDB.

**Important**
You must upload the source video file to the Amazon S3 bucket before you upload the metadata file. Note that the upload must complete before you upload the metadata file.
