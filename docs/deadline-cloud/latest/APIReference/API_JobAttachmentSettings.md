---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobAttachmentSettings.html
---

# JobAttachmentSettings
<a name="API_JobAttachmentSettings"></a>

The job attachment settings. These are the Amazon S3 bucket name and the Amazon S3 prefix.

## Contents
<a name="API_JobAttachmentSettings_Contents"></a>

 ** rootPrefix **   <a name="deadlinecloud-Type-JobAttachmentSettings-rootPrefix"></a>
The root prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9-_/]+`
Required: Yes

 ** s3BucketName **   <a name="deadlinecloud-Type-JobAttachmentSettings-s3BucketName"></a>
The Amazon S3 bucket name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_JobAttachmentSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobAttachmentSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobAttachmentSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobAttachmentSettings)
