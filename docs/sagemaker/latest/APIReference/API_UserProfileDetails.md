---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UserProfileDetails.html
---

# UserProfileDetails
<a name="API_UserProfileDetails"></a>

The user profile details.

## Contents
<a name="API_UserProfileDetails_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-UserProfileDetails-CreationTime"></a>
The creation time.
Type: Timestamp
Required: No

 ** DomainId **   <a name="sagemaker-Type-UserProfileDetails-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-UserProfileDetails-LastModifiedTime"></a>
The last modified time.
Type: Timestamp
Required: No

 ** Status **   <a name="sagemaker-Type-UserProfileDetails-Status"></a>
The status.
Type: String
Valid Values: `Deleting | Failed | InService | Pending | Updating | Update_Failed | Delete_Failed`
Required: No

 ** UserProfileName **   <a name="sagemaker-Type-UserProfileDetails-UserProfileName"></a>
The user profile name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_UserProfileDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UserProfileDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UserProfileDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UserProfileDetails)
