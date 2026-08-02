---
source_url: https://docs.aws.amazon.com/transcribe/latest/dg/feature-matrix.html
---

# Amazon Transcribe features
<a name="feature-matrix"></a>

To help you decide which Amazon Transcribe solution best fits your use case, the following table offers a feature comparison.

Note that 'batch' and 'post-call' refer to transcribing a file that is located in an Amazon S3 bucket and 'streaming' and 'real-time' refer to transcribing media in real time.

<a name="table-feature-matrix"></a>
<table>
<thead>
  <tr><th>Feature</th><th>Amazon Transcribe</th><th>[Amazon Transcribe Medical](transcribe-medical.md)1</th><th>[Amazon Transcribe Call Analytics](call-analytics.md)</th></tr>
</thead>
<tbody>
  <tr><td colspan="4">Configuration options</td></tr>
  <tr><td>[Alternative transcriptions](alternatives.md)</td><td>batch, streaming</td><td>batch, streaming</td><td>no</td></tr>
  <tr><td>[Channel identification](channel-id.md)</td><td>batch, streaming</td><td>batch, streaming</td><td>post-call, real-time</td></tr>
  <tr><td>[Job queueing](job-queueing.md)</td><td>batch</td><td>no</td><td>post-call</td></tr>
  <tr><td>[Language identification](lang-id.md)</td><td>batch, streaming</td><td>no</td><td>post-call</td></tr>
  <tr><td>[Multi-language identification](lang-id-batch.md#lang-id-batch-multi-language)</td><td>batch, streaming</td><td>no</td><td>no</td></tr>
  <tr><td>[Speaker diarization](diarization.md)</td><td>batch, streaming</td><td>batch, streaming</td><td>post-call</td></tr>
  <tr><td>[Transcribing digits](how-numbers.md)2</td><td>batch, streaming</td><td>batch, streaming</td><td>post-call, real-time</td></tr>
  <tr><td colspan="4">Conversation analytics</td></tr>
  <tr><td>[Call characteristics](call-analytics-batch.md#tca-characteristics-batch)</td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td>[Call summarization](call-analytics-batch.md#tca-summarization-batch)2</td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td>[Custom categorization](call-analytics-batch.md#tca-categorization-batch)</td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td>[Real-time category events](call-analytics-streaming.md#tca-category-events-stream)</td><td>no</td><td>no</td><td>real-time</td></tr>
  <tr><td>[Real-time issue detection](call-analytics-streaming.md#tca-issue-detection-stream)2</td><td>no</td><td>no</td><td>real-time</td></tr>
  <tr><td>[Real-time speaker sentiment](call-analytics-streaming.md#tca-sentiment-stream)</td><td>no</td><td>no</td><td>real-time</td></tr>
  <tr><td>[Speaker sentiment](call-analytics-batch.md#tca-sentiment-batch)</td><td>no</td><td>no</td><td>post-call</td></tr>
  <tr><td colspan="4">Language customization</td></tr>
  <tr><td>[Custom language models](custom-language-models.md)2</td><td>batch, streaming</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td>[Custom vocabularies](custom-vocabulary.md)</td><td>batch, streaming</td><td>batch, streaming</td><td>post-call, real-time</td></tr>
  <tr><td colspan="4">Resource organization</td></tr>
  <tr><td>[Tagging](tagging.md)</td><td>batch</td><td>batch</td><td>post-call</td></tr>
  <tr><td colspan="4">Sensitive data</td></tr>
  <tr><td>[Identifying personal health information](phi-id.md)2</td><td>no</td><td>batch, streaming</td><td>no</td></tr>
  <tr><td>[Identifying personally identifiable information](pii-redaction-stream.md)2</td><td>streaming</td><td>no</td><td>real-time</td></tr>
  <tr><td>[Redacting audio](call-analytics-batch.md#tca-pii-redact-batch)2</td><td>no</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td>[Redacting transcripts](pii-redaction.md)2</td><td>batch, streaming</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td>[Vocabulary filtering](vocabulary-filtering.md)</td><td>batch, streaming</td><td>no</td><td>post-call, real-time</td></tr>
  <tr><td colspan="4">Video</td></tr>
  <tr><td>[Subtitles](subtitles.md)</td><td>batch</td><td>no</td><td>no</td></tr>
</tbody>
</table>

****
1 Amazon Transcribe Medical is only available in US English.
2 This feature is not available for all languages; review the [Supported languages and language-specific features](supported-languages.md) table for more details.
