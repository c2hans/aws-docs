---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/ingestion-workflow.html
---

# Ingestion workflow
<a name="ingestion-workflow"></a>

The ingestion workflow includes AWS Step Functions and [AWS Lambda](https://aws.amazon.com/lambda/), which orchestrate the specific ingestion workflow for a video, image, audio file, or document. When a customer uploads a new media file to the Amazon S3 ingestion bucket through the Media2Cloud on AWS web interface, the ingestion process starts. The workflow generates an asset unique identifier, computes and validates an [MD5](https://en.wikipedia.org/wiki/MD5) checksum, and extracts media information such as bitrate, formats, audio channels container format for video, or EXIF information such as GPS location, model, and make for image.

For video and audio files, the ingestion workflow initiates AWS Elemental MediaConvert to create standardized proxy files and thumbnails of the media for analysis. For image files, the ingestion workflow uses an open-source tool, [EXIFTool](https://github.com/exiftool/exiftool) to extract technical metadata and to create proxy images. Similarly for documents, the ingestion workflow generates image proxies for each page in a document. If the media content is in Amazon Glacier or [S3 Glacier Deep Archive](https://aws.amazon.com/glacier/) storage, the workflow temporarily restores the media content from archive storage to Amazon S3 storage. Proxy files are created and stored in a Amazon S3 proxy bucket, while the technical metadata extracted from media content are indexed in an Amazon OpenSearch Service cluster. When video ingestion process completes, Amazon SNS sends notifications to subscribed users who might use the notification to start other workflows. For example, third party partner solutions, such as Media Asset Manager (MAM) and Archive System, can subscribe to the Amazon SNS topic and then integrate the derived information into their workflows. When an Amazon SNS ingestion notification is received, the automated system can import the files into its system. For more information, refer to [Amazon SNS notifications](amazon-sns-notifications.md).

![Media2Cloud ingestion workflow diagram](https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-ingestion-workflow.png)
