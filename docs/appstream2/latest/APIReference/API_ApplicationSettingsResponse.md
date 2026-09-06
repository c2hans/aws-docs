---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ApplicationSettingsResponse.html
---

# ApplicationSettingsResponse
<a name="API_ApplicationSettingsResponse"></a>

Describes the persistent application settings for users of a stack.

## Contents
<a name="API_ApplicationSettingsResponse_Contents"></a>

 ** Enabled **   <a name="WorkSpacesApplications-Type-ApplicationSettingsResponse-Enabled"></a>
Specifies whether persistent application settings are enabled for users during their streaming sessions.
Type: Boolean
Required: No

 ** S3BucketName **   <a name="WorkSpacesApplications-Type-ApplicationSettingsResponse-S3BucketName"></a>
The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** SettingsGroup **   <a name="WorkSpacesApplications-Type-ApplicationSettingsResponse-SettingsGroup"></a>
The path prefix for the S3 bucket where users’ persistent application settings are stored.
Type: String
Length Constraints: Maximum length of 100.
Required: No

## See Also
<a name="API_ApplicationSettingsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ApplicationSettingsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ApplicationSettingsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ApplicationSettingsResponse)
