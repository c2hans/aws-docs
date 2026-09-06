---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DomainDetails.html
---

# DomainDetails
<a name="API_DomainDetails"></a>

The domain's details.

## Contents
<a name="API_DomainDetails_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-DomainDetails-CreationTime"></a>
The creation time.
Type: Timestamp
Required: No

 ** DomainArn **   <a name="sagemaker-Type-DomainDetails-DomainArn"></a>
The domain's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:domain/.*`
Required: No

 ** DomainId **   <a name="sagemaker-Type-DomainDetails-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** DomainName **   <a name="sagemaker-Type-DomainDetails-DomainName"></a>
The domain name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-DomainDetails-LastModifiedTime"></a>
The last modified time.
Type: Timestamp
Required: No

 ** Status **   <a name="sagemaker-Type-DomainDetails-Status"></a>
The status.
Type: String
Valid Values: `Deleting | Failed | InService | Pending | Updating | Update_Failed | Delete_Failed`
Required: No

 ** Url **   <a name="sagemaker-Type-DomainDetails-Url"></a>
The domain's URL.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_DomainDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DomainDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DomainDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DomainDetails)
