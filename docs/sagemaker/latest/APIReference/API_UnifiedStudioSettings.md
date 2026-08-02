---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UnifiedStudioSettings.html
---

# UnifiedStudioSettings
<a name="API_UnifiedStudioSettings"></a>

The settings that apply to an Amazon SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.

## Contents
<a name="API_UnifiedStudioSettings_Contents"></a>

 ** DomainAccountId **   <a name="sagemaker-Type-UnifiedStudioSettings-DomainAccountId"></a>
The ID of the AWS account that has the Amazon SageMaker Unified Studio domain. The default value, if you don't specify an ID, is the ID of the account that has the Amazon SageMaker AI domain.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** DomainId **   <a name="sagemaker-Type-UnifiedStudioSettings-DomainId"></a>
The ID of the Amazon SageMaker Unified Studio domain associated with this domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** DomainRegion **   <a name="sagemaker-Type-UnifiedStudioSettings-DomainRegion"></a>
The AWS Region where the domain is located in Amazon SageMaker Unified Studio. The default value, if you don't specify a Region, is the Region where the Amazon SageMaker AI domain is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Required: No

 ** EnvironmentId **   <a name="sagemaker-Type-UnifiedStudioSettings-EnvironmentId"></a>
The ID of the environment that Amazon SageMaker Unified Studio associates with the domain.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** ProjectId **   <a name="sagemaker-Type-UnifiedStudioSettings-ProjectId"></a>
The ID of the Amazon SageMaker Unified Studio project that corresponds to the domain.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** ProjectS3Path **   <a name="sagemaker-Type-UnifiedStudioSettings-ProjectS3Path"></a>
The location where Amazon S3 stores temporary execution data and other artifacts for the project that corresponds to the domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** SingleSignOnApplicationArn **   <a name="sagemaker-Type-UnifiedStudioSettings-SingleSignOnApplicationArn"></a>
The ARN of the Amazon DataZone application managed by Amazon SageMaker Unified Studio in the AWS IAM Identity Center.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::[0-9]+:application\/[a-zA-Z0-9-_.]+\/apl-[a-zA-Z0-9]+`
Required: No

 ** StudioWebPortalAccess **   <a name="sagemaker-Type-UnifiedStudioSettings-StudioWebPortalAccess"></a>
Sets whether you can access the domain in Amazon SageMaker Studio:
ENABLED
You can access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it in both studio interfaces.
DISABLED
You can't access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it only in that studio interface.
To migrate a domain to Amazon SageMaker Unified Studio, you specify the UnifiedStudioSettings data type when you use the UpdateDomain action.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_UnifiedStudioSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UnifiedStudioSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UnifiedStudioSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UnifiedStudioSettings)
