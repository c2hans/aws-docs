---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/amazon-sns-notifications.html
---

# Amazon SNS notifications
<a name="amazon-sns-notifications"></a>

 The Media2Cloud on AWS solution sends Amazon SNS a publish notification to the subscriber when the Step Functions ingestion, analysis, and labeling state machines are completed, or when there is an error. You can automate other workflows, such as importing data to a Media Asset Management (MAM) system, by using the Amazon SNS topic subscription created by the solution. The following JSON notification messages can be customized to your needs.

## Ingestion state machine notification message:
<a name="ingestion-state-machine-notification-message"></a>

```
{
  "uuid": "<uuid>",
  "stateMachine": "<ingest-main-state-machine>",
  "operation": "job-completed",
  "overallStatus": "PROCESSING",
  "status": "INGEST_COMPLETED",
  "progress": 100,
  "input": {
    "bucket": "<ingest-bucket>",
    "duration": 91973,
    "framerate": 29.97,
    "destination": {
      "bucket": "<proxy-bucket>",
      "prefix": "<uuid>/Demo1/"
    },
    "attributes": {},
    "type": "video",
    "uuid": "<uuid>",
    "key": "Demo1/Demo1.mp4",
    "aiOptions": {
      "sentiment": true,
      "textROI": [
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false
      ],
      "framebased": false,
      "celeb": true,
      "frameCaptureMode": 0,
      "keyphrase": true,
      "label": true,
      "facematch": true,
      "transcribe": true,
      "face": true,
      "customentity": false,
      "person": false,
      "minConfidence": 80,
      "textract": true,
      "moderation": true,
      "segment": true,
      "customlabel": false,
      "text": true,
      "entity": true,
      "faceCollectionId": "FilmActors"
    }
  },
  "data": {
    "checksum": {
      "comparedResult": "MATCHED",
      "storeChecksumOnTagging": true,
      "computed": "3839bf07b1a69f15b5f1bb3356f5e500",
      "fileSize": 14392096,
      "startTime": 1638305617773,
      "endTime": 1638305618232,
      "comparedWith": "object-metadata",
      "tagUpdated": true,
      "algorithm": "md5"
    },
    "transcode": {
      "output": "<uuid>/Demo1/transcode/",
      "jobId": "1638305622955-7qvt1m",
      "startTime": 1638305623059,
      "endTime": 1638305641739
    },
    "restore": {
      "tier": "Bulk",
      "startTime": 1638305617599,
      "endTime": 1638305617599
    },
    "mediainfo": {
      "output": [
        "<uuid>/Demo1/mediainfo/mediainfo.json",
        "<uuid>/Demo1/mediainfo/mediainfo.xml"
      ]
    },
    "indexer": {
      "terms": [
        "overallStatus",
        "lastModified",
        "status",
        "timestamp",
        "basename",
        "attributes",
        "bucket",
        "fileSize",
        "mime",
        "framerate",
        "uuid",
        "key",
        "duration",
        "md5",
        "type"
      ]
    }
  }
}
```

## Table 2: Ingestion state machine notification message key name descriptions
<a name="table-2-ingestion-state-machine-notification-message-key-name-descriptions"></a>

