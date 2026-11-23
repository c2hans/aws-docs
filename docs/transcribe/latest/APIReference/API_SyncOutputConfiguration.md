---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_SyncOutputConfiguration.html
---

# SyncOutputConfiguration

The Amazon S3 location where your transcript is written.

## Contents
<a name="API_SyncOutputConfiguration_Contents"></a>

 ** OutputMediaFileUri **   <a name="transcribe-Type-SyncOutputConfiguration-OutputMediaFileUri"></a>
The Amazon S3 location where you want your transcript written. For example:
+  `s3://amzn-s3-demo-bucket/my-transcript.json`
+  `s3://amzn-s3-demo-bucket/transcripts/`
If the location ends with an object key, Amazon Transcribe writes the transcript to that key. If it is a bucket or ends with a forward slash (`/`), it's treated as a prefix, and Amazon Transcribe writes the transcript under it to a file named with the request ID of your call and a `.json` extension.
If you use `ContentRedaction`, Amazon Transcribe writes the redacted transcript to the same location and adds `redacted-` before the file name (for example, `redacted-my-transcript.json`). With `redacted_and_unredacted`, Amazon Transcribe writes both files.
If an object already exists at that key, Amazon Transcribe overwrites it.
In a response, this is the location where Amazon Transcribe wrote your transcript. If you requested `redacted_and_unredacted` output, this is the location of the unredacted transcript.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|http(s*)://).+`
Required: Yes

## See Also
<a name="API_SyncOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/SyncOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/SyncOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/SyncOutputConfiguration)
