---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/ingestion-state-machine.html
---

# Ingestion state machine
<a name="ingestion-state-machine"></a>

 The Media2Cloud on AWS solution ingests videos, images, audio, and documents to extract media information and generate proxies using AWS Step Functions nested state machines and AWS Lambda functions. When a new media file is uploaded through the web interface, the solution sends an HTTPS request to the Amazon API Gateway RESTful API endpoint to start the ingestion process. A Lambda function invokes the main state machine that starts the nested ingestion state machine. Media2Cloud on AWS sends state machine progress and status to an AWS IoT topic that activates the web interface to display updated results to the user.

 The ingestion state machine is composed of the following processes involving AWS Step Functions nested state machines and Lambda functions.
+  **Create record** - Creates a record of the uploaded file to the Amazon DynamoDB ingestion table. Information includes the S3 object key of the file, universally unique identifier (UUID), and MD5 checksum value.
+  **Start fixity (nested)** – A nested state machine that perform the fixity check to restore the uploaded file based on its storage class.
+  **Choose by media type** - Delegates the proxy generation workflow based on the media type of the file. The media type can be image, video, audio, or document.
+  **Start image ingestion (nested)** – A sub-state machine to process an image file.
+  **Start video ingestion (nested)** - A sub-state machine to process a video file.
+  **Start audio ingestion (nested)** - A sub-state machine to process an audio file.
+  **Start document ingestion (nested)** - A sub-state machine to process a document.
+  **Update record** - Collects all results from the states such as locations of the proxies, thumbnail images, and either MediaInfo (for videos) or embedded technical metadata within videos or images and updates the results to the ingest DynamoDB table.
+  **Index ingestion results** - Indexes the technical metadata to OpenSearch Service cluster.

![Ingestion state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-ingestion-state-machine.png)

## Ingestion fixity sub-state machine
<a name="ingestion-fixity-sub-state-machine"></a>

 The ingestion fixity sub-state machine uses AWS Lambda functions to compute and validate the file checksum. If the uploaded file is stored in either of the Amazon Glacier Flexible Retrieval S3 Glacier Deep Archive storage classes, the state machine temporarily restores the object before the checksum is performed. The ingestion fixity sub-state machine manages the following processes.
+  **Check restore status -** Checks the storage class of the uploaded file using the `S3.HeadObject` API. If the file is in either the `GLACIER` or `DEEP_ARCHIVE` storage class, the Lambda function starts the restore process using the `S3.RestoreObject` API. This process also involves a state to check if the restore process is complete and transitions to computing the checksum. If not, it moves to one of the following wait states: a four-minute wait state if the restore tier is set to `Expedited`, a 12 hour wait state if the storage class is set to `DEEP_ARCHIVE` and the restore tier is set to Bulk, or a four-hour wait state for the rest of the file.
+  **Compute checksum** - Incrementally computes the MD5 checksum of a 20 GB chunk of the file using the `S3.GetObject` byte range. This process also involves a choice state to check if the checksum is completed. If not, it computes the MD5 checksum on the next 25GB chunk of the file.
+  **Validate checksum** – Compares the computed checksum value of the file against the previously computed MD5 checksum that is stored in the object metadata.

![Ingestion fixity sub-state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-ingestion-fixity-sub-state-machine.png)

## Video ingestion sub-state machine
<a name="video-ingestion-sub-state-machine"></a>

 The video ingestion sub-state machine processes video files using AWS Lambda functions. This state machine coordinates the following processes:
+  **Run mediainfo** – Runs the [MediaInfo](https://mediaarea.net/en/MediaInfo) tool to extract technical metadata from the video. The raw MediaInfo XML result is stored in an S3 proxy bucket.
+  **Start and wait for mediaconvert job** - Creates a job template based on the media information extracted by MediaInfo. If the video file contains multiple audio tracks (an MXF file can contain eight to 16 audio tracks), the Lambda function selects the best combination of audio tracks, and runs AWS Elemental MediaConvert to create the proxy files and thumbnails. The proxy files and thumbnail images are stored in an S3 proxy bucket.

![Video ingestion sub-state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-video-ingestion-sub-state-machine.png)

## Image ingestion sub-state machine
<a name="image-ingestion-sub-state-machine"></a>

 The image ingestion sub-state machine processes images using AWS Lambda. This state machine coordinates the following process:
+  **Run imageinfo** - Runs [exiftool](https://exiftool.org/) to extract EXIF information from the image file, generates an image proxy file, and stores the proxies to an S3 proxy bucket.

![Image ingestion sub-state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-image-ingestion-sub-state-machine.png)

## Audio ingestion sub-state machine
<a name="audio-ingestion-sub-state-machine"></a>

 The audio ingestion sub-state machine processes audio files using AWS Lambda functions. This state machine coordinates the following processes:
+  **Run mediainfo** – Runs the [MediaInfo](https://mediaarea.net/en/MediaInfo) tool to extract technical metadata and cover art from the audio file. The raw MediaInfo XML result is stored in an S3 proxy bucket.
+  **Start and wait for transcode job** – Uses AWS Elemental MediaConvert service to create a M4A audio proxy file for Amazon Transcribe processing and for streaming to the web application. The proxy files are stored in an S3 proxy bucket.

![Audio ingestion sub-state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-audio-ingestion-sub-state-machine.png)

## Document ingestion sub-state machine
<a name="document-ingestion-sub-state-machine"></a>

 The document ingestion sub-state machine processes document files using AWS Lambda. This state machine coordinates the following process:
+  **Run PDFinfo and extract pages** – Runs the PDF.JS tool to extract document metadata and converts pages to PNG image proxies. The PNG image proxies are stored in an S3 proxy bucket.

![Document ingestion sub-state machine workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-document-ingestion-sub-state-machine.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