|  Key name  |  Description  |
| --- | --- |
|  operation  |  Last state of the state machine: job-completed  |
|  uuid  |  UUID of the file  |
|  stateMachine  |  Ingestion state machine name  |
|  overallStatus  |  Status of the next step of the workflow  |
|  status  |  Status of the state machine: INGEST\_COMPLETED  |
|  progress  |  Progress of the state machine  |
|  input  |  Input parameters  |
|  input.bucket  |  Ingestion bucket where the uploaded file is stored  |
|  input.duration  |  Duration of the file in milliseconds  |
|  input.framerate  |  Frame rate of the uploaded file  |
|  destination  |  Location where proxy files will be stored  |
|  destination.bucket  |  S3 Bucket created to store proxy files  |
|  destination.prefix  |  Folder structure created within the S3 proxy file bucket  |
|  attributes  |  Object attributes  |
|  type  |  MIME type of the file that has been uploaded  |
|  uuid  |  UUID of the file  |
|  key  |  Path to the uploaded file in the S3 proxy file bucket  |
|  aiOptions  |  User selected AI services to run on the uploaded asset  |
|  aiOptions.sentiment  |  Boolean value indicates if sentiment detection is activated  |
|  aiOptions.textROI  |  Boolean value indicates if text regions of interest is activated  |
|  aiOptions.framebased  |  Boolean value indicates if frame-based analysis is activated  |
|  aiOptions.celeb  |  Boolean value indicates if celebrity detection is activated  |
|  aiOptions.frameCaptureMode  |  Integer value indicates if frame capture mode is activated  |
|  aiOptions.keyphrase  |  Boolean value indicates if Amazon Comprehend key phrase detection analysis is activated  |
|  aiOptions.label  |  Boolean value indicates if label detection is activated  |
|  aiOptions.facematch  |  Boolean value indicates if face match is activated  |
|  aiOptions.transcribe  |  Boolean value indicates if Amazon Transcribe is activated  |
|  aiOptions.face  |  Boolean value indicates if face detection is activated  |
|  aiOptions.customentity  |  Boolean value indicates if Amazon Comprehend custom entity recognizer is activated  |
|  aiOptions.person  |  Boolean value indicates if person detection is activated  |
|  aiOptions.minConfidence  |  An integer representing the confidence level results to display in the web UI  |
|  aiOptions.textract  |  Boolean value indicates if Amazon Textract is activated  |
|  aiOptions.moderation  |  Boolean value indicates if Amazon Rekognition moderation detection is activated  |
|  aiOptions.segment  |  Boolean value indicates if segment detection is activated  |
|  aiOptions.customlabel  |  Boolean value indicates if custom labels is activated  |
|  aiOptions.text  |  Boolean value indicates if text detection is activated  |
|  aiOptions.entity  |  Boolean value indicates if entity detection is activated  |
|  aiOptions.faceCollectionId  |  If a user activated the use of a face collection to match faces found in a file the name of the face collection will be displayed  |
|  data.checksum  |  Gathers the information from the checksum comparison process  |
|  data.checksum.compareResult  |  Status of the checksum comparison. MATCHED is success  |
|  data.checksum.storeChecksumOnTagging  |  A flag indicates if the checksum value is stored in Amazon S3 object tagging  |
|  data.checksum.computed  |  The computed MD5 or SHA1 checksum  |
|  data.checksum.fileSize  |  File size of the uploaded file  |
|  data.checksum.startTime  |  Start time of the checksum process  |
|  data.checksum.endTime  |  End time of the checksum process  |
|  data.checksum.comparedWith  |  Indicates how we compare the *computed* checksum <br /> object-metadata refers to `x-amz-metadat-md5` is used for comparison <br /> object-tagging refers to an existing `computed-md5` object tag is used for comparison <br /> object-etag refers to the object `ETag` value is used for comparison  |
|  data.checksum.tagUpdated  |  Indicate if the solution successfully updates the object tagging with the computed checksum value  |
|  data.checksum.algorithm  |  Checksum algorithm type: md5 or sha1  |
|  transcode.output  |  Location of the transcoded proxies in an S3 proxy bucket  |
|  transcode.jobId  |  AWS Elemental MediaConvert job ID when the solution creates proxies  |
|  transcode.startTime  |  Start time of AWS Elemental MediaConvert job  |
|  transcode.endTime  |  End time of AWS Elemental MediaConvert job  |
|  restore.tier  |  If object is in GLACIER or DEEP\_ARCHIVE storage the process for retrieval  |
|  restore.startTime  |  If object is in GLACIER or DEEP\_ARCHIVE storage, startTime indicates the start time of the restore process  |
|  restore.endTime  |  If object is in GLACIER or DEEP\_ARCHIVE storage, endTime indicates the end time of the restore process  |
|  mediainfo.output  |  Location of the raw mediainfo XML output in an S3 proxy bucket  |
|  indexer.terms  |  A list of terms indexed to Amazon OpenSearch Service cluster  |

## Analysis state machine notification message:
<a name="analysis-state-machine-notification-message"></a>

