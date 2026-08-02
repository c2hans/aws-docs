---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_BucketLevelPermissions.html
---

# BucketLevelPermissions
<a name="API_BucketLevelPermissions"></a>

Contains information about the bucket level permissions for the S3 bucket.

## Contents
<a name="API_BucketLevelPermissions_Contents"></a>

 ** accessControlList **   <a name="guardduty-Type-BucketLevelPermissions-accessControlList"></a>
Contains information on how Access Control Policies are applied to the bucket.
Type: [AccessControlList](API_AccessControlList.md) object
Required: No

 ** blockPublicAccess **   <a name="guardduty-Type-BucketLevelPermissions-blockPublicAccess"></a>
Contains information on which account level S3 Block Public Access settings are applied to the S3 bucket.
Type: [BlockPublicAccess](API_BlockPublicAccess.md) object
Required: No

 ** bucketPolicy **   <a name="guardduty-Type-BucketLevelPermissions-bucketPolicy"></a>
Contains information on the bucket policies for the S3 bucket.
Type: [BucketPolicy](API_BucketPolicy.md) object
Required: No

## See Also
<a name="API_BucketLevelPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/BucketLevelPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/BucketLevelPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/BucketLevelPermissions)
