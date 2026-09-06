---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobDetailsJobAttachmentSettings.html
---

# JobDetailsJobAttachmentSettings
<a name="API_JobDetailsJobAttachmentSettings"></a>

The job attachment settings returned to workers for a job. These are the Amazon S3 bucket name and the Amazon S3 prefix.

## Contents
<a name="API_JobDetailsJobAttachmentSettings_Contents"></a>

 ** rootPrefix **   <a name="deadlinecloud-Type-JobDetailsJobAttachmentSettings-rootPrefix"></a>
The root prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9-_/]+`
Required: Yes

 ** s3BucketName **   <a name="deadlinecloud-Type-JobDetailsJobAttachmentSettings-s3BucketName"></a>
The Amazon S3 bucket name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_JobDetailsJobAttachmentSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsJobAttachmentSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsJobAttachmentSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsJobAttachmentSettings)