```
 {
  "uuid": "<uuid>",
  "stateMachine": "<analysis-main-state-machine>",
  "operation": "job-completed",
  "overallStatus": "COMPLETED",
  "status": "ANALYSIS_COMPLETED",
  "progress": 100,
  "input": {
    ...,
    "video": {
      "enabled": true,
      "key": "<uuid>/Demo1/transcode/aiml/Demo1.mp4"
    },
    "audio": {
      "enabled": true,
      "key": "<uuid>/Demo1/transcode/aiml/Demo1.m4a"
    },
    "image": {
      "enabled": false
    },
    "document": {
      "enabled": false
    },
    "request": {
      "timestamp": 1638305649796
    },
    "metrics": {
      "duration": 91973,
      "requestTime": 1638305649796,
      "startTime": 1638305651875,
      "endTime": 1638305714837
    }
  },
  "data": {
    "video": {
      "status": "COMPLETED",
      "startTime": 1638305652358,
      "endTime": 1638305712306,
      "executionArn": "<analysis-video-state-machine-arn>",
      "rekognition": {
        "[type]": {
          "startTime": 1638305654505,
          "endTime": 1638305693000,
          "backlogId": "<random-id> ",
          "jobId": "<job-id>",
          "numOutputs": 1,
          "output": "<uuid>/Demo1/raw/<time>/rekognition/[type]/mapFile.json",
          "metadata": "<uuid>/Demo1/metadata/[type]/",
          "timeseries": "<uuid>/Demo1/timeseries/[type]/",
          "vtt": "<uuid>/Demo1/vtt/[type]/"
        }
      }
    },
    "audio": {
      "status": "COMPLETED",
      "startTime": 1638305652379,
      "endTime": 1638305710319,
      "executionArn": "<analysis-audio-state-machine-arn>",
      "transcribe": {
        "output": "<uuid>/Demo1/raw/<time>/transcribe/<job-id>.json",
        "jobId": "<job-id>",
        "startTime": 1638305654014,
        "endTime": 1638305707564,
        "languageCode": "en-US",
        "vtt": "<uuid>/Demo1/raw/<time>/transcribe/<job-id>.vtt"
      },
      "comprehend": {
        "[type]": {
          "startTime": 1638305708528,
          "endTime": 1638305708956,
          "output": "<uuid>/Demo1/raw/<time>/comprehend/[type]/output.manifest",
          "metadata": "<uuid>/Demo1/metadata/[type]/output.json"
        }
      }
    },
    "src": {
      "bucket": "<ingest-bucket>",
      "key": "Demo1/Demo1.mp4",
      "type": "video"
    }
  }
}
```

## Table 3: Analysis state machine notification message key name descriptions
<a name="table-3-analysis-state-machine-notification-message-key-name-descriptions"></a>

