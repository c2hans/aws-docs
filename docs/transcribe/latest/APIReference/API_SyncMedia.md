---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_SyncMedia.html
---

# SyncMedia

The audio to transcribe. Specify exactly one of `MediaBytes` or `MediaFileUri`.

Audio sent in the request (`MediaBytes`) can be up to 25 MB. Audio in Amazon S3 (`MediaFileUri`) can be up to 500 MB.

## Contents
<a name="API_SyncMedia_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** MediaBytes **   <a name="transcribe-Type-SyncMedia-MediaBytes"></a>
Your audio file, provided inline in the request. The maximum size is 25 MB (26,214,400 bytes) of audio, measured before base64 encoding.
If you use an AWS SDK, the SDK base64-encodes the bytes for you. If you call the API directly, base64-encode the bytes yourself.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 26214400.
Required: No

 ** MediaFileUri **   <a name="transcribe-Type-SyncMedia-MediaFileUri"></a>
The Amazon S3 location of the media file you want to transcribe. For example:
+  `s3://amzn-s3-demo-bucket/my-media-file.flac`
+  `s3://amzn-s3-demo-bucket/media-files/my-media-file.flac`
The maximum file size is 500 MB. You must have read permission for the file.
The Amazon S3 bucket that contains your input media must be located in the same AWS Region where you're making your transcription request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|http(s*)://).+`
Required: No

## See Also
<a name="API_SyncMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/SyncMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/SyncMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/SyncMedia)
