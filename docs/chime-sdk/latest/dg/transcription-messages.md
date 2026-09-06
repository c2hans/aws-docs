---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-messages.html
---

# Understanding transcription files for Amazon Chime SDK media capture pipelines
<a name="transcription-messages"></a>

The transcription-messages folder contains transcription files in the .txt format. However, the folder only receives files when you enable live transcription. For more information about enabling live transcription, see [Using Amazon Chime SDK live transcription](meeting-transcription.md).

The folder includes all partial and complete transcription messages, and each message is a JSON object. File names contain the <yyyy-mm-dd-hour-min-seconds-milleseconds> timestamp. You can see transcription file examples at [Processing a received Amazon Chime SDK live transcript event](delivery-examples.md).