|  Key Name  |  Description  |
| --- | --- |
|  uuid  |  UUID of the file  |
|  stateMachine  |  Analysis state machine name  |
|  operation  |  Last state of the state machine: job-completed  |
|  overallStatus  |  Overall status of the sate machine: COMPLETED  |
|  status  |  Status of the state machine: ANALYSIS\_COMPLETED  |
|  progress  |  Progress of the state machine  |
|  input  |  Input parameters similar to Ingestion state machine notification message with the additional parameters described below  |
|  Input.video.enabled  |  Boolean value indicating if the object is a video  |
|  input.video.key  |  Path to the file  |
|  input.audio.enabled  |  Boolean value indicating if the video file has audio  |
|  input.audio.key  |  Path to the file  |
|  input.image.enabled  |  Boolean value indicating if the object is an image  |
|  input.document.enabled  |  Boolean value indicating if the object is a document  |
|  input.request.timestamp  |  Time that the analysis job was submitted  |
|  input.metrics.duration  |  Length of the file  |
|  intput.metrics.requestTime  |  Time the analysis job was initiated  |
|  input.metrics.startTime  |  Start time of the analysis job  |
|  input.metrics.endTime  |  End time of the analysis job  |
|  data.video  |  Video analysis information  |
|  data.video.status  |  Status of the video analysis process  |
|  data.video.startTime  |  Start time of the video analysis process  |
|  data.video.endTime  |  End time of the video analysis process  |
|  data.video.executionArn  |  Video analysis state machine run ARN  |
|  data.video.rekognition  |  Amazon Rekognition results  |
|  data.video.rekognition.[type]  |  Amazon Rekognition detection results of a specific [type] that refers to celeb, face, faceMatch, label, segment, text, person, or moderation.  |
|  data.video.rekognition.[type].startTime  |  Start time of the Amazon Rekognition detection process  |
|  data.video.rekognition.[type].endTime  |  End time of the Amazon Rekognition detection process  |
|  data.video.rekognition.[type].backlogId  |  ID of the job in the backlog  |
|  data.video.rekognition.[type].jobId  |  Amazon Rekognition job ID  |
|  data.video.rekognition.[type].numOutputs  |  Integer showing the number of outputs from this analysis  |
|  data.video.rekognition.[type].output  |  Location of the raw results from Amazon Rekognition process stored in an S3 proxy bucket  |
|  data.video.rekognition.[type].metadata  |  Location of the metadata tracks the solution generated stored in an S3 proxy bucket  |
|  data.video.rekognition.[type].timeseries  |  Location of the time series metadata tracks the solution generated stored in an S3 proxy bucket  |
|  data.video.rekognition.[type].vtt  |  Location of the WebVTT tracks the solution generated stored in an S3 proxy bucket  |
|  data.audio  |  Audio analysis results  |
|  data.audio.status  |  Status of the audio analysis process  |
|  data.audio.startTime  |  Start time of the audio analysis process  |
|  data.audio.endTime  |  End time of the audio analysis process  |
|  data.audio.executionArn  |  Audio analysis state machine run ARN  |
|  data.audio.transcribe  |  Amazon Transcribe results  |
|  data.audio.transcribe.output  |  Location of the raw results from Amazon Transcribe service stored in an S3 proxy bucket  |
|  data.audio.transcribe.jobId  |  Amazon Transcribe job ID  |
|  data.audio.transcribe.startTime  |  Start time of the transcribe process  |
|  data.audio.transcribe.endTime  |  End time of the transcribe process  |
|  data.audio.transcribe.languageCode  |  The language code provided to Amazon Transcribe for the language the transcript should be in  |
|  data.audio.transcribe.vtt  |  Location of the WebVTT tracks the solution generated, stored in an S3 proxy bucket  |
|  data.audio.comprehend  |  Amazon Comprehend results  |
|  data.audio.comprehend.[type]  |  Amazon Comprehend detection results of a specific [type] that refers to entity, keyphrase, or sentiment.  |
|  data.audio.comprehend.[type].startTime  |  Start time of Amazon Comprehend detection process  |
|  data.audio.comprehend.[type].endTime  |  End time of Amazon Comprehend detection process  |
|  data.audio.comprehend.[type].output  |  Location of the raw results from Amazon Comprehend detection process, stored in an S3 proxy bucket  |
|  data.audio.comprehend.[type].metadata  |  Location of the metadata tracks the solution generated, stored in an S3 proxy bucket  |
|  data.source  |  Information about the source file  |
|  data.source.bucket  |  Name of the S3 ingestion bucket  |
|  data.source.key  |  Object key  |
|  data.source.type  |  MIME type of the object being analyzed  |

## State machine error notification message:
<a name="state-machine-error-notification-message"></a>

```
 {
   "uuid": "{{<uuid>}}",
   "stateMachine": "<state-machine-name>",
   "status": "ERROR",
   "errorMessage": "Cannot destructure property `workerId` of 'undefined' or 'null'.",
   "input": {
     "uuid": "{{<uuid>}}"
   }
 }
```

## Table 4: State machine error notification message key name descriptions
<a name="table-4-state-machine-error-notification-message-key-name-descriptions"></a>

|  Key Name  |  Description  |
| --- | --- |
|  uuid  |  UUID of the file  |
|  stateMachine  |  The state machine that generated the error  |
|  status  |  ERROR  |
|  errorMessage  |  The detailed error message  |
|  input  |  The input parameter used to start the state machine  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
