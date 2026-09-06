---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_PermissionConfiguration.html
---

# PermissionConfiguration
<a name="API_PermissionConfiguration"></a>

Contains information about how permissions are configured for the S3 bucket.

## Contents
<a name="API_PermissionConfiguration_Contents"></a>

 ** accountLevelPermissions **   <a name="guardduty-Type-PermissionConfiguration-accountLevelPermissions"></a>
Contains information about the account level permissions on the S3 bucket.
Type: [AccountLevelPermissions](API_AccountLevelPermissions.md) object
Required: No

 ** bucketLevelPermissions **   <a name="guardduty-Type-PermissionConfiguration-bucketLevelPermissions"></a>
Contains information about the bucket level permissions for the S3 bucket.
Type: [BucketLevelPermissions](API_BucketLevelPermissions.md) object
Required: No

## See Also
<a name="API_PermissionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/PermissionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/PermissionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/PermissionConfiguration)
