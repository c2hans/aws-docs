---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroupEntry.html
---

# ListStorageLensGroupEntry
<a name="API_control_ListStorageLensGroupEntry"></a>

 Each entry contains a Storage Lens group that exists in the specified home Region.

## Contents
<a name="API_control_ListStorageLensGroupEntry_Contents"></a>

 ** HomeRegion **   <a name="AmazonS3-Type-control_ListStorageLensGroupEntry-HomeRegion"></a>
 Contains the AWS Region where the Storage Lens group was created.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z0-9\-]+`
Required: Yes

 ** Name **   <a name="AmazonS3-Type-control_ListStorageLensGroupEntry-Name"></a>
 Contains the name of the Storage Lens group that exists in the specified home Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** StorageLensGroupArn **   <a name="AmazonS3-Type-control_ListStorageLensGroupEntry-StorageLensGroupArn"></a>
 Contains the Amazon Resource Name (ARN) of the Storage Lens group. This property is read-only.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\-group\/.*`
Required: Yes

## See Also
<a name="API_control_ListStorageLensGroupEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListStorageLensGroupEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListStorageLensGroupEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListStorageLensGroupEntry)
