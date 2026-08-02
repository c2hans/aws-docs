---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_S3File.html
---

# S3File
<a name="API_S3File"></a>

Contains information for the S3 bucket that contains media files.

## Contents
<a name="API_S3File_Contents"></a>

 ** bucketName **   <a name="Social-Type-S3File-bucketName"></a>
The bucket name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
Required: Yes

 ** key **   <a name="Social-Type-S3File-key"></a>
The S3 key prefix that defines the storage location of your media files. The prefix works like a folder path in S3, and is combined with the WhatsApp mediaId to create the final file path.
For example, if a media file's WhatsApp mediaId is `123.ogg`, and the key is `audio/example.ogg`, the final file path is `audio/example.ogg123.ogg`.
For the same mediaId, a key of `audio/` results in the file path `audio/123.ogg`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_S3File_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/S3File)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/S3File)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/S3File)
