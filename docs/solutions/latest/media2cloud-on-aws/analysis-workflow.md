---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/analysis-workflow.html
---

# Analysis workflow
<a name="analysis-workflow"></a>

 The analysis workflow includes AWS Step Functions and AWS Lambda which leverage Amazon Rekognition, Amazon Transcribe, Amazon Comprehend, and Amazon Textract to analyze and extract machine learning metadata from the proxy files generated in the ingestion workflow. The Media2Cloud on AWS solution provides the following preset options for the analysis process when you deploy the template: **Default**, **All**, and **Audio and Text**.
+  **Default** - Activates *celebrity recognition*, *labels*, *transcription*, *key phrases*, *entities*, and *text* processes.
+  **All** - Activates all detections including *celebrity recognition*, *labels*, *transcription*, *key phrases*, *entities*, *text*, *faces*, *face matches*, *person*, *moderation*, *sentiment*, and *topic* processes.
+  **Audio and Text** - Activates *transcription*, *key phrases*, *entities*, and *text* processes.

 The web interface also allows the end user to refine the AI/ML settings during the upload process.

 The analysis workflow includes four sub-state machines to process the analysis.
+  The video analysis state machine analyzes and extracts AI/ML metadata from the video proxy using Amazon Rekognition video APIs.
+  The audio analysis state machine analyzes and extracts AI/ML metadata from the audio stream of the proxy file using Amazon Transcribe and Amazon Comprehend.
+  The image analysis state machine analyzes and extracts image metadata with Amazon Rekognition image APIs.
+  The document analysis state machine extracts text, images, and data using Amazon Textract.

 To start the analysis workflow, a Lambda function first checks an incoming analysis request and prepares the optimal AI/ML analysis option to run, based on the type of media in the request, and the availability of specific detections. For video and audio, it transforms the metadata results into WebVTT subtitle tracks, chapter markers, key phrases, labels, sentiments, entities, and locations. The analysis workflow can also provide customized analysis output if the customer uses [Amazon Rekognition custom label models](https://aws.amazon.com/rekognition/custom-labels-features/), [Amazon Transcribe custom vocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html) or [Amazon Comprehend custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html). The machine learning metadata results are stored in an Amazon S3 proxy bucket and indexed in an Amazon OpenSearch Service cluster. When the analysis is completed, Amazon SNS sends notifications to subscribed users. For more information, refer to [Amazon SNS notifications](amazon-sns-notifications.md).

![Media2Cloud on AWS analysis workflow diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-analysis-workflow.png)
