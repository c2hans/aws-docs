---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_RecordingData.html
---

# RecordingData

The audio source of a recording. In a `CreateVoice` request, specify exactly one of `S3Url` and `Bytes`. In a response, a recording that Amazon Polly read from Amazon S3 includes its `S3Url`. A recording that you passed as `Bytes` includes neither field, because Amazon Polly doesn't return the audio.

## Contents
<a name="API_RecordingData_Contents"></a>

 ** Bytes **   <a name="polly-Type-RecordingData-Bytes"></a>
The audio data, passed directly in the request. The data must be in the format that `Format` specifies and can be up to 5 MB. Amazon Polly doesn't store the audio after it creates the voice, and doesn't return this field in responses.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 5242880.
Required: No

 ** S3Url **   <a name="polly-Type-RecordingData-S3Url"></a>
The Amazon S3 URL of the audio object, in the form `s3://bucket/key`. You need `s3:GetObject` permission on the object.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]/.+$`
Required: No

## See Also
<a name="API_RecordingData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/RecordingData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/RecordingData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/RecordingData)
